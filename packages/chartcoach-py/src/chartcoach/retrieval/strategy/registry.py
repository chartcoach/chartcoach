from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from chartcoach.catalog import Catalog
from chartcoach.index import LanceVectorIndexBackend
from chartcoach.retrieval.config import RetrievalRunConfig
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.dspy_models import create_lm
from chartcoach.retrieval.strategy.pipelines import (
    AnnDenseStrategy,
    AgenticHybridStrategy,
    Bm25PrfStrategy,
    DecomposeParallelStrategy,
    DenseMmrStrategy,
    DenseSparseRrfStrategy,
    FacetFusionHybridStrategy,
    HydeHybridStrategy,
    HybridRrfStrategy,
    HybridRrfFacilitySetSelectStrategy,
    HybridRrfLabelSetSelectStrategy,
    LabelFirstAbstractStrategy,
    LabelGatedAnnStrategy,
    MultiReprFusionStrategy,
    NeighborhoodExplorerStrategy,
    QueryFusionHybridStrategy,
    RoleAwareSectionsStrategy,
    SparseSpladeStrategy,
    UtilityRerankHybridStrategy,
)
from chartcoach.retrieval.strategy.pipelines.guideline_status import (
    create_status_scorer,
)
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.pipelines.utility_reranker import (
    create_utility_reranker,
)
from chartcoach.retrieval.strategy.pipelines.vision import ChartVisionModule
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
)

if TYPE_CHECKING:
    import dspy
    from chartcoach.index.sparse import CatalogSparseIndex
else:
    dspy = require_dspy()


class StrategyFactory(Protocol):
    def __call__(
        self, *, catalog: Catalog, run_config: RetrievalRunConfig
    ) -> RetrievalStrategy: ...


StrategyRegistration = tuple[type[RetrievalStrategy], StrategyFactory]


_INDEX_CACHE: dict[tuple[int, str], CatalogVectorIndex] = {}
_ABSTRACT_INDEX_CACHE: dict[tuple[int, str], CatalogVectorIndex] = {}
_SPARSE_INDEX_CACHE: dict[tuple[int, str], CatalogSparseIndex] = {}


def _strategy_lm(run_config: RetrievalRunConfig) -> dspy.LM:
    cfg = run_config.lms.strategy
    return create_lm(
        model=cfg.model,
        timeout_seconds=cfg.timeout_seconds,
        num_retries=cfg.num_retries,
    )


def _strategy_vlm(run_config: RetrievalRunConfig) -> dspy.LM:
    cfg = run_config.lms.vlm
    return create_lm(
        model=cfg.model,
        timeout_seconds=cfg.timeout_seconds,
        num_retries=cfg.num_retries,
    )


def _status_lm(run_config: RetrievalRunConfig) -> dspy.LM:
    cfg = run_config.lms.guideline_status
    return create_lm(
        model=cfg.model,
        timeout_seconds=cfg.timeout_seconds,
        num_retries=cfg.num_retries,
    )


def _vision_module(run_config: RetrievalRunConfig) -> ChartVisionModule | None:
    if not run_config.chart_vision.enabled:
        return None
    return ChartVisionModule(
        vlm=_strategy_vlm(run_config), config=run_config.chart_vision
    )


