from __future__ import annotations

from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Literal
from urllib.parse import urlparse

from .remote import (
    DownloadReporter,
    default_catalog_bundle,
    download_catalog_bundle,
    release_metadata_url,
)

if TYPE_CHECKING:
    from .collection import Catalog

CatalogSource = str | PathLike[str] | None
CatalogSourceKind = Literal["default", "metadata-url", "bundle", "folder", "parquet"]


@dataclass(frozen=True, slots=True)
class CatalogLocation:
    """Resolved catalog source kind and locator data."""

    kind: CatalogSourceKind
    source: CatalogSource
    path: Path | None = None
    metadata_url: str | None = None

    @property
    def is_default(self) -> bool:
        return self.kind == "default"


def locate_catalog(source: CatalogSource = None) -> CatalogLocation:
    """Classify a catalog source without loading it."""

    if source is None:
        return CatalogLocation(kind="default", source=None)
    if isinstance(source, str) and _is_http_url(source):
        return CatalogLocation(
            kind="metadata-url",
            source=source,
            metadata_url=release_metadata_url(source),
        )

    path = Path(source)
    if path.is_dir():
        if (path / "entries.parquet").exists():
            return CatalogLocation(kind="bundle", source=source, path=path)
        return CatalogLocation(kind="folder", source=source, path=path)
    return CatalogLocation(kind="parquet", source=source, path=path)


def open_catalog(
    source: CatalogSource | CatalogLocation = None,
    *,
    reporter: DownloadReporter | None = None,
) -> "Catalog":
    """Load a catalog from a default, remote, local folder, bundle, or parquet file."""

    from .collection import Catalog

    location = source if isinstance(source, CatalogLocation) else locate_catalog(source)
    if location.kind == "default":
        return Catalog.from_bundle(default_catalog_bundle(reporter=reporter))
    if location.kind == "metadata-url":
        if location.metadata_url is None:
            raise ValueError("Catalog metadata URL location is missing metadata_url.")
        return Catalog.from_bundle(
            download_catalog_bundle(location.metadata_url, reporter=reporter)
        )
    if location.path is None:
        raise ValueError("Catalog file location is missing path.")
    if location.kind == "bundle":
        return Catalog.from_bundle(location.path)
    if location.kind == "folder":
        return Catalog.from_folder(location.path)
    return Catalog.from_parquet(location.path)


def _is_http_url(value: str) -> bool:
    return urlparse(value).scheme in {"http", "https"}


__all__ = [
    "CatalogLocation",
    "CatalogSource",
    "CatalogSourceKind",
    "locate_catalog",
    "open_catalog",
]
