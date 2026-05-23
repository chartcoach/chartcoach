from __future__ import annotations

from collections.abc import Sequence
from typing import Any, TypeAlias, cast

import polars as pl

from ..catalog.collection import Catalog
from ..tools.catalog import CatalogTools
from ..constants import DEFAULT_CHROMA_TOP_K
from .chroma import ChromaIndex
from .json import normalize_for_json
from .results import SearchResultRow, flatten_search_result
from .sql_tools import SqlTools

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
        default_top_k: int = DEFAULT_CHROMA_TOP_K,
        sql_tools: SqlTools | None = None,
    ) -> None:
        self._index = index
        self._conn = conn
        self._default_top_k = default_top_k
        self._sql_tools = sql_tools if sql_tools is not None else SqlTools(conn)

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

        return self._sql_tools.sql(sql, row_limit=row_limit)

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
        return normalize_for_json(result)

    def search_guidelines(
        self,
        query_text: str,
        *,
        limit: int | None = None,
        roles: Sequence[str] | None = None,
        labels: Sequence[str] | None = None,
        label_prefixes: Sequence[str] | None = None,
        candidate_limit: int | None = None,
    ) -> dict[str, Any]:
        """Semantically search and return deduplicated guideline-level rows.

        This is the reviewer-friendly layer over document search. It searches
        section and overview documents, keeps the best matching document for each
        guideline, and joins the result back to catalog metadata.
        """

        resolved_limit = self._default_top_k if limit is None else limit
        catalog_tools = CatalogTools(self.index.catalog)
        catalog_tools.validate_guideline_filters(
            labels=labels or (),
            label_prefixes=label_prefixes or (),
        )
        resolved_roles = self._resolve_search_roles(roles or ())
        parent_ids = _guideline_ids_matching_filters(
            self.index.catalog,
            labels=labels or (),
            label_prefixes=label_prefixes or (),
        )
        if parent_ids is not None and not parent_ids:
            return {
                "query": query_text,
                "rows": [],
                "row_count": 0,
                "limit": resolved_limit,
            }

        where = _metadata_filter(parent_ids=parent_ids, roles=resolved_roles)
        rows = self._filtered_search_rows(
            query_text,
            where=where,
            limit=resolved_limit,
            candidate_limit=candidate_limit,
        )

        seen: set[str] = set()
        guideline_ids: list[str] = []
        best_rows: list[SearchResultRow] = []
        for row in rows:
            if row.guideline_id in seen:
                continue
            seen.add(row.guideline_id)
            guideline_ids.append(row.guideline_id)
            best_rows.append(row)
            if len(best_rows) >= resolved_limit:
                break

        if not best_rows:
            return {
                "query": query_text,
                "rows": [],
                "row_count": 0,
                "limit": resolved_limit,
            }

        catalog_rows = {
            row["id"]: row
            for row in self.index.catalog.guidelines_df.filter(
                pl.col("id").is_in(guideline_ids)
            )
            .select("id", "title", "description", "labels")
            .to_dicts()
        }
        output_rows: list[dict[str, Any]] = []
        for rank, row in enumerate(best_rows, start=1):
            guideline = catalog_rows.get(row.guideline_id, {})
            output_rows.append(
                {
                    "rank": rank,
                    "id": row.guideline_id,
                    "title": guideline.get("title"),
                    "description": guideline.get("description"),
                    "labels": guideline.get("labels") or row.labels,
                    "matched_document_id": row.document_id,
                    "matched_role": row.role,
                    "distance": row.distance,
                    "matched_text": row.document,
                }
            )

        return {
            "query": query_text,
            "rows": output_rows,
            "row_count": len(output_rows),
            "limit": resolved_limit,
        }

    def _resolve_search_roles(self, roles: Sequence[str]) -> tuple[str, ...]:
        if not roles:
            return ()

        available = set(_indexed_roles(self.index.documents_df))
        resolved = tuple(_normalize_search_role(role) for role in roles)
        missing = sorted(set(resolved) - available)
        if missing:
            available_text = ", ".join(sorted(available))
            raise ValueError(
                f"Unknown indexed document role(s): {', '.join(missing)}. Available roles: {available_text}"
            )
        return resolved

    def _filtered_search_rows(
        self,
        query_text: str,
        *,
        where: MetadataFilter | None,
        limit: int,
        candidate_limit: int | None,
    ) -> list[SearchResultRow]:
        collection_count = self.index.collection.count()
        if collection_count == 0:
            return []

        current_limit = min(candidate_limit or max(limit * 8, 24), collection_count)
        while True:
            result = self.search(query_text, limit=current_limit, where=where)
            rows = flatten_search_result(result)
            unique_guideline_count = len({row.guideline_id for row in rows})
            if unique_guideline_count >= limit or current_limit >= collection_count:
                return rows
            current_limit = min(current_limit * 2, collection_count)

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
        return normalize_for_json(result)


def _indexed_roles(documents_df: pl.DataFrame) -> tuple[str, ...]:
    return tuple(
        documents_df.select(
            role=pl.col("metadata").struct.field("role"),
        )
        .unique()
        .sort("role")
        .get_column("role")
        .to_list()
    )


def _normalize_search_role(role: str) -> str:
    if role in {"overview", "document"} or role.startswith("section."):
        return role
    return f"section.{role}"


def _guideline_ids_matching_filters(
    catalog: Catalog,
    *,
    labels: Sequence[str],
    label_prefixes: Sequence[str],
) -> tuple[str, ...] | None:
    if not labels and not label_prefixes:
        return None

    ids: list[str] = []
    for entry in catalog.entries:
        guideline_labels = entry.guideline.labels
        if all(label in guideline_labels for label in labels) and all(
            any(label.startswith(prefix) for label in guideline_labels)
            for prefix in label_prefixes
        ):
            ids.append(entry.id)
    return tuple(ids)


def _metadata_filter(
    *,
    parent_ids: Sequence[str] | None,
    roles: Sequence[str],
) -> MetadataFilter | None:
    filters: list[MetadataFilter] = []
    if parent_ids is not None:
        filters.append({"parent_id": {"$in": list(parent_ids)}})
    if roles:
        filters.append({"role": {"$in": list(roles)}})
    if not filters:
        return None
    if len(filters) == 1:
        return filters[0]
    return {"$and": filters}


__all__ = ["SearchTools"]
