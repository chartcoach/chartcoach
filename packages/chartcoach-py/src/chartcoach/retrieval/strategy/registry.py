from __future__ import annotations

from typing import Protocol

from chartcoach.retrieval.runtime import StrategyRuntime
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.pipelines import (
    AnnDenseStrategy,
    AgenticHybridStrategy,
    Bm25PrfStrategy,
    DecomposeParallelStrategy,
    DenseMmrStrategy,
    DenseSparseRrfStrategy,
    FacetFusionHybridStrategy,
    HydeHybridStrategy,
    HybridRrfFacilitySetSelectStrategy,
    HybridRrfLabelSetSelectStrategy,
    HybridRrfStrategy,
    LabelFirstAbstractStrategy,
    LabelGatedAnnStrategy,
    MultiReprFusionStrategy,
    NeighborhoodExplorerStrategy,
    QueryFusionHybridStrategy,
    RoleAwareSectionsStrategy,
    SparseSpladeStrategy,
    UtilityRerankHybridStrategy,
)
from chartcoach.retrieval.strategy.pipelines.utility_reranker import (
    create_utility_reranker,
)


class StrategyFactory(Protocol):
    def __call__(self, *, runtime: StrategyRuntime) -> RetrievalStrategy: ...


StrategyRegistration = tuple[type[RetrievalStrategy], StrategyFactory]


def create_bm25_prf_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return Bm25PrfStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_ann_dense_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return AnnDenseStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_dense_mmr_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return DenseMmrStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_hybrid_rrf_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return HybridRrfStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_multirepr_fusion_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return MultiReprFusionStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        abstract_searcher=runtime.abstract_searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
    )


def create_utility_rerank_hybrid_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    utility = create_utility_reranker(
        lm=runtime.new_strategy_lm(),
        config=cfg.utility_reranker,
    )
    return UtilityRerankHybridStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        utility_reranker=utility,
    )


def create_hybrid_rrf_setselect_label_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return HybridRrfLabelSetSelectStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_hybrid_rrf_setselect_facility_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return HybridRrfFacilitySetSelectStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_label_gated_ann_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return LabelGatedAnnStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_label_first_abstract_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return LabelFirstAbstractStrategy(
        catalog=runtime.catalog,
        abstract_searcher=runtime.abstract_searcher(),
        lm=runtime.new_strategy_lm(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_decompose_parallel_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return DecomposeParallelStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_role_aware_sections_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return RoleAwareSectionsStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_neighborhood_explorer_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return NeighborhoodExplorerStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_facet_fusion_hybrid_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return FacetFusionHybridStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        config=cfg.facet_fusion,
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_query_fusion_hybrid_strategy(
    *, runtime: StrategyRuntime
) -> RetrievalStrategy:
    cfg = runtime.run_config
    return QueryFusionHybridStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        config=cfg.query_fusion,
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_hyde_hybrid_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return HydeHybridStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_agentic_hybrid_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return AgenticHybridStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        lm=runtime.new_strategy_lm(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_sparse_splade_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return SparseSpladeStrategy(
        catalog=runtime.catalog,
        sparse_index=runtime.sparse_index(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_dense_sparse_rrf_strategy(*, runtime: StrategyRuntime) -> RetrievalStrategy:
    cfg = runtime.run_config
    return DenseSparseRrfStrategy(
        catalog=runtime.catalog,
        searcher=runtime.searcher(),
        sparse_index=runtime.sparse_index(),
        focus=cfg.focus,
        vision=runtime.vision(),
        status_scorer=runtime.maybe_status_scorer(),
    )


def create_default_strategy_registrations() -> list[StrategyRegistration]:
    return [
        (Bm25PrfStrategy, create_bm25_prf_strategy),
        (AnnDenseStrategy, create_ann_dense_strategy),
        (DenseMmrStrategy, create_dense_mmr_strategy),
        (DenseSparseRrfStrategy, create_dense_sparse_rrf_strategy),
        (HybridRrfStrategy, create_hybrid_rrf_strategy),
        (MultiReprFusionStrategy, create_multirepr_fusion_strategy),
        (UtilityRerankHybridStrategy, create_utility_rerank_hybrid_strategy),
        (HybridRrfLabelSetSelectStrategy, create_hybrid_rrf_setselect_label_strategy),
        (
            HybridRrfFacilitySetSelectStrategy,
            create_hybrid_rrf_setselect_facility_strategy,
        ),
        (SparseSpladeStrategy, create_sparse_splade_strategy),
        (LabelGatedAnnStrategy, create_label_gated_ann_strategy),
        (LabelFirstAbstractStrategy, create_label_first_abstract_strategy),
        (DecomposeParallelStrategy, create_decompose_parallel_strategy),
        (RoleAwareSectionsStrategy, create_role_aware_sections_strategy),
        (NeighborhoodExplorerStrategy, create_neighborhood_explorer_strategy),
        (FacetFusionHybridStrategy, create_facet_fusion_hybrid_strategy),
        (QueryFusionHybridStrategy, create_query_fusion_hybrid_strategy),
        (HydeHybridStrategy, create_hyde_hybrid_strategy),
        (AgenticHybridStrategy, create_agentic_hybrid_strategy),
    ]
