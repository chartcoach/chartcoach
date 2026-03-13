from importlib.metadata import version

from .catalog import Catalog, CatalogEntry, CatalogIndex
from .guideline import Guideline, GuidelineSection

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogEntry",
    "CatalogIndex",
    "Guideline",
    "GuidelineSection",
]
