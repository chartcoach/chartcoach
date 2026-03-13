from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any

from chromadb.api.types import Include, Where, WhereDocument
from pydantic import BaseModel

from .catalog import CATALOG_DF_RELATION, CatalogIndex, EMBEDDINGS_TABLE
from .guideline import Guideline, GuidelineSection

DEFAULT_CHROMA_QUERY_INCLUDE: Include = ["documents", "metadatas", "distances"]
DEFAULT_CHROMA_GET_INCLUDE: Include = ["documents", "metadatas"]
VECTOR_PREVIEW_LIMIT = 8
VECTOR_ROW_PREVIEW_LIMIT = 2


class CatalogIndexTools:
    """Agent-oriented tools for a built ``CatalogIndex``.

    This wrapper is deliberately transport-neutral: the methods return only plain
    Python data so they can be exposed later through a CLI, MCP server, or other
    programmatic adapter with little or no extra translation logic.

    The surface is intentionally thin. Instead of wrapping every likely analysis
    into a custom method, it gives agents:

    - rich discovery via ``duckdb_info()`` and ``chroma_info()``
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

    def agent_context(self) -> dict[str, Any]:
        """Return a compact machine-readable summary for agent planning.

        This is the shortest discovery surface in the module. It is designed for
        agents that want a reliable picture of what they can query before moving
        on to ``duckdb_info()``, ``chroma_info()``, raw SQL, or raw Chroma calls.

        The payload is intentionally compact:

        - index-level defaults and counts
        - canonical join paths between DuckDB, Chroma, and full guideline rows
        - live DuckDB relation schemas with row counts but no sample rows
        - Chroma metadata keys and default include behavior
        - the top-level guideline and section field shapes

        Returns:
            A JSON-safe dictionary describing the live index structure without
            the larger sample payloads returned by ``duckdb_info()`` and ``chroma_info()``.
        """
        return {
            "index": {
                "catalog_entry_count": len(self.index.catalog),
                "collection_name": getattr(self.index.collection, "name", None),
                "default_row_limit": self._default_row_limit,
                "default_top_k": self._default_top_k,
                "default_sample_limit": self._default_sample_limit,
                "auto_build": self._auto_build,
            },
            "joins": self._join_hints(),
            "duckdb": {
                "relations": self._duckdb_relations(include_samples=False),
                "role_values": self._embedding_roles(),
            },
            "chroma": {
                "count": self.index.collection.count(),
                "metadata_keys": self._chroma_metadata_keys(),
                "default_query_include": list(DEFAULT_CHROMA_QUERY_INCLUDE),
                "default_get_include": list(DEFAULT_CHROMA_GET_INCLUDE),
                "role_values": self._embedding_roles(),
            },
            "guideline_shape": {
                "guideline_fields": self._model_field_summaries(Guideline),
                "section_fields": self._model_field_summaries(GuidelineSection),
            },
        }

    def duckdb_info(self, *, sample_limit: int | None = None) -> dict[str, Any]:
        """Describe the live DuckDB relations registered by ``CatalogIndex``.

        This is the primary discovery method for relational access. It returns
        schema, counts, and sample rows for every non-system relation currently
        visible on the DuckDB connection, including the relations that matter most
        for catalog analysis:

        - ``embeddings``: one row per embedded text fragment
        - ``catalog_df``: one row per guideline with full structured fields

        Useful structure hints:

        - ``embeddings.id`` joins to ``catalog_df.id``.
        - ``embeddings.slug`` is the per-document identifier used in vector
          indexing.
        - ``embeddings.role`` identifies the semantic chunk type such as
          ``overview`` or ``section.advice``.
        - ``catalog_df.sections`` contains structured section objects with
          ``role``, ``title``, and ``content``.

        Args:
            sample_limit: Maximum sample rows to include per relation. Defaults
                to the tool's configured sample limit.

        Returns:
            A JSON-safe dictionary with relation metadata, row counts, sample
            rows, and lightweight join hints that help agents write their own
            SQL creatively.
        """
        applied_sample_limit = sample_limit or self._default_sample_limit
        tables_result = self._execute_duckdb_query("SHOW ALL TABLES", row_limit=None)
        tables = tables_result["rows"]

        return {
            "default_row_limit": self._default_row_limit,
            "sample_limit": applied_sample_limit,
            "registered_relation_count": len(tables),
            "relations": self._duckdb_relations(
                include_samples=True,
                sample_limit=applied_sample_limit,
            ),
            "join_hints": self._join_hints(),
            "role_values": self._embedding_roles(),
            "query_notes": [
                f"Use {EMBEDDINGS_TABLE} for vector-indexed text chunks and chunk-level roles.",
                f"Use {CATALOG_DF_RELATION} for full guideline structure, labels, sections, and references.",
                f"Join {EMBEDDINGS_TABLE}.id to {CATALOG_DF_RELATION}.id when combining semantic chunks with full guideline data.",
            ],
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
        Use ``duckdb_info()`` first to inspect the live schema, counts, and samples.

        Typical patterns:

        - inspect role distributions in ``embeddings``
        - join ``embeddings`` to ``catalog_df`` on guideline id
        - aggregate labels, section roles, or description text
        - prototype analysis queries before baking them into a higher-level tool
        - issue ad hoc local DuckDB statements when exploration or maintenance
          is easier in SQL than through a curated helper

        Args:
            sql: One DuckDB SQL statement.
            row_limit: Optional maximum number of rows to return. If omitted, a
                default cap is applied when the statement returns rows.

        Returns:
            A JSON-safe dictionary with ``columns``, ``rows``, ``row_count``,
            the applied row limit, and a ``truncated`` flag. Statements that do
            not produce a result set return empty ``columns`` and ``rows``.
        """
        return self._execute_duckdb_query(sql, row_limit=row_limit)

    def chroma_info(
        self,
        *,
        sample_limit: int | None = None,
    ) -> dict[str, Any]:
        """Describe the bound Chroma collection and return a representative sample.

        This method is the Chroma-side discovery tool. It combines a collection
        count, a sample payload, and high-value shape hints so agents can write
        their own semantic or filter queries without requiring a large wrapper surface.

        Useful structure hints:

        - returned ``ids`` correspond to the document slug used in DuckDB as ``embeddings.slug``
        - metadata typically includes ``parent_id``, ``role``, ``labels``, and ``content_hash``
        - metadata ``parent_id`` links back to the guideline id in DuckDB
        - metadata ``role`` mirrors the chunk role used in DuckDB

        Args:
            sample_limit: Number of sample documents to return from the collection.
                          Defaults to the tool's configured sample limit.

        Returns:
            A JSON-safe dictionary with collection count, a sample payload,
            metadata keys, common role values, and the default include behavior
            for ``chroma_query()`` and ``chroma_get()``.
        """
        applied_sample_limit = sample_limit or self._default_sample_limit
        sample_payload = self.index.collection.peek(limit=applied_sample_limit)
        normalized_sample = _summarize_info_embeddings(
            _normalize_for_json(sample_payload)
        )

        metadata_keys = self._chroma_metadata_keys()
        sample_metadatas = normalized_sample.get("metadatas", [])

        return {
            "name": getattr(self.index.collection, "name", None),
            "count": self.index.collection.count(),
            "sample_limit": applied_sample_limit,
            "sample": normalized_sample,
            "metadata_keys": metadata_keys,
            "sample_metadata_keys": sorted(
                {
                    key
                    for metadata in sample_metadatas
                    for key in (metadata or {}).keys()
                }
            ),
            "role_values": self._embedding_roles(),
            "default_query_include": list(DEFAULT_CHROMA_QUERY_INCLUDE),
            "default_get_include": list(DEFAULT_CHROMA_GET_INCLUDE),
            "join_hints": self._join_hints(),
        }

    def chroma_query(
        self,
        query_texts: list[str],
        *,
        n_results: int | None = None,
        where: Where | None = None,
        where_document: WhereDocument | None = None,
        include: Include | None = None,
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
            where=where,
            where_document=where_document,
            include=include or list(DEFAULT_CHROMA_QUERY_INCLUDE),
        )
        return _normalize_for_json(result)

    def chroma_get(
        self,
        *,
        ids: list[str] | None = None,
        where: Where | None = None,
        where_document: WhereDocument | None = None,
        include: Include | None = None,
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
            where=where,
            where_document=where_document,
            include=include or list(DEFAULT_CHROMA_GET_INCLUDE),
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
    ) -> list[dict[str, Any]]:
        tables = self._execute_duckdb_query("SHOW ALL TABLES", row_limit=None)["rows"]
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
        if not sql.strip():
            raise ValueError("SQL cannot be empty.")

        applied_row_limit = row_limit or self._default_row_limit
        cursor = self.index.conn.execute(sql)
        if cursor.description is None:
            return {
                "sql": sql,
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
            "sql": sql,
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


__all__ = ["CatalogIndexTools"]
