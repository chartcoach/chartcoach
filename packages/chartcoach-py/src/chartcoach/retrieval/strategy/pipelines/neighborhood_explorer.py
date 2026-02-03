from __future__ import annotations

from dataclasses import dataclass
from typing import cast

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .guideline_status import StatusScorer, filter_guidelines_by_status
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, with_chart_vision


def _section_text(entry, role: str) -> str:  # noqa: ANN001
    for section in entry.guideline.sections:
        if section.role == role and section.content.strip():
            return section.content.strip()
    return ""


def _seed_role_for_focus(entry, focus: str) -> str:  # noqa: ANN001
    if focus == "violations":
        for role in ("fix", "mistakes", "exceptions", "check", "advice"):
            if _section_text(entry, role):
                return role
        return "advice"
    if focus == "satisfied":
        for role in ("check", "reason", "context", "advice"):
            if _section_text(entry, role):
                return role
        return "check"
    return "advice"


@dataclass(frozen=True, slots=True)
class NeighborhoodExplorerConfig:
    anchor_k: int = 6
    neighbor_k: int = 24
    diverge_k: int = 8
    rrf_k: int = 60
    raw_multiplier: int = 12


class NeighborhoodExplorerStrategy(RetrievalStrategy):
    """Neighborhood exploration over section embeddings (anchors + similar/contrasting neighbors)."""

    id = "neighborhood-explorer@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        config: NeighborhoodExplorerConfig = NeighborhoodExplorerConfig(),
        default_k: int = 20,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._config: NeighborhoodExplorerConfig = config
        self._default_k: int = int(default_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

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
        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles

        situation = self._searcher.build_query_text(request)
        qvec = self._searcher.vector_index.embed_query(situation)

        raw_k = max(30, min(5_000, effective_k * int(self._config.raw_multiplier)))
        hits_df = self._searcher.search_hybrid(
            query_text=situation,
            query_vector=qvec,
            reranker=RRFReranker(K=self._config.rrf_k),
            k=raw_k,
            roles=roles_used,
            fts_columns="text",
        )
        if hits_df.is_empty() and roles is not None and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(focus_mode)
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                roles=roles_used,
                fts_columns="text",
            )

        anchor_k = max(1, min(int(self._config.anchor_k), effective_k))
        anchors_df = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_df, k=anchor_k
        )
        anchor_rows = anchors_df.to_dicts()
        anchor_ids = [gid for gid in anchors_df["id"].to_list() if isinstance(gid, str)]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        anchors = [id_to_entry[gid] for gid in anchor_ids if gid in id_to_entry]

        rankings: list[list[str]] = [anchor_ids]
        similar_ids: list[str] = []
        exception_ids: list[str] = []
        divergent_ids: list[str] = []

        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}

        def _add_rows(rows: list[dict[str, object]]) -> None:
            for row in rows:
                gid = row.get("id")
                if not isinstance(gid, str) or not gid:
                    continue
                ev = row.get("evidence")
                if isinstance(ev, list) and ev:
                    evidence_by_id.setdefault(gid, []).extend(
                        [
                            cast("dict[str, object]", e)
                            for e in ev
                            if isinstance(e, dict)
                        ]
                    )
                best_role = row.get("best_role")
                if isinstance(best_role, str) and best_role:
                    best_role_by_id.setdefault(gid, best_role)

        _add_rows(anchor_rows)

        for anchor in anchors:
            seed_role = _seed_role_for_focus(anchor, focus_mode)
            seed_text = _section_text(anchor, seed_role) or anchor.guideline.description
            seed_vec = self._searcher.vector_index.embed_query(seed_text)

            neigh_df = self._searcher.search_dense(
                query_vector=seed_vec,
                k=max(10, int(self._config.neighbor_k)),
                roles={seed_role},
            ).filter(pl.col("id") != anchor.id)
            neigh_agg = self._searcher.aggregate_guideline_hits_with_evidence(
                neigh_df, k=max(1, int(self._config.neighbor_k))
            )
            _add_rows(neigh_agg.to_dicts())
            neigh_ids = [
                gid for gid in neigh_agg["id"].to_list() if isinstance(gid, str)
            ]
            if neigh_ids:
                rankings.append(neigh_ids)
                similar_ids.extend(neigh_ids)

            context_text = _section_text(anchor, "context")
            advice_text = _section_text(anchor, "advice")
            if not context_text or not advice_text:
                continue

            ctx_vec = self._searcher.vector_index.embed_query(context_text)
            ctx_df = self._searcher.search_dense(
                query_vector=ctx_vec,
                k=max(20, int(self._config.neighbor_k)),
                roles={"context"},
            ).filter(pl.col("id") != anchor.id)
            ctx_agg = self._searcher.aggregate_guideline_hits_with_evidence(
                ctx_df, k=max(1, int(self._config.neighbor_k))
            )
            _add_rows(ctx_agg.to_dicts())
            ctx_scores = {
                str(row["id"]): float(row["score"])
                for row in ctx_agg.select("id", "score").to_dicts()
                if isinstance(row.get("id"), str)
            }

            advice_vec = self._searcher.vector_index.embed_query(advice_text)
            scored: list[tuple[str, float]] = []
            for gid, ctx_score in ctx_scores.items():
                entry = id_to_entry.get(gid)
                if entry is None:
                    continue
                cand_advice = _section_text(entry, "advice")
                if not cand_advice:
                    continue
                cand_vec = self._searcher.vector_index.embed_query(cand_advice)
                adv_sim = float(np.dot(advice_vec, cand_vec))
                scored.append((gid, ctx_score - adv_sim))

            scored.sort(key=lambda t: t[1], reverse=True)
            top_div = [gid for gid, _s in scored[: int(self._config.diverge_k)]]
            if top_div:
                rankings.append(top_div)
                divergent_ids.extend(top_div)

            exc_df = self._searcher.search_dense(
                query_vector=ctx_vec,
                k=max(20, int(self._config.neighbor_k)),
                roles={"exceptions"},
            ).filter(pl.col("id") != anchor.id)
            exc_agg = self._searcher.aggregate_guideline_hits_with_evidence(
                exc_df, k=max(1, int(self._config.neighbor_k))
            )
            _add_rows(exc_agg.to_dicts())
            exc_ids = [gid for gid in exc_agg["id"].to_list() if isinstance(gid, str)]
            if exc_ids:
                rankings.append(exc_ids)
                exception_ids.extend(exc_ids)

        fused_scores = rrf_scores(rankings=rankings, k=self._config.rrf_k)
        fused = rrf_rank(rankings=rankings, k=self._config.rrf_k)

        status_meta: dict[str, object] = {}
        candidate_k = effective_k
        status_scorer = self._status_scorer
        use_status_filter = (
            focus_mode != "all"
            and self._focus.use_status_filter
            and status_scorer is not None
        )
        if use_status_filter:
            assert status_scorer is not None
            status_cfg = status_scorer.config
            candidate_k = max(
                effective_k, effective_k * int(status_cfg.candidate_multiplier)
            )

        candidate_ids = fused[:candidate_k]
        candidate_entries = [
            id_to_entry[gid] for gid in candidate_ids if gid in id_to_entry
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
            "score_kind": "neighborhood_rrf_fusion",
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "exploration": {
                "anchor_ids": anchor_ids,
                "similar_ids": len(set(similar_ids)),
                "divergent_ids": len(set(divergent_ids)),
                "exception_ids": len(set(exception_ids)),
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
