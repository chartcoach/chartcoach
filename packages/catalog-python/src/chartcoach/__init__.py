"""ChartCoach exposes catalog, guideline, and section models."""

from importlib.metadata import version

from .catalog.collection import Catalog, CatalogEntry
from .catalog.manifest import CatalogManifest
from .guideline.core import Guideline, Section
from .guideline.labels import ParsedLabel, parse_label
from .tools import CatalogToolError, CatalogTools

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogEntry",
    "CatalogManifest",
    "CatalogToolError",
    "CatalogTools",
    "Guideline",
    "ParsedLabel",
    "Section",
    "parse_label",
]
