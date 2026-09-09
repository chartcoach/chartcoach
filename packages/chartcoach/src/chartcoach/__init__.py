"""Load Guideline Catalog entries, releases, and LanceDB indexes."""

from __future__ import annotations

from importlib.metadata import version

from ._catalog import (
    Catalog,
    CatalogError,
    CatalogInfo,
    CatalogManifest,
    CatalogRelease,
    CitationRecord,
    CitationSource,
    GuidelineEntryRecord,
    ProfileInfo,
    SectionRecord,
    SourceDetail,
    TableColumnInfo,
    TableInfo,
    open_catalog,
)
from ._catalog.guidelines import Guideline, Section
from ._catalog.manifest import ManifestDefinition
from ._catalog.read import FullSourceRecord, MinimalSourceRecord
from ._catalog.releases import ReleaseArtifact

__version__ = version("chartcoach")

__all__ = [
    "Catalog",
    "CatalogError",
    "CatalogInfo",
    "CatalogManifest",
    "CatalogRelease",
    "CitationRecord",
    "CitationSource",
    "FullSourceRecord",
    "Guideline",
    "GuidelineEntryRecord",
    "ManifestDefinition",
    "MinimalSourceRecord",
    "ProfileInfo",
    "ReleaseArtifact",
    "Section",
    "SectionRecord",
    "SourceDetail",
    "TableColumnInfo",
    "TableInfo",
    "__version__",
    "open_catalog",
]
