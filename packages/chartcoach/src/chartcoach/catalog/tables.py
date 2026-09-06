from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

import polars as pl

from .labels import parse_label
from .schemas import (
    CATALOG_SCHEMA,
    GUIDELINE_LABELS_SCHEMA,
    GUIDELINES_SCHEMA,
    SECTIONS_SCHEMA,
)

if TYPE_CHECKING:
    from .entries import Guideline


def build_catalog_df(guidelines: Sequence[Guideline]) -> pl.DataFrame:
    """Build the serialized catalog dataframe."""
    if not guidelines:
        return pl.DataFrame(schema=CATALOG_SCHEMA)

    return pl.from_dicts(
        [guideline.to_record() for guideline in guidelines],
        schema=CATALOG_SCHEMA,
    )


def build_guidelines_df(catalog_df: pl.DataFrame) -> pl.DataFrame:
    """Build guideline rows with markdown derived from sections."""
    if catalog_df.is_empty():
        return pl.DataFrame(schema=GUIDELINES_SCHEMA)
    section = pl.element()
    body = (
        pl.col("sections")
        .list.eval(
            pl.when(section.struct.field("role") == "__dangling__")
            .then(section.struct.field("content"))
            .otherwise(
                pl.concat_str(
                    [
                        pl.lit("## "),
                        section.struct.field("title"),
                        pl.lit(" <!-- role: "),
                        section.struct.field("role"),
                        pl.lit(" -->\n\n"),
                        section.struct.field("content"),
                    ]
                )
            )
        )
        .list.join("\n\n")
    )
    return catalog_df.select(
        "id",
        "title",
        "description",
        "labels",
        body.alias("body"),
        "sections",
    )


def build_sections_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of guideline sections."""
    if guidelines_df.is_empty():
        return pl.DataFrame(schema=SECTIONS_SCHEMA)
    sections = (
        guidelines_df.select("id", "sections")
        .explode("sections", empty_as_null=True)
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


def build_guideline_labels_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    """Build a dataframe of per-guideline labels."""
    labels = (
        guidelines_df.select("id", "labels")
        .explode("labels", empty_as_null=True)
        .drop_nulls()
    )
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