def _shared_index(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> CatalogVectorIndex:
    config = run_config.embedding
    cache_key = (id(catalog), config.digest())
    cached = _INDEX_CACHE.get(cache_key)
    if cached is not None:
        return cached

    from chartcoach.embedding import (
        GuidelineFieldTextSource,
        GuidelineLabelsTextSource,
        SectionsWithTitleTextSource,
    )

    sources = [
        SectionsWithTitleTextSource(),
        GuidelineFieldTextSource("title"),
        GuidelineFieldTextSource("description"),
        GuidelineLabelsTextSource(),
    ]
    index = CatalogVectorIndex.from_catalog(
        catalog,
        sources=sources,
        config=config,
        index_backend=LanceVectorIndexBackend(),
    )
    _INDEX_CACHE[cache_key] = index
    return index


def _shared_searcher(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> GuidelineSearcher:
    vector_index = _shared_index(catalog=catalog, run_config=run_config)
    return GuidelineSearcher(catalog=catalog, vector_index=vector_index)


def _shared_abstract_index(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> CatalogVectorIndex:
    config = run_config.embedding
    cache_key = (id(catalog), config.digest())
    cached = _ABSTRACT_INDEX_CACHE.get(cache_key)
    if cached is not None:
        return cached

    from chartcoach.embedding import GuidelineAbstractTextSource

    sources = [GuidelineAbstractTextSource()]
    index = CatalogVectorIndex.from_catalog(
        catalog,
        sources=sources,
        config=config,
        index_backend=LanceVectorIndexBackend(),
    )
    _ABSTRACT_INDEX_CACHE[cache_key] = index
    return index


def _shared_abstract_searcher(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> GuidelineSearcher:
    vector_index = _shared_abstract_index(catalog=catalog, run_config=run_config)
    return GuidelineSearcher(catalog=catalog, vector_index=vector_index)


def _shared_sparse_index(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> CatalogSparseIndex:
    from chartcoach.index.sparse import CatalogSparseIndex
    from chartcoach.embedding import GuidelineAbstractTextSource

    config = run_config.sparse_embedding
    cache_key = (id(catalog), config.digest())
    cached = _SPARSE_INDEX_CACHE.get(cache_key)
    if cached is not None:
        return cached

    sources = [GuidelineAbstractTextSource()]
    index = CatalogSparseIndex.from_catalog(catalog, sources=sources, config=config)
    _SPARSE_INDEX_CACHE[cache_key] = index
    return index


def create_bm25_prf_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return Bm25PrfStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_ann_dense_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return AnnDenseStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_dense_mmr_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return DenseMmrStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_hybrid_rrf_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return HybridRrfStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_multirepr_fusion_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    return MultiReprFusionStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        abstract_searcher=_shared_abstract_searcher(
            catalog=catalog, run_config=run_config
        ),
        focus=run_config.focus,
        vision=_vision_module(run_config),
    )


def create_utility_rerank_hybrid_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    utility = create_utility_reranker(
        lm=_strategy_lm(run_config),
        config=run_config.utility_reranker,
    )
    return UtilityRerankHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        utility_reranker=utility,
    )


def create_hybrid_rrf_setselect_label_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return HybridRrfLabelSetSelectStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_hybrid_rrf_setselect_facility_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return HybridRrfFacilitySetSelectStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_label_gated_ann_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return LabelGatedAnnStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_label_first_abstract_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return LabelFirstAbstractStrategy(
        catalog=catalog,
        abstract_searcher=_shared_abstract_searcher(
            catalog=catalog, run_config=run_config
        ),
        lm=lm,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_decompose_parallel_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return DecomposeParallelStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_role_aware_sections_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return RoleAwareSectionsStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_neighborhood_explorer_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return NeighborhoodExplorerStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_facet_fusion_hybrid_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        config=run_config.facet_fusion,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_query_fusion_hybrid_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        config=run_config.query_fusion,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_hyde_hybrid_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return HydeHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_agentic_hybrid_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    lm = _strategy_lm(run_config)
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return AgenticHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        lm=lm,
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_sparse_splade_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return SparseSpladeStrategy(
        catalog=catalog,
        sparse_index=_shared_sparse_index(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
    )


def create_dense_sparse_rrf_strategy(
    *, catalog: Catalog, run_config: RetrievalRunConfig
) -> RetrievalStrategy:
    status_scorer = create_status_scorer(
        lm=_status_lm(run_config),
        config=run_config.status_scorer,
    )
    return DenseSparseRrfStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog, run_config=run_config),
        sparse_index=_shared_sparse_index(catalog=catalog, run_config=run_config),
        focus=run_config.focus,
        vision=_vision_module(run_config),
        status_scorer=status_scorer,
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
