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

    def embed_query(self, input: list[str]) -> list[list[float]]:
        return self(input)


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
    assert conn.execute("select count(*) from guidelines").fetchone()[0] == 1
    assert conn.execute("select count(*) from labels").fetchone()[0] == 1
    assert conn.execute("select count(*) from embeddings").fetchone()[0] == 3


def test_search_tools_returns_guideline_level_hits(tmp_path: Path) -> None:
    pytest.importorskip("chromadb")
    pytest.importorskip("duckdb")

    from chartcoach.search.chroma import ChromaIndex
    from chartcoach.search.session import SearchSession

    catalog = Catalog(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line", "component:label"),
                )
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="full-axis-bars",
                    title="Use full value axes for bars",
                    description="Keep bar axes on the honest baseline.",
                    body="## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
                    labels=("chart:bar", "component:axis"),
                )
            ),
        ]
    )
    index = ChromaIndex.create(
        catalog,
        path=tmp_path / "chroma",
        embedding_fn=TinyEmbeddingFunction(),
    )

    with SearchSession(catalog, index) as session:
        result = session.tools.search_guidelines(
            "labels near marks",
            limit=1,
            labels=["component:label"],
        )
        overview_result = session.tools.search_guidelines(
            "direct labels",
            limit=1,
            labels=["component:label"],
            roles=["overview"],
        )

    assert result["row_count"] == 1
    assert result["rows"][0]["id"] == "direct-labels"
    assert "title" in result["rows"][0]
    assert "matched_text" in result["rows"][0]
    assert overview_result["rows"][0]["matched_role"] == "overview"
