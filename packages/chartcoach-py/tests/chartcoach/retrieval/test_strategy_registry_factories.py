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


def test_registry_factories_instantiate_strategies(
    embedding_atlas_cache_dir, monkeypatch, catalog: Catalog, retrieval_run_config
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

    from chartcoach.index.sparse import CatalogSparseIndex, SparseEmbeddingConfig
    from chartcoach.embedding import GuidelineFieldTextSource

    class DummySparseEmbedder:
        def embed(self, texts):  # noqa: ANN001
            return [([0], [1.0]) for _ in texts]

    fake_sparse = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(model="fake", max_length=16, top_k_terms=8),
        embedder=DummySparseEmbedder(),
    )
    monkeypatch.setattr(
        registry,
        "_shared_sparse_index",
        lambda *, catalog, run_config: fake_sparse,  # noqa: ARG005
    )

    factories = registry.create_default_strategy_registrations()
    for strategy_cls, factory in factories:
        strategy = factory(catalog=catalog, run_config=retrieval_run_config)
        assert strategy.id == strategy_cls.id


def test_create_default_strategy_registrations_includes_expected_ids() -> None:
    regs = registry.create_default_strategy_registrations()
    ids = {cls.id for cls, _factory in regs}
    assert {
        "bm25-prf@v1",
        "dense-mmr@v1",
        "hybrid-rrf@v1",
        "multirepr-rrf@v1",
        "utility-rerank-hybrid@v1",
        "hybrid-rrf-setselect-label@v1",
        "hybrid-rrf-setselect-facility@v1",
        "query-fusion-hybrid@v1",
        "hyde-hybrid@v1",
        "agentic-hybrid@v1",
        "dense-sparse-rrf@v1",
        "sparse-splade@v1",
    } <= ids
