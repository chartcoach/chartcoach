from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, cast

from chromadb.api.types import Include, Where, WhereDocument

from .catalog import CatalogIndex

DEFAULT_CHROMA_QUERY_INCLUDE: Include = ["documents", "metadatas", "distances"]
DEFAULT_CHROMA_GET_INCLUDE: Include = ["documents", "metadatas"]
READ_ONLY_SQL_PREFIXES = {"SELECT", "WITH", "SHOW", "DESCRIBE", "DESC", "EXPLAIN"}
MetadataFilter = dict[str, Any]
DocumentFilter = dict[str, Any]
IncludeFields = list[str]


class CatalogIndexTools:
    """Transport-neutral query surface over a built ``CatalogIndex``."""

    def __init__(
        self,
        index: CatalogIndex,
        *,
        default_row_limit: int = 200,
        default_top_k: int = 10,
        auto_build: bool = True,
    ) -> None:
        self._index = index
        self._default_row_limit = default_row_limit
        self._default_top_k = default_top_k
        self._auto_build = auto_build
        if self._auto_build:
            self._index.build()

    @property
    def index(self) -> CatalogIndex:
        """Return the wrapped ``CatalogIndex`` instance."""
        return self._index

    def duckdb_query(
        self,
        sql: str,
        *,
        row_limit: int | None = None,
    ) -> dict[str, Any]:
        """Execute one read-only DuckDB statement against the persisted relations.

        Use standard SQL discovery when you need orientation, for example:
        ``show all tables``, ``describe <table>``, or ``select * from "<table>" limit ...``.
        """
        return self._execute_duckdb_query(sql, row_limit=row_limit)

    def chroma_query(
        self,
        query_texts: list[str],
        *,
        n_results: int | None = None,
        where: MetadataFilter | None = None,
        where_document: DocumentFilter | None = None,
        include: IncludeFields | None = None,
    ) -> dict[str, Any]:
        """Run semantic search over the bound Chroma collection.

        Metadata filters are passed through directly. For list-valued labels,
        use the live collection syntax ``{"labels": {"$contains": "<label>"}}``.
        """
        if not query_texts:
            raise ValueError("The 'query_texts' list cannot be empty.")

        result = self.index.collection.query(
            query_texts=query_texts,
            n_results=n_results or self._default_top_k,
            where=cast(Where | None, where),
            where_document=cast(WhereDocument | None, where_document),
            include=cast(Include, include or list(DEFAULT_CHROMA_QUERY_INCLUDE)),
        )
        return _normalize_for_json(result)

    def chroma_get(
        self,
        *,
        ids: list[str] | None = None,
        where: MetadataFilter | None = None,
        where_document: DocumentFilter | None = None,
        include: IncludeFields | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch documents directly from the bound Chroma collection.

        Metadata filters are passed through directly. For list-valued labels,
        use the live collection syntax ``{"labels": {"$contains": "<label>"}}``.
        """
        result = self.index.collection.get(
            ids=ids,
            where=cast(Where | None, where),
            where_document=cast(WhereDocument | None, where_document),
            include=cast(Include, include or list(DEFAULT_CHROMA_GET_INCLUDE)),
            limit=limit,
            offset=offset,
        )
        return _normalize_for_json(result)

    def _execute_duckdb_query(
        self,
        sql: str,
        *,
        row_limit: int | None,
    ) -> dict[str, Any]:
        normalized_sql = _validate_read_only_sql(sql)

        applied_row_limit = row_limit or self._default_row_limit
        cursor = self.index.conn.execute(normalized_sql)
        if cursor.description is None:
            return {
                "sql": normalized_sql,
                "columns": [],
                "rows": [],
                "row_count": 0,
                "row_limit": applied_row_limit
                if row_limit is not None
                else self._default_row_limit,
                "truncated": False,
            }

        columns = [column[0] for column in cursor.description]
        fetched_rows = cursor.fetchmany(applied_row_limit + 1)
        truncated = len(fetched_rows) > applied_row_limit
        rows = fetched_rows[:applied_row_limit]

        normalized_rows = [
            {
                column_name: _normalize_for_json(value)
                for column_name, value in zip(columns, row, strict=True)
            }
            for row in rows
        ]
        normalized_columns = [
            {
                "name": column[0],
                "type_code": _normalize_for_json(column[1]),
            }
            for column in cursor.description
        ]

        return {
            "sql": normalized_sql,
            "columns": normalized_columns,
            "rows": normalized_rows,
            "row_count": len(normalized_rows),
            "row_limit": applied_row_limit
            if row_limit is not None
            else self._default_row_limit,
            "truncated": truncated,
        }


def _normalize_for_json(value: Any) -> Any:
    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, datetime | date | time):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): _normalize_for_json(item) for key, item in value.items()}
    if isinstance(value, tuple | list | set):
        return [_normalize_for_json(item) for item in value]
    if hasattr(value, "tolist") and callable(value.tolist):
        return _normalize_for_json(value.tolist())
    if hasattr(value, "item") and callable(value.item):
        return _normalize_for_json(value.item())
    return str(value)


def _validate_read_only_sql(sql: str) -> str:
    normalized_sql = sql.strip()
    if not normalized_sql:
        raise ValueError("SQL cannot be empty.")

    statements = [part.strip() for part in normalized_sql.split(";") if part.strip()]
    if len(statements) != 1:
        raise ValueError("duckdb_query only allows a single read-only SQL statement.")

    statement = statements[0]
    keyword = statement.split(maxsplit=1)[0].upper()
    if keyword not in READ_ONLY_SQL_PREFIXES:
        raise ValueError("duckdb_query only allows read-only SQL statements.")

    return statement


__all__ = ["CatalogIndexTools"]
