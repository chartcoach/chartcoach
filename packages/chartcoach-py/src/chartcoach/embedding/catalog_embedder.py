from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import polars as pl

from chartcoach.catalog.catalog import Catalog

from .text_sources import CatalogTextSource, DEFAULT_TEXT_SOURCES


def embed_text(text_df: pl.DataFrame, **kwargs: Any) -> pl.DataFrame:
    """Lazily import the embedding implementation (optional dependency)."""

    from .atlas import embed_text as _embed_text

    return _embed_text(text_df, **kwargs)


def project_embedded_text(
    embedded_text_df: pl.DataFrame,
    *,
    x: str = "projection_x",
    y: str = "projection_y",
    neighbors: str = "neighbors",
    embedding_column: str = "embedding",
    umap_args: dict[str, object] | None = None,
) -> pl.DataFrame:
    """Lazily import the projection implementation (optional dependency)."""

    from .atlas import project_embedded_text as _project_embedded_text

    return _project_embedded_text(
        embedded_text_df,
        x=x,
        y=y,
        neighbors=neighbors,
        embedding_column=embedding_column,
        umap_args=umap_args,
    )


@dataclass(slots=True)
class CatalogEmbedder:
    """Embeds catalog text into vector space.

    This utility knows how to extract text from a `Catalog` and compute embeddings
    via `chartcoach.embedding`, but it is intentionally agnostic to how embeddings
    are indexed or queried (DuckDB/Lance/etc.).
    """

    catalog: Catalog
    text_sources: tuple[CatalogTextSource, ...] = DEFAULT_TEXT_SOURCES

    def text_df(
        self, *, sources: Sequence[CatalogTextSource] | None = None
    ) -> pl.DataFrame:
        used_sources = self.text_sources if sources is None else tuple(sources)
        if not used_sources:
            return pl.DataFrame(
                schema={"id": pl.String, "role": pl.String, "content": pl.String}
            )
        return pl.concat(
            [source.text_df(self.catalog) for source in used_sources], how="vertical"
        )

    def embedded_text_df(
        self,
        *,
        sources: Sequence[CatalogTextSource] | None = None,
        **embed_kwargs: Any,
    ) -> pl.DataFrame:
        return embed_text(self.text_df(sources=sources), **embed_kwargs)

    def projected_text_df(
        self,
        *,
        sources: Sequence[CatalogTextSource] | None = None,
        select: list[pl.Expr | str] | None = None,
        x: str = "projection_x",
        y: str = "projection_y",
        neighbors: str = "neighbors",
        embedding_column: str = "embedding",
        umap_args: dict[str, object] | None = None,
        **embed_kwargs: Any,
    ) -> pl.DataFrame:
        df = self.catalog.df()
        embedded_text_df = embed_text(
            self.text_df(sources=sources),
            embedding_column=embedding_column,
            **embed_kwargs,
        )

        if select is not None:
            id_df = df.select("id")
            selected_df = df.select(*select)
            join_df = pl.concat([id_df, selected_df], how="horizontal")
            embedded_text_df = embedded_text_df.join(
                join_df,
                on="id",
                how="left",
            )

        return project_embedded_text(
            embedded_text_df,
            x=x,
            y=y,
            neighbors=neighbors,
            embedding_column=embedding_column,
            umap_args={} if umap_args is None else umap_args,
        )

    def group_by_guideline(
        self,
        df: pl.DataFrame,
        *,
        id_column: str = "id",
        items_column: str = "items",
    ) -> pl.DataFrame:
        value_columns = [c for c in df.columns if c != id_column]
        return df.group_by(id_column).agg(pl.struct(value_columns).alias(items_column))
