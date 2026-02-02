from __future__ import annotations

import re

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, focus_config_from_env, fallback_roles_for_focus, primary_roles_for_focus
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision


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
        default_k: int = 20,
        raw_multiplier: int = 12,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

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

        roles = primary_roles_for_focus(self._focus.mode)
        roles_used = roles
        query_text = self._searcher.build_query_text(request)
        raw_k = max(10, min(2_000, effective_k * self._raw_multiplier))

        hits_0 = self._searcher.search_fts(query_text=query_text, k=raw_k, roles=roles_used)
        if hits_0.is_empty() and roles is not None and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(self._focus.mode)
            hits_0 = self._searcher.search_fts(
                query_text=query_text, k=raw_k, roles=roles_used
            )
        expanded = _expand_query_from_hits(query_text=query_text, hits_df=hits_0)
        hits_1 = (
            hits_0
            if expanded == query_text
            else self._searcher.search_fts(query_text=expanded, k=raw_k, roles=roles_used)
        )

        hits_df = hits_1
        if not hits_0.is_empty() and not hits_1.is_empty() and expanded != query_text:
            hits_df = (
                pl.concat([hits_0, hits_1], how="vertical")
                .sort("score", descending=True)
                .unique(subset=["id", "role"], keep="first", maintain_order=True)
            )

        focus_mode = self._focus.mode
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
        hit_by_id = {
            row["id"]: row
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
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "bm25",
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
                    "score": float(hit_by_id.get(entry.id, {}).get("score") or 0.0),
                    "best_role": hit_by_id.get(entry.id, {}).get("best_role"),
                    "evidence": hit_by_id.get(entry.id, {}).get("evidence") or [],
                }
                for entry in ordered_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
