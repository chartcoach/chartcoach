from __future__ import annotations

from pathlib import Path

import pytest

from chartcoach import Catalog, CatalogEntry, Guideline


class TinyEmbeddingFunction:
    model_name = "tiny-test-embedding"

    @staticmethod
    def name() -> str:
        return "tiny-test-embedding"

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


def _catalog() -> Catalog:
    return Catalog(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line",),
                )
            )
        ]
    )


def test_chroma_index_and_sql_layer_are_composable(tmp_path: Path) -> None:
    pytest.importorskip("chromadb")
    pytest.importorskip("duckdb")

    from chartcoach.search.chroma import ChromaIndex
    from chartcoach.search.sql import connect_catalog

    catalog = _catalog()
    index = ChromaIndex.create(
        catalog,
        path=tmp_path / "chroma",
        embedding_fn=TinyEmbeddingFunction(),
    )
    conn = connect_catalog(catalog, search=index)

    assert index.documents_df.height == 3
    assert index.collection.count() == 3
    assert index.collection.metadata["catalog_digest"] == catalog.hexdigest()
    assert "documents_digest" in index.collection.metadata
    assert "documents_version" in index.collection.metadata
    assert conn.execute("select count(*) from catalog").fetchone()[0] == 1
    assert conn.execute("select count(*) from embeddings").fetchone()[0] == 3
