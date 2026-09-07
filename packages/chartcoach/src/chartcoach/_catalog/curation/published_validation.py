from __future__ import annotations

import hashlib
import json
from collections.abc import Iterator, Mapping
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from typing import Any, cast
from urllib.parse import urlsplit

from obspec import Get
from obspec.exceptions import NotFoundError, map_exception
from obstore.store import from_url

from .._object_store import CATALOG_STORE_SCHEMES, copy_storage_options, obstore_uri
from ..errors import CatalogOperationError
from ..paths import paths
from ..profile_layout import discover_profile_artifacts
from ..profiles import MAX_PROFILE_BYTES, ProfileMetadata
from ..releases import CatalogRelease
from ..releases.hashing import release_digest
from ..releases.models import ReleaseArtifact, safe_sha256
from ..releases.services import validate_artifact_size
from .validation import validate_release

_MAX_JSON_BYTES = 1024 * 1024


def validate_published_release(
    destination: str,
    *,
    digest: str | None = None,
    storage_options: Mapping[str, object] | None = None,
) -> CatalogRelease:
    """Validate fresh published bytes for a selected or exact catalog release.

    Omit digest to verify catalog.json against its published release.json.
    Artifact bytes are streamed into temporary files and fully validated.
    The destination and runtime cache remain unchanged.
    """

    if digest is not None:
        digest = safe_sha256(digest, label="Catalog release digest")
    return _validate_published_release(
        _open_store(destination, storage_options), digest
    )


def _validate_published_release(
    source: Get, digest: str | None = None
) -> CatalogRelease:
    selected = None
    if digest is None:
        selected = _read_release(source, paths.selected())
        digest = selected.digest
    else:
        digest = safe_sha256(digest, label="Catalog release digest")
    release_paths = paths.release(digest)
    release = _read_release(source, release_paths.json())
    if release.digest != digest:
        raise ValueError(
            "Published release digest does not match its requested location."
        )
    if selected is not None and selected != release:
        raise ValueError(
            "Selected catalog.json does not match its published release.json."
        )
    if release.digest != release_digest(release.artifacts):
        raise ValueError("Published release digest does not match its artifacts.")
    profiles = discover_profile_artifacts(release.artifacts)
    metadata_paths = {profile.metadata for profile in profiles.values()}
    for path, artifact in release.artifacts.items():
        validate_artifact_size(path, artifact)
        if path in metadata_paths and artifact.bytes > MAX_PROFILE_BYTES:
            raise ValueError(f"Profile metadata exceeds the 64 KiB limit: {path}")

    with TemporaryDirectory(prefix="chartcoach-published-") as directory:
        root = Path(directory)
        (root / "release.json").write_bytes(_release_json_bytes(release))
        ordered_paths = [
            *sorted(metadata_paths),
            *(path for path in release.artifacts if path not in metadata_paths),
        ]
        for path in ordered_paths:
            target = root.joinpath(*PurePosixPath(path).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            _download_artifact(
                source, release_paths.artifact(path), release.artifacts[path], target
            )
            if path in metadata_paths:
                ProfileMetadata.from_bytes(target.read_bytes())
        return validate_release(root)


def _open_store(
    destination: str,
    storage_options: Mapping[str, object] | None,
    *,
    create: bool = False,
) -> Get:
    scheme = urlsplit(destination).scheme.lower()
    if scheme not in CATALOG_STORE_SCHEMES:
        choices = ", ".join(sorted(f"{value}://" for value in CATALOG_STORE_SCHEMES))
        raise ValueError(f"Catalog destination must use one of: {choices}.")
    options = copy_storage_options(storage_options)
    if scheme == "file":
        if create:
            options.setdefault("mkdir", True)
        else:
            options["mkdir"] = False
    try:
        store_factory = cast(Any, from_url)
        return cast(Get, store_factory(obstore_uri(destination), **options))
    except Exception as exc:
        raise CatalogOperationError(
            "Catalog object store could not be opened.",
            hints=[
                "Check the destination URI, storage options, and access credentials."
            ],
        ) from exc


def _object_chunks(source: Get, path: str) -> Iterator[memoryview]:
    try:
        for buffer in source.get(path):
            yield memoryview(buffer)
    except Exception as exc:
        if isinstance(map_exception(exc), NotFoundError):
            raise FileNotFoundError(
                f"Published catalog object is missing: {path}"
            ) from exc
        raise CatalogOperationError(
            f"Published catalog object could not be read: {path}",
            hints=["Check that the object exists and the storage client can read it."],
        ) from exc


def _read_release(source: Get, path: str) -> CatalogRelease:
    data = bytearray()
    for view in _object_chunks(source, path):
        if len(data) + view.nbytes > _MAX_JSON_BYTES:
            raise ValueError("Catalog release JSON exceeds the 1 MiB limit.")
        data.extend(view)
    return CatalogRelease.from_mapping(json.loads(data))


def _download_artifact(
    source: Get, path: str, artifact: ReleaseArtifact, target: Path
) -> None:
    size = 0
    checksum = hashlib.sha256()
    with target.open("wb") as output:
        for view in _object_chunks(source, path):
            size += view.nbytes
            if size > artifact.bytes:
                raise ValueError(f"Catalog artifact byte count does not match: {path}")
            checksum.update(view)
            output.write(view)
    if size != artifact.bytes:
        raise ValueError(f"Catalog artifact byte count does not match: {path}")
    if checksum.hexdigest() != artifact.sha256:
        raise ValueError(f"Catalog artifact SHA-256 does not match: {path}")


def _release_json_bytes(release: CatalogRelease) -> bytes:
    data = json.dumps(
        release.to_record(), ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    if len(data) > _MAX_JSON_BYTES:
        raise ValueError("Catalog release JSON exceeds the 1 MiB limit.")
    return data


__all__ = ["validate_published_release"]
