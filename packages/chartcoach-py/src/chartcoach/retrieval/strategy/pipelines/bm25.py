from __future__ import annotations

import re

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .searcher import GuidelineSearcher


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
