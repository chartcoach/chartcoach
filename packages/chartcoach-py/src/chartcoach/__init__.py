from importlib.metadata import version
from .catalog import Catalog
from .model import CatalogEntry, Guideline, GuidelineSection
from .index import CatalogIndex

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogEntry",
    "CatalogIndex",
    "Guideline",
    "GuidelineSection",
]
