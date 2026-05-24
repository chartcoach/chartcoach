from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping, Sequence
from typing import Any, cast

import polars as pl

from ..constants import DEFAULT_CHROMA_TOP_K
from .chroma import ChromaIndex

DEFAULT_SEARCH_INCLUDE = ["documents", "metadatas", "distances"]
MetadataFilter = dict[str, Any]
DocumentFilter = dict[str, Any]


@dc.dataclass(frozen=True)
class GuidelineSearchHit:
    rank: int
    document_id: str
    guideline_id: str
    role: str
    distance: object
    labels: list[str]
    document: str
    title: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "rank": self.rank,
            "id": self.guideline_id,
            "title": self.title,
            "description": self.description,
            "labels": self.labels,
            "matched_document_id": self.document_id,
            "matched_role": self.role,
            "distance": self.distance,
            "matched_text": self.document,
        }


@dc.dataclass(frozen=True)
class GuidelineSearchResult:
    query: str
    rows: tuple[GuidelineSearchHit, ...]
    limit: int
    candidate_limit: int
    where: MetadataFilter | None = None
    where_document: DocumentFilter | None = None

    @property
    def row_count(self) -> int:
        return len(self.rows)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "rows": [row.to_dict() for row in self.rows],
            "row_count": self.row_count,
            "limit": self.limit,
            "candidate_limit": self.candidate_limit,
            "where": self.where,
            "where_document": self.where_document,
        }


@dc.dataclass(frozen=True)
class _SearchHit:
    document_id: str
    guideline_id: str
    role: str
    distance: object
    labels: list[str]
    document: str


def search_guidelines(
    index: ChromaIndex,
    query_text: str,
    *,
    limit: int = DEFAULT_CHROMA_TOP_K,
    candidate_limit: int | None = None,
    where: MetadataFilter | None = None,
    where_document: DocumentFilter | None = None,
) -> GuidelineSearchResult:
    """Search Chroma documents and return deduplicated guideline rows."""

    rows, resolved_candidate_limit = _search_unique_guideline_rows(
        index,
        query_text,
        where=where,
        where_document=where_document,
        limit=limit,
        candidate_limit=candidate_limit,
    )

    seen: set[str] = set()
    guideline_ids: list[str] = []
    best_rows: list[_SearchHit] = []
    for row in rows:
        if row.guideline_id in seen:
            continue
        seen.add(row.guideline_id)
        guideline_ids.append(row.guideline_id)
        best_rows.append(row)
        if len(best_rows) >= limit:
            break

    if not best_rows:
        return _empty_search_result(
            query_text,
            limit,
            resolved_candidate_limit,
            where=where,
            where_document=where_document,
        )

    catalog_rows = _guideline_rows(index, guideline_ids)
    output_rows: list[GuidelineSearchHit] = []
    for rank, row in enumerate(best_rows, start=1):
        guideline = catalog_rows[row.guideline_id]
        output_rows.append(
            GuidelineSearchHit(
                rank=rank,
                document_id=row.document_id,
                guideline_id=row.guideline_id,
                role=row.role,
                distance=row.distance,
                labels=cast(list[str], guideline.get("labels") or row.labels),
                document=row.document,
                title=cast(str, guideline["title"]),
                description=cast(str, guideline["description"]),
            )
        )

    return GuidelineSearchResult(
        query=query_text,
        rows=tuple(output_rows),
        limit=limit,
        candidate_limit=resolved_candidate_limit,
        where=where,
        where_document=where_document,
    )


def _search_unique_guideline_rows(
    index: ChromaIndex,
    query_text: str,
    *,
    where: MetadataFilter | None,
    where_document: DocumentFilter | None,
    limit: int,
    candidate_limit: int | None,
) -> tuple[list[_SearchHit], int]:
    collection_count = int(index.collection.count())
    if collection_count == 0:
        return [], 0
    max_candidates = collection_count if candidate_limit is None else candidate_limit
    max_candidates = max(limit, min(max_candidates, collection_count))
    requested = min(max(limit, 50), max_candidates)
    rows: list[_SearchHit] = []

    while True:
        rows = _search_index_rows(
            index,
            query_text,
            where=where,
            where_document=where_document,
            chroma_n_results=requested,
        )
        if _unique_guideline_count(rows) >= limit or requested >= max_candidates:
            return rows, requested
        requested = min(max_candidates, max(requested * 2, requested + 1))


