from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, cast

from chromadb.api.types import Include, Where, WhereDocument
from pydantic import BaseModel

from .catalog import CATALOG_DF_RELATION, CatalogIndex, EMBEDDINGS_TABLE
from .guideline import Guideline, GuidelineSection

DEFAULT_CHROMA_QUERY_INCLUDE: Include = ["documents", "metadatas", "distances"]
DEFAULT_CHROMA_GET_INCLUDE: Include = ["documents", "metadatas"]
VECTOR_PREVIEW_LIMIT = 8
VECTOR_ROW_PREVIEW_LIMIT = 2
READ_ONLY_SQL_PREFIXES = {"SELECT", "WITH", "SHOW", "DESCRIBE", "DESC", "EXPLAIN"}
MetadataFilter = dict[str, Any]
DocumentFilter = dict[str, Any]
IncludeFields = list[str]


class CatalogIndexTools:
    """Agent-oriented tools for a built ``CatalogIndex``.

    This wrapper is deliberately transport-neutral: the methods return only plain
    Python data so they can be exposed later through a CLI, MCP server, or other
    programmatic adapter with little or no extra translation logic.

    The surface is intentionally thin. Instead of wrapping every likely analysis
    into a custom method, it gives agents:

    - one consolidated discovery call via ``read_info()``
    - direct raw SQL over DuckDB for flexible relational analysis
    - thin access to Chroma ``query`` and ``get`` for semantic retrieval and
      metadata/document filtering

    By default, the wrapper will build the supplied index immediately so its
    DuckDB relations and Chroma collection are ready for querying.
    """

    def __init__(
        self,
        index: CatalogIndex,
        *,
        default_row_limit: int = 200,
        default_top_k: int = 10,
        default_sample_limit: int = 5,
        auto_build: bool = True,
    ) -> None:
        self._index = index
        self._default_row_limit = default_row_limit
        self._default_top_k = default_top_k
        self._default_sample_limit = default_sample_limit
        self._auto_build = auto_build
        if self._auto_build:
            self._index.build()

    @property
    def index(self) -> CatalogIndex:
        """Return the wrapped ``CatalogIndex`` instance."""
        return self._index

    def read_info(self, *, sample_limit: int | None = None) -> dict[str, Any]:
        """Return the canonical read-only discovery payload for the live index.

        This consolidates the previously separate context, DuckDB, and Chroma
        discovery surfaces into one bounded response so clients can plan read
        queries without wading through duplicated metadata.

        The payload includes:

        - index defaults and collection/catalog counts
        - canonical join paths across DuckDB and Chroma
        - shared role values for embedded text chunks
        - live DuckDB relations with schema, row counts, notes, and sample rows
        - Chroma collection metadata plus a representative sample payload
        - top-level guideline and section field shapes

        Args:
            sample_limit: Maximum sample rows or sample documents to include in
                the consolidated discovery payload. Defaults to the tool's
                configured sample limit.

        Returns:
            A JSON-safe dictionary describing the full read surface with bounded
            sample data and no duplicated discovery branches.
        """
        applied_sample_limit = sample_limit or self._default_sample_limit
        table_rows = self._duckdb_table_rows()
        role_values = self._embedding_roles()
        join_hints = self._join_hints()
        sample_payload = self.index.collection.peek(limit=applied_sample_limit)
        normalized_sample = _summarize_info_embeddings(
            _normalize_for_json(sample_payload)
        )
        sample_metadatas = normalized_sample.get("metadatas", [])

        return {
            "index": {
                "catalog_entry_count": len(self.index.catalog),
                "collection_name": getattr(self.index.collection, "name", None),
                "default_row_limit": self._default_row_limit,
                "default_top_k": self._default_top_k,
                "default_sample_limit": self._default_sample_limit,
                "sample_limit": applied_sample_limit,
                "auto_build": self._auto_build,
                "duckdb_relation_count": len(table_rows),
                "chroma_document_count": self.index.collection.count(),
            },
            "joins": join_hints,
            "role_values": role_values,
            "duckdb": {
                "relations": self._duckdb_relations(
                    include_samples=True,
                    sample_limit=applied_sample_limit,
                    table_rows=table_rows,
                ),
                "query_notes": [
                    f"Use {EMBEDDINGS_TABLE} for vector-indexed text chunks and chunk-level roles.",
                    f"Use {CATALOG_DF_RELATION} for full guideline structure, labels, sections, and references.",
                    f"Join {EMBEDDINGS_TABLE}.id to {CATALOG_DF_RELATION}.id when combining semantic chunks with full guideline data.",
                ],
            },
            "chroma": {
                "metadata_keys": self._chroma_metadata_keys(),
                "sample": normalized_sample,
                "sample_metadata_keys": sorted(
                    {
                        key
                        for metadata in sample_metadatas
                        for key in (metadata or {}).keys()
                    }
                ),
                "default_query_include": list(DEFAULT_CHROMA_QUERY_INCLUDE),
                "default_get_include": list(DEFAULT_CHROMA_GET_INCLUDE),
            },
            "guideline_shape": {
                "guideline_fields": self._model_field_summaries(Guideline),
                "section_fields": self._model_field_summaries(GuidelineSection),
            },
        }

    def duckdb_query(
        self,
        sql: str,
        *,
        row_limit: int | None = None,
    ) -> dict[str, Any]:
        """Execute a DuckDB statement against the indexed catalog.

        This method is intentionally raw because agents are often good at writing
        analysis SQL once they understand the available relations.
        Use ``read_info()`` first to inspect the live schema, counts, joins,
        and representative samples.

        Typical patterns:

        - inspect role distributions in ``embeddings``
        - join ``embeddings`` to ``catalog_df`` on guideline id
        - aggregate labels, section roles, or description text
        - prototype analysis queries before baking them into a higher-level tool
        - issue ad hoc local DuckDB statements when exploration or maintenance
          is easier in SQL than through a curated helper

        Args:
            sql: One read-only DuckDB SQL statement.
            row_limit: Optional maximum number of rows to return. If omitted, a
                default cap is applied when the statement returns rows.

        Returns:
            A JSON-safe dictionary with ``columns``, ``rows``, ``row_count``,
            the applied row limit, and a ``truncated`` flag. Statements that do
            not produce a result set return empty ``columns`` and ``rows``.
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

        This is a thin wrapper over ``collection.query()`` with the same core
        concepts used in ``chroma-mcp``:

        - ``query_texts`` for semantic retrieval
        - ``where`` for metadata filters
        - ``where_document`` for document-content filters
        - ``include`` to control the returned payload

        Example metadata filters:

        - ``{"role": "section.advice"}``
        - ``{"parent_id": "use-direct-labels"}``
        - ``{"$and": [{"role": "section.reason"}, {"parent_id": "some-guideline"}]}``

        Example document filters:

        - ``{"$contains": "legend"}``
        - ``{"$and": [{"$contains": "legend"}, {"$not_contains": "map"}]}``

        Use ``read_info()`` first if you need the consolidated relation, join,
        and metadata overview before constructing a search.

        The tool does not constrain your search strategy. It simply exposes the
        live collection with defaults that are useful for analysis and agentic
        retrieval workflows.

        Args:
            query_texts: One or more semantic queries.
            n_results: Maximum results to return per query text. Defaults to the
                tool's configured top-k.
            where: Optional metadata filter tree passed through to Chroma.
            where_document: Optional document-content filter tree passed through
                to Chroma.
            include: Optional include list. Defaults to documents, metadatas,
                and distances.

        Returns:
            The Chroma query result normalized into plain Python data.
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
        """Retrieve documents from the bound Chroma collection.

        This is the direct-access companion to ``chroma_query()``. Use it when
        you already know document IDs or when you want filtered retrieval without
        a semantic query vector.

        Common patterns:

        - fetch known IDs returned by ``chroma_query()``
        - retrieve all chunks for one guideline via ``{"parent_id": "..."}``
        - filter by chunk role such as ``{"role": "section.advice"}``
        - page through filtered documents using ``limit`` and ``offset``

        Args:
            ids: Optional document IDs to fetch directly.
            where: Optional metadata filter tree passed through to Chroma.
            where_document: Optional document-content filter tree passed through
                to Chroma.
            include: Optional include list. Defaults to documents and metadatas.
            limit: Optional maximum number of matching documents to return.
            offset: Optional number of matches to skip before returning results.

        Returns:
            The Chroma get result normalized into plain Python data.
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

    def _duckdb_relation_notes(self, relation_name: str) -> list[str]:
        if relation_name == EMBEDDINGS_TABLE:
            return [
                "One row per embedded text chunk.",
                f"Use id to join back to {CATALOG_DF_RELATION}.id.",
                "Use slug as the chunk-level identifier and role to target chunk types.",
            ]
        if relation_name == CATALOG_DF_RELATION:
            return [
                "One row per guideline.",
                "Includes full title, description, labels, body, sections, and references.",
                f"Use id as the primary join key from {EMBEDDINGS_TABLE}.id or Chroma metadata.parent_id.",
            ]
        return []

    def _duckdb_relations(
        self,
        *,
        include_samples: bool,
        sample_limit: int | None = None,
        table_rows: list[dict[str, Any]] | None = None,
    ) -> list[dict[str, Any]]:
        tables = table_rows or self._duckdb_table_rows()
        relations: list[dict[str, Any]] = []
        for relation in tables:
            relation_name = str(relation["name"])
            info: dict[str, Any] = {
                "name": relation_name,
                "database": relation["database"],
                "schema": relation["schema"],
                "temporary": relation["temporary"],
                "columns": [
                    {"name": column_name, "type": column_type}
                    for column_name, column_type in zip(
                        relation["column_names"],
                        relation["column_types"],
                        strict=True,
                    )
                ],
                "row_count": self._count_relation_rows(relation_name),
                "notes": self._duckdb_relation_notes(relation_name),
            }
            if include_samples:
                info["sample_rows"] = self._sample_relation_rows(
                    relation_name,
                    sample_limit=sample_limit or self._default_sample_limit,
                )
            relations.append(info)
        return relations

    def _duckdb_table_rows(self) -> list[dict[str, Any]]:
        return self._execute_duckdb_query("SHOW ALL TABLES", row_limit=None)["rows"]

    @staticmethod
    def _join_hints() -> list[dict[str, str]]:
        return [
            {
                "left": f"{EMBEDDINGS_TABLE}.id",
                "right": f"{CATALOG_DF_RELATION}.id",
                "description": "Join embedded text rows back to the full structured guideline record.",
            },
            {
                "left": "chroma.id",
                "right": f"duckdb.{EMBEDDINGS_TABLE}.slug",
                "description": "Join a Chroma result row back to the DuckDB embeddings table by document slug.",
            },
            {
                "left": "chroma.metadata.parent_id",
                "right": f"duckdb.{CATALOG_DF_RELATION}.id",
                "description": "Join a Chroma result row back to the full guideline record by guideline id.",
            },
        ]

    @staticmethod
    def _model_field_summaries(model: type[BaseModel]) -> list[dict[str, str]]:
        return [
            {
                "name": field_name,
                "type": str(field_info.annotation),
            }
            for field_name, field_info in model.model_fields.items()
        ]

    def _embedding_roles(self) -> list[str]:
        if self.index.catalog.docs_df.height == 0:
            return []

        role_rows = self.index.conn.execute(
            f'SELECT DISTINCT role FROM "{EMBEDDINGS_TABLE}" ORDER BY role'
        ).fetchall()
        return [str(role) for (role,) in role_rows]

    def _chroma_metadata_keys(self) -> list[str]:
        docs_df = self.index.catalog.docs_df
        if docs_df.height == 0:
            return []

        first_metadata = docs_df.get_column("metadata").to_list()[0]
        return sorted(str(key) for key in first_metadata.keys())

    def _count_relation_rows(self, relation_name: str) -> int:
        query = f"SELECT COUNT(*) FROM {self._quote_identifier(relation_name)}"
        row = self.index.conn.execute(query).fetchone()
        if row is None:
            raise RuntimeError(f"Failed to count relation rows for {relation_name}.")
        return int(row[0])

    def _sample_relation_rows(
        self,
        relation_name: str,
        *,
        sample_limit: int,
    ) -> list[dict[str, Any]]:
        query = (
            f"SELECT * FROM {self._quote_identifier(relation_name)} "
            f"LIMIT {int(sample_limit)}"
        )
        return _summarize_info_embeddings(
            self._execute_duckdb_query(query, row_limit=None)["rows"]
        )

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

    @staticmethod
    def _quote_identifier(identifier: str) -> str:
        return '"' + identifier.replace('"', '""') + '"'


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


