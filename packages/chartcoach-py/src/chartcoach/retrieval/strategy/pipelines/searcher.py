from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.request_text import build_situation_with_query
from chartcoach.retrieval.strategy.types import RetrievalRequest
from chartcoach.retrieval.strategy.vector_index import CatalogVectorIndex


@dataclass(slots=True)
class GuidelineSearcher:
    """Thin helper around a hybrid-capable `CatalogVectorIndex`."""

    catalog: Catalog
    vector_index: CatalogVectorIndex

    def __post_init__(self) -> None:
        # Fail fast: these pipelines require an index backend that supports hybrid + FTS.
        _ = self.vector_index.lance()

    def build_query_text(self, request: RetrievalRequest) -> str:
        return build_situation_with_query(request)

    def search_dense(
        self,
        *,
        query_vector: np.ndarray,
        k: int,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame:
        return self.vector_index.lance().search(
            query_vector,
            k=k,
            roles=roles,
            ids=ids,
        )

    def search_fts(
        self,
        *,
        query_text: str,
        k: int,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame:
        return self.vector_index.lance().search_fts(
            query_text,
            k=k,
            roles=roles,
            ids=ids,
        )

    def search_hybrid(
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,
        k: int,
        reranker: object | None = None,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
        fts_columns: str | list[str] | None = None,
    ) -> pl.DataFrame:
        return self.vector_index.lance().search_hybrid(
            query_text=query_text,
            query_vector=query_vector,
            reranker=reranker,
            k=k,
            roles=roles,
            ids=ids,
            fts_columns=fts_columns,
        )

    @staticmethod
    def aggregate_guideline_hits(
        hits_df: pl.DataFrame,
        *,
        k: int,
        score_column: str = "score",
        score_boost: float = 0.25,
    ) -> pl.DataFrame:
        """Aggregate row-level hits into guideline-level ranking.

        We use a conservative scoring scheme:
        - base score = max score over matched rows
        - boost = score_boost * mean score over matched rows
        """

        if hits_df.is_empty() or k <= 0:
            return pl.DataFrame({"id": [], "score": [], "best_role": []})

        if score_column not in hits_df.columns:
            raise ValueError(f"Missing required column {score_column!r}.")

        sorted_hits = hits_df.sort(score_column, descending=True)
        agg = (
            sorted_hits.group_by("id")
            .agg(
                pl.first(score_column).alias("max_score"),
                pl.mean(score_column).alias("mean_score"),
                pl.first("role").alias("best_role"),
            )
            .with_columns(
                score=pl.col("max_score") + (pl.col("mean_score") * float(score_boost))
            )
            .sort("score", descending=True)
            .head(int(k))
        )
        return agg.select("id", "score", "best_role")
