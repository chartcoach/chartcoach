from __future__ import annotations

import dataclasses as dc
from collections.abc import Sequence
from typing import TYPE_CHECKING

import polars as pl

from ..guideline.bibliography import parse_bibtex_reference
from ..guideline.labels import parse_label

if TYPE_CHECKING:
    from .collection import _CatalogRecord


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
CATALOG_SCHEMA = pl.Schema(
    {
        "id": pl.String,
        "guideline": GUIDELINE_SCHEMA,
        "references": pl.List(pl.String),
    }
)
GUIDELINES_SCHEMA = {
    "id": pl.String,
    "title": pl.String,
    "bibliography": pl.String,
    "description": pl.String,
    "labels": pl.List(pl.String),
    "body": pl.String,
    "sections": pl.List(SECTION_SCHEMA),
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
    "family": pl.String,
    "category": pl.String,
    "modifier": pl.String,
}
LABELS_SCHEMA = {
    "family": pl.String,
    "category": pl.String,
    "modifier": pl.String,
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
    "bibtex": pl.String,
}
GUIDELINE_SOURCES_SCHEMA = {
    "guideline_id": pl.String,
    "reference_id": pl.String,
    "source_type": pl.String,
    "authors": pl.List(pl.String),
    "authors_text": pl.String,
    "year": pl.String,
    "source_title": pl.String,
    "journal": pl.String,
    "booktitle": pl.String,
    "publisher": pl.String,
    "url": pl.String,
    "doi": pl.String,
    "bibtex": pl.String,
}


@dc.dataclass(frozen=True, slots=True)
class ReferenceTables:
    references: pl.DataFrame
    guideline_references: pl.DataFrame


def build_catalog_df(entries: Sequence[_CatalogRecord]) -> pl.DataFrame:
    """Build the serialized catalog dataframe."""
    if not entries:
        return pl.DataFrame(schema=CATALOG_SCHEMA)

    return pl.from_dicts([entry.to_record() for entry in entries]).select(
        pl.col("id").cast(pl.String),
        pl.col("guideline").cast(GUIDELINE_SCHEMA),
        pl.col("references").cast(pl.List(pl.String)),
    )


def build_guidelines_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of unnested guidelines."""
    if catalog_df.is_empty():
        return pl.DataFrame(schema=GUIDELINES_SCHEMA)
    return catalog_df.select("guideline").unnest("guideline")


def build_sections_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of guideline sections."""
    if guidelines_df.is_empty():
        return pl.DataFrame(schema=SECTIONS_SCHEMA)
    sections = (
        guidelines_df.select("id", "sections")
        .explode("sections")
        .drop_nulls("sections")
    )
    if sections.is_empty():
        return pl.DataFrame(schema=SECTIONS_SCHEMA)
    return sections.unnest("sections").select(
        guideline_id=pl.col("id"),
        role=pl.col("role"),
        title=pl.col("title"),
        content=pl.col("content"),
    )


def build_reference_tables(catalog_df: pl.DataFrame) -> ReferenceTables:
    """Build parsed reference tables in one BibTeX parse pass."""

    exploded = (
        catalog_df.select(
            pl.col("id").alias("guideline_id"),
            pl.col("references").alias("bibtex"),
        )
        .explode("bibtex")
        .drop_nulls("bibtex")
        .unique()
    )
    if exploded.is_empty():
        return ReferenceTables(
            references=pl.DataFrame(schema=REFERENCES_SCHEMA),
            guideline_references=pl.DataFrame(schema=GUIDELINE_REFERENCES_SCHEMA),
        )

    bibtex_to_id: dict[str, str] = {}
    reference_rows: list[dict[str, object]] = []
    seen_reference_ids: set[str] = set()
    for bibtex in exploded.select("bibtex").unique().get_column("bibtex").to_list():
        if not isinstance(bibtex, str):
            continue
        reference = parse_bibtex_reference(bibtex)
        parsed = reference.entry
        reference_id = reference.id
        bibtex_to_id[bibtex] = reference_id
        if reference_id in seen_reference_ids:
            continue
        seen_reference_ids.add(reference_id)

        authors_text = _string_or_none(parsed.get("author"))
        reference_rows.append(
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
                "bibtex": bibtex,
            }
        )
    edge_rows = [
        {"guideline_id": str(guideline_id), "reference_id": bibtex_to_id[bibtex]}
        for guideline_id, bibtex in exploded.iter_rows()
        if isinstance(bibtex, str) and bibtex in bibtex_to_id
    ]

    return ReferenceTables(
        references=(
            pl.DataFrame(reference_rows, schema=REFERENCES_SCHEMA)
            .unique("id")
            .sort("id")
        ),
        guideline_references=(
            pl.DataFrame(edge_rows, schema=GUIDELINE_REFERENCES_SCHEMA)
            .unique()
            .sort("guideline_id", "reference_id")
        ),
    )


def build_references_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of parsed BibTeX references."""

    return build_reference_tables(catalog_df).references


def build_labels_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of unique label family/category/modifier rows."""
    labels = guidelines_df.select("labels").explode("labels").drop_nulls()
    if labels.is_empty():
        return pl.DataFrame(schema=LABELS_SCHEMA)

    rows = []
    for label in labels.unique("labels").get_column("labels").to_list():
        parsed = parse_label(label)
        rows.append(
            {
                "family": parsed.family,
                "category": parsed.category,
                "modifier": parsed.modifier,
            }
        )
    return (
        pl.DataFrame(rows, schema=LABELS_SCHEMA)
        .unique()
        .sort("family", "category", "modifier")
    )


def build_guideline_labels_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of per-guideline labels."""
    labels = guidelines_df.select("id", "labels").explode("labels").drop_nulls()
    if labels.is_empty():
        return pl.DataFrame(schema=GUIDELINE_LABELS_SCHEMA)

    rows = []
    for guideline_id, label in labels.iter_rows():
        parsed = parse_label(label)
        rows.append(
            {
                "guideline_id": str(guideline_id),
                "label": parsed.label,
                "family": parsed.family,
                "category": parsed.category,
                "modifier": parsed.modifier,
            }
        )
    return (
        pl.DataFrame(rows, schema=GUIDELINE_LABELS_SCHEMA)
        .unique()
        .sort("guideline_id", "label")
    )


def build_guideline_references_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of guideline-to-reference edges."""

    return build_reference_tables(catalog_df).guideline_references


def build_guideline_sources_df(
    guideline_references_df: pl.DataFrame,
    references_df: pl.DataFrame,
) -> pl.DataFrame:
    """Build a dataframe of guideline-to-source rows for SQL joins."""

    if guideline_references_df.is_empty() or references_df.is_empty():
        return pl.DataFrame(schema=GUIDELINE_SOURCES_SCHEMA)
    sources = references_df.rename(
        {
            "id": "reference_id",
            "title": "source_title",
        }
    )
    return (
        guideline_references_df.join(sources, on="reference_id", how="left")
        .select(list(GUIDELINE_SOURCES_SCHEMA))
        .cast(pl.Schema(GUIDELINE_SOURCES_SCHEMA))
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
