from __future__ import annotations

import os
from typing import TYPE_CHECKING, Protocol

from chartcoach.catalog import Catalog
from chartcoach.env import load_env
from chartcoach.index import LanceVectorIndexBackend
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.pipelines import (
    AgenticHybridStrategy,
    Bm25PrfStrategy,
    DenseMmrStrategy,
    HydeHybridStrategy,
    HybridRrfStrategy,
    QueryFusionHybridStrategy,
)
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


DEFAULT_STRATEGY_LM_MODEL = os.environ.get("CHARTCOACH_STRATEGY_LM_MODEL") or "gpt-5.1"


_INDEX_CACHE: dict[tuple[int, str], CatalogVectorIndex] = {}


def _create_lm() -> dspy.LM:
    openai = load_env().openai.require()
    model = DEFAULT_STRATEGY_LM_MODEL
    # DSPy 3.x relies on provider-prefixed model names (e.g. `openai/gpt-4o-mini`).
    if "/" not in model and not model.startswith("ft:"):
        model = f"openai/{model}"

    # LiteLLM defaults can be too aggressive for local gateways and tool-using
    # programs. Keep this configurable and conservative by default.
    try:
        timeout = float(os.environ.get("CHARTCOACH_LM_TIMEOUT_SECONDS") or "120")
    except ValueError:
        timeout = 120.0
    try:
        retries = int(os.environ.get("CHARTCOACH_LM_NUM_RETRIES") or "6")
    except ValueError:
        retries = 6

    return dspy.LM(
        model=model,
        api_base=openai.api_base,
        api_key=openai.api_key,
        num_retries=max(0, retries),
        timeout=max(1.0, timeout),
    )


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
        SectionsTextSource,
    )

    sources = [
        SectionsTextSource(),
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


def create_bm25_prf_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    return Bm25PrfStrategy(
        catalog=catalog, searcher=_shared_searcher(catalog=catalog)
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


def create_default_strategy_registrations() -> list[StrategyRegistration]:
    return [
        (Bm25PrfStrategy, create_bm25_prf_strategy),
        (DenseMmrStrategy, create_dense_mmr_strategy),
        (HybridRrfStrategy, create_hybrid_rrf_strategy),
        (QueryFusionHybridStrategy, create_query_fusion_hybrid_strategy),
        (HydeHybridStrategy, create_hyde_hybrid_strategy),
        (AgenticHybridStrategy, create_agentic_hybrid_strategy),
    ]
