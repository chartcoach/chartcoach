from __future__ import annotations

from collections.abc import Mapping
from os import PathLike
from pathlib import Path

from .._object_store import copy_storage_options
from ..errors import CatalogError, CatalogProfileError
from ..manifest import CatalogManifest, manifest_digest
from ..model import Catalog, _read_catalog_parquet
from ..profile_layout import discover_profile_artifacts
from .location import LocalCatalogLocation, normalize_location
from .profiles import load_profile_metadata, open_profile_index
from .release import ReleaseLocation, release_location


def open_catalog(
    location: str | PathLike[str] | None = None,
    *,
    storage_options: Mapping[str, object] | None = None,
) -> Catalog:
    """Open one authored catalog, bundle, or verified catalog release."""

    options = copy_storage_options(storage_options)
    normalized = normalize_location(location)
    if isinstance(normalized, LocalCatalogLocation) and normalized.path.is_dir():
        return _open_local_directory(normalized.path.absolute(), options)

    return _open_release_catalog(release_location(normalized, options))


def _open_release_catalog(location: ReleaseLocation) -> Catalog:
    try:
        profiles = discover_profile_artifacts(location.release.artifacts)
    except ValueError as exc:
        raise CatalogProfileError(f"Catalog profile layout is invalid: {exc}") from exc
    manifest_path = location.artifact_path("MANIFEST.md")
    entries_path = location.artifact_path("entries.parquet")
    manifest = CatalogManifest.from_path(manifest_path)
    frame = _read_catalog_parquet(entries_path)
    catalog = Catalog(frame, manifest=manifest)
    entries_digest = catalog.entries_digest()
    catalog_manifest_digest = manifest_digest(manifest.markdown)

    def profile_loader(profile: str):
        return load_profile_metadata(
            location,
            profile,
            profiles=profiles,
            entries_digest=entries_digest,
            manifest_digest=catalog_manifest_digest,
        )

    def index_loader(profile: str, directory: Path | None, public: bool):
        return open_profile_index(
            location,
            profile,
            profiles=profiles,
            metadata=profile_loader(profile),
            directory=directory,
            public=public,
        )

    return Catalog._from_runtime(
        catalog,
        release=location.release,
        resolved_location=location.resolved_location,
        profile_names=tuple(profiles),
        profile_loader=profile_loader,
        index_loader=index_loader,
        artifact_loader=location.artifact_path,
        cache_loader=location.cache,
    )


def _open_local_directory(
    path: Path,
    storage_options: Mapping[str, object],
) -> Catalog:
    selection_path = path / "catalog.json"
    release_path = path / "release.json"
    if selection_path.is_file() and release_path.is_file():
        raise CatalogError(
            "Catalog directory is ambiguous because it contains both catalog.json "
            "and release.json."
        )
    if selection_path.is_file():
        return _open_release_catalog(
            release_location(LocalCatalogLocation(selection_path), storage_options)
        )
    if release_path.is_file():
        return _open_release_catalog(
            release_location(LocalCatalogLocation(release_path), storage_options)
        )

    manifest_exists = (path / "MANIFEST.md").is_file()
    authored = manifest_exists and (path / "entries").is_dir()
    bundle = manifest_exists and (path / "entries.parquet").is_file()
    if authored and bundle:
        raise CatalogError(
            "Catalog directory is ambiguous because it contains both entries/ "
            "and entries.parquet."
        )
    if authored:
        from ..authored import load_catalog

        catalog = load_catalog(path)
    elif bundle:
        manifest = CatalogManifest.from_path(path / "MANIFEST.md")
        catalog = Catalog(
            _read_catalog_parquet(path / "entries.parquet"),
            manifest=manifest,
        )
    else:
        raise CatalogError(
            "Catalog directory must contain catalog.json, release.json, or "
            "MANIFEST.md with entries/ or entries.parquet."
        )
    return Catalog._from_runtime(
        catalog,
        release=None,
        resolved_location=str(path),
    )


__all__ = ["open_catalog"]
