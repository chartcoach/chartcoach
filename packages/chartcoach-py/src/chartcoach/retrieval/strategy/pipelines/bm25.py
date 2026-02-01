from __future__ import annotations

import re

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.request_text import require_text_by_role
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .searcher import GuidelineSearcher
from .hints import build_search_text, chart_bonus, infer_hints


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
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        query_text = self._searcher.build_query_text(request)
        raw_k = max(10, min(2_000, effective_k * self._raw_multiplier))

        hits_0 = self._searcher.search_fts(query_text=query_text, k=raw_k)
        expanded = _expand_query_from_hits(query_text=query_text, hits_df=hits_0)
        hits_1 = (
            hits_0
            if expanded == query_text
            else self._searcher.search_fts(query_text=expanded, k=raw_k)
        )

        hits_df = hits_1
        if not hits_0.is_empty() and not hits_1.is_empty() and expanded != query_text:
            hits_df = (
                pl.concat([hits_0, hits_1], how="vertical")
                .group_by("id", "role")
                .agg(pl.max("score").alias("score"))
                .sort("score", descending=True)
            )

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
        ranked_ids = agg.select("id", "score", "best_role").to_dicts()

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [
            id_to_entry[row["id"]]
            for row in ranked_ids
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "bm25",
            "query_expanded": expanded != query_text,
            "hits": [
                {
                    "id": row["id"],
                    "score": float(row["score"]),
                    "best_role": row.get("best_role"),
                }
                for row in ranked_ids
                if isinstance(row.get("id"), str)
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class Bm25PrfStrategyV2(RetrievalStrategy):
    """BM25/FTS + PRF with pipeline/domain filtering and chart-label reranking."""

    id = "bm25-prf@v2"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 12,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }
        self._pipeline_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if any(l.startswith("pipeline:") for l in labels)
        }
        self._elections_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if "domain:elections" in labels
        }

    def _allowed_ids(self, *, is_election_related: bool) -> set[str]:
        allowed = set(self._id_to_labels)
        allowed -= self._pipeline_ids
        if not is_election_related:
            allowed -= self._elections_ids
        return allowed

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation = require_text_by_role(request, role="situation")
        search_text = build_search_text(situation=situation)
        hints = infer_hints(situation=situation)

        allowed_ids = self._allowed_ids(is_election_related=hints.is_election_related)
        raw_k = max(10, min(2_000, effective_k * self._raw_multiplier))

        hits_0 = self._searcher.search_fts(
            query_text=search_text,
            k=raw_k,
            ids=allowed_ids,
        )
        expanded = _expand_query_from_hits(query_text=search_text, hits_df=hits_0)
        hits_1 = (
            hits_0
            if expanded == search_text
            else self._searcher.search_fts(
                query_text=expanded,
                k=raw_k,
                ids=allowed_ids,
            )
        )

        hits_df = hits_1
        if not hits_0.is_empty() and not hits_1.is_empty() and expanded != search_text:
            hits_df = (
                pl.concat([hits_0, hits_1], how="vertical")
                .group_by("id", "role")
                .agg(pl.max("score").alias("score"))
                .sort("score", descending=True)
            )
        if "role" in hits_df.columns:
            hits_df = hits_df.filter(pl.col("role") != "labels")

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=max(effective_k, 50))
        ranked = agg.select("id", "score", "best_role").to_dicts()

        rescored: list[dict[str, object]] = []
        for row in ranked:
            gid = row.get("id")
            if not isinstance(gid, str):
                continue
            labels = self._id_to_labels.get(gid, [])
            score = float(row.get("score") or 0.0)
            rescored.append(
                {
                    **row,
                    "score": score,
                    "score_adj": score + chart_bonus(guideline_labels=labels, hints=hints),
                }
            )
        rescored.sort(
            key=lambda r: (-float(r.get("score_adj") or 0.0), str(r.get("id") or ""))
        )
        rescored = rescored[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [
            id_to_entry[row["id"]]
            for row in rescored
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "bm25_prf_label_rerank",
            "query_expanded": expanded != search_text,
            "filters": {
                "excluded_pipeline": True,
                "excluded_domain_elections": not hints.is_election_related,
            },
            "hints": {
                "is_election_related": hints.is_election_related,
                "chart_labels": sorted(hints.chart_labels),
            },
            "hits": [
                {
                    "id": row["id"],
                    "score": float(row["score"]),
                    "score_adj": float(row["score_adj"]),
                    "best_role": row.get("best_role"),
                }
                for row in rescored
                if isinstance(row.get("id"), str)
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
