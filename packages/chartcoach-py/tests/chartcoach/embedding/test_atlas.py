from __future__ import annotations

from pathlib import Path

import numpy as np
import polars as pl
import pytest

from chartcoach.embedding.atlas import embed_text, project_embedded_text
from chartcoach.embedding.vectors import vector_matrix


def test_embed_text_default_model_caches(embedding_atlas_cache_dir: Path) -> None:
    text_df = pl.DataFrame(
        {
            "id": [str(i) for i in range(6)],
            "role": ["advice"] * 6,
            "content": [f"text {i}" for i in range(6)],
        }
    )
    embedded1 = embed_text(text_df)
    embedded2 = embed_text(text_df)

    v1 = vector_matrix(embedded1.get_column("embedding"))
    v2 = vector_matrix(embedded2.get_column("embedding"))
    assert v1.shape[0] == 6
    assert v1.shape == v2.shape
    assert np.allclose(v1, v2)


def test_embed_text_litellm_branch_is_pluggable(
    monkeypatch: pytest.MonkeyPatch, embedding_atlas_cache_dir: Path
) -> None:
    import chartcoach.embedding.atlas as atlas

    def fake_projector(
        texts: list[str],
        batch_size: int,
        model: str,
        args: dict[object, object] | None = None,
    ) -> np.ndarray:
        return np.zeros((len(texts), 3), dtype=np.float32)

    monkeypatch.setattr(atlas, "_project_text_with_litellm", fake_projector)

    text_df = pl.DataFrame({"id": ["a"], "role": ["title"], "content": ["hello"]})
    embedded = embed_text(text_df, text_projector_type="litellm")
    assert vector_matrix(embedded.get_column("embedding")).shape == (1, 3)


def test_project_embedded_text_caches(embedding_atlas_cache_dir: Path) -> None:
    text_df = pl.DataFrame(
        {
            "id": [str(i) for i in range(6)],
            "role": ["advice"] * 6,
            "content": [f"text {i}" for i in range(6)],
        }
    )
    embedded = embed_text(text_df)
    projected1 = project_embedded_text(
        embedded,
        umap_args={"random_state": 0, "n_neighbors": 2},
    )
    projected2 = project_embedded_text(
        embedded,
        umap_args={"random_state": 0, "n_neighbors": 2},
    )
    assert (
        projected1.select("projection_x", "projection_y").to_dicts()
        == projected2.select("projection_x", "projection_y").to_dicts()
    )
    assert "neighbors" in projected1.columns
