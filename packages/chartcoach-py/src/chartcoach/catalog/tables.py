from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

import polars as pl

from ..guideline import format_bibtex_entry, parse_bibtex_entry

if TYPE_CHECKING:
    from .collection import CatalogEntry


SECTION_SCHEMA = pl.Struct(
    [
        pl.Field("role", pl.String),
        pl.Field("title", pl.String),
        pl.Field("content", pl.String),
    ]
)
GUIDELINE_SCHEMA = pl.Struct(
    [
        pl.Field("id", pl.String),
        pl.Field("title", pl.String),
        pl.Field("bibliography", pl.String),
        pl.Field("description", pl.String),
        pl.Field("labels", pl.List(pl.String)),
        pl.Field("body", pl.String),
        pl.Field("sections", pl.List(SECTION_SCHEMA)),
    ]
)
CATALOG_SCHEMA = {
    "id": pl.String,
    "guideline": GUIDELINE_SCHEMA,
    "references": pl.List(pl.String),
}
SECTIONS_SCHEMA = {
    "guideline_id": pl.String,
    "role": pl.String,
    "title": pl.String,
    "content": pl.String,
}
GUIDELINE_LABELS_SCHEMA = {
    "guideline_id": pl.String,
    "label": pl.String,
    "category": pl.String,
    "subcategory": pl.String,
}
GUIDELINE_REFERENCES_SCHEMA = {
    "guideline_id": pl.String,
    "reference_id": pl.String,
}
REFERENCES_SCHEMA = {
    "id": pl.String,
    "source_type": pl.String,
    "authors": pl.List(pl.String),
    "authors_text": pl.String,
    "year": pl.String,
    "title": pl.String,
    "journal": pl.String,
    "booktitle": pl.String,
    "publisher": pl.String,
    "url": pl.String,
    "doi": pl.String,
    "formatted": pl.String,
    "bibtex": pl.String,
}


def build_catalog_df(entries: Sequence[CatalogEntry]) -> pl.DataFrame:
    """Build the canonical catalog dataframe."""
    if not entries:
        return pl.DataFrame(schema=CATALOG_SCHEMA)

    return (
        pl.from_dicts([entry.model_dump() for entry in entries])
        .select("id", "guideline", "references")
        .unique("id")
        .sort("id")
    )


def build_guidelines_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of unnested guidelines."""
    return catalog_df.select("guideline").unnest("guideline")


def build_sections_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of guideline sections."""
    return (
        guidelines_df.select("id", "sections")
        .explode("sections")
        .unnest("sections")
        .select(
            guideline_id=pl.col("id"),
            role=pl.col("role"),
            title=pl.col("title"),
            content=pl.col("content"),
        )
    )


def build_references_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of parsed and formatted BibTeX references."""
    rows: list[dict[str, object]] = []
    seen: set[str] = set()

    for bibtex in (
        catalog_df.select("references")
        .explode("references")
        .drop_nulls()
        .get_column("references")
    ).to_list():
        parsed = parse_bibtex_entry(bibtex)
        reference_id = str(parsed["ID"])
        if reference_id in seen:
            continue
        seen.add(reference_id)

        authors_text = _string_or_none(parsed.get("author"))
        rows.append(
            {
                "id": reference_id,
                "source_type": _entry_type_or_none(parsed.get("ENTRYTYPE")),
                "authors": _split_authors(authors_text),
                "authors_text": authors_text,
                "year": _string_or_none(parsed.get("year")),
                "title": _string_or_none(parsed.get("title")),
                "journal": _string_or_none(parsed.get("journal")),
                "booktitle": _string_or_none(parsed.get("booktitle")),
                "publisher": _string_or_none(parsed.get("publisher")),
                "url": _string_or_none(parsed.get("url")),
                "doi": _string_or_none(parsed.get("doi")),
                "formatted": format_bibtex_entry(bibtex),
                "bibtex": bibtex,
            }
        )

    if not rows:
        return pl.DataFrame(schema=REFERENCES_SCHEMA)

    return pl.DataFrame(rows, schema=REFERENCES_SCHEMA).sort("id")


def build_labels_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of unique label categories/subcategories."""
    return (
        guidelines_df.select("labels")
        .explode("labels")
        .select(
            category=pl.col("labels").str.split(":").list.get(0),
            subcategory=pl.col("labels").str.split(":").list.get(1),
        )
        .unique()
        .sort("category", "subcategory")
    )


def build_guideline_labels_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of per-guideline labels."""
    return (
        guidelines_df.select("id", "labels")
        .explode("labels")
        .drop_nulls()
        .select(
            guideline_id=pl.col("id"),
            label=pl.col("labels"),
            category=pl.col("labels").str.split(":").list.get(0),
            subcategory=pl.col("labels").str.split(":").list.get(1),
        )
        .unique()
        .sort("guideline_id", "label")
    )


def build_guideline_references_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of guideline-to-reference edges."""
    rows: list[dict[str, str]] = []

    for guideline_id, references in catalog_df.select("id", "references").iter_rows():
        if not references:
            continue
        for bibtex in references:
            parsed = parse_bibtex_entry(bibtex)
            rows.append(
                {
                    "guideline_id": str(guideline_id),
                    "reference_id": str(parsed["ID"]),
                }
            )

    if not rows:
        return pl.DataFrame(schema=GUIDELINE_REFERENCES_SCHEMA)

    return (
        pl.DataFrame(rows, schema=GUIDELINE_REFERENCES_SCHEMA)
        .unique()
        .sort("guideline_id", "reference_id")
    )


def _string_or_none(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _split_authors(authors_text: str | None) -> list[str]:
    if authors_text is None:
        return []
    return [part.strip() for part in authors_text.split(" and ") if part.strip()]


def _entry_type_or_none(value: object) -> str | None:
    text = _string_or_none(value)
    if text is None:
        return None
    return text.lower()
