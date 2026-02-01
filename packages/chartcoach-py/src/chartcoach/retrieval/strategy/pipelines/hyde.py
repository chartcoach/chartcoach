from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.request_text import get_text_by_role, require_text_by_role
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .hints import build_search_text, chart_bonus, infer_hints
from .hints_v4 import (
    build_search_text_v4,
    chart_bonus_v4,
    domain_penalty_v4,
    infer_hints_v4,
    should_exclude_guideline_v4,
    task_bonus_v4,
)
from .hints_v5 import (
    build_search_text_v5,
    chart_bonus_v5,
    domain_penalty_v5,
    infer_hints_v5,
    multivariate_bonus_v5,
    precision_bonus_v5,
    should_exclude_guideline_v5,
    task_bonus_v5,
)
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
            "Scenario context (intent + query). "
            "Write a hypothetical high-quality critique that mentions likely chart issues and improvements."
        )
    )


class HydeSignatureV2(dspy.Signature):
    """Generate a HyDE-style pseudo-document focused on chart critique and redesign."""

    situation: str = dspy.InputField(
        desc=(
            "Designer intent and chart context. "
            "Write a hypothetical high-quality critique and redesign plan. "
            "Do not talk about information retrieval or automated pipelines."
        )
    )

    pseudo_document: str = dspy.OutputField(
        desc=(
            "A dense, specific pseudo-document (no guideline IDs) that includes likely relevant design concepts, "
            "chart/encoding terms, audience/task constraints, and common failure modes."
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
        if self._config.cross_encoder_model and candidates:
            qvec = self._searcher.vector_index.embed_query(situation)
            reranker = CrossEncoderReranker(model_name=self._config.cross_encoder_model)
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
            "fill_fallback_used": fill_fallback_used,
            "hits": [{"id": gid} for gid in final_ids[:effective_k]],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class HydeHybridStrategyV4(RetrievalStrategy):
    """HyDE v4 (radial disambiguation + precision/multivariate boosting)."""

    id = "hyde-hybrid@v4"

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
        self._program = dspy.ChainOfThought(HydeSignatureV2)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import CrossEncoderReranker, RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        title = (get_text_by_role(request, role="title") or "").strip()
        situation_raw = require_text_by_role(request, role="situation")
        hints = infer_hints_v5(title=title, situation=situation_raw)
        situation = build_search_text_v5(title=title, situation=situation_raw, hints=hints)

        allowed_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if not should_exclude_guideline_v5(guideline_labels=labels, hints=hints)
        }

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

        hits_fts = self._searcher.search_fts(query_text=situation, k=raw_k, ids=allowed_ids)
        if "role" in hits_fts.columns:
            hits_fts = hits_fts.filter(pl.col("role") != "labels")
        agg_fts = self._searcher.aggregate_guideline_hits(hits_fts, k=self._dense_candidate_k)
        rank_fts = [gid for gid in agg_fts["id"].to_list() if isinstance(gid, str)]

        pseudo_vec = self._searcher.vector_index.embed_query(pseudo)
        hits_dense = self._searcher.search_dense(
            query_vector=pseudo_vec, k=raw_k, ids=allowed_ids
        )
        if "role" in hits_dense.columns:
            hits_dense = hits_dense.filter(pl.col("role") != "labels")
        agg_dense = self._searcher.aggregate_guideline_hits(
            hits_dense, k=self._dense_candidate_k
        )
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]

        fused = rrf_rank(rankings=[rank_fts, rank_dense], k=self._config.rrf_k)
        candidates = fused[: max(effective_k, self._dense_candidate_k)]

        final_ids = candidates[:effective_k]
        cross_encoder_fallback_used = False
        if self._config.cross_encoder_model and candidates:
            qvec = self._searcher.vector_index.embed_query(situation)
            reranker = CrossEncoderReranker(model_name=self._config.cross_encoder_model)
            hits_hybrid = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=reranker,
                k=min(len(candidates), self._dense_candidate_k),
                ids=set(candidates),
                fts_columns="text",
            )
            if "role" in hits_hybrid.columns:
                hits_hybrid = hits_hybrid.filter(pl.col("role") != "labels")
            agg = self._searcher.aggregate_guideline_hits(hits_hybrid, k=effective_k)
            proposed = agg.select("id", "score", "best_role").to_dicts()
            rescored = []
            for row in proposed:
                gid = row.get("id")
                if not isinstance(gid, str):
                    continue
                labels = self._id_to_labels.get(gid, [])
                score = float(row.get("score") or 0.0)
                rescored.append(
                    (
                        gid,
                        score
                        + chart_bonus_v5(guideline_labels=labels, hints=hints)
                        + task_bonus_v5(guideline_labels=labels, hints=hints)
                        + multivariate_bonus_v5(guideline_labels=labels, hints=hints)
                        + precision_bonus_v5(guideline_labels=labels, hints=hints)
                        + domain_penalty_v5(guideline_labels=labels, hints=hints),
                        row.get("best_role"),
                    )
                )
            rescored.sort(key=lambda t: (-t[1], t[0]))
            reranked = [gid for gid, _score, _role in rescored]
            if reranked:
                final_ids = reranked[:effective_k]
            else:
                cross_encoder_fallback_used = True

        if len(final_ids) < effective_k:
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
            "score_kind": "hyde_rrf_fusion_label_rerank_v4",
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
            "fill_fallback_used": fill_fallback_used,
            "filters": {
                "excluded_pipeline": True,
                "hard_excluded_domains": True,
            },
            "hints": {
                "title_used": bool(title),
                "active_domains": sorted(hints.active_domains),
                "chart_labels": sorted(hints.chart_labels),
                "task_labels": sorted(hints.task_labels),
            },
            "hits": [{"id": gid} for gid in final_ids[:effective_k]],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class HydeHybridStrategyV2(RetrievalStrategy):
    """HyDE v2 (sanitized situation + filtering + label-aware rerank)."""

    id = "hyde-hybrid@v2"

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
        self._program = dspy.ChainOfThought(HydeSignatureV2)

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
                    pred = self._program(situation=situation)
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        pseudo = str(getattr(pred, "pseudo_document", "") if pred else "").strip()
        if not pseudo:
            pseudo = situation

        raw_k = max(30, min(3_000, effective_k * self._raw_multiplier))

        hits_fts = self._searcher.search_fts(
            query_text=situation, k=raw_k, ids=allowed_ids
        )
        if "role" in hits_fts.columns:
            hits_fts = hits_fts.filter(pl.col("role") != "labels")
        agg_fts = self._searcher.aggregate_guideline_hits(
            hits_fts, k=self._dense_candidate_k
        )
        rank_fts = [gid for gid in agg_fts["id"].to_list() if isinstance(gid, str)]

        pseudo_vec = self._searcher.vector_index.embed_query(pseudo)
        hits_dense = self._searcher.search_dense(
            query_vector=pseudo_vec, k=raw_k, ids=allowed_ids
        )
        if "role" in hits_dense.columns:
            hits_dense = hits_dense.filter(pl.col("role") != "labels")
        agg_dense = self._searcher.aggregate_guideline_hits(
            hits_dense, k=self._dense_candidate_k
        )
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]

        fused = rrf_rank(rankings=[rank_fts, rank_dense], k=self._config.rrf_k)
        candidates = fused[: max(effective_k, self._dense_candidate_k)]

        final_ids = candidates[:effective_k]
        cross_encoder_fallback_used = False
        if self._config.cross_encoder_model and candidates:
            qvec = self._searcher.vector_index.embed_query(situation)
            reranker = CrossEncoderReranker(model_name=self._config.cross_encoder_model)
            hits_hybrid = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=reranker,
                k=min(len(candidates), self._dense_candidate_k),
                ids=set(candidates),
                fts_columns="text",
            )
            if "role" in hits_hybrid.columns:
                hits_hybrid = hits_hybrid.filter(pl.col("role") != "labels")
            agg = self._searcher.aggregate_guideline_hits(hits_hybrid, k=effective_k)
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
                    )
                )
            rescored.sort(key=lambda t: (-t[1], t[0]))
            if rescored:
                final_ids = [gid for gid, _score in rescored]
            else:
                cross_encoder_fallback_used = True

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
            "score_kind": "hyde_rrf_fusion_label_rerank",
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
            "fill_fallback_used": fill_fallback_used,
            "filters": {
                "excluded_pipeline": True,
                "excluded_domain_elections": not hints.is_election_related,
            },
            "hints": {
                "is_election_related": hints.is_election_related,
                "chart_labels": sorted(hints.chart_labels),
            },
            "hits": [{"id": gid} for gid in final_ids[:effective_k]],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class HydeHybridStrategyV3(RetrievalStrategy):
    """HyDE v3 (title-aware hints + task-aware rerank + domain filtering)."""

    id = "hyde-hybrid@v3"

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
        self._program = dspy.ChainOfThought(HydeSignatureV2)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import CrossEncoderReranker, RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        title = (get_text_by_role(request, role="title") or "").strip()
        situation_raw = require_text_by_role(request, role="situation")
        hints = infer_hints_v4(title=title, situation=situation_raw)
        situation = build_search_text_v4(title=title, situation=situation_raw, hints=hints)

        allowed_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if not should_exclude_guideline_v4(guideline_labels=labels, hints=hints)
        }

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

        hits_fts = self._searcher.search_fts(
            query_text=situation, k=raw_k, ids=allowed_ids
        )
        if "role" in hits_fts.columns:
            hits_fts = hits_fts.filter(pl.col("role") != "labels")
        agg_fts = self._searcher.aggregate_guideline_hits(
            hits_fts, k=self._dense_candidate_k
        )
        rank_fts = [gid for gid in agg_fts["id"].to_list() if isinstance(gid, str)]

        pseudo_vec = self._searcher.vector_index.embed_query(pseudo)
        hits_dense = self._searcher.search_dense(
            query_vector=pseudo_vec, k=raw_k, ids=allowed_ids
        )
        if "role" in hits_dense.columns:
            hits_dense = hits_dense.filter(pl.col("role") != "labels")
        agg_dense = self._searcher.aggregate_guideline_hits(
            hits_dense, k=self._dense_candidate_k
        )
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]

        fused = rrf_rank(rankings=[rank_fts, rank_dense], k=self._config.rrf_k)
        candidates = fused[: max(effective_k, self._dense_candidate_k)]

        final_ids = candidates[:effective_k]
        cross_encoder_fallback_used = False
        if self._config.cross_encoder_model and candidates:
            qvec = self._searcher.vector_index.embed_query(situation)
            reranker = CrossEncoderReranker(model_name=self._config.cross_encoder_model)
            hits_hybrid = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=reranker,
                k=min(len(candidates), self._dense_candidate_k),
                ids=set(candidates),
                fts_columns="text",
            )
            if "role" in hits_hybrid.columns:
                hits_hybrid = hits_hybrid.filter(pl.col("role") != "labels")
            agg = self._searcher.aggregate_guideline_hits(hits_hybrid, k=effective_k)
            proposed = agg.select("id", "score", "best_role").to_dicts()
            rescored = []
            for row in proposed:
                gid = row.get("id")
                if not isinstance(gid, str):
                    continue
                labels = self._id_to_labels.get(gid, [])
                score = float(row.get("score") or 0.0)
                rescored.append(
                    (
                        gid,
                        score
                        + chart_bonus_v4(guideline_labels=labels, hints=hints)
                        + task_bonus_v4(guideline_labels=labels, hints=hints)
                        + domain_penalty_v4(guideline_labels=labels, hints=hints),
                    )
                )
            rescored.sort(key=lambda t: (-t[1], t[0]))
            if rescored:
                final_ids = [gid for gid, _score in rescored]
            else:
                cross_encoder_fallback_used = True

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
            "score_kind": "hyde_rrf_fusion_label_rerank_v3",
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
            "fill_fallback_used": fill_fallback_used,
            "filters": {
                "excluded_pipeline": True,
                "hard_excluded_domains": True,
            },
            "hints": {
                "title_used": bool(title),
                "active_domains": sorted(hints.active_domains),
                "chart_labels": sorted(hints.chart_labels),
                "task_labels": sorted(hints.task_labels),
            },
            "hits": [{"id": gid} for gid in final_ids[:effective_k]],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
