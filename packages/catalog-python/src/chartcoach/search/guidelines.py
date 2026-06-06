from __future__ import annotations

import dataclasses as dc
from collections.abc import Sequence
from typing import Any, cast

import polars as pl

from ..constants import DEFAULT_INDEX_TOP_K
from .lance import LanceIndex

FilterExpression = str


@dc.dataclass(frozen=True)
class GuidelineSearchHit:
    rank: int
    document_id: str
    guideline_id: str
    role: str
    score: float | None
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
            "score": self.score,
            "matched_text": self.document,
        }


@dc.dataclass(frozen=True)
class GuidelineSearchResult:
    query: str
    rows: tuple[GuidelineSearchHit, ...]
    limit: int
    candidate_limit: int
    where: FilterExpression | None = None

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
        }


@dc.dataclass(frozen=True)
class _SearchHit:
    document_id: str
    guideline_id: str
    role: str
    score: float | None
    labels: list[str]
    document: str


def search_guidelines(
    index: LanceIndex,
    query_text: str,
    *,
    limit: int = DEFAULT_INDEX_TOP_K,
    candidate_limit: int | None = None,
    where: FilterExpression | None = None,
) -> GuidelineSearchResult:
    """Search LanceDB documents and return deduplicated guideline rows."""

    if not query_text.strip():
        raise ValueError("query_text must be a non-empty string.")
    if limit < 1:
        raise ValueError("limit must be at least 1.")
    if candidate_limit is not None and candidate_limit < 1:
        raise ValueError("candidate_limit must be at least 1.")

    rows, resolved_candidate_limit = _search_unique_guideline_rows(
        index,
        query_text,
        where=where,
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
                score=row.score,
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
    )


def _search_unique_guideline_rows(
    index: LanceIndex,
    query_text: str,
    *,
    where: FilterExpression | None,
    limit: int,
    candidate_limit: int | None,
) -> tuple[list[_SearchHit], int]:
    document_count = index.document_count()
    if document_count == 0:
        return [], 0
    max_candidates = (
        document_count
        if candidate_limit is None
        else min(candidate_limit, document_count)
    )
    requested = min(max(limit, 50), max_candidates)
    rows: list[_SearchHit] = []

    while True:
        rows = _search_index_rows(
            index,
            query_text,
            where=where,
            limit=requested,
        )
        if _unique_guideline_count(rows) >= limit or requested >= max_candidates:
            return rows, requested
        requested = min(max_candidates, max(requested * 2, requested + 1))


def _search_index_rows(
    index: LanceIndex,
    query_text: str,
    *,
    where: FilterExpression | None,
    limit: int,
) -> list[_SearchHit]:
    return [
        _row_to_hit(row)
        for row in index.query_documents(query_text, limit=limit, where=where)
    ]


def _guideline_rows(
    index: LanceIndex,
    guideline_ids: Sequence[str],
) -> dict[str, dict[str, object]]:
    if not guideline_ids:
        return {}
    rows = {
        row["id"]: row
        for row in index.catalog.guidelines()
        .filter(pl.col("id").is_in(guideline_ids))
        .select("id", "title", "description", "labels")
        .to_dicts()
    }
    missing = sorted(set(guideline_ids) - set(rows))
    if missing:
        raise ValueError(
            "LanceDB index returned guideline id(s) not present in catalog: "
            + ", ".join(missing)
        )
    return rows


def _empty_search_result(
    query_text: str,
    limit: int,
    candidate_limit: int,
    *,
    where: FilterExpression | None,
) -> GuidelineSearchResult:
    return GuidelineSearchResult(
        query=query_text,
        rows=(),
        limit=limit,
        candidate_limit=candidate_limit,
        where=where,
    )


def _unique_guideline_count(rows: Sequence[_SearchHit]) -> int:
    return len({row.guideline_id for row in rows})


def _row_to_hit(row: dict[str, Any]) -> _SearchHit:
    document_id = _required_string(row, "id")
    guideline_id = _required_string(row, "parent_id")
    role = _required_string(row, "role")
    document = _required_string(row, "doc")
    return _SearchHit(
        document_id=document_id,
        guideline_id=guideline_id,
        role=role,
        score=_score(row.get("_score")),
        labels=_labels(row.get("labels")),
        document=document,
    )


def _required_string(row: dict[str, Any], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"LanceDB index row is missing string field {key!r}.")
    return value


def _score(value: object) -> float | None:
    if isinstance(value, int | float):
        return float(value)
    return None


def _labels(labels: object) -> list[str]:
    if not isinstance(labels, list):
        return []
    return [label for label in labels if isinstance(label, str)]


__all__ = ["GuidelineSearchHit", "GuidelineSearchResult", "search_guidelines"]
