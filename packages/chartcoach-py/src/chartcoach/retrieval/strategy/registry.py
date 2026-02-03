from __future__ import annotations

import os
from typing import TYPE_CHECKING, Protocol

from chartcoach.catalog import Catalog
from chartcoach.env import load_env
from chartcoach.index import LanceVectorIndexBackend
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.dspy_models import create_strategy_lm
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
from chartcoach.retrieval.strategy.pipelines.facet_fusion import FacetFusionConfig
from chartcoach.retrieval.strategy.pipelines.query_fusion import QueryFusionConfig
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
)

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class StrategyFactory(Protocol):
    def __call__(self, *, catalog: Catalog) -> RetrievalStrategy: ...


StrategyRegistration = tuple[type[RetrievalStrategy], StrategyFactory]


_INDEX_CACHE: dict[tuple[int, str], CatalogVectorIndex] = {}
_ABSTRACT_INDEX_CACHE: dict[tuple[int, str], CatalogVectorIndex] = {}
_SPARSE_INDEX_CACHE: dict[tuple[int, str], object] = {}


def _create_lm() -> dspy.LM:
    return create_strategy_lm()


def _default_embedding_config() -> EmbeddingConfig:
    """Resolve an embedding configuration (secrets excluded from digests)."""

    model = os.environ.get("CHARTCOACH_EMBEDDING_MODEL") or "BAAI/bge-small-en-v1.5"
    projector = (
        os.environ.get("CHARTCOACH_EMBEDDING_PROJECTOR") or "sentence_transformers"
    )

    args: dict[str, object] = {"normalize_embeddings": True}
    if projector == "litellm":
        openai = load_env().openai.require()
        # `embedding_atlas` delegates provider calls to LiteLLM.
        args = {
            "api_base": openai.api_base,
            "api_key": openai.api_key,
            "sync": True,
            "normalize_embeddings": True,
        }

    return EmbeddingConfig(
        model=model,
        text_projector_type=projector,  # type: ignore[arg-type]
        text_projector_args=args,
    )


def _shared_index(*, catalog: Catalog) -> CatalogVectorIndex:
    config = _default_embedding_config()
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


def _shared_searcher(*, catalog: Catalog) -> GuidelineSearcher:
    vector_index = _shared_index(catalog=catalog)
    return GuidelineSearcher(catalog=catalog, vector_index=vector_index)


def _shared_abstract_index(*, catalog: Catalog) -> CatalogVectorIndex:
    config = _default_embedding_config()
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


def _shared_abstract_searcher(*, catalog: Catalog) -> GuidelineSearcher:
    vector_index = _shared_abstract_index(catalog=catalog)
    return GuidelineSearcher(catalog=catalog, vector_index=vector_index)


def _default_sparse_embedding_config():
    from chartcoach.index.sparse import SparseEmbeddingConfig

    model = (
        os.environ.get("CHARTCOACH_SPARSE_EMBEDDING_MODEL")
        or os.environ.get("CHARTCOACH_SPARSE_MODEL")
        or "prithivida/Splade_PP_en_v1"
    )
    return SparseEmbeddingConfig(model=model)


def _shared_sparse_index(*, catalog: Catalog):
    from chartcoach.index.sparse import CatalogSparseIndex
    from chartcoach.embedding import GuidelineAbstractTextSource

    config = _default_sparse_embedding_config()
    cache_key = (id(catalog), config.digest())
    cached = _SPARSE_INDEX_CACHE.get(cache_key)
    if cached is not None:
        return cached  # type: ignore[return-value]

    sources = [GuidelineAbstractTextSource()]
    index = CatalogSparseIndex.from_catalog(catalog, sources=sources, config=config)
    _SPARSE_INDEX_CACHE[cache_key] = index
    return index


def create_bm25_prf_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return Bm25PrfStrategy(catalog=catalog, searcher=_shared_searcher(catalog=catalog))


def create_ann_dense_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return AnnDenseStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_dense_mmr_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return DenseMmrStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_hybrid_rrf_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return HybridRrfStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_multirepr_fusion_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return MultiReprFusionStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        abstract_searcher=_shared_abstract_searcher(catalog=catalog),
    )


def create_utility_rerank_hybrid_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return UtilityRerankHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_hybrid_rrf_setselect_label_strategy(
    *, catalog: Catalog
) -> RetrievalStrategy:
    return HybridRrfLabelSetSelectStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_hybrid_rrf_setselect_facility_strategy(
    *, catalog: Catalog
) -> RetrievalStrategy:
    return HybridRrfFacilitySetSelectStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_label_gated_ann_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    return LabelGatedAnnStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
    )


def create_label_first_abstract_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    return LabelFirstAbstractStrategy(
        catalog=catalog,
        abstract_searcher=_shared_abstract_searcher(catalog=catalog),
        lm=lm,
    )


def create_decompose_parallel_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    return DecomposeParallelStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
    )


def create_role_aware_sections_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    return RoleAwareSectionsStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
    )


def create_neighborhood_explorer_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return NeighborhoodExplorerStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
    )


def create_facet_fusion_hybrid_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    config = FacetFusionConfig(
        n_queries=int(os.environ.get("CHARTCOACH_FACET_FUSION_N_QUERIES") or "5"),
        rrf_k=int(os.environ.get("CHARTCOACH_FACET_FUSION_RRF_K") or "60"),
        cross_encoder_model=os.environ.get(
            "CHARTCOACH_FACET_FUSION_CROSS_ENCODER_MODEL"
        )
        or "cross-encoder/ms-marco-TinyBERT-L-6",
        cross_encoder_candidate_limit=int(
            os.environ.get("CHARTCOACH_FACET_FUSION_XENC_CANDIDATES") or "80"
        ),
    )
    return FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
        config=config,
    )


def create_query_fusion_hybrid_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    # Query fusion is strongest with a cross-encoder rerank. Keep it configurable.
    config = QueryFusionConfig(
        n_queries=int(os.environ.get("CHARTCOACH_FUSION_N_QUERIES") or "4"),
        rrf_k=int(os.environ.get("CHARTCOACH_FUSION_RRF_K") or "60"),
        cross_encoder_model=os.environ.get("CHARTCOACH_FUSION_CROSS_ENCODER_MODEL")
        or "cross-encoder/ms-marco-TinyBERT-L-6",
        cross_encoder_candidate_limit=int(
            os.environ.get("CHARTCOACH_FUSION_XENC_CANDIDATES") or "80"
        ),
    )
    return QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
        config=config,
    )


def create_hyde_hybrid_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    return HydeHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
    )


def create_agentic_hybrid_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    lm = _create_lm()
    return AgenticHybridStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        lm=lm,
    )


def create_sparse_splade_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return SparseSpladeStrategy(
        catalog=catalog,
        sparse_index=_shared_sparse_index(catalog=catalog),
    )


def create_dense_sparse_rrf_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return DenseSparseRrfStrategy(
        catalog=catalog,
        searcher=_shared_searcher(catalog=catalog),
        sparse_index=_shared_sparse_index(catalog=catalog),
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
