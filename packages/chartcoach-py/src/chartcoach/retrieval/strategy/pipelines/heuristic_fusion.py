from __future__ import annotations

from dataclasses import dataclass

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.request_text import get_text_by_role, require_text_by_role
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .hints import ScenarioHints, build_search_text, chart_bonus, infer_hints
from .hints_v3 import (
    build_search_text_v3,
    chart_bonus_v3,
    domain_penalty_v3,
    infer_hints_v3,
    should_exclude_guideline_v3,
)
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
from .ranking import rrf_scores
from .searcher import GuidelineSearcher


_CHART_LABEL_TO_QUERY = {
    "chart:area": "area chart",
    "chart:bar": "bar chart",
    "chart:cartogram": "cartogram",
    "chart:choropleth": "choropleth map",
    "chart:donut": "donut chart",
    "chart:icon-array": "icon array dot chart",
    "chart:line": "line chart time series",
    "chart:map": "map",
    "chart:pie": "pie chart",
    "chart:radial": "radial chart",
    "chart:sankey": "sankey alluvial flow diagram",
    "chart:slope": "slope chart dumbbell plot",
    "chart:time-series": "time series chart",
    "chart:distribution": "distribution chart population pyramid",
    "chart:dot": "dot plot lollipop chart",
    "chart:pictograph": "pictograph icon array",
}

_TASK_LABEL_TO_QUERY = {
    "task:compare": "comparison guidance",
    "task:rank": "ranking sorting guidance",
    "task:trend": "trend over time guidance",
    "task:track-change": "change over time guidance",
    "task:detect-change": "change detection guidance",
    "task:flow": "flow diagram guidance",
    "task:part-to-whole": "part-to-whole guidance",
    "task:characterize-distribution": "distribution reading guidance",
    "task:encode-multivariate": "multivariate encoding guidance",
    "task:annotate": "annotation guidance",
    "task:highlight": "highlighting guidance",
}


def _derive_queries(*, situation: str, hints: ScenarioHints) -> list[str]:
    base = build_search_text(situation=situation)
    if not base:
        return []

    chart_terms = [
        _CHART_LABEL_TO_QUERY[label]
        for label in sorted(hints.chart_labels)
        if label in _CHART_LABEL_TO_QUERY
    ]
    chart_facet = ""
    if chart_terms:
        chart_facet = f"{' '.join(chart_terms)} design guidelines"

    return [
        base,
        chart_facet or base,
        "news visualization annotations clarity context general audience",
        "avoid misleading encodings annotate baselines units uncertainty if applicable",
    ]


@dataclass(frozen=True, slots=True)
class HeuristicFusionConfig:
    rrf_k: int = 60
    per_query_raw_multiplier: int = 10
    per_query_guideline_k: int = 40


