from __future__ import annotations

from collections.abc import Callable
import hashlib
import json
from pathlib import Path, PurePosixPath
from tempfile import TemporaryFile
from typing import Protocol

from ...constants import CATALOG_ARTIFACT_BASE_URL, LANCE_DOCUMENT_TABLE
from ..paths import paths
from ..releases import CatalogRelease, ReleaseArtifact
from ..releases.hashing import release_digest
from ..releases.models import safe_relative_path, safe_sha256
from ..releases.services import MAX_RELEASE_ARTIFACT_BYTES
from .dependencies import missing_curation_dependency

try:
    from obspec import Delete, Get, List, Put
    from obstore.store import HTTPStore, LocalStore
    from platformdirs import user_cache_path

    from .archive import extract_tar_archive
except ModuleNotFoundError as exc:
    raise missing_curation_dependency(exc.name) from exc


DownloadReporter = Callable[[str, str, Path], None]
_CORE_ARTIFACT_PATHS = ("MANIFEST.md", "entries.parquet")
_MAX_JSON_BYTES = 1024 * 1024
_BUNDLE_MARKER_PREFIX = "_chartcoach/bundles"
_INDEX_MARKER_PREFIX = "_chartcoach/indexes"
_INDEX_DATA_PREFIX = "_chartcoach/index-data"


class CacheStore(Delete, Get, List, Put, Protocol):
    """Object operations used by the local cache."""


def cache_root() -> Path:
    """Return the platform cache root for catalog artifacts."""

    return user_cache_path("chartcoach", appauthor=False)


def cache_store(root: Path | None = None) -> LocalStore:
    """Return a local object store rooted at the catalog cache."""

    return LocalStore(
        cache_root() if root is None else root,
        automatic_cleanup=True,
        mkdir=True,
    )


def artifact_store() -> Get:
    """Return the public read-only catalog artifact store."""

    return HTTPStore.from_url(
        CATALOG_ARTIFACT_BASE_URL,
        client_options={"timeout": "15m"},
    )


def download_catalog_bundle(
    reference: str | None = None,
    *,
    reporter: DownloadReporter | None = None,
) -> tuple[CatalogRelease, Path]:
    root = cache_root()
    return cache_catalog_bundle(
        artifact_store(),
        cache_store(root),
        root,
        reference=reference,
        reporter=reporter,
    )


def cache_catalog_bundle(
    source: Get,
    cache: CacheStore,
    root: Path,
    *,
    reference: str | None = None,
    reporter: DownloadReporter | None = None,
) -> tuple[CatalogRelease, Path]:
    """Download a verified core bundle and mark it complete."""

    release = _resolve_release(source, cache, reference)
    release_paths = paths.release(release.digest)
    target = _local_path(root, release_paths.root())
    marker = _bundle_marker_key(release.digest)
    if _marker_matches(cache, marker, release.digest):
        return release, target

    _delete(cache, marker)
    for artifact_path in _CORE_ARTIFACT_PATHS:
        artifact = release.artifact(artifact_path)
        object_key = release_paths.artifact(artifact_path)
        if reporter is not None:
            reporter("catalog", object_key, target)
        _copy_artifact(source, object_key, cache, object_key, artifact)
    cache.put(release_paths.json(), _json_bytes(release.to_record()), mode="overwrite")
    cache.put(marker, release.digest.encode("ascii"), mode="overwrite")
    return release, target


def download_index_artifact(
    reference: str | None = None,
    *,
    profile: str,
    reporter: DownloadReporter | None = None,
) -> Path:
    root = cache_root()
    return cache_index_artifact(
        artifact_store(),
        cache_store(root),
        root,
        reference=reference,
        profile=profile,
        reporter=reporter,
    )


def cache_index_artifact(
    source: Get,
    cache: CacheStore,
    root: Path,
    *,
    reference: str | None = None,
    profile: str,
    reporter: DownloadReporter | None = None,
) -> Path:
    """Download, extract, and cache one native LanceDB profile."""

    release = _resolve_release(source, cache, reference)
    profile = safe_relative_path(profile, label="Embedding profile")
    artifact_path = f"profiles/{profile}/index.tar.gz"
    try:
        artifact = release.artifact(artifact_path)
    except KeyError:
        choices = ", ".join(repr(value) for value in _profile_ids(release)) or "none"
        raise ValueError(
            f"Catalog release does not publish profile {profile!r}. "
            f"Available profiles: {choices}."
        ) from None

    release_paths = paths.release(release.digest)
    archive_key = release_paths.artifact(artifact_path)
    index_key = _index_cache_key(release.digest, artifact.sha256)
    marker = _index_marker_key(release.digest, artifact.sha256)
    target = _local_path(root, index_key)
    if _marker_matches(cache, marker, artifact.sha256) and _index_is_usable(target):
        return target

    _discard_profile(cache, index_key=index_key, archive_key=archive_key, marker=marker)
    if reporter is not None:
        reporter("index", archive_key, target)
    try:
        _copy_artifact(source, archive_key, cache, archive_key, artifact)
        members = extract_tar_archive(
            _local_path(root, archive_key),
            cache,
            prefix=index_key,
        )
        if not any(
            path.startswith(f"{LANCE_DOCUMENT_TABLE}.lance/") for path in members
        ):
            raise ValueError(
                f"LanceDB archive does not contain table: {LANCE_DOCUMENT_TABLE}"
            )
        if not _index_is_usable(target):
            raise ValueError("Extracted LanceDB index could not be opened.")
    except BaseException:
        _discard_profile(
            cache,
            index_key=index_key,
            archive_key=archive_key,
            marker=marker,
        )
        raise

    _delete(cache, archive_key)
    cache.put(release_paths.json(), _json_bytes(release.to_record()), mode="overwrite")
    cache.put(marker, artifact.sha256.encode("ascii"), mode="overwrite")
    return target


