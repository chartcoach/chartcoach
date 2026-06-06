from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest

from chartcoach import Catalog

pytestmark = pytest.mark.search


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


def test_reuse_only_requires_existing_explicit_cache_without_mutation(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    missing_cache_dir = tmp_path / "missing"

    with pytest.raises(FileNotFoundError, match="Cached Chroma directory"):
        ChromaIndex.from_cache(
            sample_catalog,
            cache_dir=missing_cache_dir,
            embedding_fn=TinyEmbeddingFunction(),
        )
    assert not missing_cache_dir.exists()


def test_chroma_cache_requires_explicit_cache_dir(sample_catalog: Catalog) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    with pytest.raises(TypeError, match="cache_dir"):
        cast(Any, ChromaIndex.from_cache)(
            sample_catalog,
            embedding_fn=TinyEmbeddingFunction(),
        )


def test_embedding_identity_includes_config(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    class ConfigurableEmbeddingFunction(TinyEmbeddingFunction):
        def __init__(self, endpoint: str) -> None:
            self.endpoint = endpoint

        def get_config(self) -> dict[str, str]:
            return {"endpoint": self.endpoint, "model": self.model_name}

    first = ChromaIndex.cache_paths(
        sample_catalog,
        cache_dir=tmp_path / "index",
        embedding_fn=cast(Any, ConfigurableEmbeddingFunction("https://example.test/a")),
    )
    second = ChromaIndex.cache_paths(
        sample_catalog,
        cache_dir=tmp_path / "index",
        embedding_fn=cast(Any, ConfigurableEmbeddingFunction("https://example.test/b")),
    )

    assert first.embedding_name != second.embedding_name
    assert first.cache_path != second.cache_path


def test_chroma_index_exposes_native_collection(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    index = ChromaIndex.create(
        sample_catalog,
        path=tmp_path / "chroma",
        embedding_fn=TinyEmbeddingFunction(),
    )

    assert index.documents().height == 6
    assert index.collection.count() == 6
    assert index.collection.metadata["catalog_digest"] == sample_catalog.digest()
    assert "documents_digest" in index.collection.metadata
    assert "documents_version" in index.collection.metadata
    assert index.chroma_path == tmp_path / "chroma"
    assert index.collection_name == "catalog"
    assert index.embedding_name is not None


def test_search_documents_include_content_fingerprints(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search.documents import build_docs_df

    docs = build_docs_df(sample_catalog.guidelines(), sample_catalog.references())
    metadata_by_id = {
        str(row["id"]): row["metadata"]
        for row in docs.select("id", "metadata").to_dicts()
    }

    overview_hash = metadata_by_id["direct-labels---overview"]["content_hash"]
    document_hash = metadata_by_id["direct-labels---document"]["content_hash"]
    advice_hash = metadata_by_id["direct-labels---role---advice"]["content_hash"]

    assert isinstance(overview_hash, str)
    assert isinstance(document_hash, str)
    assert isinstance(advice_hash, str)
    assert overview_hash
    assert len({overview_hash, document_hash, advice_hash}) == 3


def test_search_guidelines_returns_guideline_level_hits(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search import ChromaIndex, search_guidelines

    index = ChromaIndex.create(
        sample_catalog,
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


def test_chroma_collection_remains_directly_queryable(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    index = ChromaIndex.create(
        sample_catalog,
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
    query_metadata = query_result["metadatas"][0][0]
    assert "chart:line" in query_metadata["labels"]
    assert query_metadata["parent_id"] == "direct-labels"
    assert query_metadata["role"] in {"overview", "section.advice"}
    assert get_result["ids"]
    assert get_result["metadatas"][0]["role"] == "overview"


def test_reuse_only_rejects_corrupted_chroma_cache(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    index = ChromaIndex.from_cache(
        sample_catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
        embedding_fn=TinyEmbeddingFunction(),
    )
    first_id = cast(str, index.documents().get_column("id").to_list()[0])
    index.collection.delete(ids=[first_id])

    with pytest.raises(ValueError, match="document count"):
        ChromaIndex.from_cache(
            sample_catalog,
            cache_dir=tmp_path / "index",
            cache_mode="reuse_only",
            embedding_fn=TinyEmbeddingFunction(),
        )


def test_reuse_only_opens_chroma_cache_without_building_documents(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    class GuardedEmbeddingFunction(TinyEmbeddingFunction):
        def __init__(self) -> None:
            self.calls = 0
            self.reject_calls = False

        def __call__(self, input: list[str]) -> list[list[float]]:
            self.calls += 1
            if self.reject_calls:
                raise AssertionError("reuse_only should not embed catalog documents")
            return super().__call__(input)

    embedding_fn = GuardedEmbeddingFunction()
    ChromaIndex.from_cache(
        sample_catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
        embedding_fn=embedding_fn,
    )
    assert embedding_fn.calls > 0
    embedding_fn.calls = 0
    embedding_fn.reject_calls = True

    index = ChromaIndex.from_cache(
        sample_catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_only",
        embedding_fn=embedding_fn,
    )

    assert index.collection.count() == 6
    assert embedding_fn.calls == 0


def test_reuse_or_create_creates_the_explicit_cache_path(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    from chartcoach.search.chroma import ChromaIndex

    cache_dir = tmp_path / "index"

    index = ChromaIndex.from_cache(
        sample_catalog,
        cache_dir=cache_dir,
        cache_mode="reuse_or_create",
        embedding_fn=TinyEmbeddingFunction(),
    )

    assert cache_dir.exists()
    assert index.chroma_path is not None
    assert index.chroma_path.exists()


def test_cached_chroma_paths_are_public(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("chromadb")

    import chartcoach.search.chroma as chroma

    cache_dir = tmp_path / "index"
    paths = chroma.ChromaIndex.cache_paths(
        sample_catalog,
        cache_dir=cache_dir,
        embedding_fn=TinyEmbeddingFunction(),
    )

    assert not cache_dir.exists()
    assert paths.index_root == cache_dir
    assert paths.collection_name == "catalog"
    assert paths.chroma_path.name == "chroma_db"
    assert (
        paths.cache_path.parent
        == cache_dir / sample_catalog.digest() / paths.documents_version
    )


def test_search_guidelines_backfills_unique_guideline_rows(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search import search_guidelines

    class FakeCollection:
        def __init__(self) -> None:
            self.requested: list[dict[str, object]] = []

        def count(self) -> int:
            return 100

        def query(self, **kwargs: object) -> dict[str, object]:
            self.requested.append(dict(kwargs))
            if kwargs["n_results"] == 50:
                return {
                    "ids": [
                        ["direct-labels---overview", "direct-labels---section.advice"]
                    ],
                    "documents": [["Overview text", "Advice text"]],
                    "metadatas": [
                        [
                            {
                                "parent_id": "direct-labels",
                                "role": "overview",
                                "labels": ["chart:line"],
                            },
                            {
                                "parent_id": "direct-labels",
                                "role": "section.advice",
                                "labels": ["chart:line"],
                            },
                        ]
                    ],
                    "distances": [[0.1, 0.2]],
                }
            return {
                "ids": [["direct-labels---overview", "full-axis-bars---overview"]],
                "documents": [["Overview text", "Axis text"]],
                "metadatas": [
                    [
                        {
                            "parent_id": "direct-labels",
                            "role": "overview",
                            "labels": ["chart:line"],
                        },
                        {
                            "parent_id": "full-axis-bars",
                            "role": "overview",
                            "labels": ["chart:bar"],
                        },
                    ]
                ],
                "distances": [[0.1, 0.3]],
            }

    collection = FakeCollection()
    index = SimpleNamespace(catalog=sample_catalog, collection=collection)
    where = {"labels": {"$contains": "chart"}}
    where_document = {"$contains": "axis"}

    result = search_guidelines(
        cast(Any, index),
        "axis labels",
        limit=2,
        candidate_limit=100,
        where=where,
        where_document=where_document,
    )

    assert [row.guideline_id for row in result.rows] == [
        "direct-labels",
        "full-axis-bars",
    ]
    assert [request["n_results"] for request in collection.requested] == [50, 100]
    assert all(request["where"] == where for request in collection.requested)
    assert all(
        request["where_document"] == where_document for request in collection.requested
    )
