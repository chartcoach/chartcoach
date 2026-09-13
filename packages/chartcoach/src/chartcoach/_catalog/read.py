from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Literal, cast

import polars as pl
from typing_extensions import NotRequired, TypedDict

from .errors import CatalogValidationError
from .query import query_entries, validate_ids, validate_section_roles

if TYPE_CHECKING:
    from .model import Catalog

SourceDetail = Literal["none", "minimal", "full"]


class MinimalSourceRecord(TypedDict):
    reference_id: str
    authors_text: str | None
    year: str | None
    source_title: str | None
    doi: str | None
    url: str | None


class FullSourceRecord(MinimalSourceRecord):
    guideline_id: str
    source_type: str | None
    authors: list[str]
    journal: str | None
    booktitle: str | None
    publisher: str | None


class SectionRecord(TypedDict):
    """One ordered guideline section returned by `Catalog.read`."""

    role: str
    title: str
    content: str


class GuidelineEntryRecord(TypedDict):
    """One complete selected guideline entry returned by `Catalog.read`."""

    id: str
    title: str
    description: str
    labels: list[str]
    sections: list[SectionRecord]
    sources: list[MinimalSourceRecord | FullSourceRecord]
    references: NotRequired[list[str]]


def retrieve_entry_records(
    catalog: Catalog,
    *,
    ids: Sequence[str],
    roles: Sequence[str] = (),
    source_detail: SourceDetail = "minimal",
) -> list[GuidelineEntryRecord]:
    """Return complete guideline entry records for exact guideline entry IDs.

    Args:
        catalog: Catalog to read.
        ids: Guideline entry IDs in output order.
        roles: Section roles to retain. Every role is retained when omitted.
        source_detail: `none` omits source rows, `minimal` includes citation
            fields, and `full` also includes every parsed source field plus the
            entry's raw BibTeX references.

    Returns:
        One dictionary per requested guideline entry ID.

    Raises:
        CatalogError: An ID, role, or source detail value is invalid.
    """

    _validate_source_detail(source_detail)
    validate_section_roles(catalog, roles)
    if not ids:
        validate_ids(catalog, ids)
        return []
    frame = query_entries(catalog, ids=ids, limit=len(ids), include_body=True)
    role_set = set(roles) if roles else None
    sources = (
        None
        if source_detail == "none"
        else catalog.table("guideline_sources").filter(
            pl.col("guideline_id").is_in(ids)
        )
    )
    return [
        entry_record_from_row(
            row,
            roles=role_set,
            source_detail=source_detail,
            sources=source_rows(
                sources,
                cast(str, row["id"]),
                detail=source_detail,
            ),
        )
        for row in frame.to_dicts()
    ]


def entry_record_from_row(
    row: Mapping[str, object],
    *,
    roles: set[str] | None,
    source_detail: SourceDetail,
    sources: list[dict[str, object]],
) -> GuidelineEntryRecord:
    raw_sections = cast(Sequence[Mapping[str, object]], row.get("sections") or ())
    sections: list[SectionRecord] = [
        {
            "role": str(section["role"]),
            "title": str(section["title"]),
            "content": str(section["content"]),
        }
        for section in raw_sections
        if roles is None or section.get("role") in roles
    ]
    record: GuidelineEntryRecord = {
        "id": str(row["id"]),
        "title": str(row["title"]),
        "description": str(row["description"]),
        "labels": list(cast(Sequence[str], row.get("labels") or ())),
        "sections": sections,
        "sources": cast(list[MinimalSourceRecord | FullSourceRecord], sources),
    }
    if source_detail == "full":
        record["references"] = list(cast(Sequence[str], row.get("references") or ()))
    return record


def source_rows(
    frame: pl.DataFrame | None, guideline_id: str, *, detail: SourceDetail
) -> list[dict[str, object]]:
    if detail == "none" or frame is None:
        return []
    selected = frame.filter(pl.col("guideline_id") == guideline_id)
    if selected.is_empty():
        return []
    columns = ["reference_id", "authors_text", "year", "source_title", "doi", "url"]
    if detail == "full":
        columns = [column for column in selected.columns if column != "bibtex"]
    return selected.select(
        [column for column in columns if column in selected.columns]
    ).to_dicts()


def _validate_source_detail(source_detail: str) -> None:
    if source_detail not in {"none", "minimal", "full"}:
        raise CatalogValidationError(
            f"Unknown source detail: {source_detail!r}",
            hints=["Choose one of: none, minimal, full."],
        )


__all__ = [
    "GuidelineEntryRecord",
    "SectionRecord",
    "SourceDetail",
    "entry_record_from_row",
    "retrieve_entry_records",
    "source_rows",
]
