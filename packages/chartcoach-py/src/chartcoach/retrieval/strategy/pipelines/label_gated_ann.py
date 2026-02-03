from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import (
    apply_status_filter,
    extract_guideline_ranking,
    merge_evidence,
    plan_status_filter,
    search_dense_with_focus,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig
from .guideline_status import StatusScorer
from .label_hints import (
    LabelHintsConfig,
    LabelHintsSignature,
    match_catalog_ids_by_label_hints,
)
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, prepare_chart_vision

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


@dataclass(frozen=True, slots=True)
class LabelGatedAnnConfig:
    labels: LabelHintsConfig = LabelHintsConfig()
    raw_multiplier: int = 12


class LabelGatedAnnStrategy(RetrievalStrategy):
    """Label-gated dense ANN retrieval (DSPy label hints + ANN rerank)."""

    id = "label-gated-ann@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        config: LabelGatedAnnConfig = LabelGatedAnnConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._lm: dspy.LM = lm
        self._config: LabelGatedAnnConfig = config
        self._default_k: int = int(default_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

        self._program = dspy.Predict(LabelHintsSignature)

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
        situation = self._searcher.build_query_text(request)
        situation_for_lm = (
            f"{situation}\n\nChart tokens:\n{vision_tokens_query}"
            if vision_tokens_query
            else situation
        )

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(
                        situation=situation_for_lm,
                        focus=focus_mode,
                        n=self._config.labels.n,
                    )
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        canonical_query = str(
            getattr(pred, "canonical_query", "") if pred else ""
        ).strip()
        label_hints = self._clean_list(
            getattr(pred, "label_hints", None) if pred else None
        )
        if not canonical_query:
            canonical_query = situation

        candidate_ids, matched_labels_by_hint = match_catalog_ids_by_label_hints(
            catalog=self.catalog,
            label_hints=label_hints,
        )
        ids_filter = candidate_ids or None

        query_vec = self._searcher.vector_index.embed_query(canonical_query)
        raw_k = max(20, min(3_000, effective_k * int(self._config.raw_multiplier)))

        hits_df, roles_used = search_dense_with_focus(
            searcher=self._searcher,
            query_vector=query_vec,
            k=raw_k,
            ids=ids_filter,
            focus=self._focus,
            focus_mode=focus_mode,
        )
        if hits_df.is_empty() and ids_filter is not None:
            # If gating becomes too strict, fall back to the full catalog.
            hits_df = self._searcher.search_dense(
                query_vector=query_vec,
                k=raw_k,
                roles=roles_used,
                ids=None,
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
        (
            base_ranking,
            base_evidence,
            base_roles,
            base_score_by_id,
        ) = extract_guideline_ranking(base_agg)

        rankings: list[list[str]] = []
        weights: list[float] = []
        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}

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
                ids=ids_filter,
                focus=self._focus,
                focus_mode=focus_mode,
            )
            if vision_hits_df.is_empty() and ids_filter is not None:
                vision_hits_df = self._searcher.search_dense(
                    query_vector=vision_vec,
                    k=raw_k,
                    roles=roles_used,
                    ids=None,
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
            "label_gating": {
                "label_hints": label_hints,
                "matched_labels_by_hint": matched_labels_by_hint,
                "candidate_ids": len(candidate_ids),
                "candidate_filter_used": ids_filter is not None,
                "canonical_query": canonical_query,
                "lm_attempts": lm_attempts,
                "lm_fallback_used": pred is None,
                "lm_error": lm_error if pred is None else None,
            },
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
