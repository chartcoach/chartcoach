from __future__ import annotations

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.embedding.vectors import vector_matrix
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.request_text import get_text_by_role, require_text_by_role
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .hints import build_search_text, chart_bonus, infer_hints
from .hints_v4 import (
    build_search_text_v4,
    chart_bonus_v4,
    domain_penalty_v4,
    infer_hints_v4,
    should_exclude_guideline_v4,
    task_bonus_v4,
)
from .ranking import mmr_select
from .searcher import GuidelineSearcher


class DenseMmrStrategy(RetrievalStrategy):
    """Dense bi-encoder retrieval with guideline-level aggregation + MMR."""

    id = "dense-mmr@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 10,
        mmr_lambda: float = 0.65,
        mmr_candidate_limit: int = 200,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._mmr_lambda = float(mmr_lambda)
        self._mmr_candidate_limit = int(mmr_candidate_limit)

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df = self._searcher.search_dense(query_vector=query_vec, k=raw_k)
        if hits_df.is_empty():
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=raw_k)
        agg = agg.head(int(min(self._mmr_candidate_limit, agg.height)))

        candidate_ids = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
        relevance = {
            row["id"]: float(row["score"])
            for row in agg.select("id", "score").to_dicts()
            if isinstance(row.get("id"), str)
        }

        embedding_column = self._searcher.vector_index.config.embedding_column
        embed_df = self._searcher.vector_index.embedded_text_df.filter(
            pl.col("id").is_in(candidate_ids)
        ).select("id", embedding_column)

        embeddings: dict[str, np.ndarray] = {}
        for gid in candidate_ids:
            vecs = embed_df.filter(pl.col("id") == gid).get_column(embedding_column)
            if vecs.len() == 0:
                continue
            mat = vector_matrix(vecs)
            if mat.size == 0:
                continue
            embeddings[gid] = mat.mean(axis=0)

        selected = mmr_select(
            candidate_ids=candidate_ids,
            relevance=relevance,
            embeddings=embeddings,
            k=min(effective_k, len(candidate_ids)),
            lambda_mult=self._mmr_lambda,
        )
        if len(selected) < effective_k:
            selected_set = set(selected)
            selected.extend([gid for gid in candidate_ids if gid not in selected_set])
            selected = selected[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in selected if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "cosine_similarity",
            "mmr_lambda": self._mmr_lambda,
            "mmr_candidates": len(candidate_ids),
            "hits": [
                {"id": gid, "score": float(relevance.get(gid, 0.0))}
                for gid in selected
                if gid in relevance
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class DenseMmrStrategyV2(RetrievalStrategy):
    """Dense bi-encoder retrieval + MMR with pipeline/domain filtering and label rerank."""

    id = "dense-mmr@v2"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 10,
        mmr_lambda: float = 0.65,
        mmr_candidate_limit: int = 200,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._mmr_lambda = float(mmr_lambda)
        self._mmr_candidate_limit = int(mmr_candidate_limit)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }
        self._pipeline_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if any(l.startswith("pipeline:") for l in labels)
        }
        self._elections_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if "domain:elections" in labels
        }

    def _allowed_ids(self, *, is_election_related: bool) -> set[str]:
        allowed = set(self._id_to_labels)
        allowed -= self._pipeline_ids
        if not is_election_related:
            allowed -= self._elections_ids
        return allowed

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation = require_text_by_role(request, role="situation")
        search_text = build_search_text(situation=situation)
        hints = infer_hints(situation=situation)
        allowed_ids = self._allowed_ids(is_election_related=hints.is_election_related)

        query_vec = self._searcher.vector_index.embed_query(search_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df = self._searcher.search_dense(
            query_vector=query_vec, k=raw_k, ids=allowed_ids
        )
        if hits_df.is_empty():
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )
        if "role" in hits_df.columns:
            hits_df = hits_df.filter(pl.col("role") != "labels")

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=raw_k)
        agg = agg.head(int(min(self._mmr_candidate_limit, agg.height)))

        candidate_ids = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
        relevance = {}
        for row in agg.select("id", "score").to_dicts():
            gid = row.get("id")
            if not isinstance(gid, str):
                continue
            base = float(row.get("score") or 0.0)
            bonus = chart_bonus(guideline_labels=self._id_to_labels.get(gid, []), hints=hints)
            relevance[gid] = base + bonus

        embedding_column = self._searcher.vector_index.config.embedding_column
        embed_df = (
            self._searcher.vector_index.embedded_text_df.filter(
                pl.col("id").is_in(candidate_ids)
            )
            .filter(pl.col("role") != "labels")
            .select("id", embedding_column)
        )

        embeddings: dict[str, np.ndarray] = {}
        for gid in candidate_ids:
            vecs = embed_df.filter(pl.col("id") == gid).get_column(embedding_column)
            if vecs.len() == 0:
                continue
            mat = vector_matrix(vecs)
            if mat.size == 0:
                continue
            embeddings[gid] = mat.mean(axis=0)

        selected = mmr_select(
            candidate_ids=candidate_ids,
            relevance=relevance,
            embeddings=embeddings,
            k=min(effective_k, len(candidate_ids)),
            lambda_mult=self._mmr_lambda,
        )
        if len(selected) < effective_k:
            selected_set = set(selected)
            selected.extend([gid for gid in candidate_ids if gid not in selected_set])
            selected = selected[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in selected if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "cosine_similarity_label_rerank",
            "mmr_lambda": self._mmr_lambda,
            "mmr_candidates": len(candidate_ids),
            "filters": {
                "excluded_pipeline": True,
                "excluded_domain_elections": not hints.is_election_related,
            },
            "hints": {
                "is_election_related": hints.is_election_related,
                "chart_labels": sorted(hints.chart_labels),
            },
            "hits": [
                {"id": gid, "score_adj": float(relevance.get(gid, 0.0))}
                for gid in selected
                if gid in relevance
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class DenseMmrStrategyV3(RetrievalStrategy):
    """Dense bi-encoder retrieval + MMR v3 (title-aware hints + task-aware rerank)."""

    id = "dense-mmr@v3"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 10,
        mmr_lambda: float = 0.65,
        mmr_candidate_limit: int = 200,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._mmr_lambda = float(mmr_lambda)
        self._mmr_candidate_limit = int(mmr_candidate_limit)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        title = (get_text_by_role(request, role="title") or "").strip()
        situation = require_text_by_role(request, role="situation")
        hints = infer_hints_v4(title=title, situation=situation)
        search_text = build_search_text_v4(title=title, situation=situation, hints=hints)

        allowed_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if not should_exclude_guideline_v4(guideline_labels=labels, hints=hints)
        }

        query_vec = self._searcher.vector_index.embed_query(search_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df = self._searcher.search_dense(
            query_vector=query_vec, k=raw_k, ids=allowed_ids
        )
        if hits_df.is_empty():
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )
        if "role" in hits_df.columns:
            hits_df = hits_df.filter(pl.col("role") != "labels")

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=raw_k)
        agg = agg.head(int(min(self._mmr_candidate_limit, agg.height)))

        candidate_ids = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
        relevance: dict[str, float] = {}
        for row in agg.select("id", "score").to_dicts():
            gid = row.get("id")
            if not isinstance(gid, str):
                continue
            base = float(row.get("score") or 0.0)
            labels = self._id_to_labels.get(gid, [])
            relevance[gid] = (
                base
                + chart_bonus_v4(guideline_labels=labels, hints=hints)
                + task_bonus_v4(guideline_labels=labels, hints=hints)
                + domain_penalty_v4(guideline_labels=labels, hints=hints)
            )

        embedding_column = self._searcher.vector_index.config.embedding_column
        embed_df = (
            self._searcher.vector_index.embedded_text_df.filter(
                pl.col("id").is_in(candidate_ids)
            )
            .filter(pl.col("role") != "labels")
            .select("id", embedding_column)
        )

        embeddings: dict[str, np.ndarray] = {}
        for gid in candidate_ids:
            vecs = embed_df.filter(pl.col("id") == gid).get_column(embedding_column)
            if vecs.len() == 0:
                continue
            mat = vector_matrix(vecs)
            if mat.size == 0:
                continue
            embeddings[gid] = mat.mean(axis=0)

        selected = mmr_select(
            candidate_ids=candidate_ids,
            relevance=relevance,
            embeddings=embeddings,
            k=min(effective_k, len(candidate_ids)),
            lambda_mult=self._mmr_lambda,
        )
        if len(selected) < effective_k:
            selected_set = set(selected)
            selected.extend([gid for gid in candidate_ids if gid not in selected_set])
            selected = selected[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in selected if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "cosine_similarity_label_rerank_v3",
            "mmr_lambda": self._mmr_lambda,
            "mmr_candidates": len(candidate_ids),
            "filters": {
                "excluded_pipeline": True,
                "hard_excluded_domains": True,
            },
            "hints": {
                "title_used": bool(title),
                "active_domains": sorted(hints.active_domains),
                "chart_labels": sorted(hints.chart_labels),
                "task_labels": sorted(hints.task_labels),
            },
            "hits": [
                {"id": gid, "score_adj": float(relevance.get(gid, 0.0))}
                for gid in selected
                if gid in relevance
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
