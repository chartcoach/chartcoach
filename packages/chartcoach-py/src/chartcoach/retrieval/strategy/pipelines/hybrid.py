from __future__ import annotations

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, focus_config_from_env, fallback_roles_for_focus, primary_roles_for_focus
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision


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
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._rrf_k = int(rrf_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        vision_meta: dict[str, object] = {}
        if self._vlm is not None and self._vision_config.enabled:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=ChartVisionModule(vlm=self._vlm, config=self._vision_config),
            )

        focus_mode = self._focus.mode
        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles
        hits_df = self._searcher.search_hybrid(
            query_text=query_text,
            query_vector=query_vec,
            reranker=RRFReranker(K=self._rrf_k),
            k=raw_k,
            roles=roles_used,
            fts_columns="text",
        )
        if hits_df.is_empty() and roles is not None and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(focus_mode)
            hits_df = self._searcher.search_hybrid(
                query_text=query_text,
                query_vector=query_vec,
                reranker=RRFReranker(K=self._rrf_k),
                k=raw_k,
                roles=roles_used,
                fts_columns="text",
            )

        status_meta: dict[str, object] = {}
        candidate_k = effective_k
        if focus_mode != "all":
            status_lm, _, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
            candidate_k = max(
                effective_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=candidate_k)
        candidate_rows = agg.select("id", "score", "best_role").to_dicts()

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [
            id_to_entry[row["id"]]
            for row in candidate_rows
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]
        ordered_entries = candidate_entries[:effective_k]
        if focus_mode != "all" and ordered_entries:
            _status_lm, status_module, status_cfg = shared_status_scorer()
            self._status_lm = _status_lm
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
            "score_kind": "hybrid_relevance",
            "reranker": {"type": "rrf", "k": self._rrf_k},
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "hits": [
                {
                    "id": row["id"],
                    "score": float(row["score"]),
                    "best_role": row.get("best_role"),
                }
                for row in candidate_rows[:effective_k]
                if isinstance(row.get("id"), str)
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
