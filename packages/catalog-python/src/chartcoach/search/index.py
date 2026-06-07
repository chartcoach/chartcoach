from __future__ import annotations

import dataclasses as dc
from typing import TYPE_CHECKING, cast

import polars as pl

from ..catalog.collection import Catalog
from ..constants import DEFAULT_INDEX_TOP_K
from .lance import Document, Mode, documents, query

if TYPE_CHECKING:
    from lancedb import Table

_DOCUMENT_COLUMNS = ("id", "parent_id", "role", "labels", "content_hash", "text")


@dc.dataclass(frozen=True)
class Hit:
    rank: int
    document_id: str
    guideline_id: str
    role: str
    score: float | None
    labels: list[str]
    document: str
    title: str
    description: str

    def to_dict(self) -> dict[str, object]:
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
class Result:
    query: str
    rows: tuple[Hit, ...]
    limit: int
    candidate_limit: int
    where: str | None = None

    @property
    def row_count(self) -> int:
        return len(self.rows)

    def to_dict(self) -> dict[str, object]:
        return {
            "query": self.query,
            "rows": [row.to_dict() for row in self.rows],
            "row_count": self.row_count,
            "limit": self.limit,
            "candidate_limit": self.candidate_limit,
            "where": self.where,
        }


@dc.dataclass(frozen=True)
class _DocumentHit:
    document_id: str
    guideline_id: str
    role: str
    content_hash: str
    score: float | None
    labels: list[str]
    document: str


def search(
    catalog: Catalog,
    table: "Table",
    text: str,
    *,
    limit: int = DEFAULT_INDEX_TOP_K,
    candidate_limit: int | None = None,
    where: str | None = None,
    mode: Mode = "auto",
) -> Result:
    """Search indexed documents and return deduplicated guideline rows."""

    if not text.strip():
        raise ValueError("query must be a non-empty string.")
    if limit < 1:
        raise ValueError("limit must be at least 1.")
    if candidate_limit is not None and candidate_limit < 1:
        raise ValueError("candidate_limit must be at least 1.")

    _validate_table_documents(catalog, table)
    rows, resolved_candidate_limit = _search_unique_guideline_rows(
        table,
        text,
        where=where,
        mode=mode,
        limit=limit,
        candidate_limit=candidate_limit,
    )

    seen: set[str] = set()
    guideline_ids: list[str] = []
    best_rows: list[_DocumentHit] = []
    for row in rows:
        if row.guideline_id in seen:
            continue
        seen.add(row.guideline_id)
        guideline_ids.append(row.guideline_id)
        best_rows.append(row)
        if len(best_rows) >= limit:
            break

    if not best_rows:
        return _empty_result(
            text,
            limit,
            resolved_candidate_limit,
            where=where,
        )

    catalog_rows = _guideline_rows(catalog, guideline_ids)
    output_rows: list[Hit] = []
    for rank, row in enumerate(best_rows, start=1):
        guideline = catalog_rows[row.guideline_id]
        output_rows.append(
            Hit(
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

    return Result(
        query=text,
        rows=tuple(output_rows),
        limit=limit,
        candidate_limit=resolved_candidate_limit,
        where=where,
    )


def _search_unique_guideline_rows(
    table: "Table",
    text: str,
    *,
    where: str | None,
    mode: Mode,
    limit: int,
    candidate_limit: int | None,
) -> tuple[list[_DocumentHit], int]:
    document_count = int(table.count_rows())
    if document_count == 0:
        return [], 0
    max_candidates = (
        document_count
        if candidate_limit is None
        else min(candidate_limit, document_count)
    )
    requested = min(max(limit, 50), max_candidates)
    rows: list[_DocumentHit] = []

    while True:
        rows = _search_rows(
            table,
            text,
            where=where,
            mode=mode,
            limit=requested,
        )
        if _unique_guideline_count(rows) >= limit or requested >= max_candidates:
            return rows, requested
        requested = min(max_candidates, max(requested * 2, requested + 1))


def _search_rows(
    table: "Table",
    text: str,
    *,
    where: str | None,
    mode: Mode,
    limit: int,
) -> list[_DocumentHit]:
    return [
        _row_to_hit(row)
        for row in query(
            table,
            text,
            limit=limit,
            where=where,
            mode=mode,
        )
    ]


def _guideline_rows(
    catalog: Catalog,
    guideline_ids: list[str],
) -> dict[str, dict[str, object]]:
    if not guideline_ids:
        return {}
    rows = {
        row["id"]: row
        for row in catalog.guidelines()
        .filter(pl.col("id").is_in(guideline_ids))
        .select("id", "title", "description", "labels")
        .to_dicts()
    }
    missing = sorted(set(guideline_ids) - set(rows))
    if missing:
        raise ValueError(
            "LanceDB table returned guideline id(s) not present in catalog: "
            + ", ".join(missing)
        )
    return rows


def _validate_table_documents(catalog: Catalog, table: "Table") -> None:
    expected = _document_signatures(documents(catalog))
    actual = _document_signatures(cast(pl.DataFrame, pl.from_arrow(table.to_arrow())))
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    changed = sorted(
        document_id
        for document_id in set(expected) & set(actual)
        if expected[document_id] != actual[document_id]
    )
    if missing or extra or changed:
        parts: list[str] = []
        if missing:
            parts.append("missing " + ", ".join(missing))
        if extra:
            parts.append("extra " + ", ".join(extra))
        if changed:
            parts.append("changed " + ", ".join(changed))
        raise ValueError(
            "LanceDB table documents do not match the current catalog: "
            + "; ".join(parts)
        )


def _document_signatures(frame: pl.DataFrame) -> dict[str, tuple[object, ...]]:
    missing = [column for column in _DOCUMENT_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(
            "LanceDB table is missing catalog document column(s): "
            + ", ".join(missing)
        )
    rows = frame.select(_DOCUMENT_COLUMNS).to_dicts()
    return {
        cast(str, row["id"]): (
            row["parent_id"],
            row["role"],
            tuple(cast(list[str], row["labels"])),
            row["content_hash"],
            row["text"],
        )
        for row in rows
    }


def _empty_result(
    text: str,
    limit: int,
    candidate_limit: int,
    *,
    where: str | None,
) -> Result:
    return Result(
        query=text,
        rows=(),
        limit=limit,
        candidate_limit=candidate_limit,
        where=where,
    )


def _unique_guideline_count(rows: list[_DocumentHit]) -> int:
    return len({row.guideline_id for row in rows})


def _row_to_hit(row: Document) -> _DocumentHit:
    document_id = _required_string(row, "id")
    guideline_id = _required_string(row, "parent_id")
    role = _required_string(row, "role")
    document = _required_string(row, "text")
    return _DocumentHit(
        document_id=document_id,
        guideline_id=guideline_id,
        role=role,
        content_hash=_required_string(row, "content_hash"),
        score=_score(row.get("_score"), row.get("_distance")),
        labels=_labels(row.get("labels")),
        document=document,
    )


def _required_string(row: Document, key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"LanceDB table row is missing string field {key!r}.")
    return value


def _score(score: object, distance: object) -> float | None:
    if isinstance(score, int | float):
        return float(score)
    if isinstance(distance, int | float):
        return float(distance)
    return None


def _labels(labels: object) -> list[str]:
    if not isinstance(labels, list):
        return []
    return [label for label in labels if isinstance(label, str)]


__all__ = [
    "Hit",
    "Result",
    "search",
]
