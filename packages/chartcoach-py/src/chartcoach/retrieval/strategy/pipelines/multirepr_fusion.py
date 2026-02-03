from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import search_hybrid_with_roles_fallback
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, with_chart_vision


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

    @staticmethod
    def _merge_evidence(*sources: object, limit: int = 3) -> list[dict[str, object]]:
        merged: list[dict[str, object]] = []
        for source in sources:
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
        if self._vision is not None:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=self._vision,
            )

        focus_mode = self._focus.mode
        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

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

        for name, searcher, roles, weight in plan:
            hits_df, roles_used = search_hybrid_with_roles_fallback(
                searcher=searcher,
                query_text=query_text,
                query_vector=query_vec,
                k=raw_k,
                reranker=RRFReranker(K=self._config.rrf_k),
                roles=roles,
                fallback_roles=fallback_roles_for_focus(focus_mode),
                allow_role_fallback=self._focus.allow_role_fallback,
                fts_columns="text",
            )

            agg = searcher.aggregate_guideline_hits_with_evidence(
                hits_df, k=candidate_k
            )
            rows = agg.to_dicts()
            ranking: list[str] = []
            for row in rows:
                gid = row.get("id")
                if not isinstance(gid, str) or not gid:
                    continue
                ranking.append(gid)
                ev = row.get("evidence")
                if isinstance(ev, list) and ev:
                    evidence_by_id.setdefault(gid, []).extend(
                        [e for e in ev if isinstance(e, dict)]
                    )
                best_role = row.get("best_role")
                if isinstance(best_role, str) and best_role:
                    best_role_by_id.setdefault(gid, best_role)

            if ranking:
                rankings.append(ranking)
                weights.append(float(weight))
                repr_meta.append(
                    {
                        "name": name,
                        "roles": sorted(roles_used) if roles_used else None,
                        "weight": float(weight),
                        "guidelines": len(ranking),
                    }
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
                    "evidence": self._merge_evidence(
                        evidence_by_id.get(entry.id), limit=3
                    ),
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
