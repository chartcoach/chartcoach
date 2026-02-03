from __future__ import annotations

import re

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import (
    apply_status_filter,
    extract_guideline_ranking,
    merge_evidence,
    plan_status_filter,
    search_fts_with_focus,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig
from .guideline_status import StatusScorer
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, prepare_chart_vision


_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "has",
    "have",
    "how",
    "in",
    "into",
    "is",
    "it",
    "its",
    "of",
    "on",
    "or",
    "should",
    "that",
    "the",
    "this",
    "to",
    "vs",
    "with",
}


def _tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]{2,}", text.lower()) if t not in _STOPWORDS]


def _expand_query_from_hits(
    *,
    query_text: str,
    hits_df: pl.DataFrame,
    max_terms: int = 8,
    doc_limit: int = 20,
) -> str:
    """Pseudo relevance feedback (PRF) query expansion for BM25/FTS."""

    if hits_df.is_empty() or max_terms <= 0 or "text" not in hits_df.columns:
        return query_text

    original_terms = set(_tokenize(query_text))
    if not original_terms:
        return query_text

    texts = (
        hits_df.select("text")
        .head(int(doc_limit))
        .to_series()
        .cast(pl.String)
        .to_list()
    )

    freqs: dict[str, int] = {}
    for doc in texts:
        for token in _tokenize(str(doc)):
            if token in original_terms:
                continue
            freqs[token] = freqs.get(token, 0) + 1

    if not freqs:
        return query_text

    top = sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))[: int(max_terms)]
    expansion = " ".join(t for t, _n in top)
    return f"{query_text}\n\n{expansion}".strip()


class Bm25PrfStrategy(RetrievalStrategy):
    """Lexical BM25 retrieval (FTS) with PRF query expansion."""

    id = "bm25-prf@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        default_k: int = 20,
        raw_multiplier: int = 12,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._default_k: int = int(default_k)
        self._raw_multiplier: int = int(raw_multiplier)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

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
        query_text = self._searcher.build_query_text(request)
        raw_k = max(10, min(2_000, effective_k * self._raw_multiplier))

        hits_0, roles_used = search_fts_with_focus(
            searcher=self._searcher,
            query_text=query_text,
            k=raw_k,
            focus=self._focus,
            focus_mode=focus_mode,
        )
        expanded = _expand_query_from_hits(query_text=query_text, hits_df=hits_0)
        hits_1 = (
            hits_0
            if expanded == query_text
            else self._searcher.search_fts(
                query_text=expanded, k=raw_k, roles=roles_used
            )
        )

        hits_df = hits_1
        if not hits_0.is_empty() and not hits_1.is_empty() and expanded != query_text:
            hits_df = (
                pl.concat([hits_0, hits_1], how="vertical")
                .sort("score", descending=True)
                .unique(subset=["id", "role"], keep="first", maintain_order=True)
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
            vision_hits_df, _vision_roles_used = search_fts_with_focus(
                searcher=self._searcher,
                query_text=vision_tokens_query,
                k=raw_k,
                focus=self._focus,
                focus_mode=focus_mode,
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
        score_kind = "bm25"
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
            "query_expanded": expanded != query_text,
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
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
