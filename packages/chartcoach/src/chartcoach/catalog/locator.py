from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

from ..constants import LANCE_DOCUMENT_TABLE
from .releases.models import CatalogRelease, safe_sha256

if TYPE_CHECKING:
    from lancedb import Table

    from .collection import Catalog


def open_catalog(
    source: str | PathLike[str] | None = None,
) -> "Catalog":
    """Load a local catalog or a published release."""

    from .collection import Catalog

    published = _published_release_reference(source)
    if source is None or published is not None:
        from .curation.cache import download_catalog_bundle

        _release, bundle = download_catalog_bundle(published)
        return Catalog.from_bundle(bundle)

    path = Path(source)
    if path.is_dir() and (path / "entries.parquet").exists():
        return Catalog.from_bundle(path)
    if path.is_dir():
        return Catalog.from_folder(path)
    raise ValueError("Catalog source must be an authored folder or a bundle directory.")


def open_index(
    source: str | PathLike[str] | None = None,
    *,
    profile: str | None = None,
) -> "Table":
    """Open the fixed document table from a local or published index."""

    published = _published_release_reference(source)
    location: str | PathLike[str]
    if source is None or published is not None:
        if profile is None:
            raise ValueError("Pass profile for a published LanceDB index.")
        from .curation.cache import download_index_artifact

        location = download_index_artifact(published, profile=profile)
    else:
        location = source

    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "LanceDB indexes require the optional `chartcoach[index]` dependencies.",
            name=exc.name,
        ) from exc
    uri = location if isinstance(location, str) else Path(location)
    return lancedb.connect(uri).open_table(LANCE_DOCUMENT_TABLE)


def resolve_release(reference: str | None = None) -> CatalogRelease:
    """Read the public catalog entry document or one exact release."""

    published = _published_release_reference(reference)
    if reference is not None and published is None:
        raise ValueError("Catalog release reference must be a digest.")
    from .curation.cache import read_release, artifact_store

    return read_release(artifact_store(), published)


def _published_release_reference(
    locator: str | PathLike[str] | None,
) -> str | None:
    if not isinstance(locator, str):
        return None
    try:
        return safe_sha256(locator, label="Catalog release digest")
    except ValueError:
        return None


__all__ = ["open_catalog", "open_index", "resolve_release"]
