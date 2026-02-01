from __future__ import annotations

from functools import lru_cache
from typing import Literal, Protocol

import numpy as np
import polars as pl
from embedding_atlas.projection import (
    Projection,
    _project_text_with_litellm,
    _run_umap,
)
from embedding_atlas.utils import Hasher, cache_path

from .vectors import vector_matrix


class TextProjector(Protocol):
    __name__: str

    def __call__(
        self,
        texts: list[str],
        batch_size: int,
        model: str,
        args: dict[str, object] | None = None,
    ) -> np.ndarray: ...


@lru_cache(maxsize=8)
def _get_sentence_transformer(model: str, device: str | None):
    from sentence_transformers import SentenceTransformer

    if device:
        return SentenceTransformer(model, device=device)
    return SentenceTransformer(model)


def _project_text_with_sentence_transformers_cached(
    texts: list[str],
    batch_size: int,
    model: str,
    args: dict[str, object] | None = None,
) -> np.ndarray:
    # `embedding_atlas`' default projector reloads models frequently. Cache for
    # retrieval loops where we embed lots of short queries.
    device = None
    normalize_embeddings = False
    show_progress_bar = False

    if isinstance(args, dict):
        raw_device = args.get("device")
        if isinstance(raw_device, str):
            device = raw_device
        raw_normalize = args.get("normalize_embeddings")
        if isinstance(raw_normalize, bool):
            normalize_embeddings = raw_normalize
        raw_show = args.get("show_progress_bar")
        if isinstance(raw_show, bool):
            show_progress_bar = raw_show

    model_instance = _get_sentence_transformer(model, device)
    return model_instance.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=show_progress_bar,
        convert_to_numpy=True,
        normalize_embeddings=normalize_embeddings,
    )


def embed_text(
    text_df: pl.DataFrame,
    model: str = "all-MiniLM-L6-v2",
    batch_size: int = 256,
    text_projector_type: Literal[
        "sentence_transformers", "litellm"
    ] = "sentence_transformers",
    embedding_column: str = "embedding",
    **text_projector_args: object,
) -> pl.DataFrame:
    texts = text_df["content"].fill_null("").to_list()
    text_projector: TextProjector = (
        _project_text_with_litellm
        if text_projector_type == "litellm"
        else _project_text_with_sentence_transformers_cached
    )

    excluded_text_projector_args = {"api_key", "api_base", "sync"}
    hashed_text_projector_args: dict[str, object] = {
        k: v
        for k, v in (text_projector_args or {}).items()
        if k not in excluded_text_projector_args
    }
    hasher = Hasher()
    hasher.update(
        {
            "version": 2,
            "texts": texts,
            "model": model,
            **hashed_text_projector_args,
            "text_projector": text_projector.__name__,
        }
    )
    digest = hasher.hexdigest()
    cpath = cache_path("embeddings") / digest

    if Projection.exists(cpath):
        projection = Projection.load(cpath)
        hidden_vectors = projection.projection
    else:
        hidden_vectors = text_projector(
            texts,
            batch_size,
            model,
            text_projector_args,
        )
        Projection.save(
            cpath,
            Projection(
                projection=hidden_vectors,
                knn_indices=np.array([]),
                knn_distances=np.array([]),
            ),
        )

    return pl.concat(
        [
            text_df.select("id", "role", "content"),
            pl.DataFrame(hidden_vectors).select(
                pl.concat_arr("*").alias(embedding_column)
            ),
        ],
        how="horizontal",
    )


def project_embedded_text(
    embedded_text_df: pl.DataFrame,
    x: str = "projection_x",
    y: str = "projection_y",
    neighbors: str = "neighbors",
    embedding_column: str = "embedding",
    umap_args: dict[str, object] | None = None,
) -> pl.DataFrame:
    vectors = vector_matrix(embedded_text_df.get_column(embedding_column))

    hasher = Hasher()
    hasher.update(
        {
            "version": 2,
            "vectors": vectors,
            "umap_args": {} if umap_args is None else umap_args,
        }
    )
    digest = hasher.hexdigest()
    cpath = cache_path("projections") / digest

    if Projection.exists(cpath):
        result = Projection.load(cpath)
    else:
        result = _run_umap(vectors, {} if umap_args is None else umap_args)
        Projection.save(cpath, result)

    neighbors_df = pl.from_dicts(
        [
            {
                neighbors: {
                    "distances": b,
                    "ids": a,
                },
            }
            for a, b in zip(result.knn_indices, result.knn_distances)
        ]
    )
    projection_df = pl.DataFrame(result.projection).rename(
        {
            "column_0": x,
            "column_1": y,
        }
    )
    return pl.concat(
        [
            embedded_text_df,
            projection_df,
            neighbors_df,
        ],
        how="horizontal",
    )
