from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
import hashlib
import json
import os
from os import PathLike
from pathlib import Path, PurePosixPath
import shutil
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Any, Literal, cast
from urllib.parse import unquote, urlsplit, urlunsplit
from urllib.request import Request, url2pathname, urlopen
from uuid import uuid4

from platformdirs import user_cache_path

from ..constants import (
    CATALOG_ARTIFACT_BASE_URL,
    CATALOG_ENTRY_PATH,
    LANCE_DOCUMENT_TABLE,
)
from .errors import CatalogError
from .releases import CatalogRelease, ReleaseArtifact
from .releases.archive import extract_tar_archive
from .releases.hashing import release_digest, sha256_file
from .releases.models import safe_relative_path
from .releases.services import MAX_RELEASE_ARTIFACT_BYTES

if TYPE_CHECKING:
    from lancedb import Table

    from .collection import Catalog


_CLOUD_SCHEMES = frozenset(
    {
        "abfs",
        "abfss",
        "adl",
        "az",
        "azure",
        "gcp",
        "gcs",
        "gs",
        "s3",
        "s3a",
    }
)
_DESCRIPTOR_NAMES = frozenset({"catalog.json", "release.json"})
_MAX_JSON_BYTES = 1024 * 1024
_MAX_CORE_ARTIFACT_BYTES = 64 * 1024**2
_READ_CHUNK_BYTES = 1024 * 1024
_CACHE_MARKER = ".complete"
_OFFICIAL_CATALOG_URL = f"{CATALOG_ARTIFACT_BASE_URL.rstrip('/')}/{CATALOG_ENTRY_PATH}"


@dataclass(frozen=True, slots=True)
class _LocalSource:
    path: Path


@dataclass(frozen=True, slots=True)
class _RemoteSource:
    uri: str
    transport: Literal["http", "cloud"]


@dataclass(frozen=True, slots=True)
class _ReleaseLocation:
    release: CatalogRelease
    artifact_base: Path | str
    transport: Literal["local", "http", "cloud"]
    storage_options: Mapping[str, object]

    def artifact_path(self, path: str) -> Path:
        artifact = self.release.artifact(path)
        if self.transport == "local":
            base = self.artifact_base
            if not isinstance(base, Path):
                raise AssertionError("Local release base must be a path.")
            local_path = base.joinpath(*PurePosixPath(path).parts)
            _verify_local_artifact(base, local_path, path, artifact)
            return local_path

        base = self.artifact_base
        if not isinstance(base, str):
            raise AssertionError("Remote release base must be a URI.")
        uri = _join_uri_path(base, path)
        return _cache_remote_artifact(
            uri,
            transport=self.transport,
            storage_options=self.storage_options,
            path=path,
            artifact=artifact,
        )


def open_catalog(
    source: str | PathLike[str] | None = None,
    *,
    storage_options: Mapping[str, object] | None = None,
) -> "Catalog":
    """Open an authored catalog, bundle, or release descriptor."""

    options = _copy_storage_options(storage_options)
    normalized = _normalize_source(source)
    if isinstance(normalized, _LocalSource) and normalized.path.is_dir():
        direct = _open_local_directory(normalized.path)
        if direct is not None:
            return direct

    location = _release_location(normalized, options)
    from .collection import _load_catalog_bundle

    return _load_catalog_bundle(
        location.artifact_path("MANIFEST.md"),
        location.artifact_path("entries.parquet"),
        release=location.release,
    )


def open_index(
    source: str | PathLike[str] | None = None,
    *,
    profile: str,
    storage_options: Mapping[str, object] | None = None,
) -> "Table":
    """Open one release-backed native LanceDB profile."""

    options = _copy_storage_options(storage_options)
    normalized = _normalize_source(source)
    if isinstance(normalized, _LocalSource) and normalized.path.is_dir():
        if not (normalized.path / "release.json").is_file():
            raise CatalogError(
                "Index sources must be a release directory, catalog.json, or "
                "release.json path or URI."
            )
    location = _release_location(normalized, options)
    profile = safe_relative_path(profile, label="Embedding profile")
    artifact_path = f"profiles/{profile}/index.tar.gz"
    try:
        archive = location.artifact_path(artifact_path)
        artifact = location.release.artifact(artifact_path)
    except KeyError:
        choices = ", ".join(repr(value) for value in _profile_ids(location.release))
        raise CatalogError(
            f"Catalog release does not publish profile {profile!r}. "
            f"Available profiles: {choices or 'none'}."
        ) from None

    index_path = _cached_index(archive, artifact.sha256)
    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Release-backed indexes require the optional `chartcoach[index]` "
            "dependencies.",
            name=exc.name,
        ) from exc
    return lancedb.connect(index_path).open_table(LANCE_DOCUMENT_TABLE)


