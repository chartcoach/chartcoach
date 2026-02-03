from __future__ import annotations

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.embedding.vectors import vector_matrix
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .guideline_status import StatusScorer, filter_guidelines_by_status
from .ranking import mmr_select
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, with_chart_vision


class DenseMmrStrategy(RetrievalStrategy):
    """Dense bi-encoder retrieval with guideline-level aggregation + MMR."""

    id = "dense-mmr@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        default_k: int = 20,
        raw_multiplier: int = 10,
        mmr_lambda: float = 0.65,
        mmr_candidate_limit: int = 200,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._default_k: int = int(default_k)
        self._raw_multiplier: int = int(raw_multiplier)
        self._mmr_lambda: float = float(mmr_lambda)
        self._mmr_candidate_limit: int = int(mmr_candidate_limit)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        vision_meta: dict[str, object] = {}
        if self._vision is not None:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=self._vision,
            )

        focus_mode = self._focus.mode
        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles
        hits_df = self._searcher.search_dense(
            query_vector=query_vec, k=raw_k, roles=roles_used
        )
        if hits_df.is_empty() and roles is not None and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(focus_mode)
            hits_df = self._searcher.search_dense(
                query_vector=query_vec, k=raw_k, roles=roles_used
            )
        if hits_df.is_empty():
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "focus": {
                        "mode": focus_mode,
                        "roles": sorted(roles_used) if roles_used else None,
                    },
                    "chart_vision": vision_meta,
                    "hits": [],
                },
            )

        agg = self._searcher.aggregate_guideline_hits_with_evidence(hits_df, k=raw_k)
        agg = agg.head(int(min(self._mmr_candidate_limit, agg.height)))

        candidate_ids = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
        hit_by_id = {
            row["id"]: row for row in agg.to_dicts() if isinstance(row.get("id"), str)
        }
        relevance = {
            gid: float(hit_by_id.get(gid, {}).get("score") or 0.0)
            for gid in candidate_ids
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

        status_meta: dict[str, object] = {}
        status_scorer = self._status_scorer
        use_status_filter = (
            focus_mode != "all"
            and self._focus.use_status_filter
            and status_scorer is not None
        )
        output_candidates = effective_k
        if use_status_filter:
            assert status_scorer is not None
            status_cfg = status_scorer.config
            output_candidates = max(
                effective_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        selected = mmr_select(
            candidate_ids=candidate_ids,
            relevance=relevance,
            embeddings=embeddings,
            k=min(output_candidates, len(candidate_ids)),
            lambda_mult=self._mmr_lambda,
        )
        if len(selected) < output_candidates:
            selected_set = set(selected)
            selected.extend([gid for gid in candidate_ids if gid not in selected_set])
            selected = selected[:output_candidates]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [id_to_entry[gid] for gid in selected if gid in id_to_entry]
        ordered_entries = candidate_entries[:effective_k]
        if use_status_filter and ordered_entries:
            assert status_scorer is not None
            status_module = status_scorer.module
            status_cfg = status_scorer.config
            ordered_entries, status_meta = filter_guidelines_by_status(
                request=request,
                entries=candidate_entries,
                output_k=effective_k,
                focus=focus_mode,
                status_module=status_module,
                config=status_cfg,
            )

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "cosine_similarity",
            "mmr_lambda": self._mmr_lambda,
            "mmr_candidates": len(candidate_ids),
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "hits": [
                {
                    "id": entry.id,
                    "score": float(relevance.get(entry.id, 0.0)),
                    "best_role": hit_by_id.get(entry.id, {}).get("best_role"),
                    "evidence": hit_by_id.get(entry.id, {}).get("evidence") or [],
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
