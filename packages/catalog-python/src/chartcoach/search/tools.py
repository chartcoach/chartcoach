from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, TypeAlias, cast

from ..constants import DEFAULT_CHROMA_TOP_K, DEFAULT_DUCKDB_ROW_LIMIT
from .chroma import ChromaIndex

DEFAULT_SEARCH_INCLUDE = ["documents", "metadatas", "distances"]
DEFAULT_GET_INCLUDE = ["documents", "metadatas"]
MetadataFilter = dict[str, Any]
DocumentFilter = dict[str, Any]
IncludeFields = list[str]
QueryInput: TypeAlias = str | list[str]


class SearchTools:
    """Small API for progressive-disclosure retrieval over the catalog.

    Use `sql` first to discover the available DuckDB relations, inspect columns,
    sample rows, and build lightweight shortlist queries. Use `get` to read exact
    indexed documents once you know which records you want. Use `search` as a
    secondary semantic tool after SQL narrowing, or when you need to compare the
    meaning of a small candidate set.
    """

    def __init__(
        self,
        index: ChromaIndex,
        conn: Any,
        *,
        default_row_limit: int = DEFAULT_DUCKDB_ROW_LIMIT,
        default_top_k: int = DEFAULT_CHROMA_TOP_K,
    ) -> None:
        self._index = index
        self._conn = conn
        self._default_row_limit = default_row_limit
        self._default_top_k = default_top_k

    @property
    def index(self) -> ChromaIndex:
        """Return the prepared search data behind these tools."""

        return self._index

    @property
    def conn(self) -> Any:
        """Return the DuckDB connection behind the SQL tool."""

        return self._conn

    def sql(
        self,
        sql: str,
        *,
        row_limit: int | None = None,
    ) -> dict[str, Any]:
        """Run DuckDB SQL against the prepared catalog tables.

        This is the best first tool when you do not yet know the schema. Start by
        discovering the available relations and columns with queries such as:

        - `show all tables`
        - `describe <table_name>`
        - `select * from <table_name> limit 5`
        - `select distinct <column> from <table_name> limit 20`

        After you understand the schema, use SQL to build deterministic candidate
        sets with lightweight fields such as ids, titles, descriptions, counts,
        and matched labels before escalating to document retrieval.

        Returns a JSON-safe dict with the executed SQL, column metadata, sampled
        rows, row counts, the applied row limit, and whether the result was
        truncated.
        """

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
        """Semantically search the indexed catalog documents.

        This searches embedded text documents such as overviews, full guideline
        documents, and individual sections. Use it after SQL has already revealed
        the schema and narrowed the candidate space, or when you need a semantic
        comparison among a small set of plausible records.

        Prefer short semantic probes over focused candidates. Do not rely on this
        as the first move when SQL can first tell you which relations, columns,
        labels, or metadata values actually exist.

        Metadata filters use Chroma's filter syntax, so sample the available docs
        and metadata first before composing complex predicates.
        """

        resolved_queries = (
            [query_texts] if isinstance(query_texts, str) else query_texts
        )
        if not resolved_queries:
            raise ValueError("query_texts cannot be empty.")

        result = self.index.collection.query(
            query_texts=resolved_queries,
            n_results=self._default_top_k if limit is None else limit,
            where=cast(Any, where),
            where_document=cast(Any, where_document),
            include=cast(Any, include or list(DEFAULT_SEARCH_INCLUDE)),
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
        """Fetch exact indexed documents by id or exact metadata filter.

        Use this once SQL or prior samples have already identified the precise
        documents you want to read. Prefer `ids` when you know the exact records,
        because it is more deterministic than another semantic search.

        If you use metadata filters, remember that Chroma requires boolean
        operators such as `$and` for multi-predicate filters. Sample a few docs
        first so you understand the available metadata fields and document-id
        patterns before depending on them.
        """

        result = self.index.collection.get(
            ids=ids,
            where=cast(Any, where),
            where_document=cast(Any, where_document),
            include=cast(Any, include or list(DEFAULT_GET_INCLUDE)),
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
        cursor = self.conn.execute(normalized_sql)
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


__all__ = ["SearchTools"]
