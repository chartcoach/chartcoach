from __future__ import annotations

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.request_text import require_text_by_role
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .hints import build_search_text, chart_bonus, infer_hints
from .searcher import GuidelineSearcher


class HybridRrfStrategy(RetrievalStrategy):
    """Hybrid lexical+dense retrieval with reciprocal-rank fusion (RRF)."""

    id = "hybrid-rrf@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 12,
        rrf_k: int = 60,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._rrf_k = int(rrf_k)

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df = self._searcher.search_hybrid(
            query_text=query_text,
            query_vector=query_vec,
            reranker=RRFReranker(K=self._rrf_k),
            k=raw_k,
            fts_columns="text",
        )

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
        ranked = agg.select("id", "score", "best_role").to_dicts()

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [
            id_to_entry[row["id"]]
            for row in ranked
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "hybrid_relevance",
            "reranker": {"type": "rrf", "k": self._rrf_k},
            "hits": [
                {
                    "id": row["id"],
                    "score": float(row["score"]),
                    "best_role": row.get("best_role"),
                }
                for row in ranked
                if isinstance(row.get("id"), str)
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class HybridRrfStrategyV2(RetrievalStrategy):
    """Hybrid RRF with pipeline/domain filtering and chart-label reranking."""

    id = "hybrid-rrf@v2"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 12,
        rrf_k: int = 60,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._rrf_k = int(rrf_k)

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
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation = require_text_by_role(request, role="situation")
        query_text = build_search_text(situation=situation)
        hints = infer_hints(situation=situation)
        allowed_ids = self._allowed_ids(is_election_related=hints.is_election_related)

        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df = self._searcher.search_hybrid(
            query_text=query_text,
            query_vector=query_vec,
            reranker=RRFReranker(K=self._rrf_k),
            k=raw_k,
            ids=allowed_ids,
            fts_columns="text",
        )
        if "role" in hits_df.columns:
            hits_df = hits_df.filter(pl.col("role") != "labels")

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=max(effective_k, 50))
        ranked = agg.select("id", "score", "best_role").to_dicts()

        rescored: list[dict[str, object]] = []
        for row in ranked:
            gid = row.get("id")
            if not isinstance(gid, str):
                continue
            labels = self._id_to_labels.get(gid, [])
            score = float(row.get("score") or 0.0)
            rescored.append(
                {
                    **row,
                    "score": score,
                    "score_adj": score + chart_bonus(guideline_labels=labels, hints=hints),
                }
            )
        rescored.sort(
            key=lambda r: (-float(r.get("score_adj") or 0.0), str(r.get("id") or ""))
        )
        rescored = rescored[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [
            id_to_entry[row["id"]]
            for row in rescored
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "hybrid_relevance_label_rerank",
            "reranker": {"type": "rrf", "k": self._rrf_k},
            "filters": {
                "excluded_pipeline": True,
                "excluded_domain_elections": not hints.is_election_related,
            },
            "hints": {
                "is_election_related": hints.is_election_related,
                "chart_labels": sorted(hints.chart_labels),
            },
            "hits": [
                {
                    "id": row["id"],
                    "score": float(row["score"]),
                    "score_adj": float(row["score_adj"]),
                    "best_role": row.get("best_role"),
                }
                for row in rescored
                if isinstance(row.get("id"), str)
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
