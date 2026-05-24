from __future__ import annotations

import inspect
from pathlib import Path
from typing import Any, cast

import pytest

from chartcoach import Catalog, CatalogEntry, Guideline, Section


class TinyEmbeddingFunction:
    model_name = "tiny-test-embedding"

    def __init__(self) -> None:
        pass

    @staticmethod
    def name() -> str:
        return "tiny-test-embedding"

    @staticmethod
    def build_from_config(config: dict[str, str]) -> "TinyEmbeddingFunction":
        TinyEmbeddingFunction.validate_config(config)
        return TinyEmbeddingFunction()

    def get_config(self) -> dict[str, str]:
        return {"model_name": self.model_name}

    @staticmethod
    def validate_config(config: dict[str, str]) -> None:
        if config and config != {"model_name": TinyEmbeddingFunction.model_name}:
            raise ValueError("Unexpected TinyEmbeddingFunction config.")

    def is_legacy(self) -> bool:
        return False

    def default_space(self) -> str:
        return "l2"

    def supported_spaces(self) -> list[str]:
        return ["l2"]

    def __call__(self, input: list[str]) -> list[list[float]]:
        vectors: list[list[float]] = []
        for text in input:
            vectors.append(
                [
                    float(len(text) % 11),
                    float(sum(ord(char) for char in text) % 13),
                    float(text.count("label")),
                ]
            )
        return vectors

    def embed_query(self, input: list[str]) -> list[list[float]]:
        return self(input)


def _catalog() -> Catalog:
    return Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line",),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Place labels near marks.",
                        ),
                    ),
                )
            )
        ]
    )


def test_search_cache_defaults_are_read_only() -> None:
    from chartcoach.search.chroma import ChromaIndex

    assert (
        inspect.signature(ChromaIndex.from_cache).parameters["cache_dir"].default
        is inspect.Parameter.empty
    )
    assert inspect.signature(ChromaIndex.from_cache).parameters["cache_mode"].default == (
        "reuse_only"
    )


def test_embedding_identity_includes_config() -> None:
    from chartcoach.search.chroma import _embedding_name

    class ConfigurableEmbeddingFunction(TinyEmbeddingFunction):
        def __init__(self, endpoint: str) -> None:
            self.endpoint = endpoint

        def get_config(self) -> dict[str, str]:
            return {"endpoint": self.endpoint, "model": self.model_name}

    first = cast(Any, ConfigurableEmbeddingFunction("https://example.test/a"))
    second = cast(Any, ConfigurableEmbeddingFunction("https://example.test/b"))

    assert _embedding_name(first) != _embedding_name(second)


def test_chroma_index_exposes_native_collection(tmp_path: Path) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    catalog = _catalog()
    index = ChromaIndex.create(
        catalog,
        path=tmp_path / "chroma",
        embedding_fn=TinyEmbeddingFunction(),
    )

    assert index.documents().height == 3
    assert index.collection.count() == 3
    assert index.collection.metadata["catalog_digest"] == catalog.digest()
    assert "documents_digest" in index.collection.metadata
    assert "documents_version" in index.collection.metadata
    assert index.chroma_path == tmp_path / "chroma"
    assert index.collection_name == "catalog"
    assert index.embedding_name is not None


def test_search_guidelines_returns_guideline_level_hits(tmp_path: Path) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search import ChromaIndex, search_guidelines

    catalog = Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line", "component:label"),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Place labels near marks.",
                        ),
                    ),
                )
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="full-axis-bars",
                    title="Use full value axes for bars",
                    description="Keep bar axes on the honest baseline.",
                    body="## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
                    labels=("chart:bar", "component:axis"),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Start bar value axes at zero.",
                        ),
                    ),
                )
            ),
        ]
    )
    index = ChromaIndex.create(
        catalog,
        path=tmp_path / "chroma",
        embedding_fn=TinyEmbeddingFunction(),
    )

    result = search_guidelines(
        index,
        "labels near marks",
        limit=1,
        where={"labels": {"$contains": "component:label"}},
    )
    overview_result = search_guidelines(
        index,
        "direct labels",
        limit=1,
        where={
            "$and": [
                {"labels": {"$contains": "component:label"}},
                {"role": "overview"},
            ]
        },
    )

    assert result.row_count == 1
    assert result.rows[0].guideline_id == "direct-labels"
    assert result.rows[0].title == "Use direct labels"
    assert result.rows[0].document
    assert result.to_dict()["rows"][0]["id"] == "direct-labels"
    assert overview_result.rows[0].role == "overview"


def test_chroma_collection_remains_directly_queryable(tmp_path: Path) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    catalog = _catalog()
    index = ChromaIndex.create(
        catalog,
        path=tmp_path / "chroma",
        embedding_fn=TinyEmbeddingFunction(),
    )

    query_result = index.collection.query(
        query_texts=["direct labels"],
        n_results=1,
        where={"labels": {"$contains": "chart:line"}},
        include=["documents", "metadatas", "distances"],
    )
    get_result = index.collection.get(
        where={"role": "overview"},
        include=["documents", "metadatas"],
        limit=1,
    )

    assert query_result["ids"][0]
    assert "chart:line" in query_result["metadatas"][0][0]["labels"]
    assert set(query_result["metadatas"][0][0]) == {
        "content_hash",
        "labels",
        "parent_id",
        "role",
    }
    assert get_result["ids"]
    assert get_result["metadatas"][0]["role"] == "overview"


def test_reuse_only_rejects_corrupted_chroma_cache(tmp_path: Path) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    catalog = _catalog()
    index = ChromaIndex.from_cache(
        catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
        embedding_fn=TinyEmbeddingFunction(),
    )
    first_id = cast(str, index.documents().get_column("id").to_list()[0])
    index.collection.delete(ids=[first_id])

    with pytest.raises(ValueError, match="document count"):
        ChromaIndex.from_cache(
            catalog,
            cache_dir=tmp_path / "index",
            cache_mode="reuse_only",
            embedding_fn=TinyEmbeddingFunction(),
        )


def test_reuse_only_opens_chroma_cache_without_building_documents(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pytest.importorskip("chromadb")

    import chartcoach.search.chroma as chroma

    catalog = _catalog()
    chroma.ChromaIndex.from_cache(
        catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
        embedding_fn=TinyEmbeddingFunction(),
    )
    monkeypatch.setattr(
        chroma,
        "_build_documents",
        lambda _catalog: (_ for _ in ()).throw(
            AssertionError("reuse_only should not build Chroma documents")
        ),
    )

    index = chroma.ChromaIndex.from_cache(
        catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_only",
        embedding_fn=TinyEmbeddingFunction(),
    )

    assert index.collection.count() == 3


def test_cached_chroma_paths_are_public(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    monkeypatch.setattr(
        chroma,
        "_resolve_embedding",
        lambda _embedding_fn: chroma._ResolvedEmbedding(
            embedding_fn=object(),
            embedding_name="tiny/test",
        ),
    )
    monkeypatch.setattr(
        chroma,
        "_build_documents",
        lambda _catalog: (_ for _ in ()).throw(
            AssertionError("cache_paths should not build index documents")
        ),
    )
    catalog = _catalog()
    paths = chroma.ChromaIndex.cache_paths(
        catalog,
        cache_dir=tmp_path / "index",
    )

    assert paths.index_root == tmp_path / "index"
    assert paths.collection_name == "catalog"
    assert paths.documents_version == chroma._documents_version()
    assert paths.chroma_path.name == "chroma_db"
    assert (
        paths.cache_path.parent
        == tmp_path / "index" / catalog.digest() / paths.documents_version
    )
