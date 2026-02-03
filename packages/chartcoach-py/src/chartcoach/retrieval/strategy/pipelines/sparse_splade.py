from __future__ import annotations

from chartcoach.catalog import Catalog
from chartcoach.index.sparse import CatalogSparseIndex
from chartcoach.retrieval.operators import apply_status_filter, plan_status_filter
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, primary_roles_for_focus
from .guideline_status import StatusScorer
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, with_chart_vision


class SparseSpladeStrategy(RetrievalStrategy):
    """Neural sparse retrieval baseline (SPLADE-like) over guideline texts."""

    id = "sparse-splade@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        sparse_index: CatalogSparseIndex,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        default_k: int = 20,
        raw_multiplier: int = 18,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._sparse_index: CatalogSparseIndex = sparse_index
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
        if self._vision is not None:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=GuidelineSearcher.build_base_query_text(request),
                vision=self._vision,
            )

        focus_mode = self._focus.mode
        query_text = GuidelineSearcher.build_query_text(request)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))

        status_meta: dict[str, object] = {}
        status_scorer = self._status_scorer
        status_plan = plan_status_filter(
            focus_mode=focus_mode,
            requested_k=effective_k,
            status_scorer=status_scorer,
            status_filter_enabled=self._focus.use_status_filter,
        )
        candidate_k = status_plan.candidate_k

        hits_df = self._sparse_index.search_sparse(query_text, k=raw_k)
        agg = GuidelineSearcher.aggregate_guideline_hits_with_evidence(
            hits_df, k=candidate_k
        )
        candidate_rows = agg.to_dicts()
        hit_by_id = {
            row["id"]: row for row in candidate_rows if isinstance(row.get("id"), str)
        }

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [
            id_to_entry[row["id"]]
            for row in candidate_rows
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
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

        roles = primary_roles_for_focus(focus_mode)
        meta = {
            "sparse_index": self._sparse_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "sparse_relevance",
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles) if roles else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "hits": [
                {
                    "id": entry.id,
                    "score": float(hit_by_id.get(entry.id, {}).get("score") or 0.0),
                    "best_role": hit_by_id.get(entry.id, {}).get("best_role"),
                    "evidence": hit_by_id.get(entry.id, {}).get("evidence") or [],
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
