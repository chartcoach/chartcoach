from __future__ import annotations

from typing import cast

from chartcoach.catalog import Catalog
from chartcoach.index.sparse import CatalogSparseIndex
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
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision


class DenseSparseRrfStrategy(RetrievalStrategy):
    """Dense + neural sparse fusion baseline using Reciprocal Rank Fusion (RRF)."""

    id = "dense-sparse-rrf@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        sparse_index: CatalogSparseIndex,
        default_k: int = 20,
        raw_multiplier: int = 18,
        candidate_multiplier: int = 6,
        rrf_k: int = 60,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._sparse_index = sparse_index
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._candidate_multiplier = int(candidate_multiplier)
        self._rrf_k = int(rrf_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

    @staticmethod
    def _merge_evidence(
        primary: object,
        secondary: object,
        *,
        limit: int = 3,
    ) -> list[dict[str, object]]:
        merged: list[dict[str, object]] = []
        for source in (primary, secondary):
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

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
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
        hits_dense = self._searcher.search_dense(
            query_vector=query_vec, k=raw_k, roles=roles_used
        )
        if (
            hits_dense.is_empty()
            and roles is not None
            and self._focus.allow_role_fallback
        ):
            roles_used = fallback_roles_for_focus(focus_mode)
            hits_dense = self._searcher.search_dense(
                query_vector=query_vec, k=raw_k, roles=roles_used
            )

        hits_sparse = self._sparse_index.search_sparse(query_text, k=raw_k)

        status_meta: dict[str, object] = {}
        use_status_filter = focus_mode != "all" and self._focus.use_status_filter
        candidate_k = max(effective_k, effective_k * self._candidate_multiplier)
        if use_status_filter:
            status_lm, _, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
            candidate_k = max(
                candidate_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        agg_dense = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_dense, k=candidate_k
        )
        agg_sparse = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_sparse, k=candidate_k
        )

        rows_dense = agg_dense.to_dicts()
        rows_sparse = agg_sparse.to_dicts()
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]
        rank_sparse = [
            gid for gid in agg_sparse["id"].to_list() if isinstance(gid, str)
        ]

        hit_dense_by_id = {
            row["id"]: row for row in rows_dense if isinstance(row.get("id"), str)
        }
        hit_sparse_by_id = {
            row["id"]: row for row in rows_sparse if isinstance(row.get("id"), str)
        }

        fused_scores = rrf_scores(rankings=[rank_dense, rank_sparse], k=self._rrf_k)
        fused = rrf_rank(rankings=[rank_dense, rank_sparse], k=self._rrf_k)
        fused_candidates = fused[:candidate_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        candidate_entries = [
            id_to_entry[gid] for gid in fused_candidates if gid in id_to_entry
        ]

        ordered_entries = candidate_entries[:effective_k]
        if use_status_filter and ordered_entries:
            _status_lm, status_module, status_cfg = shared_status_scorer()
            self._status_lm = _status_lm
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
            "sparse_index": self._sparse_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "candidate_k": candidate_k,
            "score_kind": "dense_sparse_rrf",
            "fusion": {"type": "rrf", "k": self._rrf_k},
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "hits": [
                {
                    "id": entry.id,
                    "score": float(fused_scores.get(entry.id, 0.0)),
                    "best_role": (
                        hit_dense_by_id.get(entry.id, {}).get("best_role")
                        or hit_sparse_by_id.get(entry.id, {}).get("best_role")
                    ),
                    "evidence": self._merge_evidence(
                        hit_dense_by_id.get(entry.id, {}).get("evidence"),
                        hit_sparse_by_id.get(entry.id, {}).get("evidence"),
                        limit=3,
                    ),
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
