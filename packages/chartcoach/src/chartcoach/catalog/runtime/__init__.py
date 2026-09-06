from __future__ import annotations

from collections.abc import Mapping
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

from ...constants import LANCE_DOCUMENT_TABLE
from .._object_store import copy_storage_options
from ..errors import CatalogError
from ..releases.models import safe_relative_path
from .cache import cached_index
from .release import ReleaseLocation, profile_ids, release_location
from .source import LocalSource, normalize_source

if TYPE_CHECKING:
    from lancedb import Table

    from ..collection import Catalog


def open_catalog(
    source: str | PathLike[str] | None = None,
    *,
    storage_options: Mapping[str, object] | None = None,
) -> Catalog:
    """Open an authored catalog, bundle, or release descriptor."""

    options = copy_storage_options(storage_options)
    normalized = normalize_source(source)
    if isinstance(normalized, LocalSource) and normalized.path.is_dir():
        direct = _open_local_directory(normalized.path)
        if direct is not None:
            return direct

    return _open_release_catalog(release_location(normalized, options))


def open_index(
    source: str | PathLike[str] | None = None,
    *,
    profile: str,
    storage_options: Mapping[str, object] | None = None,
) -> Table:
    """Open one release-backed native LanceDB profile."""

    options = copy_storage_options(storage_options)
    normalized = normalize_source(source)
    _require_release_source(normalized)
    return _open_release_index(
        release_location(normalized, options),
        profile=profile,
    )


def open_catalog_index(
    source: str | PathLike[str] | None = None,
    *,
    profile: str,
    storage_options: Mapping[str, object] | None = None,
) -> tuple[Catalog, Table]:
    """Open one release snapshot as a catalog and native index table."""

    options = copy_storage_options(storage_options)
    normalized = normalize_source(source)
    _require_release_source(normalized)
    location = release_location(normalized, options)
    return (
        _open_release_catalog(location),
        _open_release_index(location, profile=profile),
    )


def _open_release_catalog(location: ReleaseLocation) -> Catalog:
    from ..collection import _load_catalog_bundle

    return _load_catalog_bundle(
        location.artifact_path("MANIFEST.md"),
        location.artifact_path("entries.parquet"),
        release=location.release,
    )


def _open_release_index(location: ReleaseLocation, *, profile: str) -> Table:
    profile = safe_relative_path(profile, label="Embedding profile")
    artifact_path = f"profiles/{profile}/index.tar.gz"
    try:
        archive = location.artifact_path(artifact_path)
        artifact = location.release.artifact(artifact_path)
    except KeyError:
        choices = ", ".join(repr(value) for value in profile_ids(location.release))
        raise CatalogError(
            f"Catalog release does not publish profile {profile!r}. "
            f"Available profiles: {choices or 'none'}."
        ) from None

    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Release-backed indexes require the optional `chartcoach[index]` "
            "dependencies.",
            name=exc.name,
        ) from exc
    index_path = cached_index(archive, artifact.sha256)
    try:
        return lancedb.connect(index_path).open_table(LANCE_DOCUMENT_TABLE)
    except (OSError, RuntimeError, ValueError):
        index_path = cached_index(archive, artifact.sha256, refresh=True)
        return lancedb.connect(index_path).open_table(LANCE_DOCUMENT_TABLE)


def _require_release_source(source: object) -> None:
    if (
        isinstance(source, LocalSource)
        and source.path.is_dir()
        and not (source.path / "release.json").is_file()
    ):
        raise CatalogError(
            "Index sources must be a release directory, catalog.json, or "
            "release.json path or URI."
        )


def _open_local_directory(path: Path) -> Catalog | None:
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
        from ..storage import load_catalog

        return load_catalog(path)
    if bundle:
        from ..collection import _load_catalog_bundle

        return _load_catalog_bundle(
            path / "MANIFEST.md",
            path / "entries.parquet",
        )
    raise CatalogError(
        "Catalog directory must contain release.json, or MANIFEST.md with "
        "entries/ or entries.parquet."
    )


__all__ = ["open_catalog", "open_catalog_index", "open_index"]