def _open_local_directory(path: Path) -> "Catalog | None":
    release_path = path / "release.json"
    if release_path.is_file():
        return None

    manifest = (path / "MANIFEST.md").is_file()
    authored = manifest and (path / "entries").is_dir()
    bundle = manifest and (path / "entries.parquet").is_file()
    if authored and bundle:
        raise CatalogError(
            "Catalog directory is ambiguous because it contains both entries/ "
            "and entries.parquet."
        )
    if authored:
        from .storage import load_catalog

        return load_catalog(path)
    if bundle:
        from .collection import _load_catalog_bundle

        return _load_catalog_bundle(
            path / "MANIFEST.md",
            path / "entries.parquet",
        )
    raise CatalogError(
        "Catalog directory must contain release.json, or MANIFEST.md with "
        "entries/ or entries.parquet."
    )


def _release_location(
    source: _LocalSource | _RemoteSource,
    storage_options: Mapping[str, object],
) -> _ReleaseLocation:
    if isinstance(source, _LocalSource):
        path = source.path
        descriptor = path / "release.json" if path.is_dir() else path
        if descriptor.name not in _DESCRIPTOR_NAMES:
            raise CatalogError(
                "Catalog file sources must be named catalog.json or release.json."
            )
        if not descriptor.is_file():
            raise CatalogError(f"Catalog source does not exist: {descriptor}")
        release = _parse_release(_read_local_bytes(descriptor, _MAX_JSON_BYTES))
        base = (
            descriptor.parent / "catalog" / "releases" / release.digest
            if descriptor.name == "catalog.json"
            else descriptor.parent
        )
        return _ReleaseLocation(release, base, "local", storage_options)

    name = _uri_name(source.uri)
    if name not in _DESCRIPTOR_NAMES:
        raise CatalogError(
            "Remote catalog sources must name catalog.json or release.json."
        )
    release = _parse_release(
        _read_remote_bytes(
            source.uri,
            transport=source.transport,
            storage_options=storage_options,
            limit=_MAX_JSON_BYTES,
            no_cache=name == "catalog.json",
        )
    )
    base = (
        _join_uri_path(_uri_parent(source.uri), "catalog", "releases", release.digest)
        if name == "catalog.json"
        else _uri_parent(source.uri)
    )
    return _ReleaseLocation(release, base, source.transport, storage_options)


def _normalize_source(
    source: str | PathLike[str] | None,
) -> _LocalSource | _RemoteSource:
    if source is None:
        return _RemoteSource(_OFFICIAL_CATALOG_URL, "http")
    if not isinstance(source, str):
        value = os.fspath(source)
        if not isinstance(value, str):
            raise TypeError("Catalog source paths must contain text.")
        return _LocalSource(Path(value))

    scheme = _path_scheme(source)
    if scheme is None:
        return _LocalSource(Path(source))
    scheme = scheme.lower()
    if scheme == "file":
        return _LocalSource(_file_uri_path(source))
    if scheme in {"http", "https"}:
        return _RemoteSource(source, "http")
    if scheme in _CLOUD_SCHEMES:
        return _RemoteSource(source, "cloud")
    raise CatalogError(f"Unsupported catalog source scheme: {scheme}.")


def _path_scheme(value: str) -> str | None:
    index = value.find("://")
    return None if index < 0 else value[:index]


def _file_uri_path(uri: str) -> Path:
    parsed = urlsplit(uri)
    if parsed.query or parsed.fragment or parsed.netloc not in {"", "localhost"}:
        raise CatalogError("file:// catalog sources must name a local path.")
    try:
        return Path(url2pathname(unquote(parsed.path)))
    except (UnicodeDecodeError, ValueError) as exc:
        raise CatalogError("file:// catalog source is invalid.") from exc


def _parse_release(data: bytes) -> CatalogRelease:
    try:
        value = json.loads(data.decode("utf-8"))
        release = CatalogRelease.from_mapping(value)
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise CatalogError(f"Catalog release descriptor is invalid: {exc}") from exc
    if release.digest != release_digest(release.artifacts):
        raise CatalogError("Catalog release digest does not match its artifact set.")
    for path, artifact in release.artifacts.items():
        if artifact.bytes > MAX_RELEASE_ARTIFACT_BYTES:
            raise CatalogError(f"Catalog artifact exceeds the 1 GiB limit: {path}")
        if (
            path in {"MANIFEST.md", "entries.parquet"}
            and artifact.bytes > _MAX_CORE_ARTIFACT_BYTES
        ):
            raise CatalogError(f"Catalog artifact exceeds the 64 MiB limit: {path}")
    return release


