from __future__ import annotations

from .catalog.collection import Catalog
from .catalog.index import Index
from .tools import Tools


class Coach:
    """Main ChartCoach object for browsing, searching, and querying guidance."""

    def __init__(self, catalog: Catalog, index: Index) -> None:
        if index.catalog.hexdigest() != catalog.hexdigest():
            raise ValueError("index must be built from the same catalog content.")

        self._catalog = catalog
        self._index = index
        self._tools: Tools | None = None

    @property
    def catalog(self) -> Catalog:
        """Return the source catalog behind this coach."""

        return self._catalog

    @property
    def index(self) -> Index:
        """Return the prepared search data and tables for this coach."""

        return self._index

    @property
    def tools(self) -> Tools:
        """Return the tools for semantic search, lookup, and SQL."""

        if self._tools is None:
            self._tools = Tools(self.index)
        return self._tools


__all__ = ["Coach"]
