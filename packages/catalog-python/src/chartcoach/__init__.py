"""ChartCoach exposes catalog, entry, and section models."""

from importlib.metadata import version

from .catalog.collection import Catalog
from .catalog.entries import Guideline, Section
from .catalog.labels import ParsedLabel, parse_label
from .catalog.manifest import CatalogManifest

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogManifest",
    "Guideline",
    "ParsedLabel",
    "Section",
    "parse_label",
]