def _read_local_bytes(path: Path, limit: int) -> bytes:
    try:
        size = path.stat().st_size
        if size > limit:
            raise CatalogError("Catalog JSON exceeds the 1 MiB limit.")
        with path.open("rb") as source:
            data = source.read(limit + 1)
    except OSError as exc:
        raise CatalogError(f"Could not read catalog source: {path}") from exc
    if len(data) > limit:
        raise CatalogError("Catalog JSON exceeds the 1 MiB limit.")
    return data


def _read_remote_bytes(
    uri: str,
    *,
    transport: Literal["http", "cloud"],
    storage_options: Mapping[str, object],
    limit: int,
    no_cache: bool = False,
) -> bytes:
    data = bytearray()
    for chunk in _remote_chunks(
        uri,
        transport=transport,
        storage_options=storage_options,
        no_cache=no_cache,
    ):
        view = memoryview(chunk)
        if len(data) + view.nbytes > limit:
            raise CatalogError("Catalog JSON exceeds the 1 MiB limit.")
        data.extend(view)
    return bytes(data)


def _remote_chunks(
    uri: str,
    *,
    transport: Literal["http", "cloud"],
    storage_options: Mapping[str, object],
    no_cache: bool = False,
) -> Iterable[bytes | bytearray | memoryview]:
    if transport == "cloud":
        yield from _cloud_chunks(uri, storage_options)
        return

    headers, timeout = _http_options(storage_options)
    if no_cache:
        headers["Cache-Control"] = "no-cache"
    request = Request(uri, headers=headers)
    try:
        with urlopen(request, timeout=timeout) as response:
            while chunk := response.read(_READ_CHUNK_BYTES):
                yield chunk
    except OSError as exc:
        raise CatalogError("Failed to load catalog resource over HTTP.") from exc


def _cloud_chunks(
    uri: str,
    storage_options: Mapping[str, object],
) -> Iterable[bytes | bytearray | memoryview]:
    try:
        from obstore.store import from_url
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Cloud catalog sources require the optional `chartcoach[cloud]` "
            "dependencies.",
            name=exc.name,
        ) from exc

    try:
        store_factory = cast(Any, from_url)
        store = store_factory(
            _obstore_uri(_uri_parent(uri)),
            **dict(storage_options),
        )
        yield from store.get(_uri_name(uri))
    except Exception as exc:
        raise CatalogError(
            "Failed to load catalog resource from cloud storage."
        ) from exc


def _http_options(
    storage_options: Mapping[str, object],
) -> tuple[dict[str, str], float]:
    options = dict(storage_options)
    unsupported = set(options) - {"headers", "timeout"}
    if unsupported:
        names = ", ".join(sorted(unsupported))
        raise CatalogError(f"Unsupported HTTP storage options: {names}.")

    raw_headers = options.get("headers", {})
    if not isinstance(raw_headers, Mapping) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in raw_headers.items()
    ):
        raise CatalogError("HTTP storage option headers must map strings to strings.")
    raw_timeout = options.get("timeout", 900.0)
    if isinstance(raw_timeout, bool) or not isinstance(raw_timeout, int | float):
        raise CatalogError("HTTP storage option timeout must be a positive number.")
    timeout = float(raw_timeout)
    if timeout <= 0:
        raise CatalogError("HTTP storage option timeout must be a positive number.")
    headers = {cast(str, key): cast(str, value) for key, value in raw_headers.items()}
    return headers, timeout


def _cache_remote_artifact(
    uri: str,
    *,
    transport: Literal["http", "cloud"],
    storage_options: Mapping[str, object],
    path: str,
    artifact: ReleaseArtifact,
) -> Path:
    target = _cache_root() / "artifacts" / artifact.sha256
    if _cached_artifact_is_valid(target, artifact):
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = target.parent / f".{artifact.sha256}.{uuid4().hex}.tmp"
    digest = hashlib.sha256()
    size = 0
    try:
        with staging.open("xb") as output:
            for chunk in _remote_chunks(
                uri,
                transport=transport,
                storage_options=storage_options,
            ):
                view = memoryview(chunk)
                size += view.nbytes
                if size > artifact.bytes:
                    raise CatalogError(f"Catalog artifact byte count mismatch: {path}")
                digest.update(view)
                output.write(view)
        if size != artifact.bytes:
            raise CatalogError(f"Catalog artifact byte count mismatch: {path}")
        if digest.hexdigest() != artifact.sha256:
            raise CatalogError(f"Catalog artifact SHA-256 mismatch: {path}")
        os.replace(staging, target)
    finally:
        staging.unlink(missing_ok=True)
    return target


