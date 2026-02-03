from __future__ import annotations

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import search_hybrid_with_focus
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig
from .searcher import GuidelineSearcher
from .utility_reranker import UtilityReranker, rank_by_utility
from .vision import ChartVisionModule, prepare_chart_vision


class UtilityRerankHybridStrategy(RetrievalStrategy):
    """Hybrid retrieval followed by a task-aligned utility/harm reranker."""

    id = "utility-rerank-hybrid@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        utility_reranker: UtilityReranker,
        vision: ChartVisionModule | None = None,
        default_k: int = 20,
        raw_multiplier: int = 18,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._utility = utility_reranker
        self._vision = vision
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._focus = focus or FocusConfig()

        # Expose the LM to the eval harness so it can snapshot and report
        # per-scenario LM usage deltas (via strategy._lm.history).
        self._lm = self._utility.lm

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

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
        situation_for_rerank = (
            f"{query_text}\n\nChart tokens:\n{vision_tokens_query}"
            if vision_tokens_query
            else query_text
        )
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df, roles_used = search_hybrid_with_focus(
            searcher=self._searcher,
            query_text=query_text,
            query_vector=query_vec,
            k=raw_k,
            reranker=RRFReranker(K=60),
            focus=self._focus,
            focus_mode=focus_mode,
            fts_columns="text",
        )

        module = self._utility.module
        cfg = self._utility.config

        agg = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_df, k=int(cfg.candidate_k)
        )
        rows = agg.to_dicts()
        evidence_by_id: dict[str, object] = {}
        for row in rows:
            gid = row.get("id")
            if isinstance(gid, str) and gid:
                evidence_by_id[gid] = row.get("evidence")

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidates = [
            id_to_entry[row["id"]]
            for row in rows
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]

        scored = rank_by_utility(
            request=request,
            situation_text=situation_for_rerank,
            entries=candidates,
            evidence_by_id=evidence_by_id,
            module=module,
        )
        ordered_entries = [entry for entry, _score in scored[:effective_k]]
        score_by_id: dict[str, dict[str, object]] = {
            entry.id: score for entry, score in scored
        }

        def _coerce_float(raw: object, *, fallback: float = 0.0) -> float:
            if isinstance(raw, (int, float)):
                return float(raw)
            if isinstance(raw, str):
                try:
                    return float(raw)
                except ValueError:
                    return fallback
            return fallback

        hits: list[dict[str, object]] = []
        for entry in ordered_entries:
            score_payload = score_by_id.get(entry.id)
            score = _coerce_float(
                score_payload.get("utility") if score_payload is not None else None,
                fallback=0.0,
            )
            ev = evidence_by_id.get(entry.id)
            hits.append(
                {
                    "id": entry.id,
                    "score": score,
                    "best_role": None,
                    "evidence": ev if isinstance(ev, list) else [],
                    "utility": score_payload,
                }
            )

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "candidate_k": int(cfg.candidate_k),
            "score_kind": "utility_rerank",
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            "utility_reranker": {
                "candidate_k": int(cfg.candidate_k),
                "risk_weight": float(cfg.risk_weight),
                "unclear_penalty": float(cfg.unclear_penalty),
            },
            "hits": hits,
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
