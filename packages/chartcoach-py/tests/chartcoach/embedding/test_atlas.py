from __future__ import annotations

from pathlib import Path

import numpy as np
import polars as pl
import pytest

from chartcoach.embedding.atlas import embed_text, project_embedded_text
from chartcoach.embedding.vectors import vector_matrix


def test_embed_text_default_model_caches(
    monkeypatch: pytest.MonkeyPatch, embedding_atlas_cache_dir: Path
) -> None:
    import sys
    import types

    import chartcoach.embedding.atlas as atlas

    atlas._get_sentence_transformer.cache_clear()

    class FakeSentenceTransformer:
        def __init__(self, model: str, device: str | None = None) -> None:  # noqa: ARG002
            self.calls = 0

        def encode(  # noqa: D401
            self,
            texts: list[str],
            *,
            batch_size: int,  # noqa: ARG002
            show_progress_bar: bool,  # noqa: ARG002
            convert_to_numpy: bool,  # noqa: ARG002
            normalize_embeddings: bool,  # noqa: ARG002
        ) -> np.ndarray:
            self.calls += 1
            # Make output depend on input length so regressions are obvious.
            return np.ones((len(texts), 3), dtype=np.float32)

    fake_module = types.ModuleType("sentence_transformers")
    fake_module.SentenceTransformer = FakeSentenceTransformer  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)

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

    model = atlas._get_sentence_transformer("all-MiniLM-L6-v2", None)
    assert isinstance(model, FakeSentenceTransformer)
    assert model.calls == 1

    atlas._get_sentence_transformer.cache_clear()


def test_embed_text_litellm_branch_is_pluggable(
    monkeypatch: pytest.MonkeyPatch, embedding_atlas_cache_dir: Path
) -> None:
    import chartcoach.embedding.atlas as atlas

    def fake_projector(
        texts: list[str],
        batch_size: int,
        model: str,
        args: dict[str, object] | None = None,
    ) -> np.ndarray:
        return np.zeros((len(texts), 3), dtype=np.float32)

    monkeypatch.setattr(atlas, "_project_text_with_litellm", fake_projector)

    text_df = pl.DataFrame({"id": ["a"], "role": ["title"], "content": ["hello"]})
    embedded = embed_text(text_df, text_projector_type="litellm")
    assert vector_matrix(embedded.get_column("embedding")).shape == (1, 3)


def test_sentence_transformer_projector_reads_args_without_downloading_models(
    monkeypatch: pytest.MonkeyPatch, embedding_atlas_cache_dir: Path
) -> None:
    import sys
    import types

    import chartcoach.embedding.atlas as atlas

    atlas._get_sentence_transformer.cache_clear()

    class FakeSentenceTransformer:
        def __init__(self, model: str, device: str | None = None) -> None:
            self.model = model
            self.device = device
            self.calls: list[dict[str, object]] = []

        def encode(
            self,
            texts: list[str],
            *,
            batch_size: int,
            show_progress_bar: bool,
            convert_to_numpy: bool,
            normalize_embeddings: bool,
        ) -> np.ndarray:
            self.calls.append(
                {
                    "batch_size": batch_size,
                    "show_progress_bar": show_progress_bar,
                    "convert_to_numpy": convert_to_numpy,
                    "normalize_embeddings": normalize_embeddings,
                }
            )
            return np.ones((len(texts), 2), dtype=np.float32)

    fake_module = types.ModuleType("sentence_transformers")
    fake_module.SentenceTransformer = FakeSentenceTransformer  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "sentence_transformers", fake_module)

    result = atlas._project_text_with_sentence_transformers_cached(
        ["hi"],
        batch_size=1,
        model="fake-model",
        args={
            "device": "cpu",
            "normalize_embeddings": True,
            "show_progress_bar": True,
        },
    )
    assert result.shape == (1, 2)

    transformer = atlas._get_sentence_transformer("fake-model", "cpu")
    assert isinstance(transformer, FakeSentenceTransformer)
    assert transformer.device == "cpu"
    assert transformer.calls == [
        {
            "batch_size": 1,
            "show_progress_bar": True,
            "convert_to_numpy": True,
            "normalize_embeddings": True,
        }
    ]

    atlas._get_sentence_transformer.cache_clear()


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
