from __future__ import annotations

from os import PathLike
from pathlib import Path, PureWindowsPath
from typing import TYPE_CHECKING
from urllib.parse import urlparse

from .catalog.collection import Catalog
from .catalog.locator import (
    CatalogLocation,
    CatalogSource,
    locate_catalog,
    open_catalog,
)
from .catalog.remote import DownloadReporter, default_index_path
from .constants import DEFAULT_INDEX_TOP_K, LANCE_DOCUMENT_TABLE
from .search import Mode, Query
from .search import open as open_lance_index
from .search import query as query_lance_index
from .search.index import Result, search as search_guidelines, validate_table_documents
from .search.lance import Document

if TYPE_CHECKING:
    from lancedb import Table

IndexLocation = str | PathLike[str]


class ChartCoach:
    """Facade for a catalog and its optional LanceDB index."""

    def __init__(
        self,
        source: CatalogSource = None,
        *,
        catalog: Catalog | None = None,
        index: IndexLocation | None = None,
        table: "Table | None" = None,
        table_name: str = LANCE_DOCUMENT_TABLE,
        reporter: DownloadReporter | None = None,
    ) -> None:
        if source is not None and catalog is not None:
            raise ValueError("Pass source or catalog, not both.")
        self._catalog_location: CatalogLocation | None = (
            None if catalog is not None else locate_catalog(source)
        )
        self._catalog = catalog
        self._use_default_index = (
            self._catalog_location is not None and self._catalog_location.is_default
        )
        self._index_location = index
        self._table = table
        self._table_name = table_name
        self._reporter = reporter
        self._catalog_index: CatalogIndex | None = None

    @property
    def catalog(self) -> Catalog:
        """Return the loaded catalog."""

        if self._catalog is None:
            self._catalog = open_catalog(
                self._catalog_location,
                reporter=self._reporter,
            )
        return self._catalog

    @property
    def index(self) -> "CatalogIndex":
        """Return the index namespace for this catalog."""

        if self._catalog_index is None:
            self._catalog_index = CatalogIndex(
                self.catalog,
                location=self._index_location,
                table=self._table,
                table_name=self._table_name,
                use_default_location=self._use_default_index,
                reporter=self._reporter,
            )
        return self._catalog_index

    def search(
        self,
        text: str,
        *,
        limit: int = DEFAULT_INDEX_TOP_K,
        candidate_limit: int | None = None,
        where: str | None = None,
        mode: Mode = "auto",
    ) -> Result:
        """Search indexed documents and return deduplicated guideline rows."""

        index = self.index
        index._ensure_compatible()
        return search_guidelines(
            self.catalog,
            index.table,
            text,
            limit=limit,
            candidate_limit=candidate_limit,
            where=where,
            mode=mode,
            validate_table=False,
        )


class CatalogIndex:
    """LanceDB index namespace bound to one catalog."""

    def __init__(
        self,
        catalog: Catalog,
        *,
        location: IndexLocation | None = None,
        table: "Table | None" = None,
        table_name: str = LANCE_DOCUMENT_TABLE,
        use_default_location: bool = False,
        reporter: DownloadReporter | None = None,
    ) -> None:
        self.catalog = catalog
        self.table_name = table_name
        self._location = location
        self._table = table
        self._use_default_location = use_default_location
        self._reporter = reporter
        self._is_compatible = False

    @property
    def location(self) -> IndexLocation:
        """Return the LanceDB database path or URI."""

        if self._location is None:
            if not self._use_default_location:
                raise ValueError(
                    "Pass index=... or table=... to use indexed search with a "
                    "custom catalog."
                )
            self._location = default_index_path(
                table_name=self.table_name,
                reporter=self._reporter,
            )
        return self._location

    @property
    def path(self) -> Path:
        """Return the local LanceDB database path."""

        location = self.location
        if isinstance(location, PathLike):
            return Path(location)
        parsed = urlparse(location)
        if parsed.scheme and parsed.scheme != "file":
            if PureWindowsPath(location).drive.lower() == f"{parsed.scheme}:":
                return Path(location)
            raise ValueError("LanceDB index is URI-backed. Use `.location` instead.")
        return Path(parsed.path if parsed.scheme == "file" else location)

    @property
    def table(self) -> "Table":
        """Return the native LanceDB table."""

        if self._table is None:
            self._table = open_lance_index(
                self.location,
                table_name=self.table_name,
            )
        return self._table

    def query(
        self,
        search_query: Query,
        *,
        limit: int = DEFAULT_INDEX_TOP_K,
        where: str | None = None,
        mode: Mode = "auto",
    ) -> list[Document]:
        """Run a raw LanceDB query over indexed catalog documents."""

        return query_lance_index(
            self.table,
            search_query,
            limit=limit,
            where=where,
            mode=mode,
        )

    def _ensure_compatible(self) -> None:
        if not self._is_compatible:
            validate_table_documents(self.catalog, self.table)
            self._is_compatible = True


def open(
    source: CatalogSource = None,
    *,
    catalog: Catalog | None = None,
    index: IndexLocation | None = None,
    table: "Table | None" = None,
    table_name: str = LANCE_DOCUMENT_TABLE,
    reporter: DownloadReporter | None = None,
) -> ChartCoach:
    """Open the chartcoach facade for a catalog and optional LanceDB index."""

    return ChartCoach(
        source,
        catalog=catalog,
        index=index,
        table=table,
        table_name=table_name,
        reporter=reporter,
    )


__all__ = [
    "CatalogIndex",
    "ChartCoach",
    "IndexLocation",
    "open",
]