def _search_index_rows(
    index: ChromaIndex,
    query_text: str,
    *,
    where: MetadataFilter | None,
    where_document: DocumentFilter | None,
    chroma_n_results: int,
) -> list[_SearchHit]:
    kwargs: dict[str, Any] = {
        "query_texts": [query_text],
        "n_results": chroma_n_results,
        "include": list(DEFAULT_SEARCH_INCLUDE),
    }
    if where is not None:
        kwargs["where"] = cast(Any, where)
    if where_document is not None:
        kwargs["where_document"] = cast(Any, where_document)
    return _query_hits(cast(Mapping[str, Any], index.collection.query(**kwargs)))


def _guideline_rows(
    index: ChromaIndex,
    guideline_ids: Sequence[str],
) -> dict[str, dict[str, object]]:
    if not guideline_ids:
        return {}
    rows = {
        row["id"]: row
        for row in index.catalog.guidelines().filter(pl.col("id").is_in(guideline_ids))
        .select("id", "title", "description", "labels")
        .to_dicts()
    }
    missing = sorted(set(guideline_ids) - set(rows))
    if missing:
        raise ValueError(
            "Chroma index returned guideline id(s) not present in catalog: "
            + ", ".join(missing)
        )
    return rows


def _empty_search_result(
    query_text: str,
    limit: int,
    candidate_limit: int,
    *,
    where: MetadataFilter | None,
    where_document: DocumentFilter | None,
) -> GuidelineSearchResult:
    return GuidelineSearchResult(
        query=query_text,
        rows=(),
        limit=limit,
        candidate_limit=candidate_limit,
        where=where,
        where_document=where_document,
    )


def _unique_guideline_count(rows: Sequence[_SearchHit]) -> int:
    return len({row.guideline_id for row in rows})


def _query_hits(result: Mapping[str, Any]) -> list[_SearchHit]:
    ids_by_query = _list_of_lists(result.get("ids"))
    documents_by_query = _list_of_lists(result.get("documents"))
    metadatas_by_query = _list_of_lists(result.get("metadatas"))
    distances_by_query = _list_of_lists(result.get("distances"))
    if not ids_by_query:
        return []

    rows: list[_SearchHit] = []
    documents = _sequence_at(documents_by_query, 0)
    metadatas = _sequence_at(metadatas_by_query, 0)
    distances = _sequence_at(distances_by_query, 0)
    for index, document_id in enumerate(ids_by_query[0]):
        metadata = _mapping_at(metadatas, index)
        guideline_id = metadata.get("parent_id")
        role = metadata.get("role")
        if not isinstance(document_id, str) or not isinstance(guideline_id, str):
            continue
        rows.append(
            _SearchHit(
                document_id=document_id,
                guideline_id=guideline_id,
                role=role if isinstance(role, str) else "",
                distance=_value_at(distances, index),
                labels=_labels_from_metadata(metadata),
                document=str(_value_at(documents, index) or ""),
            )
        )
    return rows


def _list_of_lists(value: object) -> list[list[object]]:
    if not isinstance(value, list):
        return []
    return [cast(list[object], item) for item in value if isinstance(item, list)]


def _sequence_at(values: Sequence[list[object]], index: int) -> list[object]:
    return values[index] if index < len(values) else []


def _value_at(values: Sequence[object], index: int) -> object:
    return values[index] if index < len(values) else None


def _mapping_at(values: Sequence[object], index: int) -> Mapping[str, object]:
    value = _value_at(values, index)
    if isinstance(value, Mapping):
        return cast(Mapping[str, object], value)
    return {}


def _labels_from_metadata(metadata: Mapping[str, object]) -> list[str]:
    labels = metadata.get("labels")
    if not isinstance(labels, list):
        return []
    return [label for label in labels if isinstance(label, str)]


__all__ = ["GuidelineSearchHit", "GuidelineSearchResult", "search_guidelines"]
