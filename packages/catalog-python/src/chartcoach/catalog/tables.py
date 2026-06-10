from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

import polars as pl

from .labels import parse_label
from .schemas import (
    CATALOG_SCHEMA,
    GUIDELINE_SCHEMA,
    GUIDELINES_SCHEMA,
    GUIDELINE_LABELS_SCHEMA,
    LABELS_SCHEMA,
    SECTIONS_SCHEMA,
)

if TYPE_CHECKING:
    from .entries import CatalogEntry


def build_catalog_df(entries: Sequence["CatalogEntry"]) -> pl.DataFrame:
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