def read_release(source: Get, reference: str | None = None) -> CatalogRelease:
    """Read the selected release or one exact digest."""

    digest = (
        None
        if reference is None
        else safe_sha256(reference, label="Catalog release digest")
    )
    key = paths.selected() if digest is None else paths.release(digest).json()
    release = CatalogRelease.from_mapping(_read_json(source, key))
    _validate_release(release, expected=digest or release.digest)
    return release


def _resolve_release(
    source: Get,
    cache: Get,
    reference: str | None,
) -> CatalogRelease:
    if reference is not None:
        digest = safe_sha256(reference, label="Catalog release digest")
        try:
            release = CatalogRelease.from_mapping(
                _read_json(cache, paths.release(digest).json())
            )
            _validate_release(release, expected=digest)
            return release
        except (
            FileNotFoundError,
            UnicodeDecodeError,
            ValueError,
            json.JSONDecodeError,
        ):
            pass
    return read_release(source, reference)


def _validate_release(release: CatalogRelease, *, expected: str) -> None:
    if release.digest != expected or release.digest != release_digest(
        release.artifacts
    ):
        raise ValueError(f"Catalog release does not match digest {expected!r}.")
    for path, artifact in release.artifacts.items():
        if artifact.bytes > MAX_RELEASE_ARTIFACT_BYTES:
            raise ValueError(f"Catalog artifact exceeds the 1 GiB limit: {path}")


def _profile_ids(release: CatalogRelease) -> tuple[str, ...]:
    prefix = "profiles/"
    suffix = "/index.tar.gz"
    return tuple(
        sorted(
            path.removeprefix(prefix).removesuffix(suffix)
            for path in release.artifacts
            if path.startswith(prefix) and path.endswith(suffix)
        )
    )


def _index_is_usable(path: Path) -> bool:
    try:
        import lancedb

        lancedb.connect(path).open_table(LANCE_DOCUMENT_TABLE)
    except Exception:
        return False
    return True


def _copy_artifact(
    source: Get,
    source_key: str,
    target: Put,
    target_key: str,
    artifact: ReleaseArtifact,
) -> None:
    digest = hashlib.sha256()
    size = 0
    with TemporaryFile("w+b") as staging:
        for buffer in source.get(source_key):
            view = memoryview(buffer)
            size += view.nbytes
            if size > artifact.bytes:
                raise ValueError(f"Catalog artifact size mismatch: {source_key}")
            digest.update(view)
            staging.write(view)
        if size != artifact.bytes:
            raise ValueError(f"Catalog artifact size mismatch: {source_key}")
        if digest.hexdigest() != artifact.sha256:
            raise ValueError(f"Catalog artifact digest mismatch: {source_key}")
        staging.seek(0)
        target.put(target_key, staging, mode="overwrite", use_multipart=True)


def _marker_matches(store: Get, key: str, expected: str) -> bool:
    try:
        return bytes(store.get(key).buffer()).decode("ascii") == expected
    except (FileNotFoundError, UnicodeDecodeError):
        return False


def _discard_profile(
    cache: CacheStore,
    *,
    index_key: str,
    archive_key: str,
    marker: str,
) -> None:
    prefix = f"{index_key}/"
    objects = [
        item["path"]
        for batch in cache.list(prefix)
        for item in batch
        if item["path"].startswith(prefix)
    ]
    for key in (*objects, archive_key, marker):
        _delete(cache, key)


def _delete(store: Delete, key: str) -> None:
    try:
        store.delete(key)
    except FileNotFoundError:
        pass


def _bundle_marker_key(digest: str) -> str:
    return f"{_BUNDLE_MARKER_PREFIX}/{digest}.complete"


def _index_marker_key(release_digest: str, archive_sha256: str) -> str:
    return f"{_INDEX_MARKER_PREFIX}/{release_digest}-{archive_sha256}.complete"


def _index_cache_key(release_digest: str, archive_sha256: str) -> str:
    return f"{_INDEX_DATA_PREFIX}/{release_digest}-{archive_sha256}"


def _read_json(store: Get, key: str) -> object:
    data = bytearray()
    for buffer in store.get(key):
        view = memoryview(buffer)
        if len(data) + view.nbytes > _MAX_JSON_BYTES:
            raise ValueError("Catalog JSON exceeds the 1 MiB limit.")
        data.extend(view)
    return json.loads(data)


def _local_path(root: Path, key: str) -> Path:
    path = PurePosixPath(key)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Catalog cache key must be relative: {key!r}")
    return root.joinpath(*path.parts)


def _json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


__all__ = [
    "artifact_store",
    "cache_catalog_bundle",
    "cache_index_artifact",
    "cache_root",
    "cache_store",
    "download_catalog_bundle",
    "download_index_artifact",
    "read_release",
]
