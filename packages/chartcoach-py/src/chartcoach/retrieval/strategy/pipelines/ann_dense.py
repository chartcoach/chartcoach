from __future__ import annotations

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import (
    apply_status_filter,
    extract_guideline_ranking,
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


class AnnDenseStrategy(RetrievalStrategy):
    """Dense ANN retrieval baseline (no reranking), aggregated to guideline-level."""

    id = "ann-dense@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        default_k: int = 20,
        raw_multiplier: int = 12,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._default_k: int = int(default_k)
        self._raw_multiplier: int = int(raw_multiplier)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

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
        hits_df, roles_used = search_dense_with_focus(
            searcher=self._searcher,
            query_vector=query_vec,
            k=raw_k,
            focus=self._focus,
            focus_mode=focus_mode,
        )

        status_meta: dict[str, object] = {}
        status_scorer = self._status_scorer
        status_plan = plan_status_filter(
            focus_mode=focus_mode,
            requested_k=effective_k,
            status_scorer=status_scorer,
            status_filter_enabled=self._focus.use_status_filter,
        )
        candidate_k = status_plan.candidate_k

        base_agg = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_df, k=candidate_k
        )
        rankings: list[list[str]] = []
        weights: list[float] = []
        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}

        (
            base_ranking,
            base_evidence,
            base_roles,
            base_score_by_id,
        ) = extract_guideline_ranking(base_agg)
        if base_ranking:
            rankings.append(base_ranking)
            weights.append(1.0)
            evidence_by_id.update(base_evidence)
            best_role_by_id.update(base_roles)

        if vision_tokens_query:
            assert self._vision is not None
            vision_vec = self._searcher.vector_index.embed_query(vision_tokens_query)
            vision_hits_df, _vision_roles_used = search_dense_with_focus(
                searcher=self._searcher,
                query_vector=vision_vec,
                k=raw_k,
                focus=self._focus,
                focus_mode=focus_mode,
            )
            vision_agg = self._searcher.aggregate_guideline_hits_with_evidence(
                vision_hits_df, k=candidate_k
            )
            (
                vision_ranking,
                vision_evidence,
                vision_roles,
                _vision_score_by_id,
            ) = extract_guideline_ranking(vision_agg)
            if vision_ranking:
                rankings.append(vision_ranking)
                weights.append(float(self._vision.config.fusion_weight))
                for gid, ev in vision_evidence.items():
                    evidence_by_id.setdefault(gid, []).extend(ev)
                best_role_by_id.update(vision_roles)

        fused_scores: dict[str, float] | None = None
        candidate_ids = base_ranking
        score_kind = "cosine_similarity"
        if len(rankings) > 1:
            fused_scores = rrf_scores(rankings=rankings, k=60, weights=weights)
            candidate_ids = rrf_rank(rankings=rankings, k=60, weights=weights)
            score_kind = "vision_fused_weighted_rrf"

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [id_to_entry[gid] for gid in candidate_ids if gid in id_to_entry][
            :candidate_k
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
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": score_kind,
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "hits": [
                {
                    "id": entry.id,
                    "score": float(
                        (fused_scores or {}).get(entry.id, 0.0)
                        if fused_scores is not None
                        else base_score_by_id.get(entry.id, 0.0)
                    ),
                    "best_role": best_role_by_id.get(entry.id),
                    "evidence": merge_evidence(evidence_by_id.get(entry.id), limit=3),
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