def _summarize_info_embeddings(value: Any) -> Any:
    if isinstance(value, Mapping):
        summarized: dict[str, Any] = {}
        for key, item in value.items():
            if key == "embedding":
                summarized[str(key)] = _summarize_vector_like(item)
                continue
            if key == "embeddings":
                summarized[str(key)] = _summarize_embeddings_like(item)
                continue
            summarized[str(key)] = _summarize_info_embeddings(item)
        return summarized

    if isinstance(value, list):
        return [_summarize_info_embeddings(item) for item in value]

    return value


def _summarize_vector_like(value: Any) -> Any:
    if not isinstance(value, list):
        return value
    if not value:
        return []
    if not _is_numeric_sequence(value):
        return [_summarize_info_embeddings(item) for item in value]

    return {
        "kind": "vector",
        "length": len(value),
        "preview": value[:VECTOR_PREVIEW_LIMIT],
        "truncated": len(value) > VECTOR_PREVIEW_LIMIT,
    }


def _summarize_embeddings_like(value: Any) -> Any:
    if not isinstance(value, list):
        return value
    if not value:
        return []

    if _is_numeric_sequence(value):
        return _summarize_vector_like(value)

    if all(isinstance(item, list) and _is_numeric_sequence(item) for item in value):
        first_vector = value[0]
        return {
            "kind": "embeddings",
            "count": len(value),
            "vector_length": len(first_vector),
            "preview": [
                item[:VECTOR_PREVIEW_LIMIT] for item in value[:VECTOR_ROW_PREVIEW_LIMIT]
            ],
            "truncated": (
                len(value) > VECTOR_ROW_PREVIEW_LIMIT
                or len(first_vector) > VECTOR_PREVIEW_LIMIT
            ),
        }

    return [_summarize_info_embeddings(item) for item in value]


def _is_numeric_sequence(value: list[Any]) -> bool:
    return all(isinstance(item, int | float) for item in value)


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
