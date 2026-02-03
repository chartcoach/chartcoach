from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import (
    extract_guideline_ranking,
    merge_evidence,
    search_hybrid_with_roles_fallback,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, prepare_chart_vision


@dataclass(frozen=True, slots=True)
class MultiReprFusionConfig:
    """Configuration for multi-representation fusion."""

    rrf_k: int = 60
    raw_multiplier: int = 14
    candidate_multiplier: int = 8


class MultiReprFusionStrategy(RetrievalStrategy):
    """Fuse role/representation-specific hybrid rankings via weighted RRF."""

    id = "multirepr-rrf@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        abstract_searcher: GuidelineSearcher,
        vision: ChartVisionModule | None = None,
        config: MultiReprFusionConfig = MultiReprFusionConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._abstract_searcher = abstract_searcher
        self._config = config
        self._default_k = int(default_k)
        self._focus = focus or FocusConfig()
        self._vision = vision

    def _representation_plan(
        self, focus_mode: str
    ) -> list[tuple[str, GuidelineSearcher, set[str] | None, float]]:
        """Return (name, searcher, roles, weight) tuples for this request."""

        plan: list[tuple[str, GuidelineSearcher, set[str] | None, float]] = []

        # Guideline-level abstract channel (title+description+labels).
        plan.append(("abstract", self._abstract_searcher, None, 1.0))

        if focus_mode == "satisfied":
            plan.append(("checks", self._searcher, {"check"}, 1.1))
            plan.append(("reason", self._searcher, {"reason", "context"}, 0.9))
            return plan

        if focus_mode == "violations":
            plan.append(("fixes", self._searcher, {"fix", "mistakes"}, 1.2))
            plan.append(("exceptions", self._searcher, {"exceptions"}, 1.1))
            plan.append(("checks", self._searcher, {"check"}, 0.9))
            return plan

        # Focus=all: include a broad mix of representations.
        plan.append(("fixes", self._searcher, {"fix", "mistakes"}, 1.05))
        plan.append(("exceptions", self._searcher, {"exceptions"}, 1.0))
        plan.append(("checks", self._searcher, {"check"}, 0.95))
        plan.append(("reason", self._searcher, {"reason", "context"}, 0.85))
        return plan

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
        query_vec: np.ndarray = self._searcher.vector_index.embed_query(query_text)
        vision_vec = (
            self._searcher.vector_index.embed_query(vision_tokens_query)
            if vision_tokens_query
            else None
        )

        raw_k = max(20, min(3_000, effective_k * int(self._config.raw_multiplier)))
        candidate_k = max(
            effective_k, effective_k * int(self._config.candidate_multiplier)
        )

        plan = self._representation_plan(focus_mode)

        rankings: list[list[str]] = []
        weights: list[float] = []
        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}
        repr_meta: list[dict[str, object]] = []

        reranker = RRFReranker(K=self._config.rrf_k)

        def _run_channel(
            *,
            channel: str,
            qtext: str,
            qvec: np.ndarray,
            weight_scale: float,
        ) -> None:
            for name, searcher, roles, weight in plan:
                hits_df, roles_used = search_hybrid_with_roles_fallback(
                    searcher=searcher,
                    query_text=qtext,
                    query_vector=qvec,
                    k=raw_k,
                    reranker=reranker,
                    roles=roles,
                    fallback_roles=fallback_roles_for_focus(focus_mode),
                    allow_role_fallback=self._focus.allow_role_fallback,
                    fts_columns="text",
                )
                agg = searcher.aggregate_guideline_hits_with_evidence(
                    hits_df, k=candidate_k
                )
                ranking, ev_by_id, role_by_id, _score_by_id = extract_guideline_ranking(
                    agg
                )
                if not ranking:
                    continue
                rankings.append(ranking)
                weights.append(float(weight) * float(weight_scale))
                for gid, ev in ev_by_id.items():
                    evidence_by_id.setdefault(gid, []).extend(ev)
                best_role_by_id.update(role_by_id)
                repr_meta.append(
                    {
                        "name": name,
                        "channel": channel,
                        "roles": sorted(roles_used) if roles_used else None,
                        "weight": float(weight) * float(weight_scale),
                        "guidelines": len(ranking),
                    }
                )

        _run_channel(channel="intent", qtext=query_text, qvec=query_vec, weight_scale=1.0)
        if vision_tokens_query and vision_vec is not None:
            assert self._vision is not None
            _run_channel(
                channel="vision_tokens",
                qtext=vision_tokens_query,
                qvec=vision_vec,
                weight_scale=float(self._vision.config.fusion_weight),
            )

        fused_scores = rrf_scores(
            rankings=rankings, k=self._config.rrf_k, weights=weights
        )
        fused = rrf_rank(rankings=rankings, k=self._config.rrf_k, weights=weights)

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        fused_candidates = [gid for gid in fused[:candidate_k] if gid in id_to_entry]
        ordered_entries = [id_to_entry[gid] for gid in fused_candidates[:effective_k]]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "candidate_k": candidate_k,
            "score_kind": "multirepr_weighted_rrf",
            "fusion": {
                "type": "weighted_rrf",
                "k": self._config.rrf_k,
                "representations": repr_meta,
            },
            "focus": {
                "mode": focus_mode,
                "roles": sorted(primary_roles_for_focus(focus_mode) or []) or None,
            },
            "chart_vision": vision_meta,
            "hits": [
                {
                    "id": entry.id,
                    "score": float(fused_scores.get(entry.id, 0.0)),
                    "best_role": best_role_by_id.get(entry.id),
                    "evidence": merge_evidence(evidence_by_id.get(entry.id), limit=3),
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
