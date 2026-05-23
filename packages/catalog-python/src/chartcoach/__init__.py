"""ChartCoach helps you search and inspect a catalog of chart guidance."""

from importlib.metadata import version

from .catalog.collection import Catalog, CatalogEntry
from .guideline.core import Guideline, Section

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogEntry",
    "Guideline",
    "Section",
]