def _cached_artifact_is_valid(path: Path, artifact: ReleaseArtifact) -> bool:
    try:
        return (
            path.is_file()
            and path.stat().st_size == artifact.bytes
            and sha256_file(path) == artifact.sha256
        )
    except OSError:
        return False


def _verify_local_artifact(
    base: Path,
    path: Path,
    artifact_path: str,
    artifact: ReleaseArtifact,
) -> None:
    try:
        if _symlink_component(base, path) is not None or not path.is_file():
            raise CatalogError(f"Catalog artifact is missing: {artifact_path}")
        size = path.stat().st_size
    except OSError as exc:
        raise CatalogError(f"Could not read catalog artifact: {artifact_path}") from exc
    if size != artifact.bytes:
        raise CatalogError(f"Catalog artifact byte count mismatch: {artifact_path}")
    if sha256_file(path) != artifact.sha256:
        raise CatalogError(f"Catalog artifact SHA-256 mismatch: {artifact_path}")


def _symlink_component(base: Path, path: Path) -> Path | None:
    base = base.absolute()
    try:
        relative = path.absolute().relative_to(base)
    except ValueError:
        return path
    current = base
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            return current
    return None


def _cached_index(archive: Path, digest: str) -> Path:
    target = _cache_root() / "indexes" / digest
    if _index_cache_is_complete(target, digest):
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(target, ignore_errors=True)
    with TemporaryDirectory(prefix=f".{digest}.", dir=target.parent) as temporary:
        staged = Path(temporary) / "index"
        extract_tar_archive(archive, staged)
        if not (staged / f"{LANCE_DOCUMENT_TABLE}.lance").is_dir():
            raise CatalogError(
                f"LanceDB archive does not contain table: {LANCE_DOCUMENT_TABLE}"
            )
        (staged / _CACHE_MARKER).write_text(digest, encoding="ascii")
        try:
            os.replace(staged, target)
        except FileExistsError:
            if not _index_cache_is_complete(target, digest):
                raise
    return target


def _index_cache_is_complete(target: Path, digest: str) -> bool:
    try:
        return (target / _CACHE_MARKER).read_text(encoding="ascii") == digest and (
            target / f"{LANCE_DOCUMENT_TABLE}.lance"
        ).is_dir()
    except (OSError, UnicodeDecodeError):
        return False


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


def _copy_storage_options(
    storage_options: Mapping[str, object] | None,
) -> dict[str, object]:
    if storage_options is None:
        return {}
    if not isinstance(storage_options, Mapping) or not all(
        isinstance(key, str) for key in storage_options
    ):
        raise TypeError("storage_options must map strings to values.")
    return dict(storage_options)


def _cache_root() -> Path:
    return user_cache_path("chartcoach", appauthor=False)


def _uri_name(uri: str) -> str:
    return PurePosixPath(unquote(urlsplit(uri).path)).name


def _uri_parent(uri: str) -> str:
    parsed = urlsplit(uri)
    parent = PurePosixPath(parsed.path).parent.as_posix()
    if not parent.startswith("/"):
        parent = f"/{parent}"
    if not parent.endswith("/"):
        parent += "/"
    return urlunsplit((parsed.scheme, parsed.netloc, parent, "", ""))


def _join_uri_path(base: str, *parts: str) -> str:
    parsed = urlsplit(base)
    path = PurePosixPath(parsed.path, *parts).as_posix()
    if not path.startswith("/"):
        path = f"/{path}"
    return urlunsplit((parsed.scheme, parsed.netloc, path, "", ""))


def _obstore_uri(uri: str) -> str:
    parsed = urlsplit(uri)
    scheme = {"gcp": "gs", "gcs": "gs"}.get(parsed.scheme.lower(), parsed.scheme)
    return urlunsplit(
        (scheme, parsed.netloc, parsed.path, parsed.query, parsed.fragment)
    )


__all__ = ["open_catalog", "open_index"]