class HeuristicFusionHybridStrategyV2(RetrievalStrategy):
    """Deterministic multi-query hybrid retrieval (heuristic facets + RRF + label rerank)."""

    id = "heuristic-fusion-hybrid@v2"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        config: HeuristicFusionConfig = HeuristicFusionConfig(),
        default_k: int = 20,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._config = config
        self._default_k = int(default_k)

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

    def _allowed_ids(self, *, hints: ScenarioHints) -> set[str]:
        allowed = set(self._id_to_labels)
        allowed -= self._pipeline_ids
        if not hints.is_election_related:
            allowed -= self._elections_ids
        return allowed

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation = require_text_by_role(request, role="situation")
        hints = infer_hints(situation=situation)
        allowed_ids = self._allowed_ids(hints=hints)

        queries = [q for q in _derive_queries(situation=situation, hints=hints) if q.strip()]
        if not queries:
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )

        raw_k = max(
            30, min(3_000, effective_k * int(self._config.per_query_raw_multiplier))
        )
        per_query_k = max(effective_k, int(self._config.per_query_guideline_k))

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

        fused_scores = rrf_scores(rankings=per_query_rankings, k=self._config.rrf_k)
        adjusted: list[tuple[str, float]] = []
        for gid, score in fused_scores.items():
            labels = self._id_to_labels.get(gid, [])
            adjusted.append(
                (
                    gid,
                    float(score) + chart_bonus(guideline_labels=labels, hints=hints),
                )
            )
        adjusted.sort(key=lambda kv: (-kv[1], kv[0]))
        fused = [gid for gid, _score in adjusted]

        final_ids = fused[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in final_ids if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "heuristic_rrf_fusion",
            "queries": queries,
            "rrf_k": self._config.rrf_k,
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


def _derive_queries_v3(*, title: str | None, situation: str, hints) -> list[str]:
    base = build_search_text_v3(title=title, situation=situation)
    if not base:
        return []

    chart_terms = [
        _CHART_LABEL_TO_QUERY[label]
        for label in sorted(getattr(hints, "chart_labels", []) or [])
        if label in _CHART_LABEL_TO_QUERY
    ]
    chart_facet = ""
    if chart_terms:
        chart_facet = f"{' '.join(chart_terms)} design guidelines"

    return [
        base,
        chart_facet or base,
        "news visualization annotations clarity context general audience",
        "bar chart sorting highlighting annotations axis baseline if applicable",
    ]


class HeuristicFusionHybridStrategyV3(RetrievalStrategy):
    """Deterministic multi-query hybrid retrieval v3 (title-aware hints + domain filtering)."""

    id = "heuristic-fusion-hybrid@v3"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        config: HeuristicFusionConfig = HeuristicFusionConfig(),
        default_k: int = 20,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._config = config
        self._default_k = int(default_k)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        title = (get_text_by_role(request, role="title") or "").strip()
        situation = require_text_by_role(request, role="situation")
        hints = infer_hints_v3(title=title, situation=situation)

        allowed_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if not should_exclude_guideline_v3(guideline_labels=labels, hints=hints)
        }

        queries = [
            q for q in _derive_queries_v3(title=title, situation=situation, hints=hints) if q.strip()
        ]
        if not queries:
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )

        raw_k = max(
            30, min(3_000, effective_k * int(self._config.per_query_raw_multiplier))
        )
        per_query_k = max(effective_k, int(self._config.per_query_guideline_k))

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

        fused_scores = rrf_scores(rankings=per_query_rankings, k=self._config.rrf_k)
        adjusted: list[tuple[str, float]] = []
        for gid, score in fused_scores.items():
            labels = self._id_to_labels.get(gid, [])
            adjusted.append(
                (
                    gid,
                    float(score)
                    + chart_bonus_v3(guideline_labels=labels, hints=hints)
                    + domain_penalty_v3(guideline_labels=labels, hints=hints),
                )
            )
        adjusted.sort(key=lambda kv: (-kv[1], kv[0]))
        fused = [gid for gid, _score in adjusted]

        final_ids = fused[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in final_ids if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "heuristic_rrf_fusion_v3",
            "queries": queries,
            "rrf_k": self._config.rrf_k,
            "filters": {
                "excluded_pipeline": True,
                "hard_excluded_domains": True,
            },
            "hints": {
                "title_used": bool(title),
                "active_domains": sorted(hints.active_domains),
                "chart_labels": sorted(hints.chart_labels),
            },
            "hits": [{"id": gid} for gid in final_ids],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


def _derive_queries_v4(*, title: str | None, situation: str, hints) -> list[str]:
    base = build_search_text_v4(title=title, situation=situation, hints=hints)
    if not base:
        return []

    chart_terms = [
        _CHART_LABEL_TO_QUERY[label]
        for label in sorted(getattr(hints, "chart_labels", []) or [])
        if label in _CHART_LABEL_TO_QUERY
    ]
    chart_facet = ""
    if chart_terms:
        chart_facet = f"{' '.join(chart_terms)} design guidelines"

    task_terms = [
        _TASK_LABEL_TO_QUERY[label]
        for label in sorted(getattr(hints, "task_labels", []) or [])
        if label in _TASK_LABEL_TO_QUERY
    ]
    task_facet = ""
    if task_terms:
        task_facet = f"{' '.join(task_terms)}"

    return [
        base,
        chart_facet or base,
        task_facet or base,
        "news visualization annotations clarity context general audience",
        "avoid misleading encodings annotate baselines units uncertainty if applicable",
    ]


def _derive_queries_v5(*, title: str | None, situation: str, hints) -> list[str]:
    base = build_search_text_v5(title=title, situation=situation, hints=hints)
    if not base:
        return []

    chart_terms = [
        _CHART_LABEL_TO_QUERY[label]
        for label in sorted(getattr(hints, "chart_labels", []) or [])
        if label in _CHART_LABEL_TO_QUERY
    ]
    chart_facet = ""
    if chart_terms:
        chart_facet = f"{' '.join(chart_terms)} design guidelines"

    # Radial magnitude charts are often called polar-area / coxcomb / radial-bar charts.
    if "chart:radial" in (getattr(hints, "chart_labels", []) or []):
        chart_facet = f"{chart_facet} radial bar polar area coxcomb" if chart_facet else "radial bar polar area coxcomb"

    task_terms = [
        _TASK_LABEL_TO_QUERY[label]
        for label in sorted(getattr(hints, "task_labels", []) or [])
        if label in _TASK_LABEL_TO_QUERY
    ]
    task_facet = ""
    if task_terms:
        task_facet = f"{' '.join(task_terms)}"

    return [
        base,
        chart_facet or base,
        task_facet or base,
        "news visualization annotations clarity context general audience",
        "prefer position/length over angle/area for accurate comparisons when possible",
    ]


class HeuristicFusionHybridStrategyV4(RetrievalStrategy):
    """Deterministic multi-query hybrid retrieval v4 (task-aware rerank + title-aware hints)."""

    id = "heuristic-fusion-hybrid@v4"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        config: HeuristicFusionConfig = HeuristicFusionConfig(),
        default_k: int = 20,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._config = config
        self._default_k = int(default_k)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        title = (get_text_by_role(request, role="title") or "").strip()
        situation = require_text_by_role(request, role="situation")
        hints = infer_hints_v4(title=title, situation=situation)

        allowed_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if not should_exclude_guideline_v4(guideline_labels=labels, hints=hints)
        }

        queries = [
            q
            for q in _derive_queries_v4(title=title, situation=situation, hints=hints)
            if q.strip()
        ]
        if not queries:
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )

        raw_k = max(
            30, min(3_000, effective_k * int(self._config.per_query_raw_multiplier))
        )
        per_query_k = max(effective_k, int(self._config.per_query_guideline_k))

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

        fused_scores = rrf_scores(rankings=per_query_rankings, k=self._config.rrf_k)
        adjusted: list[tuple[str, float]] = []
        for gid, score in fused_scores.items():
            labels = self._id_to_labels.get(gid, [])
            adjusted.append(
                (
                    gid,
                    float(score)
                    + chart_bonus_v4(guideline_labels=labels, hints=hints)
                    + task_bonus_v4(guideline_labels=labels, hints=hints)
                    + domain_penalty_v4(guideline_labels=labels, hints=hints),
                )
            )
        adjusted.sort(key=lambda kv: (-kv[1], kv[0]))
        fused = [gid for gid, _score in adjusted]

        final_ids = fused[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in final_ids if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "heuristic_rrf_fusion_v4",
            "queries": queries,
            "rrf_k": self._config.rrf_k,
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
            "hits": [{"id": gid} for gid in final_ids],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)


