from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, focus_config_from_env
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .label_hints import (
    LabelHintsConfig,
    LabelHintsSignature,
    match_catalog_ids_by_label_hints,
)
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


@dataclass(frozen=True, slots=True)
class LabelFirstAbstractConfig:
    labels: LabelHintsConfig = LabelHintsConfig()
    raw_multiplier: int = 16


class LabelFirstAbstractStrategy(RetrievalStrategy):
    """Label-first retrieval over per-guideline abstracts (DSPy label hints + abstract index)."""

    id = "label-first-abstract@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        abstract_searcher: GuidelineSearcher,
        lm: dspy.LM,
        config: LabelFirstAbstractConfig = LabelFirstAbstractConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._abstract_searcher = abstract_searcher
        self._lm = lm
        self._config = config
        self._default_k = int(default_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

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
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        vision_meta: dict[str, object] = {}
        if self._vlm is not None and self._vision_config.enabled:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._abstract_searcher.build_base_query_text(request),
                vision=ChartVisionModule(vlm=self._vlm, config=self._vision_config),
            )

        focus_mode = self._focus.mode
        situation = self._abstract_searcher.build_query_text(request)

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(
                        situation=situation, focus=focus_mode, n=self._config.labels.n
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

        query_vec = self._abstract_searcher.vector_index.embed_query(canonical_query)
        raw_k = max(30, min(5_000, effective_k * int(self._config.raw_multiplier)))

        hits_df = self._abstract_searcher.search_hybrid(
            query_text=canonical_query,
            query_vector=query_vec,
            reranker=RRFReranker(),
            k=raw_k,
            ids=ids_filter,
            fts_columns="text",
        )
        if hits_df.is_empty() and ids_filter is not None:
            hits_df = self._abstract_searcher.search_hybrid(
                query_text=canonical_query,
                query_vector=query_vec,
                reranker=RRFReranker(),
                k=raw_k,
                ids=None,
                fts_columns="text",
            )

        status_meta: dict[str, object] = {}
        use_status_filter = focus_mode != "all" and self._focus.use_status_filter
        candidate_k = effective_k
        if use_status_filter:
            status_lm, _, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
            candidate_k = max(
                effective_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        agg = self._abstract_searcher.aggregate_guideline_hits_with_evidence(
            hits_df, k=candidate_k
        )
        candidate_rows = agg.to_dicts()

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [
            id_to_entry[row["id"]]
            for row in candidate_rows
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]
        ordered_entries = candidate_entries[:effective_k]
        if use_status_filter and ordered_entries:
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

        row_by_id = {
            str(row.get("id")): row
            for row in candidate_rows
            if isinstance(row.get("id"), str)
        }
        meta = {
            **self._abstract_searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "hybrid_relevance",
            "focus": {"mode": focus_mode, "roles": None},
            "chart_vision": vision_meta,
            **status_meta,
            "label_plan": {
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
                    "score": float(row_by_id.get(entry.id, {}).get("score") or 0.0),
                    "best_role": row_by_id.get(entry.id, {}).get("best_role"),
                    "evidence": row_by_id.get(entry.id, {}).get("evidence") or [],
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
