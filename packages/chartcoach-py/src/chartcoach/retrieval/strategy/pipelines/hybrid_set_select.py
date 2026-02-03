from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import (
    apply_status_filter,
    extract_guideline_ranking,
    merge_evidence,
    plan_status_filter,
    search_hybrid_with_focus,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig
from .guideline_status import StatusScorer
from .ranking import (
    facility_location_select,
    label_round_robin_select,
    rrf_rank,
    rrf_scores,
)
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, prepare_chart_vision


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
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        default_k: int = 20,
        raw_multiplier: int = 12,
        rrf_k: int = 60,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._method: str = method
        self._config: SetSelectConfig = config
        self._default_k: int = int(default_k)
        self._raw_multiplier: int = int(raw_multiplier)
        self._rrf_k: int = int(rrf_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

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
        vision_tokens_query: str | None = None
        if self._vision is not None:
            request, vision_tokens_query, vision_meta = prepare_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=self._vision,
            )

        focus_mode = self._focus.mode
        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df, roles_used = search_hybrid_with_focus(
            searcher=self._searcher,
            query_text=query_text,
            query_vector=query_vec,
            k=raw_k,
            reranker=RRFReranker(K=self._rrf_k),
            focus=self._focus,
            focus_mode=focus_mode,
            fts_columns="text",
        )

        status_meta: dict[str, object] = {}
        status_scorer = self._status_scorer
        base_candidate_k = max(
            effective_k, effective_k * int(self._config.candidate_multiplier)
        )
        status_plan = plan_status_filter(
            focus_mode=focus_mode,
            requested_k=effective_k,
            base_candidate_k=base_candidate_k,
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

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        if vision_tokens_query:
            assert self._vision is not None
            vision_vec = self._searcher.vector_index.embed_query(vision_tokens_query)
            vision_hits_df, _vision_roles_used = search_hybrid_with_focus(
                searcher=self._searcher,
                query_text=vision_tokens_query,
                query_vector=vision_vec,
                k=raw_k,
                reranker=RRFReranker(K=self._rrf_k),
                focus=self._focus,
                focus_mode=focus_mode,
                fts_columns="text",
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
        relevance = dict(base_score_by_id)
        score_kind = "hybrid_relevance_setselect"
        if len(rankings) > 1:
            fused_scores = rrf_scores(rankings=rankings, k=60, weights=weights)
            candidate_ids = rrf_rank(rankings=rankings, k=60, weights=weights)
            relevance = fused_scores
            score_kind = "vision_fused_weighted_rrf_setselect"

        candidate_entries = [id_to_entry[gid] for gid in candidate_ids if gid in id_to_entry][
            :candidate_k
        ]

        if status_plan.use_status_filter and candidate_entries:
            assert status_scorer is not None
            candidate_entries, status_meta = apply_status_filter(
                request=request,
                entries=candidate_entries,
                output_k=min(candidate_k, len(candidate_entries)),
                focus_mode=focus_mode,
                status_scorer=status_scorer,
            )

        candidate_ids = [e.id for e in candidate_entries]
        relevance = {gid: float(relevance.get(gid, 0.0)) for gid in candidate_ids}

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
            "score_kind": score_kind,
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


class HybridRrfLabelSetSelectStrategy(_HybridSetSelectBase):
    """Hybrid retrieval + label round-robin set selection baseline."""

    id = "hybrid-rrf-setselect-label@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        focus: FocusConfig | None = None,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
    ) -> None:
        super().__init__(
            catalog=catalog,
            searcher=searcher,
            method="label_round_robin",
            config=SetSelectConfig(),
            focus=focus,
            vision=vision,
            status_scorer=status_scorer,
        )


class HybridRrfFacilitySetSelectStrategy(_HybridSetSelectBase):
    """Hybrid retrieval + facility-location set selection baseline."""

    id = "hybrid-rrf-setselect-facility@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        focus: FocusConfig | None = None,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
    ) -> None:
        super().__init__(
            catalog=catalog,
            searcher=searcher,
            method="facility_location",
            config=SetSelectConfig(),
            focus=focus,
            vision=vision,
            status_scorer=status_scorer,
        )
