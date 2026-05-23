from __future__ import annotations

from os import PathLike
from typing import Any

from ..catalog.collection import Catalog
from ..tools.catalog import CatalogTools
from .chroma import CacheMode, ChromaIndex
from .registry import ToolSpec, tool_specs
from .sql import connect_catalog
from .sql_tools import SqlTools
from .tools import SearchTools


class SearchSession:
    """Catalog plus optional-search tools for retrieval workflows."""

    def __init__(
        self,
        catalog: Catalog,
        index: ChromaIndex,
        conn: Any | None = None,
        *,
        close_conn: bool = False,
    ) -> None:
        if index.catalog.hexdigest() != catalog.hexdigest():
            raise ValueError("index must be built from the same catalog content.")

        self._catalog = catalog
        self._index = index
        self._conn = (
            conn if conn is not None else connect_catalog(catalog, search=index)
        )
        self._close_conn = close_conn or conn is None
        self._catalog_tools: CatalogTools | None = None
        self._sql_tools: SqlTools | None = None
        self._tools: SearchTools | None = None

    @classmethod
    def from_cache(
        cls,
        catalog: Catalog | str | PathLike[str],
        *,
        cache_dir: str | PathLike[str] | None = None,
        cache_mode: CacheMode = "reuse_or_create",
        cache_embeddings: bool = True,
        embedding_fn: Any | None = None,
    ) -> "SearchSession":
        """Open a content-addressed Chroma index and SQL session for a catalog."""

        resolved_catalog = _resolve_catalog(catalog)
        index = ChromaIndex.from_cache(
            resolved_catalog,
            cache_dir=cache_dir,
            cache_mode=cache_mode,
            cache_embeddings=cache_embeddings,
            embedding_fn=embedding_fn,
        )
        return cls(resolved_catalog, index)

    @property
    def catalog(self) -> Catalog:
        """Return the source catalog."""

        return self._catalog

    @property
    def index(self) -> ChromaIndex:
        """Return the Chroma index."""

        return self._index

    @property
    def conn(self) -> Any:
        """Return the DuckDB connection with catalog and embedding tables."""

        return self._conn

    @property
    def tools(self) -> SearchTools:
        """Return SQL, exact-get, and semantic-search tools."""

        if self._tools is None:
            self._tools = SearchTools(self.index, self.conn, sql_tools=self.sql_tools)
        return self._tools

    @property
    def sql_tools(self) -> SqlTools:
        """Return read-only SQL tools over the prepared DuckDB connection."""

        if self._sql_tools is None:
            self._sql_tools = SqlTools(self.conn)
        return self._sql_tools

    @property
    def catalog_tools(self) -> CatalogTools:
        """Return deterministic catalog discovery and retrieval tools."""

        if self._catalog_tools is None:
            self._catalog_tools = CatalogTools(self.catalog)
        return self._catalog_tools

    @property
    def tool_specs(self) -> tuple[ToolSpec, ...]:
        """Return the transport-neutral public tool registry."""

        return tool_specs(
            catalog_tools=self.catalog_tools,
            sql_tools=self.sql_tools,
            search_tools=self.tools,
        )

    def close(self) -> None:
        """Close the owned SQL connection."""

        if self._close_conn and self._conn is not None:
            self._conn.close()
            self._conn = None

    def __enter__(self) -> "SearchSession":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()


def open_search_session(
    catalog: Catalog | str | PathLike[str],
    *,
    cache_dir: str | PathLike[str] | None = None,
    cache_mode: CacheMode = "reuse_or_create",
    cache_embeddings: bool = True,
    embedding_fn: Any | None = None,
) -> SearchSession:
    """Open a composable search session from a catalog or catalog parquet path."""

    return SearchSession.from_cache(
        catalog,
        cache_dir=cache_dir,
        cache_mode=cache_mode,
        cache_embeddings=cache_embeddings,
        embedding_fn=embedding_fn,
    )


def _resolve_catalog(catalog: Catalog | str | PathLike[str]) -> Catalog:
    if isinstance(catalog, Catalog):
        return catalog
    return Catalog.from_parquet(catalog)


__all__ = ["SearchSession", "open_search_session"]
