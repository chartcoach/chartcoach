"""Load Guideline Catalog entries, releases, and LanceDB indexes."""

from __future__ import annotations

from importlib.metadata import version

from .catalog import (
    Catalog,
    CatalogError,
    CatalogInfo,
    CatalogManifest,
    CatalogRelease,
    CitationRecord,
    CitationSource,
    GuidelineEntryRecord,
    GuidelineMatch,
    ProfileInfo,
    SearchResult,
    SectionRecord,
    SourceDetail,
    SqlColumn,
    SqlResult,
    open_catalog,
)

__version__ = version("chartcoach")

__all__ = [
    "Catalog",
    "CatalogError",
    "CatalogInfo",
    "CatalogManifest",
    "CatalogRelease",
    "CitationRecord",
    "CitationSource",
    "GuidelineEntryRecord",
    "GuidelineMatch",
    "ProfileInfo",
    "SearchResult",
    "SectionRecord",
    "SourceDetail",
    "SqlColumn",
    "SqlResult",
    "__version__",
    "open_catalog",
]
