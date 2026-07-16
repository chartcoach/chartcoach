"""Load catalog records, releases, and native LanceDB indexes."""

from __future__ import annotations

from importlib.metadata import version

from .catalog import (
    Catalog,
    CatalogManifest,
    CatalogRelease,
    open_catalog,
    open_index,
    paths,
    resolve_release,
)

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogManifest",
    "CatalogRelease",
    "open_catalog",
    "open_index",
    "paths",
    "resolve_release",
]
