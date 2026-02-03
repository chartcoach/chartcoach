from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture()
def embedding_atlas_cache_dir(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    import embedding_atlas.utils

    cache_root = tmp_path / "embedding_atlas"
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setattr(
        embedding_atlas.utils,
        "user_cache_path",
        lambda *args, **kwargs: cache_root,
    )
    return cache_root


@pytest.fixture()
def retrieval_run_config():
    """Deterministic retrieval run config for tests (avoid env-dependent defaults)."""

    from chartcoach.index.sparse import SparseEmbeddingConfig
    from chartcoach.retrieval.config import (
        LmEndpointConfig,
        LmModelsConfig,
        RetrievalRunConfig,
    )
    from chartcoach.retrieval.strategy.pipelines.facet_fusion import FacetFusionConfig
    from chartcoach.retrieval.strategy.pipelines.focus import FocusConfig
    from chartcoach.retrieval.strategy.pipelines.guideline_status import (
        StatusScorerConfig,
    )
    from chartcoach.retrieval.strategy.pipelines.query_fusion import QueryFusionConfig
    from chartcoach.retrieval.strategy.pipelines.utility_reranker import (
        UtilityRerankerConfig,
    )
    from chartcoach.retrieval.strategy.pipelines.vision import ChartVisionConfig
    from chartcoach.retrieval.strategy.vector_index import EmbeddingConfig

    return RetrievalRunConfig(
        embedding=EmbeddingConfig(
            model="test-embedding",
            text_projector_type="sentence_transformers",
            text_projector_args={"normalize_embeddings": True},
        ),
        sparse_embedding=SparseEmbeddingConfig(model="test-sparse"),
        lms=LmModelsConfig(
            strategy=LmEndpointConfig(model="gpt-5.1"),
            vlm=LmEndpointConfig(model="gpt-5.2"),
            guideline_status=LmEndpointConfig(model="gpt-5.1"),
        ),
        focus=FocusConfig(),
        chart_vision=ChartVisionConfig(enabled=False),
        status_scorer=StatusScorerConfig(),
        query_fusion=QueryFusionConfig(),
        facet_fusion=FacetFusionConfig(),
        utility_reranker=UtilityRerankerConfig(),
        strategy_timeout_seconds=None,
    )
