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
            labels=pl.col("guideline").struct.field("labels").list.join(";").fill_null(""),
        )

        if not self.include_labels:
            return df.select(
                "id",
                "role",
                content=pl.concat_str(["title", "description"], separator=self.separator),
            )

        return (
            df.with_columns(
                label_line=pl.when(pl.col("labels") != "")
                .then(pl.lit(self.label_prefix) + pl.col("labels"))
                .otherwise(pl.lit(""))
            )
            .select(
                "id",
                "role",
                content=pl.concat_str(
                    ["title", "description", "label_line"], separator=self.separator
                ).str.strip_chars(),
            )
        )


DEFAULT_TEXT_SOURCES: tuple[CatalogTextSource, ...] = (
    SectionsTextSource(),
    GuidelineFieldTextSource("title"),
    GuidelineFieldTextSource("description"),
)
