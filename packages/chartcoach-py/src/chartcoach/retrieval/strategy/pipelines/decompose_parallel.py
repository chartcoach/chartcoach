from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .guideline_status import StatusScorer, filter_guidelines_by_status
from .label_hints import match_catalog_ids_by_label_hints
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, with_chart_vision

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class DecomposeParallelSignature(dspy.Signature):
    """Decompose a chart+intent into facets for parallel retrieval."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "It may include optional chart image notes. "
            "Decompose into multiple retrieval facets that cover different aspects (audience, task, chart form, risks)."
        )
    )
    focus: str = dspy.InputField(
        desc="One of: all, violations, satisfied. Use it to prioritize facets."
    )
    n: int = dspy.InputField(desc="Number of facets to return.", ge=2, le=10, default=6)

    canonical_query: str = dspy.OutputField(
        desc="A short retrieval query capturing the main chart intent."
    )
    facet_queries: list[str] = dspy.OutputField(
        desc=(
            "A list of short, diverse facet queries (each focusing on one aspect). "
            "Include chart-type / encoding / task / audience / failure-mode facets when relevant."
        )
    )
    label_hints: list[str] = dspy.OutputField(
        desc=(
            "Optional label-like hints (key:value when possible) to prune the guideline catalog upstream."
        )
    )


@dataclass(frozen=True, slots=True)
class DecomposeParallelConfig:
    n_facets: int = 6
    rrf_k: int = 60
    per_query_raw_multiplier: int = 10
    per_query_guideline_k: int = 48


class DecomposeParallelStrategy(RetrievalStrategy):
    """Parallel facet retrieval + fusion (DSPy decomposition + RRF)."""

    id = "decompose-parallel@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        config: DecomposeParallelConfig = DecomposeParallelConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._lm: dspy.LM = lm
        self._config: DecomposeParallelConfig = config
        self._default_k: int = int(default_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

        self._program = dspy.Predict(DecomposeParallelSignature)

    @staticmethod
    def _clean_list(raw: object) -> list[str]:
        out: list[str] = []
        if isinstance(raw, list):
            for item in raw:
                if isinstance(item, str) and item.strip():
                    out.append(item.strip())
        elif isinstance(raw, str) and raw.strip():
            out.append(raw.strip())
        seen: set[str] = set()
        deduped: list[str] = []
        for item in out:
            key = " ".join(item.lower().split())
            if key in seen:
                continue
            seen.add(key)
            deduped.append(item)
        return deduped

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
                    pred = self._program(
                        situation=situation, focus=focus_mode, n=self._config.n_facets
                    )
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        canonical = str(getattr(pred, "canonical_query", "") if pred else "").strip()
        facets = self._clean_list(
            getattr(pred, "facet_queries", None) if pred else None
        )
        label_hints = self._clean_list(
            getattr(pred, "label_hints", None) if pred else None
        )

        if not canonical:
            canonical = situation
        queries = [canonical, *facets]
        queries = self._clean_list(queries)

        candidate_ids, matched_labels_by_hint = match_catalog_ids_by_label_hints(
            catalog=self.catalog,
            label_hints=label_hints,
        )
        ids_filter = candidate_ids or None

        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles
        raw_k = max(
            30, min(5_000, effective_k * int(self._config.per_query_raw_multiplier))
        )
        per_query_k = max(effective_k, int(self._config.per_query_guideline_k))

        rankings: list[list[str]] = []
        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}
        for q in queries:
            qvec = self._searcher.vector_index.embed_query(q)
            hits_df = self._searcher.search_hybrid(
                query_text=q,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                roles=roles_used,
                ids=ids_filter,
                fts_columns="text",
            )
            if (
                hits_df.is_empty()
                and roles is not None
                and self._focus.allow_role_fallback
            ):
                roles_used = fallback_roles_for_focus(focus_mode)
                hits_df = self._searcher.search_hybrid(
                    query_text=q,
                    query_vector=qvec,
                    reranker=RRFReranker(K=self._config.rrf_k),
                    k=raw_k,
                    roles=roles_used,
                    ids=ids_filter,
                    fts_columns="text",
                )
            if hits_df.is_empty() and ids_filter is not None:
                hits_df = self._searcher.search_hybrid(
                    query_text=q,
                    query_vector=qvec,
                    reranker=RRFReranker(K=self._config.rrf_k),
                    k=raw_k,
                    roles=roles_used,
                    ids=None,
                    fts_columns="text",
                )
            agg = self._searcher.aggregate_guideline_hits_with_evidence(
                hits_df, k=per_query_k
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
            rankings.append(ranking)

        fused_scores = rrf_scores(rankings=rankings, k=self._config.rrf_k)
        fused = rrf_rank(rankings=rankings, k=self._config.rrf_k)

        status_meta: dict[str, object] = {}
        status_scorer = self._status_scorer
        use_status_filter = (
            focus_mode != "all"
            and self._focus.use_status_filter
            and status_scorer is not None
        )
        candidate_k = max(effective_k, effective_k)
        if use_status_filter:
            assert status_scorer is not None
            status_cfg = status_scorer.config
            candidate_k = max(
                effective_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        candidate_ids_ranked = fused[:candidate_k]
        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [
            id_to_entry[gid] for gid in candidate_ids_ranked if gid in id_to_entry
        ]
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

        def _top_evidence(gid: str, *, limit: int = 3) -> list[dict[str, object]]:
            items = evidence_by_id.get(gid) or []
            filtered = [
                e
                for e in items
                if isinstance(e, dict) and str(e.get("text") or "").strip()
            ]
            filtered.sort(key=lambda x: float(x.get("score") or 0.0), reverse=True)
            return filtered[: max(0, int(limit))]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "facet_rrf_fusion",
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "decomposition": {
                "canonical_query": canonical,
                "facet_queries": facets,
                "label_hints": label_hints,
                "matched_labels_by_hint": matched_labels_by_hint,
                "candidate_ids": len(candidate_ids),
                "candidate_filter_used": ids_filter is not None,
                "lm_attempts": lm_attempts,
                "lm_fallback_used": pred is None,
                "lm_error": lm_error if pred is None else None,
            },
            "hits": [
                {
                    "id": entry.id,
                    "score": float(fused_scores.get(entry.id, 0.0)),
                    "best_role": best_role_by_id.get(entry.id),
                    "evidence": _top_evidence(entry.id, limit=3),
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
