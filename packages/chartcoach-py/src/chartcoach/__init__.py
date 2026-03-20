"""ChartCoach helps you search and inspect a catalog of chart guidance."""

from importlib.metadata import version

from .catalog.collection import Catalog, Entry
from .catalog.index import Index
from .coach import Coach
from .create import CacheMode, Settings, create
from .guideline.core import Guideline, Section
from .tools import Tools

__version__ = version("chartcoach")

__all__ = [
    "__version__",
    "CacheMode",
    "Catalog",
    "Coach",
    "Entry",
    "Guideline",
    "Index",
    "Section",
    "Settings",
    "Tools",
    "create",
]
