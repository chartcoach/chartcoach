from __future__ import annotations

import polars as pl

import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval.strategy import registry


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use accessible colors",
                    description="Ensure color choices are accessible.",
                    labels=["topic:color"],
                    body="## Advice <!-- role: advice -->\nUse colorblind-safe palettes.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axes clearly",
                    description="Axis labels should be clear.",
                    labels=["topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd axis titles.\n",
                ),
                references=[],
            ),
        ]
    )


def test_default_embedding_config_supports_sentence_transformers(monkeypatch) -> None:
    monkeypatch.delenv("CHARTCOACH_EMBEDDING_MODEL", raising=False)
    monkeypatch.delenv("CHARTCOACH_EMBEDDING_PROJECTOR", raising=False)

    cfg = registry._default_embedding_config()
    assert cfg.model
    assert cfg.text_projector_type == "sentence_transformers"
    assert cfg.text_projector_args.get("normalize_embeddings") is True


def test_default_embedding_config_supports_litellm(monkeypatch) -> None:
    monkeypatch.setenv("CHARTCOACH_EMBEDDING_PROJECTOR", "litellm")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "x")

    cfg = registry._default_embedding_config()
    assert cfg.text_projector_type == "litellm"
    assert cfg.text_projector_args.get("api_base") == "http://example.invalid/v1"
    assert cfg.text_projector_args.get("api_key") == "x"
    assert cfg.text_projector_args.get("normalize_embeddings") is True


def test_registry_factories_instantiate_strategies(
    embedding_atlas_cache_dir, monkeypatch, catalog: Catalog
) -> None:
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "x")

    import chartcoach.embedding

    def fake_embed_text(
        df: pl.DataFrame, *, embedding_column: str = "embedding", **_kwargs
    ):
        vectors: list[list[float]] = []
        for text in df["content"].to_list():
            vectors.append([1.0, 0.0] if "color" in str(text).lower() else [0.0, 1.0])
        return pl.concat(
            [
                df.select("id", "role", "content"),
                pl.DataFrame({embedding_column: vectors}),
            ],
            how="horizontal",
        )

    monkeypatch.setattr(chartcoach.embedding, "embed_text", fake_embed_text)

    # Strategies should instantiate without making network calls.
    assert registry.create_bm25_prf_strategy(catalog=catalog).id == "bm25-prf@v1"
    assert (
        registry.create_dense_mmr_strategy(catalog=catalog).id == "dense-mmr@v1"
    )
    assert (
        registry.create_hybrid_rrf_strategy(catalog=catalog).id == "hybrid-rrf@v1"
    )
    assert registry.create_ann_dense_strategy(catalog=catalog).id == "ann-dense@v1"
    assert (
        registry.create_label_gated_ann_strategy(catalog=catalog).id
        == "label-gated-ann@v1"
    )
    assert (
        registry.create_label_first_abstract_strategy(catalog=catalog).id
        == "label-first-abstract@v1"
    )
    assert (
        registry.create_decompose_parallel_strategy(catalog=catalog).id
        == "decompose-parallel@v1"
    )
    assert (
        registry.create_role_aware_sections_strategy(catalog=catalog).id
        == "role-aware-sections@v1"
    )
    assert (
        registry.create_neighborhood_explorer_strategy(catalog=catalog).id
        == "neighborhood-explorer@v1"
    )
    assert (
        registry.create_facet_fusion_hybrid_strategy(catalog=catalog).id
        == "facet-fusion-hybrid@v1"
    )
    assert (
        registry.create_query_fusion_hybrid_strategy(catalog=catalog).id
        == "query-fusion-hybrid@v1"
    )
    assert registry.create_hyde_hybrid_strategy(catalog=catalog).id == "hyde-hybrid@v1"
    assert (
        registry.create_agentic_hybrid_strategy(catalog=catalog).id
        == "agentic-hybrid@v1"
    )


def test_create_lm_uses_defaults_on_invalid_env(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    monkeypatch.setenv("CHARTCOACH_LM_TIMEOUT_SECONDS", "not-a-number")
    monkeypatch.setenv("CHARTCOACH_LM_NUM_RETRIES", "not-a-number")

    lm = registry._create_lm()
    assert lm.num_retries == 6
    assert lm.kwargs.get("timeout") == 120.0


def test_create_default_strategy_registrations_includes_expected_ids() -> None:
    regs = registry.create_default_strategy_registrations()
    ids = {cls.id for cls, _factory in regs}
    assert {
        "bm25-prf@v1",
        "dense-mmr@v1",
        "hybrid-rrf@v1",
        "query-fusion-hybrid@v1",
        "hyde-hybrid@v1",
        "agentic-hybrid@v1",
    } <= ids


def test_shared_abstract_index_uses_cache(monkeypatch, catalog: Catalog) -> None:
    registry._ABSTRACT_INDEX_CACHE.clear()

    monkeypatch.setattr(
        registry, "_default_embedding_config", lambda: registry.EmbeddingConfig(model="fake")
    )

    created: list[object] = []

    def fake_from_catalog(cls, _catalog, **_kwargs):  # noqa: ANN001
        obj = object()
        created.append(obj)
        return obj

    monkeypatch.setattr(
        registry.CatalogVectorIndex, "from_catalog", classmethod(fake_from_catalog)
    )

    idx1 = registry._shared_abstract_index(catalog=catalog)
    idx2 = registry._shared_abstract_index(catalog=catalog)
    assert idx1 is idx2
    assert len(created) == 1
