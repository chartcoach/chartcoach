from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, fallback_roles_for_focus, focus_config_from_env
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision

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
        config: RoleAwareSectionsConfig = RoleAwareSectionsConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._config = config
        self._default_k = int(default_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

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
        if self._vlm is not None and self._vision_config.enabled:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=ChartVisionModule(vlm=self._vlm, config=self._vision_config),
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
            getattr(pred, "roles", None) if pred else None, max_roles=self._config.max_roles
        )
        roles_used = set(routed_roles) if routed_roles else None

        query_vec = self._searcher.vector_index.embed_query(situation)
        raw_k = max(30, min(5_000, effective_k * int(self._config.raw_multiplier)))

        hits_df = self._searcher.search_hybrid(
            query_text=situation,
            query_vector=query_vec,
            reranker=RRFReranker(K=self._config.rrf_k),
            k=raw_k,
            roles=roles_used,
            fts_columns="text",
        )
        if hits_df.is_empty() and roles_used and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(focus_mode)
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=query_vec,
                reranker=RRFReranker(K=self._config.rrf_k),
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

        agg = self._searcher.aggregate_guideline_hits_with_evidence(hits_df, k=candidate_k)
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
        if focus_mode != "all" and ordered_entries:
            status_lm, status_module, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
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
