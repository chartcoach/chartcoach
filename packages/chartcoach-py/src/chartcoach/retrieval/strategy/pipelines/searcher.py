from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.situation import situation_text_parts
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

    @staticmethod
    def build_base_query_text(request: RetrievalRequest) -> str:
        return situation_text_parts(request).base

    @staticmethod
    def build_query_text(request: RetrievalRequest) -> str:
        return situation_text_parts(request).with_chart_vision

    @staticmethod
    def _sanitize_fts_query(query_text: str) -> str:
        # Lance FTS treats double quotes as phrase-query syntax, which requires
        # token positions that our current index does not store.
        return query_text.replace('"', " ")

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
        query_text = self._sanitize_fts_query(query_text)
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
        query_text = self._sanitize_fts_query(query_text)
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
        return GuidelineSearcher.aggregate_guideline_hits_with_evidence(
            hits_df,
            k=k,
            score_column=score_column,
            score_boost=score_boost,
            evidence_per_guideline=0,
        ).select("id", "score", "best_role")

    @staticmethod
    def aggregate_guideline_hits_with_evidence(
        hits_df: pl.DataFrame,
        *,
        k: int,
        score_column: str = "score",
        score_boost: float = 0.25,
        evidence_per_guideline: int = 3,
        evidence_max_chars: int = 280,
    ) -> pl.DataFrame:
        """Aggregate row-level hits into a guideline-level ranking, retaining evidence snippets.

        Scoring:
        - base score = max score over matched rows
        - boost = score_boost * mean score over matched rows

        Evidence:
        - per-guideline, keep the top `evidence_per_guideline` matched rows (highest score).
        - each snippet includes (role, text, score) pulled from the index row.
        """

        if hits_df.is_empty() or k <= 0:
            return pl.DataFrame({"id": [], "score": [], "best_role": [], "evidence": []})

        if score_column not in hits_df.columns:
            raise ValueError(f"Missing required column {score_column!r}.")

        sorted_hits = hits_df.sort(score_column, descending=True)

        has_text = "text" in sorted_hits.columns
        keep_evidence = evidence_per_guideline > 0 and has_text
        if keep_evidence:
            text_expr = (
                pl.col("text")
                .cast(pl.String)
                .fill_null("")
                .str.replace_all("\r", " ")
                .str.replace_all("\n", " ")
                .str.replace_all("\t", " ")
                .str.strip_chars()
            )
            if evidence_max_chars > 0:
                text_expr = text_expr.str.slice(0, int(evidence_max_chars))

            evidence_expr = (
                pl.struct(
                    [
                        pl.col("role").alias("role"),
                        text_expr.alias("text"),
                        pl.col(score_column).alias("score"),
                    ]
                )
                .head(int(evidence_per_guideline))
                .alias("evidence")
            )
        else:
            evidence_expr = pl.lit([]).alias("evidence")

        agg = (
            sorted_hits.group_by("id", maintain_order=True)
            .agg(
                pl.first(score_column).alias("max_score"),
                pl.mean(score_column).alias("mean_score"),
                pl.first("role").alias("best_role"),
                evidence_expr,
            )
            .with_columns(
                score=pl.col("max_score") + (pl.col("mean_score") * float(score_boost))
            )
            .sort("score", descending=True)
            .head(int(k))
        )
        return agg.select("id", "score", "best_role", "evidence")
