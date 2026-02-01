from __future__ import annotations

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .searcher import GuidelineSearcher


class HybridRrfStrategy(RetrievalStrategy):
    """Hybrid lexical+dense retrieval with reciprocal-rank fusion (RRF)."""

    id = "hybrid-rrf@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        default_k: int = 20,
        raw_multiplier: int = 12,
        rrf_k: int = 60,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._rrf_k = int(rrf_k)

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        query_text = self._searcher.build_query_text(request)
        query_vec = self._searcher.vector_index.embed_query(query_text)

        raw_k = max(20, min(3_000, effective_k * self._raw_multiplier))
        hits_df = self._searcher.search_hybrid(
            query_text=query_text,
            query_vector=query_vec,
            reranker=RRFReranker(K=self._rrf_k),
            k=raw_k,
            fts_columns="text",
        )

        agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
        ranked = agg.select("id", "score", "best_role").to_dicts()

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [
            id_to_entry[row["id"]]
            for row in ranked
            if isinstance(row.get("id"), str) and row["id"] in id_to_entry
        ]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "hybrid_relevance",
            "reranker": {"type": "rrf", "k": self._rrf_k},
            "hits": [
                {
                    "id": row["id"],
                    "score": float(row["score"]),
                    "best_role": row.get("best_role"),
                }
                for row in ranked
                if isinstance(row.get("id"), str)
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
