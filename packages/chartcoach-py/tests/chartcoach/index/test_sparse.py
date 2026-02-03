from __future__ import annotations

import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.embedding import GuidelineFieldTextSource
from chartcoach.index.sparse import (
    CatalogSparseIndex,
    SparseEmbeddingConfig,
    create_sparse_embedder,
)


class _FakeSparseEmbedder:
    def embed(self, texts):  # noqa: ANN001
        out = []
        for text in texts:
            lowered = str(text).lower()
            if "color" in lowered:
                out.append(([1], [1.0]))
            elif "axis" in lowered:
                out.append(([2], [1.0]))
            else:
                out.append(([0], [1.0]))
        return out


class _ConstantSparseEmbedder:
    def embed(self, texts):  # noqa: ANN001
        return [([0], [1.0]) for _ in texts]


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use accessible colors",
                    description="",
                    labels=["topic:color"],
                    body="## Advice <!-- role: advice -->\nUse colorblind-safe palettes.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axis titles",
                    description="",
                    labels=["topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd axis titles.\n",
                ),
                references=[],
            ),
        ]
    )


def test_sparse_embedding_config_digest_changes() -> None:
    cfg1 = SparseEmbeddingConfig()
    cfg2 = SparseEmbeddingConfig()
    assert cfg1.digest() == cfg2.digest()

    cfg3 = SparseEmbeddingConfig(model="other")
    assert cfg1.digest() != cfg3.digest()


def test_create_sparse_embedder_supports_transformers_via_injection(
    monkeypatch,
) -> None:
    import chartcoach.index.sparse as sparse_mod

    class DummyEmbedder:
        def __init__(self, *, config: SparseEmbeddingConfig) -> None:
            self.config = config

        def embed(self, texts):  # noqa: ANN001
            return [([], []) for _ in texts]

    monkeypatch.setattr(sparse_mod, "_TransformersSpladeEmbedder", DummyEmbedder)
    embedder = create_sparse_embedder(SparseEmbeddingConfig())
    assert isinstance(embedder, DummyEmbedder)

    with pytest.raises(ValueError, match="Unknown sparse embedding provider"):
        sparse_mod.create_sparse_embedder(
            SparseEmbeddingConfig(  # type: ignore[arg-type]
                provider="nope",
                model="x",
                max_length=16,
                top_k_terms=8,
            )
        )


def test_catalog_sparse_index_empty_catalog_skips_sparse_deps() -> None:
    empty = Catalog(entries=[])
    index = CatalogSparseIndex.from_catalog(
        empty,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=None,
    )
    assert index.search_sparse("anything", k=5).is_empty()
    assert index.embedder.embed(["q"]) == [([], [])]


def test_catalog_sparse_index_search_filters_and_meta(catalog: Catalog) -> None:
    config = SparseEmbeddingConfig()
    index = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=config,
        embedder=_FakeSparseEmbedder(),
    )

    hits = index.search_sparse("color", k=5)
    assert hits.get_column("id").to_list() == ["g1"]

    assert index.search_sparse("color", k=5, roles={"advice"}).is_empty()
    hits = index.search_sparse("color", k=5, roles={"title"})
    assert hits.get_column("id").to_list() == ["g1"]

    assert index.search_sparse("axis", k=5, ids={"g1"}).is_empty()
    hits = index.search_sparse("axis", k=5, ids={"g2"})
    assert hits.get_column("id").to_list() == ["g2"]

    assert index.search_sparse("", k=5).is_empty()
    with pytest.raises(ValueError, match="k must be positive"):
        index.search_sparse("color", k=0)

    meta = index.meta()
    assert meta["provider"] == config.provider
    assert meta["model"] == config.model
    assert meta["digest"]
    assert meta["text_sources"]


def test_catalog_sparse_index_tiebreaks_by_id() -> None:
    catalog = Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="A",
                    description="",
                    labels=[],
                    body="## Advice <!-- role: advice -->\nA\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="B",
                    description="",
                    labels=[],
                    body="## Advice <!-- role: advice -->\nB\n",
                ),
                references=[],
            ),
        ]
    )
    index = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=_ConstantSparseEmbedder(),
    )
    hits = index.search_sparse("query", k=5)
    assert hits.get_column("id").to_list() == ["g1", "g2"]


def test_catalog_sparse_index_covers_edge_branches(catalog: Catalog) -> None:
    import polars as pl

    from chartcoach.embedding import (
        GuidelineAbstractTextSource,
        GuidelineLabelsTextSource,
        SectionsTextSource,
    )

    class ZeroWeightEmbedder:
        def embed(self, texts):  # noqa: ANN001
            return [([0, 1], [0.0, 1.0]) for _ in texts]

    # weight==0 is ignored when building postings
    index = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=ZeroWeightEmbedder(),
    )
    assert 0 not in index.postings

    # Cover text source descriptions.
    for source in (
        SectionsTextSource(),
        GuidelineAbstractTextSource(),
        GuidelineLabelsTextSource(),
    ):
        idx = CatalogSparseIndex.from_catalog(
            catalog,
            sources=[source],
            config=SparseEmbeddingConfig(),
            embedder=_ConstantSparseEmbedder(),
        )
        assert idx.meta()["text_sources"]

    class DummySource:
        def text_df(self, _catalog):  # noqa: ANN001
            return pl.DataFrame({"id": ["g1"], "role": ["dummy"], "content": ["x"]})

    idx = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[DummySource()],  # type: ignore[arg-type]
        config=SparseEmbeddingConfig(),
        embedder=_ConstantSparseEmbedder(),
    )
    assert idx.meta()["text_sources"][0]["type"] == "DummySource"

    class EmptyQueryEmbedder:
        def embed(self, texts):  # noqa: ANN001
            return [([], []) for _ in texts]

    # q_indices empty -> early empty return.
    idx = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=EmptyQueryEmbedder(),
    )
    assert idx.search_sparse("query", k=5).is_empty()

    class MissingPostingEmbedder:
        def embed(self, texts):  # noqa: ANN001
            out = []
            for text in texts:
                if "query" in str(text).lower():
                    out.append(([999], [1.0]))
                else:
                    out.append(([0], [1.0]))
            return out

    # postings missing -> safe continue.
    idx = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=MissingPostingEmbedder(),
    )
    assert idx.search_sparse("query", k=5).is_empty()

    class NegativeQueryEmbedder:
        def embed(self, texts):  # noqa: ANN001
            out = []
            for text in texts:
                if "query" in str(text).lower():
                    out.append(([0], [-1.0]))
                else:
                    out.append(([0], [1.0]))
            return out

    # score<=0 is filtered.
    idx = CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=NegativeQueryEmbedder(),
    )
    assert idx.search_sparse("query", k=5).is_empty()