class HeuristicFusionHybridStrategyV5(RetrievalStrategy):
    """Deterministic multi-query hybrid retrieval v5 (radial disambiguation + precision/multivariate boosting)."""

    id = "heuristic-fusion-hybrid@v5"

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        config: HeuristicFusionConfig = HeuristicFusionConfig(),
        default_k: int = 20,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._config = config
        self._default_k = int(default_k)

        self._id_to_labels = {
            entry.id: list(entry.guideline.labels) for entry in catalog.entries
        }

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import RRFReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        title = (get_text_by_role(request, role="title") or "").strip()
        situation = require_text_by_role(request, role="situation")
        hints = infer_hints_v5(title=title, situation=situation)

        allowed_ids = {
            gid
            for gid, labels in self._id_to_labels.items()
            if not should_exclude_guideline_v5(guideline_labels=labels, hints=hints)
        }

        queries = [
            q
            for q in _derive_queries_v5(title=title, situation=situation, hints=hints)
            if q.strip()
        ]
        if not queries:
            return RetrievalResponse(
                catalog=Catalog(entries=[]),
                meta={
                    **self._searcher.vector_index.meta(),
                    "k": effective_k,
                    "hits": [],
                },
            )

        raw_k = max(
            30, min(3_000, effective_k * int(self._config.per_query_raw_multiplier))
        )
        per_query_k = max(effective_k, int(self._config.per_query_guideline_k))

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

        fused_scores = rrf_scores(rankings=per_query_rankings, k=self._config.rrf_k)
        adjusted: list[tuple[str, float]] = []
        for gid, score in fused_scores.items():
            labels = self._id_to_labels.get(gid, [])
            adjusted.append(
                (
                    gid,
                    float(score)
                    + chart_bonus_v5(guideline_labels=labels, hints=hints)
                    + task_bonus_v5(guideline_labels=labels, hints=hints)
                    + multivariate_bonus_v5(guideline_labels=labels, hints=hints)
                    + precision_bonus_v5(guideline_labels=labels, hints=hints)
                    + domain_penalty_v5(guideline_labels=labels, hints=hints),
                )
            )
        adjusted.sort(key=lambda kv: (-kv[1], kv[0]))
        fused = [gid for gid, _score in adjusted]

        final_ids = fused[:effective_k]

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        ordered_entries = [id_to_entry[gid] for gid in final_ids if gid in id_to_entry]

        meta = {
            **self._searcher.vector_index.meta(),
            "k": effective_k,
            "raw_k": raw_k,
            "score_kind": "heuristic_rrf_fusion_v5",
            "queries": queries,
            "rrf_k": self._config.rrf_k,
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
            "hits": [{"id": gid} for gid in final_ids],
        }

        return RetrievalResponse(catalog=Catalog(entries=ordered_entries), meta=meta)
