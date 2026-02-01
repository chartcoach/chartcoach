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


class FacetPlanSignature(dspy.Signature):
    """Extract facets + query variants for retrieving visualization design guidelines."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario context (intent + query). "
            "The goal is to improve an existing visualization (not to build an IR system)."
        )
    )
    n: int = dspy.InputField(desc="Number of facet queries to return.", ge=1, le=8, default=5)

    canonical_query: str = dspy.OutputField(
        desc="A short, search-optimized query that captures the main design intent."
    )
    facet_queries: list[str] = dspy.OutputField(
        desc=(
            "A list of short, diverse search queries, each focusing on a different facet "
            "(chart type/encoding, task/goal, audience, common failure modes, annotation/labeling)."
        )
    )
    chart_terms: list[str] = dspy.OutputField(
        desc="Chart and encoding terms present or strongly implied (e.g., 'choropleth', 'sankey', 'time series')."
    )
    task_terms: list[str] = dspy.OutputField(
        desc="Analytic/communication tasks implied (e.g., 'compare', 'rank', 'show change', 'part-to-whole')."
    )
    risk_terms: list[str] = dspy.OutputField(
        desc="Likely design risks/failure modes to check (e.g., 'area encoding distortion', 'color semantics')."
    )


@dataclass(frozen=True, slots=True)
class FacetFusionConfig:
    n_queries: int = 5
    rrf_k: int = 60
    cross_encoder_model: str | None = "cross-encoder/ms-marco-TinyBERT-L-6"
    cross_encoder_candidate_limit: int = 80


class FacetFusionHybridStrategy(RetrievalStrategy):
    """LLM facet extraction + hybrid retrieval with RRF fusion and optional cross-encoder rerank."""

    id = "facet-fusion-hybrid@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        config: FacetFusionConfig = FacetFusionConfig(),
        default_k: int = 20,
        per_query_raw_multiplier: int = 10,
        per_query_guideline_k: int = 40,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._config = config
        self._default_k = int(default_k)
        self._per_query_raw_multiplier = int(per_query_raw_multiplier)
        self._per_query_guideline_k = int(per_query_guideline_k)

        self._program = dspy.Predict(FacetPlanSignature)

    @staticmethod
    def _clean_list(raw: object) -> list[str]:
        items: list[str] = []
        if isinstance(raw, list):
            for item in raw:
                if isinstance(item, str):
                    stripped = item.strip()
                    if stripped:
                        items.append(stripped)
        elif isinstance(raw, str) and raw.strip():
            items.append(raw.strip())
        return items

    @staticmethod
    def _dedupe(items: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for item in items:
            norm = " ".join(item.lower().split())
            if not norm or norm in seen:
                continue
            seen.add(norm)
            out.append(item)
        return out

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
                    pred = self._program(situation=situation, n=self._config.n_queries)
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        canonical = str(getattr(pred, "canonical_query", "") if pred else "").strip()
        facet_queries = self._clean_list(getattr(pred, "facet_queries", None) if pred else None)
        chart_terms = self._clean_list(getattr(pred, "chart_terms", None) if pred else None)
        task_terms = self._clean_list(getattr(pred, "task_terms", None) if pred else None)
        risk_terms = self._clean_list(getattr(pred, "risk_terms", None) if pred else None)

        queries = [canonical or situation, *facet_queries]
        queries = self._dedupe([q for q in queries if q.strip()])
        queries = queries[: max(1, int(self._config.n_queries))]

        raw_k = max(30, min(3_000, effective_k * self._per_query_raw_multiplier))
        per_query_k = max(effective_k, self._per_query_guideline_k)

        per_query_rankings: list[list[str]] = []
        for q in queries:
            qvec = self._searcher.vector_index.embed_query(q)
            hits_df = self._searcher.search_hybrid(
                query_text=q,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=per_query_k)
            per_query_rankings.append(
                [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
            )

        fused = rrf_rank(rankings=per_query_rankings, k=self._config.rrf_k)
        fused = fused[: max(effective_k, self._config.cross_encoder_candidate_limit)]

        reranked = fused
        cross_encoder_fallback_used = False
        if self._config.cross_encoder_model and fused:
            qvec = self._searcher.vector_index.embed_query(situation)
            reranker = CrossEncoderReranker(model_name=self._config.cross_encoder_model)
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=reranker,
                k=min(len(fused), self._config.cross_encoder_candidate_limit),
                ids=set(fused),
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
            proposed = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
            if proposed:
                reranked = proposed
            else:
                cross_encoder_fallback_used = True

        final_ids = reranked[:effective_k]
        if len(final_ids) < effective_k:
            cross_encoder_fallback_used = True
            seen = set(final_ids)
            for gid in fused:
                if gid in seen:
                    continue
                final_ids.append(gid)
                seen.add(gid)
                if len(final_ids) >= effective_k:
                    break

        fill_fallback_used = False
        if len(final_ids) < effective_k and self.catalog.entries:
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
            "score_kind": "facet_rrf_fusion",
            "queries": queries,
            "lm_attempts": lm_attempts,
            "lm_fallback_used": pred is None,
            "lm_error": lm_error if pred is None else None,
            "rrf_k": self._config.rrf_k,
            "cross_encoder": (
                {"model": self._config.cross_encoder_model}
                if self._config.cross_encoder_model
                else None
            ),
            "cross_encoder_fallback_used": cross_encoder_fallback_used,
            "fill_fallback_used": fill_fallback_used,
            "plan": {
                "canonical_query": canonical,
                "chart_terms": chart_terms,
                "task_terms": task_terms,
                "risk_terms": risk_terms,
            },
            "hits": [{"id": gid} for gid in final_ids],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)

