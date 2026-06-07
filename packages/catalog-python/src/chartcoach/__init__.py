"""ChartCoach exposes catalog, guideline, and section models."""

from importlib.metadata import version

from .catalog.collection import Catalog
from .catalog.manifest import CatalogManifest
from .guideline.core import Guideline, Section
from .guideline.labels import ParsedLabel, parse_label

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
