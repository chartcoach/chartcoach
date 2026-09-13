from __future__ import annotations

from collections.abc import Mapping
from os import PathLike
from pathlib import Path, PurePosixPath
from typing import Protocol, cast

from obspec import Get, Put
from obspec.exceptions import AlreadyExistsError, NotFoundError, map_exception

from ..paths import paths
from ..releases import CatalogRelease
from .published_validation import (
    _open_store,
    _read_release,
    _release_json_bytes,
    _validate_published_release,
)
from .validation import validate_release


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
        cast(_ReleaseStore, _open_store(destination, storage_options, create=True)),
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
        cast(_ReleaseStore, _open_store(destination, storage_options)),
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
        return _validate_published_release(destination, release.digest)

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
        return _validate_published_release(destination, release.digest)
    return release


def _select_release(store: _ReleaseStore, digest: str) -> CatalogRelease:
    """Select an existing immutable release by digest."""

    release = _validate_published_release(store, digest)
    store.put(
        paths.selected(),
        _release_json_bytes(release),
        mode="overwrite",
    )
    return release


def _existing_release(source: Get, path: str) -> CatalogRelease | None:
    try:
        return _read_release(source, path)
    except Exception as exc:
        if isinstance(map_exception(exc), NotFoundError):
            return None
        raise


__all__ = ["publish_release", "select_release"]
