from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import polars as pl

from chartcoach.catalog.catalog import Catalog


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


DEFAULT_TEXT_SOURCES: tuple[CatalogTextSource, ...] = (
    SectionsTextSource(),
    GuidelineFieldTextSource("title"),
    GuidelineFieldTextSource("description"),
)
