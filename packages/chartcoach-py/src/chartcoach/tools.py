from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, TypeAlias, cast

from chromadb.api.types import Include, Where, WhereDocument

from .catalog.index import Index
from .constants import DEFAULT_CHROMA_TOP_K, DEFAULT_DUCKDB_ROW_LIMIT

DEFAULT_SEARCH_INCLUDE: Include = ["documents", "metadatas", "distances"]
DEFAULT_GET_INCLUDE: Include = ["documents", "metadatas"]
MetadataFilter = dict[str, Any]
DocumentFilter = dict[str, Any]
IncludeFields = list[str]
QueryInput: TypeAlias = str | list[str]


class Tools:
    """Small API for semantic search, direct lookup, and SQL."""

    def __init__(
        self,
        index: Index,
        *,
        default_row_limit: int = DEFAULT_DUCKDB_ROW_LIMIT,
        default_top_k: int = DEFAULT_CHROMA_TOP_K,
    ) -> None:
        self._index = index
        self._default_row_limit = default_row_limit
        self._default_top_k = default_top_k

    @property
    def index(self) -> Index:
        """Return the prepared search data behind these tools."""

        return self._index

    def sql(
        self,
        sql: str,
        *,
        row_limit: int | None = None,
    ) -> dict[str, Any]:
        """Run SQL against the prepared DuckDB file."""

        return self._execute_sql(sql, row_limit=row_limit)

    def search(
        self,
        query_texts: QueryInput,
        *,
        limit: int | None = None,
        where: MetadataFilter | None = None,
        where_document: DocumentFilter | None = None,
        include: IncludeFields | None = None,
    ) -> dict[str, Any]:
        """Search by meaning, with optional metadata filters before scoring."""

        resolved_queries = (
            [query_texts] if isinstance(query_texts, str) else query_texts
        )
        if not resolved_queries:
            raise ValueError("query_texts cannot be empty.")

        result = self.index.collection.query(
            query_texts=resolved_queries,
            n_results=self._default_top_k if limit is None else limit,
            where=cast(Where | None, where),
            where_document=cast(WhereDocument | None, where_document),
            include=cast(Include, include or list(DEFAULT_SEARCH_INCLUDE)),
        )
        return _normalize_for_json(result)

    def get(
        self,
        *,
        ids: list[str] | None = None,
        where: MetadataFilter | None = None,
        where_document: DocumentFilter | None = None,
        include: IncludeFields | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch stored search documents directly by id or filter."""

        result = self.index.collection.get(
            ids=ids,
            where=cast(Where | None, where),
            where_document=cast(WhereDocument | None, where_document),
            include=cast(Include, include or list(DEFAULT_GET_INCLUDE)),
            limit=limit,
            offset=offset,
        )
        return _normalize_for_json(result)

    def _execute_sql(
        self,
        sql: str,
        *,
        row_limit: int | None,
    ) -> dict[str, Any]:
        normalized_sql = sql.strip()
        if not normalized_sql:
            raise ValueError("SQL cannot be empty.")
        applied_row_limit = self._default_row_limit if row_limit is None else row_limit
        cursor = self.index.conn.execute(normalized_sql)
        if cursor.description is None:
            return {
                "sql": normalized_sql,
                "columns": [],
                "rows": [],
                "row_count": 0,
                "row_limit": applied_row_limit,
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
            "row_limit": applied_row_limit,
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


__all__ = ["Tools"]
