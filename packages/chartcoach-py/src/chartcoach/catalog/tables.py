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
        .select("id", "role", "content")
    )


def build_references_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of formatted BibTeX references."""
    return (
        catalog_df.select("references")
        .explode("references")
        .drop_nulls()
        .unique()
        .select(
            bibtex="references",
            obj=pl.col("references").map_elements(
                lambda entry: {
                    "id": parse_bibtex_entry(entry)["ID"],
                    "formatted": format_bibtex_entry(entry),
                },
                return_dtype=pl.Struct(
                    [
                        pl.Field("id", pl.String),
                        pl.Field("formatted", pl.String),
                    ]
                ),
            ),
        )
        .select(
            id=pl.col("obj").struct.field("id"),
            bibtex="bibtex",
            formatted=pl.col("obj").struct.field("formatted"),
        )
        .sort("id")
    )


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
