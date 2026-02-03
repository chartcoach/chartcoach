from __future__ import annotations

from typing import cast

from chartcoach.catalog import Catalog
from chartcoach.index.sparse import CatalogSparseIndex
from chartcoach.retrieval.operators import (
    apply_status_filter,
    merge_evidence,
    plan_status_filter,
    search_dense_with_focus,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig
from .guideline_status import StatusScorer
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, prepare_chart_vision


class DenseSparseRrfStrategy(RetrievalStrategy):
    """Dense + neural sparse fusion baseline using Reciprocal Rank Fusion (RRF)."""

    id = "dense-sparse-rrf@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        sparse_index: CatalogSparseIndex,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        default_k: int = 20,
        raw_multiplier: int = 18,
        candidate_multiplier: int = 6,
        rrf_k: int = 60,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._sparse_index: CatalogSparseIndex = sparse_index
        self._default_k: int = int(default_k)
        self._raw_multiplier: int = int(raw_multiplier)
        self._candidate_multiplier: int = int(candidate_multiplier)
        self._rrf_k: int = int(rrf_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

    @staticmethod
    def _merge_evidence(
        primary: object,
        secondary: object,
        *,
        limit: int = 3,
    ) -> list[dict[str, object]]:
        merged: list[dict[str, object]] = []
        for source in (primary, secondary):
            if not isinstance(source, list):
                continue
            for item in source:
                if not isinstance(item, dict):
                    continue
                item_obj = cast("dict[str, object]", item)
                text = str(item_obj.get("text") or "").strip()
                if not text:
                    continue
                merged.append(item_obj)
        merged.sort(key=lambda x: float(x.get("score") or 0.0), reverse=True)
        return merged[: max(0, int(limit))]

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        vision_meta: dict[str, object] = {}
        vision_tokens_query: str | None = None
        if self._vision is not None:
            request, vision_tokens_query, vision_meta = prepare_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=self._vision,
            )

        focus_mode = self._focus.mode
        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))

        hits_dense, roles_used = search_dense_with_focus(
            searcher=self._searcher,
            query_vector=query_vec,
            k=raw_k,
            focus=self._focus,
            focus_mode=focus_mode,
        )

        hits_sparse = self._sparse_index.search_sparse(query_text, k=raw_k)

        status_meta: dict[str, object] = {}
        status_scorer = self._status_scorer
        base_candidate_k = max(effective_k, effective_k * self._candidate_multiplier)
        status_plan = plan_status_filter(
            focus_mode=focus_mode,
            requested_k=effective_k,
            base_candidate_k=base_candidate_k,
            status_scorer=status_scorer,
            status_filter_enabled=self._focus.use_status_filter,
        )
        candidate_k = status_plan.candidate_k

        agg_dense = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_dense, k=candidate_k
        )
        agg_sparse = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_sparse, k=candidate_k
        )

        rows_dense = agg_dense.to_dicts()
        rows_sparse = agg_sparse.to_dicts()
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]
        rank_sparse = [
            gid for gid in agg_sparse["id"].to_list() if isinstance(gid, str)
        ]

        hit_dense_by_id = {
            row["id"]: row for row in rows_dense if isinstance(row.get("id"), str)
        }
        hit_sparse_by_id = {
            row["id"]: row for row in rows_sparse if isinstance(row.get("id"), str)
        }

        rank_base = rrf_rank(rankings=[rank_dense, rank_sparse], k=self._rrf_k)
        fused_scores = rrf_scores(rankings=[rank_dense, rank_sparse], k=self._rrf_k)
        fused_candidates = rank_base[:candidate_k]
        score_kind = "dense_sparse_rrf"

        hit_dense_v_by_id: dict[str, dict[str, object]] = {}
        hit_sparse_v_by_id: dict[str, dict[str, object]] = {}
        if vision_tokens_query:
            vision_vec = self._searcher.vector_index.embed_query(vision_tokens_query)
            vision_dense, _vision_roles_used = search_dense_with_focus(
                searcher=self._searcher,
                query_vector=vision_vec,
                k=raw_k,
                focus=self._focus,
                focus_mode=focus_mode,
            )
            vision_sparse = self._sparse_index.search_sparse(vision_tokens_query, k=raw_k)

            vision_dense_agg = self._searcher.aggregate_guideline_hits_with_evidence(
                vision_dense, k=candidate_k
            )
            vision_sparse_agg = self._searcher.aggregate_guideline_hits_with_evidence(
                vision_sparse, k=candidate_k
            )
            rank_dense_v = [
                gid for gid in vision_dense_agg["id"].to_list() if isinstance(gid, str)
            ]
            rank_sparse_v = [
                gid for gid in vision_sparse_agg["id"].to_list() if isinstance(gid, str)
            ]
            rank_vision = rrf_rank(rankings=[rank_dense_v, rank_sparse_v], k=self._rrf_k)

            for row in vision_dense_agg.to_dicts():
                gid = row.get("id")
                if isinstance(gid, str) and gid:
                    hit_dense_v_by_id[gid] = cast("dict[str, object]", row)
            for row in vision_sparse_agg.to_dicts():
                gid = row.get("id")
                if isinstance(gid, str) and gid:
                    hit_sparse_v_by_id[gid] = cast("dict[str, object]", row)

            fused_scores = rrf_scores(
                rankings=[rank_base, rank_vision],
                k=self._rrf_k,
                weights=[1.0, float(self._vision.config.fusion_weight)],
            )
            fused_candidates = rrf_rank(
                rankings=[rank_base, rank_vision],
                k=self._rrf_k,
                weights=[1.0, float(self._vision.config.fusion_weight)],
            )[:candidate_k]
            score_kind = "vision_fused_weighted_rrf"

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [
            id_to_entry[gid] for gid in fused_candidates if gid in id_to_entry
        ]

        ordered_entries = candidate_entries[:effective_k]
        if status_plan.use_status_filter and ordered_entries:
            assert status_scorer is not None
            ordered_entries, status_meta = apply_status_filter(
                request=request,
                entries=candidate_entries,
                output_k=effective_k,
                focus_mode=focus_mode,
                status_scorer=status_scorer,
            )

        meta = {
            **self._searcher.vector_index.meta(),
            "sparse_index": self._sparse_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "candidate_k": candidate_k,
            "score_kind": score_kind,
            "fusion": {"type": "rrf", "k": self._rrf_k},
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "hits": [
                {
                    "id": entry.id,
                    "score": float(fused_scores.get(entry.id, 0.0)),
                    "best_role": (
                        hit_dense_by_id.get(entry.id, {}).get("best_role")
                        or hit_sparse_by_id.get(entry.id, {}).get("best_role")
                        or hit_dense_v_by_id.get(entry.id, {}).get("best_role")
                        or hit_sparse_v_by_id.get(entry.id, {}).get("best_role")
                    ),
                    "evidence": merge_evidence(
                        self._merge_evidence(
                            hit_dense_by_id.get(entry.id, {}).get("evidence"),
                            hit_sparse_by_id.get(entry.id, {}).get("evidence"),
                            limit=3,
                        ),
                        self._merge_evidence(
                            hit_dense_v_by_id.get(entry.id, {}).get("evidence"),
                            hit_sparse_v_by_id.get(entry.id, {}).get("evidence"),
                            limit=3,
                        ),
                        limit=3,
                    ),
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
