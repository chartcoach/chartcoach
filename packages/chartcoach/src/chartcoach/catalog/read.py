from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, cast

import polars as pl

from .query import query_entries, validate_section_roles

if TYPE_CHECKING:
    from .collection import Catalog


def retrieve_entry_records(
    catalog: Catalog,
    *,
    ids: Sequence[str],
    roles: Sequence[str] = (),
    source_detail: str = "minimal",
) -> list[dict[str, object]]:
    validate_section_roles(catalog, roles)
    frame = query_entries(catalog, ids=ids, limit=len(ids), include_body=True)
    role_set = set(roles) if roles else None
    return [
        entry_record_from_row(
            row,
            roles=role_set,
            source_detail=source_detail,
            sources=source_rows(catalog, cast(str, row["id"]), detail=source_detail),
        )
        for row in frame.to_dicts()
    ]


def entry_record_from_row(
    row: Mapping[str, object],
    *,
    roles: set[str] | None,
    source_detail: str,
    sources: list[dict[str, object]],
) -> dict[str, object]:
    raw_sections = cast(Sequence[Mapping[str, object]], row.get("sections") or ())
    sections = [
        {
            "role": str(section["role"]),
            "title": str(section["title"]),
            "content": str(section["content"]),
        }
        for section in raw_sections
        if roles is None or section.get("role") in roles
    ]
    record = {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "labels": list(cast(Sequence[str], row.get("labels") or ())),
        "sections": sections,
        "sources": sources,
    }
    if source_detail == "full":
        record["references"] = list(cast(Sequence[str], row.get("references") or ()))
    return record


def source_rows(
    catalog: Catalog, guideline_id: str, *, detail: str
) -> list[dict[str, object]]:
    if detail == "none":
        return []
    frame = catalog.guideline_sources().filter(pl.col("guideline_id") == guideline_id)
    if frame.is_empty():
        return []
    columns = ["reference_id", "authors_text", "year", "source_title", "doi", "url"]
    if detail == "full":
        columns = frame.columns
    return frame.select(
        [column for column in columns if column in frame.columns]
    ).to_dicts()


__all__ = ["entry_record_from_row", "retrieve_entry_records", "source_rows"]
