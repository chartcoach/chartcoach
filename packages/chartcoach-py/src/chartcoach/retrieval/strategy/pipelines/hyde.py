from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .ranking import rrf_rank
from .searcher import GuidelineSearcher

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class HydeSignature(dspy.Signature):
    """Generate a HyDE-style pseudo-document for retrieval."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "Write a hypothetical high-quality critique that mentions likely chart issues and improvements. "
            "Focus only on the described chart, and ignore mentions of adjacent charts in the surrounding story."
        )
    )


@dataclass(frozen=True, slots=True)
class HydeConfig:
    cross_encoder_model: str | None = "cross-encoder/ms-marco-TinyBERT-L-6"
    rrf_k: int = 60


class HydeHybridStrategy(RetrievalStrategy):
    """HyDE (LLM pseudo-document) + hybrid fusion to improve recall on short/vague queries."""

    id = "hyde-hybrid@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        config: HydeConfig = HydeConfig(),
        default_k: int = 20,
        raw_multiplier: int = 12,
        dense_candidate_k: int = 80,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._config = config
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._dense_candidate_k = int(dense_candidate_k)
        self._program = dspy.ChainOfThought(HydeSignature)
        # Lazily initialized on first use to avoid repeatedly loading weights.
        self._cross_encoder_reranker = None

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import CrossEncoderReranker, RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation = self._searcher.build_query_text(request)

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(situation=situation)
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        pseudo = str(getattr(pred, "pseudo_document", "") if pred else "").strip()
        if not pseudo:
            pseudo = situation

        raw_k = max(30, min(3_000, effective_k * self._raw_multiplier))

        # Lexical branch (precise): original situation/query.
        hits_fts = self._searcher.search_fts(query_text=situation, k=raw_k)
        agg_fts = self._searcher.aggregate_guideline_hits(
            hits_fts, k=self._dense_candidate_k
        )
        rank_fts = [gid for gid in agg_fts["id"].to_list() if isinstance(gid, str)]

        # Dense branch (semantic): HyDE pseudo-document.
        pseudo_vec = self._searcher.vector_index.embed_query(pseudo)
        hits_dense = self._searcher.search_dense(query_vector=pseudo_vec, k=raw_k)
        agg_dense = self._searcher.aggregate_guideline_hits(
            hits_dense, k=self._dense_candidate_k
        )
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]

        fused = rrf_rank(rankings=[rank_fts, rank_dense], k=self._config.rrf_k)
        candidates = fused[: max(effective_k, self._dense_candidate_k)]

        final_ids = candidates[:effective_k]
        cross_encoder_fallback_used = False
        cross_encoder_error: str | None = None
        if self._config.cross_encoder_model and candidates:
            qvec = self._searcher.vector_index.embed_query(situation)
            try:
                reranker = self._cross_encoder_reranker
                if reranker is None:
                    reranker = CrossEncoderReranker(
                        model_name=self._config.cross_encoder_model
                    )
                    self._cross_encoder_reranker = reranker

                hits_hybrid = self._searcher.search_hybrid(
                    query_text=situation,
                    query_vector=qvec,
                    reranker=reranker,
                    k=min(len(candidates), self._dense_candidate_k),
                    ids=set(candidates),
                    fts_columns="text",
                )
                agg = self._searcher.aggregate_guideline_hits(hits_hybrid, k=effective_k)
                reranked = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
                if reranked:
                    final_ids = reranked
                else:
                    cross_encoder_fallback_used = True
            except Exception as e:  # noqa: BLE001
                cross_encoder_fallback_used = True
                cross_encoder_error = str(e)

        if len(final_ids) < effective_k and candidates:
            cross_encoder_fallback_used = True
            seen = set(final_ids)
            for gid in candidates:
                if gid in seen:
                    continue
                final_ids.append(gid)
                seen.add(gid)
                if len(final_ids) >= effective_k:
                    break

        fill_fallback_used = False
        if len(final_ids) < effective_k and self.catalog.entries:
            # If HyDE fusion yields too few candidates (or the reranker returns
            # nothing), fall back to a strong hybrid retrieval to complete top-k.
            fill_fallback_used = True
            qvec = self._searcher.vector_index.embed_query(situation)
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=max(50, raw_k))
            fill_ids = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
            seen = set(final_ids)
            for gid in fill_ids:
                if gid in seen:
                    continue
                final_ids.append(gid)
                seen.add(gid)
                if len(final_ids) >= effective_k:
                    break
            final_ids = final_ids[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in final_ids if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "hyde_rrf_fusion",
            "rrf_k": self._config.rrf_k,
            "lm_attempts": lm_attempts,
            "lm_fallback_used": pred is None,
            "lm_error": lm_error if pred is None else None,
            "pseudo_document_chars": len(pseudo),
            "cross_encoder": (
                {"model": self._config.cross_encoder_model}
                if self._config.cross_encoder_model
                else None
            ),
            "cross_encoder_fallback_used": cross_encoder_fallback_used,
            "cross_encoder_error": cross_encoder_error,
            "fill_fallback_used": fill_fallback_used,
            "hits": [{"id": gid} for gid in final_ids[:effective_k]],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
