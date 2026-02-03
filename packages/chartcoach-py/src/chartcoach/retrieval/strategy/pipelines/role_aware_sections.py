from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import (
    apply_status_filter,
    plan_status_filter,
    search_hybrid_with_roles_fallback,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, fallback_roles_for_focus
from .guideline_status import StatusScorer
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, with_chart_vision

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


_ALL_SECTION_ROLES = [
    "advice",
    "check",
    "context",
    "costs",
    "exceptions",
    "fix",
    "mistakes",
    "reason",
]


class RoleRouterSignature(dspy.Signature):
    """Route a request to the most useful guideline section roles."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "It may include optional chart image notes."
        )
    )
    focus: str = dspy.InputField(
        desc="One of: all, violations, satisfied. Use it to choose which roles are most helpful."
    )

    roles: list[str] = dspy.OutputField(
        desc=(
            "A short list of section roles to retrieve from. "
            f"Valid roles: {', '.join(_ALL_SECTION_ROLES)}. "
            "For violations, prefer fix/mistakes/check/exceptions. "
            "For satisfied, prefer check/reason/context. "
            "Keep the list small (1-4)."
        )
    )


@dataclass(frozen=True, slots=True)
class RoleAwareSectionsConfig:
    rrf_k: int = 60
    raw_multiplier: int = 12
    max_roles: int = 4


class RoleAwareSectionsStrategy(RetrievalStrategy):
    """Role-aware retrieval (DSPy role router + role-restricted hybrid search)."""

    id = "role-aware-sections@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        config: RoleAwareSectionsConfig = RoleAwareSectionsConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._lm: dspy.LM = lm
        self._config: RoleAwareSectionsConfig = config
        self._default_k: int = int(default_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

        self._program = dspy.Predict(RoleRouterSignature)

    @staticmethod
    def _clean_roles(raw: object, *, max_roles: int) -> list[str]:
        roles: list[str] = []
        if isinstance(raw, list):
            for item in raw:
                if isinstance(item, str) and item.strip():
                    roles.append(item.strip().lower())
        elif isinstance(raw, str) and raw.strip():
            roles.append(raw.strip().lower())
        roles = [r for r in roles if r in _ALL_SECTION_ROLES]
        seen: set[str] = set()
        deduped: list[str] = []
        for r in roles:
            if r in seen:
                continue
            seen.add(r)
            deduped.append(r)
        return deduped[: max(0, int(max_roles))]

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
        situation = self._searcher.build_query_text(request)

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(situation=situation, focus=focus_mode)
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        routed_roles = self._clean_roles(
            getattr(pred, "roles", None) if pred else None,
            max_roles=self._config.max_roles,
        )
        roles_used = set(routed_roles) if routed_roles else None

        query_vec = self._searcher.vector_index.embed_query(situation)
        raw_k = max(30, min(5_000, effective_k * int(self._config.raw_multiplier)))

        hits_df, roles_used = search_hybrid_with_roles_fallback(
            searcher=self._searcher,
            query_text=situation,
            query_vector=query_vec,
            k=raw_k,
            reranker=RRFReranker(K=self._config.rrf_k),
            roles=roles_used,
            fallback_roles=fallback_roles_for_focus(focus_mode),
            allow_role_fallback=self._focus.allow_role_fallback,
            fts_columns="text",
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

        agg = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_df, k=candidate_k
        )
        candidate_rows = agg.to_dicts()
        row_by_id = {
            str(row.get("id")): row
            for row in candidate_rows
            if isinstance(row.get("id"), str)
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

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "hybrid_relevance",
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "role_router": {
                "roles": routed_roles,
                "lm_attempts": lm_attempts,
                "lm_fallback_used": pred is None,
                "lm_error": lm_error if pred is None else None,
            },
            "hits": [
                {
                    "id": entry.id,
                    "score": float(row_by_id.get(entry.id, {}).get("score") or 0.0),
                    "best_role": row_by_id.get(entry.id, {}).get("best_role"),
                    "evidence": row_by_id.get(entry.id, {}).get("evidence") or [],
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
