from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    focus_config_from_env,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .ranking import rrf_rank, rrf_scores
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class HydeSignature(dspy.Signature):
    """Generate a HyDE-style pseudo-document for retrieval."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "Write a hypothetical high-quality analysis oriented by `focus`. "
            "Focus only on the described chart, and ignore mentions of adjacent charts in the surrounding story. "
            "Preserve key domain-specific nouns/variables from the situation. "
            "If the situation implies paired comparisons (e.g., before-after / year-over-year / two values per category), "
            "mention change-focused design considerations (without inventing data details)."
        )
    )
    focus: str = dspy.InputField(
        desc="One of: all, violations, satisfied. Use it to choose an analysis style."
    )

    pseudo_document: str = dspy.OutputField(
        desc=(
            "A search-oriented pseudo-document that will retrieve relevant guideline text. "
            "For violations: emphasize likely problems and concrete improvements. "
            "For satisfied: emphasize likely strengths and what to preserve/verify. "
            "Keep it specific to the described chart."
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
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._config = config
        self._default_k = int(default_k)
        self._raw_multiplier = int(raw_multiplier)
        self._dense_candidate_k = int(dense_candidate_k)
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None
        self._program = dspy.ChainOfThought(HydeSignature)
        # Lazily initialized on first use to avoid repeatedly loading weights.
        self._cross_encoder_reranker = None

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
        status_meta: dict[str, object] = {}
        use_status_filter = focus_mode != "all" and self._focus.use_status_filter

        pred: dspy.Prediction | None = None
        lm_error: str | None = None
        lm_attempts = 0
        for lm in (self._lm, self._lm.copy(cache=False)):
            lm_attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(situation=situation, focus=focus_mode)
                lm_error = None
                break
            except Exception as e:  # noqa: BLE001
                lm_error = str(e)

        pseudo = str(getattr(pred, "pseudo_document", "") if pred else "").strip()
        if not pseudo:
            pseudo = situation

        raw_k = max(30, min(3_000, effective_k * self._raw_multiplier))
        roles = primary_roles_for_focus(focus_mode)
        roles_used = roles

        # Lexical branch (precise): original situation/query.
        hits_fts = self._searcher.search_fts(
            query_text=situation, k=raw_k, roles=roles_used
        )
        if (
            hits_fts.is_empty()
            and roles is not None
            and self._focus.allow_role_fallback
        ):
            roles_used = fallback_roles_for_focus(focus_mode)
            hits_fts = self._searcher.search_fts(
                query_text=situation, k=raw_k, roles=roles_used
            )
        agg_fts = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_fts, k=self._dense_candidate_k
        )
        rows_fts = agg_fts.to_dicts()
        rank_fts = [gid for gid in agg_fts["id"].to_list() if isinstance(gid, str)]

        # Dense branch (semantic): HyDE pseudo-document.
        pseudo_vec = self._searcher.vector_index.embed_query(pseudo)
        hits_dense = self._searcher.search_dense(
            query_vector=pseudo_vec, k=raw_k, roles=roles_used
        )
        agg_dense = self._searcher.aggregate_guideline_hits_with_evidence(
            hits_dense, k=self._dense_candidate_k
        )
        rows_dense = agg_dense.to_dicts()
        rank_dense = [gid for gid in agg_dense["id"].to_list() if isinstance(gid, str)]

        evidence_by_id: dict[str, list[dict[str, object]]] = {}
        best_role_by_id: dict[str, str] = {}
        for row in [*rows_fts, *rows_dense]:
            gid = row.get("id")
            if not isinstance(gid, str) or not gid:
                continue
            ev = row.get("evidence")
            if isinstance(ev, list) and ev:
                evidence_by_id.setdefault(gid, []).extend(
                    [e for e in ev if isinstance(e, dict)]
                )
            best_role = row.get("best_role")
            if isinstance(best_role, str) and best_role:
                best_role_by_id.setdefault(gid, best_role)

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

        fused_scores = rrf_scores(rankings=[rank_fts, rank_dense], k=self._config.rrf_k)
        fused = rrf_rank(rankings=[rank_fts, rank_dense], k=self._config.rrf_k)
        candidates = fused[: max(effective_k, self._dense_candidate_k)]

        final_ids = candidates[:effective_k]
        rerank_hits_by_id: dict[str, dict[str, object]] = {}
        cross_encoder_fallback_used = False
        cross_encoder_error: str | None = None
        rerank_query_chars: int | None = None
        if self._config.cross_encoder_model and candidates:
            rerank_query = pseudo
            rerank_query_chars = len(rerank_query)
            qvec = self._searcher.vector_index.embed_query(rerank_query)
            try:
                reranker = self._cross_encoder_reranker
                if reranker is None:
                    reranker = CrossEncoderReranker(
                        model_name=self._config.cross_encoder_model
                    )
                    self._cross_encoder_reranker = reranker

                hits_hybrid = self._searcher.search_hybrid(
                    query_text=rerank_query,
                    query_vector=qvec,
                    reranker=reranker,
                    k=min(len(candidates), self._dense_candidate_k),
                    ids=set(candidates),
                    roles=roles_used,
                    fts_columns="text",
                )
                agg = self._searcher.aggregate_guideline_hits_with_evidence(
                    hits_hybrid, k=effective_k
                )
                rows = agg.to_dicts()
                rerank_hits_by_id = {
                    row["id"]: row for row in rows if isinstance(row.get("id"), str)
                }
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
        fill_hits_by_id: dict[str, dict[str, object]] = {}
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
        for gid in [*final_ids, *candidates]:
            if gid in seen_ids or gid not in id_to_entry:
                continue
            ordered_candidate_ids.append(gid)
            seen_ids.add(gid)

        candidate_entries = [id_to_entry[gid] for gid in ordered_candidate_ids]
        ordered_entries = candidate_entries[:effective_k]
        if use_status_filter and ordered_entries:
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
            "score_kind": "hyde_rrf_fusion",
            "rrf_k": self._config.rrf_k,
            "focus": {
                "mode": focus_mode,
                "roles": sorted(roles_used) if roles_used else None,
            },
            "chart_vision": vision_meta,
            **status_meta,
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
            "cross_encoder_rerank_query_chars": rerank_query_chars,
            "fill_fallback_used": fill_fallback_used,
            "hits": hits,
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
