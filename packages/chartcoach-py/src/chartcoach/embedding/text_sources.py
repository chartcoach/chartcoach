from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import polars as pl

from chartcoach.catalog import Catalog


class CatalogTextSource(Protocol):
    def text_df(self, catalog: Catalog) -> pl.DataFrame: ...


@dataclass(frozen=True, slots=True)
class SectionsTextSource:
    roles: set[str] | None = None

    def text_df(self, catalog: Catalog) -> pl.DataFrame:
        df = catalog.sections_df()
        if self.roles is None:
            return df
        return df.filter(pl.col("role").is_in(sorted(self.roles)))


@dataclass(frozen=True, slots=True)
class SectionsWithTitleTextSource:
    """Index guideline sections with additional heading context.

    This avoids a common retrieval failure mode where short section content is
    embedded without the discriminative section heading.
    """

    roles: set[str] | None = None
    include_guideline_title: bool = True
    separator: str = "\n"

    def text_df(self, catalog: Catalog) -> pl.DataFrame:
        df = (
            catalog.df()
            .select("guideline")
            .unnest("guideline")
            .select(
                "id",
                guideline_title=pl.col("title").fill_null(""),
                sections=pl.col("sections"),
            )
            .explode("sections")
            .unnest("sections")
            .select(
                "id",
                "role",
                "guideline_title",
                section_title=pl.col("title").fill_null(""),
                section_content=pl.col("content").fill_null(""),
            )
        )

        if self.roles is not None:
            df = df.filter(pl.col("role").is_in(sorted(self.roles)))

        parts = [pl.col("section_content")]
        if self.include_guideline_title:
            parts = [
                pl.col("guideline_title"),
                pl.col("section_title"),
                pl.col("section_content"),
            ]
        else:
            parts = [pl.col("section_title"), pl.col("section_content")]

        return df.select(
            "id",
            "role",
            content=pl.concat_str(parts, separator=self.separator).str.strip_chars(),
        )


@dataclass(frozen=True, slots=True)
class GuidelineFieldTextSource:
    field: str
    role: str | None = None

    def text_df(self, catalog: Catalog) -> pl.DataFrame:
        role_name = self.field if self.role is None else self.role
        return catalog.df().select(
            "id",
            role=pl.lit(role_name),
            content=pl.col("guideline").struct.field(self.field).fill_null(""),
        )


@dataclass(frozen=True, slots=True)
class GuidelineLabelsTextSource:
    """Index a guideline's structured labels as a single text row."""

    role: str = "labels"
    separator: str = "; "

    def text_df(self, catalog: Catalog) -> pl.DataFrame:
        return catalog.df().select(
            "id",
            role=pl.lit(self.role),
            content=pl.col("guideline")
            .struct.field("labels")
            .list.join(self.separator)
            .fill_null(""),
        )


@dataclass(frozen=True, slots=True)
class GuidelineAbstractTextSource:
    """Index a guideline-level abstract (title + description + optional labels)."""

    role: str = "abstract"
    separator: str = "\n"
    label_prefix: str = "Labels: "
    include_labels: bool = True

    def text_df(self, catalog: Catalog) -> pl.DataFrame:
        df = catalog.df().select(
            "id",
            role=pl.lit(self.role),
            title=pl.col("guideline").struct.field("title").fill_null(""),
            description=pl.col("guideline").struct.field("description").fill_null(""),
            labels=pl.col("guideline")
            .struct.field("labels")
            .list.join(";")
            .fill_null(""),
        )

        if not self.include_labels:
            return df.select(
                "id",
                "role",
                content=pl.concat_str(
                    ["title", "description"], separator=self.separator
                ),
            )

        return df.with_columns(
            label_line=pl.when(pl.col("labels") != "")
            .then(pl.lit(self.label_prefix) + pl.col("labels"))
            .otherwise(pl.lit(""))
        ).select(
            "id",
            "role",
            content=pl.concat_str(
                ["title", "description", "label_line"], separator=self.separator
            ).str.strip_chars(),
        )


DEFAULT_TEXT_SOURCES: tuple[CatalogTextSource, ...] = (
    SectionsTextSource(),
    GuidelineFieldTextSource("title"),
    GuidelineFieldTextSource("description"),
)
