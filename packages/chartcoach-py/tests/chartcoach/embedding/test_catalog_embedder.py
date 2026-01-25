from __future__ import annotations

from pathlib import Path

import numpy as np
import polars as pl
import pytest

from chartcoach.catalog.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.embedding import (
    CatalogEmbedder,
    GuidelineFieldTextSource,
    SectionsTextSource,
)


def _make_catalog(n: int = 2) -> Catalog:
    entries: list[CatalogEntry] = []
    for i in range(n):
        gid = f"g{i}"
        entries.append(
            CatalogEntry(
                guideline=Guideline(
                    id=gid,
                    title=f"Title {i}",
                    description=f"Desc {i}",
                    bibliography=None,
                    labels=["chart:bar"],
                    body="## The Advice <!-- role: advice -->\n\nHello.",
                ),
                references=[],
            )
        )
    return Catalog(entries)


def test_catalog_embedder_text_sources_and_grouping() -> None:
    catalog = _make_catalog(2)
    embedder = CatalogEmbedder(
        catalog,
        text_sources=(
            SectionsTextSource(roles={"advice"}),
            GuidelineFieldTextSource("title"),
        ),
    )
    text_df = embedder.text_df()
    assert set(text_df.select("role").to_series().to_list()) == {"advice", "title"}

    grouped = embedder.group_by_guideline(text_df)
    assert grouped.columns == ["id", "items"]


def test_catalog_embedder_select_join_branch(
    monkeypatch: pytest.MonkeyPatch, embedding_atlas_cache_dir: Path
) -> None:
    import chartcoach.embedding.atlas as atlas

    def fake_projector(
        texts: list[str],
        batch_size: int,
        model: str,
        args: dict[object, object] | None = None,
    ) -> np.ndarray:
        return np.ones((len(texts), 4), dtype=np.float32)

    def fake_umap(
        vectors: np.ndarray, umap_args: dict[str, object]
    ) -> atlas.Projection:
        n = vectors.shape[0]
        proj = np.zeros((n, 2), dtype=np.float32)
        knn_indices = np.zeros((n, 1), dtype=np.int64)
        knn_distances = np.zeros((n, 1), dtype=np.float32)
        return atlas.Projection(
            projection=proj,
            knn_indices=knn_indices,
            knn_distances=knn_distances,
        )

    monkeypatch.setattr(
        atlas, "_project_text_with_sentence_transformers", fake_projector
    )
    monkeypatch.setattr(atlas, "_run_umap", fake_umap)

    catalog = _make_catalog(2)
    embedder = CatalogEmbedder(
        catalog, text_sources=(GuidelineFieldTextSource("title"),)
    )
    projected = embedder.projected_text_df(
        select=[pl.col("guideline").struct.field("description")],
        umap_args={"random_state": 0, "n_neighbors": 2},
    )
    assert "description" in projected.columns


def test_catalog_embedder_empty_sources_branch() -> None:
    catalog = _make_catalog(1)
    embedder = CatalogEmbedder(catalog, text_sources=())
    df = embedder.text_df(sources=[])
    assert df.is_empty()


def test_catalog_embedder_embedded_text_df_executes_embed_text(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.embedding.catalog_embedder as ce

    def fake_embed_text(text_df: pl.DataFrame, **kwargs: object) -> pl.DataFrame:
        return text_df.with_columns(pl.lit([0.0, 1.0]).alias("embedding"))

    monkeypatch.setattr(ce, "embed_text", fake_embed_text)

    catalog = _make_catalog(1)
    embedder = CatalogEmbedder(
        catalog, text_sources=(GuidelineFieldTextSource("title"),)
    )
    embedded = embedder.embedded_text_df()
    assert "embedding" in embedded.columns
