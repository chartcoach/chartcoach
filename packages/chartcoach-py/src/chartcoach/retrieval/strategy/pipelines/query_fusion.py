from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

from chartcoach.catalog import Catalog
from chartcoach.retrieval.operators import apply_status_filter, plan_status_filter
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .guideline_status import StatusScorer
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, prepare_chart_vision

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
            "Preserve key domain-specific nouns/variables from the situation, but omit unrelated surrounding context."
        )
    )
    queries: list[str] = dspy.OutputField(
        desc=(
            "A list of short, diverse search queries. "
            "Each query should focus on a different facet (chart type, task/goal, audience, risk/clarity). "
            "If the situation implies paired comparisons (e.g., before-after / year-over-year / two values per category), "
            "include at least one query about representing change or differences clearly."
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
        vision: ChartVisionModule | None = None,
        status_scorer: StatusScorer | None = None,
        config: QueryFusionConfig = QueryFusionConfig(),
        default_k: int = 20,
        per_query_raw_multiplier: int = 10,
        per_query_guideline_k: int = 40,
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher: GuidelineSearcher = searcher
        self._lm: dspy.LM = lm
        self._config: QueryFusionConfig = config
        self._default_k: int = int(default_k)
        self._per_query_raw_multiplier: int = int(per_query_raw_multiplier)
        self._per_query_guideline_k: int = int(per_query_guideline_k)
        self._focus: FocusConfig = focus or FocusConfig()
        self._vision: ChartVisionModule | None = vision
        self._status_scorer: StatusScorer | None = status_scorer

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
        if self._vision is not None:
            request, vision_tokens_query, vision_meta = prepare_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=self._vision,
            )
        else:
            vision_tokens_query = None

        situation = self._searcher.build_query_text(request)
        situation_for_lm = (
            f"{situation}\n\nChart tokens:\n{vision_tokens_query}"
            if vision_tokens_query
            else situation
        )
        focus_mode = self._focus.mode

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(
                        situation=situation_for_lm,
                        n=self._config.n_queries,
                        focus=focus_mode,
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
        query_weights: list[float] = [1.0 for _ in queries]
        if vision_tokens_query:
            assert self._vision is not None
            norm_seen = {" ".join(q.lower().split()) for q in queries}
            norm_tokens = " ".join(vision_tokens_query.lower().split())
            if norm_tokens and norm_tokens not in norm_seen:
                queries.append(vision_tokens_query)
                query_weights.append(float(self._vision.config.fusion_weight))

        raw_k = max(30, min(3_000, effective_k * self._per_query_raw_multiplier))
        per_query_k = max(effective_k, self._per_query_guideline_k)
        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles

        def _merge_evidence(
            primary: object,
            secondary: object,
            *,
            limit: int = 3,
        ) -> list[dict[str, object]]:
            merged: list[dict[str, object]] = []
            for source in (primary, secondary):
                if not isinstance(source, list):
                    continue
                for item in source:
                    if not isinstance(item, dict):
                        continue
                    payload = cast("dict[str, object]", item)
                    text = str(payload.get("text") or "").strip()
                    if not text:
                        continue
                    merged.append(payload)

            def _score(item: dict[str, object]) -> float:
                raw = item.get("score")
                if isinstance(raw, (int, float)):
                    return float(raw)
                if isinstance(raw, str):
                    try:
                        return float(raw)
                    except ValueError:
                        return 0.0
                return 0.0

            merged.sort(key=_score, reverse=True)
            return merged[: max(0, int(limit))]

        per_query_rankings: list[list[str]] = []
        per_query_weights: list[float] = []
        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}
        for q, weight in zip(queries, query_weights, strict=True):
            qvec = self._searcher.vector_index.embed_query(q)
            hits_df = self._searcher.search_hybrid(
                query_text=q,
                query_vector=qvec,
                reranker=RRFReranker(K=self._config.rrf_k),
                k=raw_k,
                roles=roles_used,
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits_with_evidence(
                hits_df, k=per_query_k
            )
            rows = agg.to_dicts()
            ranking: list[str] = []
            for row in rows:
                gid = row.get("id")
                if not isinstance(gid, str) or not gid:
                    continue
                ranking.append(gid)
                ev = row.get("evidence")
                if isinstance(ev, list) and ev:
                    evidence_by_id.setdefault(gid, []).extend(
                        [e for e in ev if isinstance(e, dict)]
                    )
                best_role = row.get("best_role")
                if isinstance(best_role, str) and best_role:
                    best_role_by_id.setdefault(gid, best_role)
            per_query_rankings.append(ranking)
            per_query_weights.append(float(weight))

        fused_scores = rrf_scores(
            rankings=per_query_rankings, k=self._config.rrf_k, weights=per_query_weights
        )
        fused = rrf_rank(
            rankings=per_query_rankings, k=self._config.rrf_k, weights=per_query_weights
        )
        if not fused and roles is not None and self._focus.allow_role_fallback:
            roles_used = fallback_roles_for_focus(focus_mode)
            per_query_rankings = []
            per_query_weights = []
            evidence_by_id = {}
            best_role_by_id = {}
            for q, weight in zip(queries, query_weights, strict=True):
                qvec = self._searcher.vector_index.embed_query(q)
                hits_df = self._searcher.search_hybrid(
                    query_text=q,
                    query_vector=qvec,
                    reranker=RRFReranker(K=self._config.rrf_k),
                    k=raw_k,
                    roles=roles_used,
                    fts_columns="text",
                )
                agg = self._searcher.aggregate_guideline_hits_with_evidence(
                    hits_df, k=per_query_k
                )
                rows = agg.to_dicts()
                ranking: list[str] = []
                for row in rows:
                    gid = row.get("id")
                    if not isinstance(gid, str) or not gid:
                        continue
                    ranking.append(gid)
                    ev = row.get("evidence")
                    if isinstance(ev, list) and ev:
                        evidence_by_id.setdefault(gid, []).extend(
                            [e for e in ev if isinstance(e, dict)]
                        )
                    best_role = row.get("best_role")
                    if isinstance(best_role, str) and best_role:
                        best_role_by_id.setdefault(gid, best_role)
                per_query_rankings.append(ranking)
                per_query_weights.append(float(weight))
            fused_scores = rrf_scores(
                rankings=per_query_rankings,
                k=self._config.rrf_k,
                weights=per_query_weights,
            )
            fused = rrf_rank(
                rankings=per_query_rankings,
                k=self._config.rrf_k,
                weights=per_query_weights,
            )
        fused = fused[: max(effective_k, self._config.cross_encoder_candidate_limit)]

        reranked = fused
        rerank_hits_by_id: dict[str, dict[str, object]] = {}
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
                agg = self._searcher.aggregate_guideline_hits_with_evidence(
                    hits_df, k=effective_k
                )
                rows = agg.to_dicts()
                proposed = [
                    gid for gid in agg["id"].to_list() if isinstance(gid, str) and gid
                ]
                rerank_hits_by_id = {
                    row["id"]: row for row in rows if isinstance(row.get("id"), str)
                }
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
        fill_hits_by_id: dict[str, dict[str, object]] = {}
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
            agg = self._searcher.aggregate_guideline_hits_with_evidence(
                hits_df, k=max(50, raw_k)
            )
            fill_rows = agg.to_dicts()
            fill_hits_by_id = {
                row["id"]: row for row in fill_rows if isinstance(row.get("id"), str)
            }
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
        status_scorer = self._status_scorer
        status_plan = plan_status_filter(
            focus_mode=focus_mode,
            requested_k=effective_k,
            status_scorer=status_scorer,
            status_filter_enabled=self._focus.use_status_filter,
        )
        if status_plan.use_status_filter and ordered_entries:
            assert status_scorer is not None
            ordered_entries, status_meta = apply_status_filter(
                request=request,
                entries=candidate_entries,
                output_k=effective_k,
                focus_mode=focus_mode,
                status_scorer=status_scorer,
            )

        def _coerce_float(raw: object, *, fallback: float = 0.0) -> float:
            if isinstance(raw, (int, float)):
                return float(raw)
            if isinstance(raw, str):
                try:
                    return float(raw)
                except ValueError:
                    return fallback
            return fallback

        hits: list[dict[str, object]] = []
        for entry in ordered_entries:
            rerank_hit = rerank_hits_by_id.get(entry.id)
            if not isinstance(rerank_hit, dict):
                rerank_hit = {}
            fill_hit = fill_hits_by_id.get(entry.id)
            if not isinstance(fill_hit, dict):
                fill_hit = {}

            score = _coerce_float(
                rerank_hit.get("score")
                if rerank_hit.get("score") is not None
                else fill_hit.get("score")
                if fill_hit.get("score") is not None
                else fused_scores.get(entry.id),
                fallback=0.0,
            )

            best_role = (
                rerank_hit.get("best_role")
                or fill_hit.get("best_role")
                or best_role_by_id.get(entry.id)
            )
            evidence = _merge_evidence(
                rerank_hit.get("evidence") or fill_hit.get("evidence"),
                evidence_by_id.get(entry.id),
                limit=3,
            )
            hits.append(
                {
                    "id": entry.id,
                    "score": score,
                    "best_role": best_role,
                    "evidence": evidence,
                }
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
            "query_weights": query_weights,
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
            "hits": hits,
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
