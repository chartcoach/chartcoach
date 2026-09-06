from __future__ import annotations

import json
from collections.abc import Mapping
from os import PathLike
from pathlib import Path, PurePosixPath
from typing import Any, Protocol, cast
from urllib.parse import urlsplit

from obspec import Get, Put
from obspec.exceptions import AlreadyExistsError, NotFoundError, map_exception
from obstore.store import from_url

from .._object_store import CATALOG_STORE_SCHEMES, copy_storage_options, obstore_uri
from ..paths import paths
from ..releases import CatalogRelease
from ..releases.hashing import release_digest
from ..releases.models import safe_sha256
from .validation import validate_release

_MAX_JSON_BYTES = 1024 * 1024


class _ReleaseStore(Get, Put, Protocol):
    """Object-store operations used to publish a release."""


def publish_release(
    source: PathLike[str],
    destination: str,
    *,
    storage_options: Mapping[str, object] | None = None,
) -> CatalogRelease:
    """Publish one immutable release to a destination URI."""

    return _publish_release(
        _open_store(destination, storage_options),
        Path(source),
    )


def select_release(
    digest: str,
    destination: str,
    *,
    storage_options: Mapping[str, object] | None = None,
) -> CatalogRelease:
    """Select a published release through the destination catalog.json."""

    return _select_release(
        _open_store(destination, storage_options),
        digest,
    )


def _publish_release(
    destination: _ReleaseStore,
    root: Path,
) -> CatalogRelease:
    """Validate and write one immutable release, committing release.json last."""

    release = validate_release(root)
    release_paths = paths.release(release.digest)
    release_path = release_paths.json()
    if existing := _existing_release(destination, release_path):
        if existing != release:
            raise ValueError(
                f"Published catalog release does not match: {release_path}"
            )
        return release

    for artifact_path in release.artifacts:
        source_path = root.joinpath(*PurePosixPath(artifact_path).parts)
        with source_path.open("rb") as source:
            destination.put(
                release_paths.artifact(artifact_path),
                source,
                mode="overwrite",
                use_multipart=True,
            )

    try:
        destination.put(release_path, _release_json_bytes(release), mode="create")
    except Exception as exc:
        if not isinstance(map_exception(exc), AlreadyExistsError):
            raise
        existing = _read_release(destination, release_path)
        if existing != release:
            raise ValueError(
                f"Published catalog release does not match: {release_path}"
            ) from exc
    return release


def _select_release(store: _ReleaseStore, digest: str) -> CatalogRelease:
    """Select an existing immutable release by digest."""

    digest = safe_sha256(digest, label="Catalog release digest")
    release = _read_release(store, paths.release(digest).json())
    if release.digest != digest or release.digest != release_digest(release.artifacts):
        raise ValueError(f"Catalog release does not match digest {digest!r}.")
    store.put(
        paths.selected(),
        _release_json_bytes(release),
        mode="overwrite",
    )
    return release


def _open_store(
    destination: str,
    storage_options: Mapping[str, object] | None,
) -> _ReleaseStore:
    scheme = urlsplit(destination).scheme.lower()
    if scheme not in CATALOG_STORE_SCHEMES:
        choices = ", ".join(sorted(f"{value}://" for value in CATALOG_STORE_SCHEMES))
        raise ValueError(f"Catalog destination must use one of: {choices}.")
    options = copy_storage_options(storage_options)
    if scheme == "file":
        options.setdefault("mkdir", True)
    store_factory = cast(Any, from_url)
    return cast(_ReleaseStore, store_factory(obstore_uri(destination), **options))


def _existing_release(source: Get, path: str) -> CatalogRelease | None:
    try:
        return _read_release(source, path)
    except Exception as exc:
        if isinstance(map_exception(exc), NotFoundError):
            return None
        raise


def _read_release(source: Get, path: str) -> CatalogRelease:
    return CatalogRelease.from_mapping(_read_json(source, path))


def _read_json(source: Get, path: str) -> object:
    data = bytearray()
    for buffer in source.get(path):
        view = memoryview(buffer)
        if len(data) + view.nbytes > _MAX_JSON_BYTES:
            raise ValueError("Catalog release JSON exceeds the 1 MiB limit.")
        data.extend(view)
    return json.loads(data)


def _release_json_bytes(release: CatalogRelease) -> bytes:
    data = json.dumps(
        release.to_record(),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    if len(data) > _MAX_JSON_BYTES:
        raise ValueError("Catalog release JSON exceeds the 1 MiB limit.")
    return data


__all__ = ["publish_release", "select_release"]
