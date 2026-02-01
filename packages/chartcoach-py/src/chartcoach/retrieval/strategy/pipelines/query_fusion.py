from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.request_text import require_text_by_role
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .hints import build_search_text, chart_bonus, infer_hints
from .ranking import rrf_rank
from .searcher import GuidelineSearcher

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class QueryFusionSignature(dspy.Signature):
    """Generate diverse search queries that cover different facets of the situation."""

    situation: str = dspy.InputField(desc="Full scenario context (intent + query).")
    n: int = dspy.InputField(
        desc="Number of queries to produce.", ge=1, le=8, default=4
    )

    queries: list[str] = dspy.OutputField(
        desc=(
            "A list of short, diverse search queries. "
            "Each query should focus on a different facet (chart type, task/goal, audience, risk/clarity)."
        )
    )


class QueryFusionSignatureV2(dspy.Signature):
    """Generate diverse design-focused search queries (avoid IR/pipeline framing)."""

    situation: str = dspy.InputField(
        desc=(
            "Designer intent and chart context. "
            "The goal is to improve an existing visualization (not to build an information-retrieval pipeline)."
        )
    )
    n: int = dspy.InputField(
        desc="Number of queries to produce.", ge=1, le=8, default=4
    )

    queries: list[str] = dspy.OutputField(
        desc=(
            "A list of short, diverse search queries. Each query should focus on a different facet "
            "(chart type/encoding, task/goal, audience, common failure modes). "
            "Avoid words like 'retrieval', 'embedding', 'pipeline', or 'article representation'."
        )
    )


@dataclass(frozen=True, slots=True)
class QueryFusionConfig:
    n_queries: int = 4
    rrf_k: int = 60
    cross_encoder_model: str | None = "cross-encoder/ms-marco-TinyBERT-L-6"
    cross_encoder_candidate_limit: int = 80


class QueryFusionHybridStrategy(RetrievalStrategy):
    """Query-fusion hybrid retrieval (DSPy multi-query + RRF + optional cross-encoder rerank)."""

    id = "query-fusion-hybrid@v1"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        config: QueryFusionConfig = QueryFusionConfig(),
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

        self._program = dspy.Predict(QueryFusionSignature)

    @staticmethod
    def _clean_queries(raw: object, *, fallback: str) -> list[str]:
        items: list[str] = []
        if isinstance(raw, list):
            for item in raw:
                if isinstance(item, str):
                    stripped = item.strip()
                    if stripped:
                        items.append(stripped)
        elif isinstance(raw, str) and raw.strip():
            items.append(raw.strip())

        if fallback.strip():
            items.insert(0, fallback.strip())

        seen: set[str] = set()
        deduped: list[str] = []
        for q in items:
            norm = " ".join(q.lower().split())
            if norm in seen:
                continue
            seen.add(norm)
            deduped.append(q)
        return deduped

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

        queries = self._clean_queries(
            getattr(pred, "queries", None) if pred is not None else None,
            fallback=situation,
        )
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
            # If query fusion fails to yield enough candidates (e.g., empty index
            # hits), fall back to a strong hybrid retrieval for a complete top-k.
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
            "score_kind": "rrf_fusion",
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
            "hits": [{"id": gid} for gid in final_ids],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class QueryFusionHybridStrategyV2(RetrievalStrategy):
    """Query-fusion hybrid retrieval v2 (sanitized situation + filtering + label-aware rerank)."""

    id = "query-fusion-hybrid@v2"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        config: QueryFusionConfig = QueryFusionConfig(),
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

        self._program = dspy.Predict(QueryFusionSignatureV2)

    def _allowed_ids(self, *, is_election_related: bool) -> set[str]:
        allowed = set(self._id_to_labels)
        allowed -= self._pipeline_ids
        if not is_election_related:
            allowed -= self._elections_ids
        return allowed

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import CrossEncoderReranker, RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation_raw = require_text_by_role(request, role="situation")
        situation = build_search_text(situation=situation_raw)
        hints = infer_hints(situation=situation_raw)
        allowed_ids = self._allowed_ids(is_election_related=hints.is_election_related)

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

        queries = QueryFusionHybridStrategy._clean_queries(
            getattr(pred, "queries", None) if pred is not None else None,
            fallback=situation,
        )
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
                ids=allowed_ids,
                fts_columns="text",
            )
            if "role" in hits_df.columns:
                hits_df = hits_df.filter(pl.col("role") != "labels")
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
            if "role" in hits_df.columns:
                hits_df = hits_df.filter(pl.col("role") != "labels")
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
            proposed = agg.select("id", "score", "best_role").to_dicts()
            rescored = []
            for row in proposed:
                gid = row.get("id")
                if not isinstance(gid, str):
                    continue
                score = float(row.get("score") or 0.0)
                rescored.append(
                    (
                        gid,
                        score
                        + chart_bonus(
                            guideline_labels=self._id_to_labels.get(gid, []),
                            hints=hints,
                        ),
                        row.get("best_role"),
                    )
                )
            rescored.sort(key=lambda t: (-t[1], t[0]))
            reranked = [gid for gid, _score, _role in rescored] or reranked
            if not rescored:
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
                ids=allowed_ids,
                fts_columns="text",
            )
            if "role" in hits_df.columns:
                hits_df = hits_df.filter(pl.col("role") != "labels")
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
            "score_kind": "rrf_fusion_label_rerank",
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
            "filters": {
                "excluded_pipeline": True,
                "excluded_domain_elections": not hints.is_election_related,
            },
            "hints": {
                "is_election_related": hints.is_election_related,
                "chart_labels": sorted(hints.chart_labels),
            },
            "hits": [{"id": gid} for gid in final_ids],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
