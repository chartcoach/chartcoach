from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import FocusConfig, focus_config_from_env, fallback_roles_for_focus, primary_roles_for_focus
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .ranking import rrf_rank
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class QueryFusionSignature(dspy.Signature):
    """Generate diverse search queries that cover different facets of the situation."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "Focus only on the chart described by the title/intent, and ignore mentions of other charts in the surrounding story. "
            "Do not invent domains or chart types that are not implied by the text."
        )
    )
    n: int = dspy.InputField(
        desc="Number of queries to produce.", ge=1, le=8, default=4
    )
    focus: str = dspy.InputField(
        desc="One of: all, violations, satisfied. Use it to choose query emphasis."
    )

    focused_situation: str = dspy.OutputField(
        desc=(
            "A short rewrite of the situation that includes ONLY the chart to improve and its intent. "
            "Preserve key domain nouns/variables (e.g., inflation, job starters, pay gap, aid) but omit unrelated surrounding context."
        )
    )
    queries: list[str] = dspy.OutputField(
        desc=(
            "A list of short, diverse search queries. "
            "Each query should focus on a different facet (chart type, task/goal, audience, risk/clarity). "
            "If the situation compares exactly two time points or otherwise implies paired values (before-after / year-over-year), "
            "you MUST include a query that contains the literal phrases 'paired values' and 'delta encoding' (and optionally 'pairwise delta')."
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
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._config = config
        self._default_k = int(default_k)
        self._per_query_raw_multiplier = int(per_query_raw_multiplier)
        self._per_query_guideline_k = int(per_query_guideline_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None

        self._program = dspy.Predict(QueryFusionSignature)
        # Lazily initialized on first use to avoid repeatedly loading weights.
        self._cross_encoder_reranker = None

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

        vision_meta: dict[str, object] = {}
        if self._vlm is not None and self._vision_config.enabled:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=ChartVisionModule(vlm=self._vlm, config=self._vision_config),
            )

        situation = self._searcher.build_query_text(request)
        focus_mode = self._focus.mode

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(
                        situation=situation, n=self._config.n_queries, focus=focus_mode
                    )
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        focused_situation = str(
            getattr(pred, "focused_situation", "") if pred is not None else ""
        ).strip()
        if not focused_situation:
            focused_situation = situation

        queries = self._clean_queries(
            getattr(pred, "queries", None) if pred is not None else None,
            fallback=focused_situation,
        )
        queries = queries[: max(1, int(self._config.n_queries))]

        raw_k = max(30, min(3_000, effective_k * self._per_query_raw_multiplier))
        per_query_k = max(effective_k, self._per_query_guideline_k)
        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles

        per_query_rankings: list[list[str]] = []
        for q in queries:
            qvec = self._searcher.vector_index.embed_query(q)
            hits_df = self._searcher.search_hybrid(
                query_text=q,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                roles=roles_used,
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=per_query_k)
            per_query_rankings.append(
                [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
            )

        fused = rrf_rank(rankings=per_query_rankings, k=self._config.rrf_k)
        if not fused and roles is not None and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(focus_mode)
            per_query_rankings = []
            for q in queries:
                qvec = self._searcher.vector_index.embed_query(q)
                hits_df = self._searcher.search_hybrid(
                    query_text=q,
                    query_vector=qvec,
                    reranker=RRFReranker(K=self._config.rrf_k),
                    k=raw_k,
                    roles=roles_used,
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
        cross_encoder_error: str | None = None
        rerank_query_chars: int | None = None
        if self._config.cross_encoder_model and fused:
            rerank_query = "\n".join(queries) if queries else focused_situation
            rerank_query_chars = len(rerank_query)
            qvec = self._searcher.vector_index.embed_query(rerank_query)
            try:
                reranker = self._cross_encoder_reranker
                if reranker is None:
                    reranker = CrossEncoderReranker(
                        model_name=self._config.cross_encoder_model
                    )
                    self._cross_encoder_reranker = reranker

                hits_df = self._searcher.search_hybrid(
                    query_text=rerank_query,
                    query_vector=qvec,
                    reranker=reranker,
                    k=min(len(fused), self._config.cross_encoder_candidate_limit),
                    ids=set(fused),
                    roles=roles_used,
                    fts_columns="text",
                )
                agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
                proposed = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
                if proposed:
                    reranked = proposed
                else:
                    cross_encoder_fallback_used = True
            except Exception as e:  # noqa: BLE001
                cross_encoder_fallback_used = True
                cross_encoder_error = str(e)

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

        fill_ids: list[str] = []
        fill_fallback_used = False
        if len(final_ids) < effective_k and self.catalog.entries:
            # If query fusion fails to yield enough candidates (e.g., empty index
            # hits), fall back to a strong hybrid retrieval for a complete top-k.
            fill_fallback_used = True
            qvec = self._searcher.vector_index.embed_query(focused_situation)
            hits_df = self._searcher.search_hybrid(
                query_text=focused_situation,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                roles=roles_used,
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
        ordered_candidate_ids: list[str] = []
        seen_ids: set[str] = set()
        for gid in [*final_ids, *fused, *fill_ids]:
            if gid in seen_ids or gid not in id_to_entry:
                continue
            ordered_candidate_ids.append(gid)
            seen_ids.add(gid)

        candidate_entries = [id_to_entry[gid] for gid in ordered_candidate_ids]
        ordered_entries = candidate_entries[:effective_k]
        status_meta: dict[str, object] = {}
        if focus_mode != "all" and ordered_entries:
            status_lm, status_module, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
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
            "score_kind": "rrf_fusion",
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
            "queries": queries,
            "focused_situation": focused_situation,
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
            "cross_encoder_error": cross_encoder_error,
            "cross_encoder_rerank_query_chars": rerank_query_chars,
            "fill_fallback_used": fill_fallback_used,
            "hits": [{"id": entry.id} for entry in ordered_entries],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
