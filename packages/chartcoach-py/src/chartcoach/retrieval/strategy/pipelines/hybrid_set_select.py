from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    focus_config_from_env,
    primary_roles_for_focus,
)
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .ranking import facility_location_select, label_round_robin_select
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision


@dataclass(frozen=True, slots=True)
class SetSelectConfig:
    candidate_multiplier: int = 8
    label_group_prefixes: tuple[str, ...] = ("goal", "topic")
    label_redundancy_gamma: float = 0.15
    facility_alpha: float = 0.4
    facility_beta: float = 0.6
    facility_gamma: float = 0.0


class _HybridSetSelectBase(RetrievalStrategy):
    id = "hybrid-rrf-setselect@base"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        method: str,
        config: SetSelectConfig,
        default_k: int = 20,
        raw_multiplier: int = 12,
        rrf_k: int = 60,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._method = method
        self._config = config
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._rrf_k = int(rrf_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

    def _mean_embeddings(self, ids: list[str]) -> dict[str, np.ndarray]:
        embedding_col = self._searcher.vector_index.config.embedding_column
        df = self._searcher.vector_index.embedded_text_df
        if df.is_empty() or not ids or embedding_col not in df.columns:
            return {}

        subset = df.filter(pl.col("id").is_in(ids)).select("id", embedding_col)
        buckets: dict[str, list[np.ndarray]] = defaultdict(list)
        for row in subset.to_dicts():
            gid = row.get("id")
            vec = row.get(embedding_col)
            if not isinstance(gid, str) or vec is None:
                continue
            buckets[gid].append(np.asarray(vec, dtype=np.float32))

        out: dict[str, np.ndarray] = {}
        for gid, vecs in buckets.items():
            if not vecs:
                continue
            out[gid] = np.mean(np.stack(vecs, axis=0), axis=0)
        return out

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
        use_status_filter = focus_mode != "all" and self._focus.use_status_filter
        candidate_k = max(
            effective_k, effective_k * int(self._config.candidate_multiplier)
        )
        if use_status_filter:
            status_lm, _, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
            candidate_k = max(
                candidate_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        agg = self._searcher.aggregate_guideline_hits_with_evidence(
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

        if use_status_filter and candidate_entries:
            _status_lm, status_module, status_cfg = shared_status_scorer()
            self._status_lm = _status_lm
            candidate_entries, status_meta = filter_guidelines_by_status(
                request=request,
                entries=candidate_entries,
                output_k=min(candidate_k, len(candidate_entries)),
                focus=focus_mode,
                status_module=status_module,
                config=status_cfg,
            )

        candidate_ids = [e.id for e in candidate_entries]
        relevance = {
            gid: float(hit_by_id.get(gid, {}).get("score") or 0.0)
            for gid in candidate_ids
        }

        selected_ids: list[str]
        if self._method == "label_round_robin":
            labels_by_id = {
                entry.id: list(entry.guideline.labels) for entry in candidate_entries
            }
            selected_ids = label_round_robin_select(
                candidate_ids=candidate_ids,
                relevance=relevance,
                labels_by_id=labels_by_id,
                k=effective_k,
                group_prefixes=self._config.label_group_prefixes,
                redundancy_gamma=float(self._config.label_redundancy_gamma),
            )
        elif self._method == "facility_location":
            embeddings = self._mean_embeddings(candidate_ids)
            selected_ids = facility_location_select(
                candidate_ids=candidate_ids,
                relevance=relevance,
                embeddings=embeddings,
                k=effective_k,
                alpha=float(self._config.facility_alpha),
                beta=float(self._config.facility_beta),
                gamma=float(self._config.facility_gamma),
            )
        else:
            raise ValueError(f"Unknown set selection method: {self._method!r}.")

        ordered_entries = [
            id_to_entry[gid] for gid in selected_ids if gid in id_to_entry
        ]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "candidate_k": candidate_k,
            "score_kind": "hybrid_relevance_setselect",
            "reranker": {"type": "rrf", "k": self._rrf_k},
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            "set_select": {
                "method": self._method,
                "candidate_multiplier": self._config.candidate_multiplier,
                "label_group_prefixes": list(self._config.label_group_prefixes),
                "label_redundancy_gamma": self._config.label_redundancy_gamma,
                "facility_alpha": self._config.facility_alpha,
                "facility_beta": self._config.facility_beta,
                "facility_gamma": self._config.facility_gamma,
            },
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


class HybridRrfLabelSetSelectStrategy(_HybridSetSelectBase):
    """Hybrid retrieval + label round-robin set selection baseline."""

    id = "hybrid-rrf-setselect-label@v1"

    def __init__(self, *, catalog: Catalog, searcher: GuidelineSearcher) -> None:
        super().__init__(
            catalog=catalog,
            searcher=searcher,
            method="label_round_robin",
            config=SetSelectConfig(),
        )


class HybridRrfFacilitySetSelectStrategy(_HybridSetSelectBase):
    """Hybrid retrieval + facility-location set selection baseline."""

    id = "hybrid-rrf-setselect-facility@v1"

    def __init__(self, *, catalog: Catalog, searcher: GuidelineSearcher) -> None:
        super().__init__(
            catalog=catalog,
            searcher=searcher,
            method="facility_location",
            config=SetSelectConfig(),
        )
