from importlib.metadata import version

from .coach import ChartCoach
from .catalog import Catalog, CatalogEntry, CatalogIndex
from .guideline import Guideline, GuidelineSection

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "Catalog",
    "CatalogEntry",
    "CatalogIndex",
    "ChartCoach",
    "Guideline",
    "GuidelineSection",
]
