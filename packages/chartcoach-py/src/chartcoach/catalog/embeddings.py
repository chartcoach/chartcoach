from typing import Literal, Protocol

import duckdb
import numpy as np
import polars as pl
from embedding_atlas.projection import (
    Projection,
    _project_text_with_litellm,
    _project_text_with_sentence_transformers,
    _run_umap,
)
from embedding_atlas.utils import Hasher, cache_path


class TextProjector(Protocol):
    __name__: str

    def __call__(
        self,
        texts: list[str],
        batch_size: int,
        model: str,
        args: dict[object, object] | None = None,
    ) -> np.ndarray: ...


def index_sections(
    embedded_sections_df: pl.DataFrame,
    conn: duckdb.DuckDBPyConnection | None = None,
    embedding_column: str = "embedding",
    tablename: str = "embeddings",
) -> duckdb.DuckDBPyConnection:
    conn = conn or duckdb.connect()
    if embedded_sections_df.is_empty():
        raise ValueError("Cannot index an empty embedded sections DataFrame.")

    first_embedding = embedded_sections_df.get_column(embedding_column)[0]
    ndims = len(first_embedding)  # polars list/array element
    # Create the vector index using VSS
    conn.execute(f"""
    INSTALL vss; LOAD vss;
    CREATE OR REPLACE TABLE "{tablename}" as (
        SELECT id,
               role,
               "{embedding_column}"::FLOAT[{ndims}]
        AS "{embedding_column}"
        FROM embedded_sections_df
    );
    CREATE INDEX idx ON "{tablename}" USING HNSW ("{embedding_column}");
    """)

    return conn


def embed_sections(
    sections_df: pl.DataFrame,
    model: str = "all-MiniLM-L6-v2",
    batch_size: int = 256,
    text_projector_type: Literal[
        "sentence_transformers", "litellm"
    ] = "sentence_transformers",
    embedding_column: str = "embedding",
    **text_projector_args: object,
) -> pl.DataFrame:
    texts = sections_df["content"].fill_null("").to_list()
    text_projector: TextProjector = (
        _project_text_with_litellm
        if text_projector_type == "litellm"
        else _project_text_with_sentence_transformers
    )

    # Some arguments may contain sensitive info (e.g., API keys) or do not invalidate the cache, so we exclude them
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
                # We only want to cache the high-dimensional vectors, not the KNN info, as it is only computed upon UMAP dim reduction
                knn_indices=np.array([]),
                knn_distances=np.array([]),
            ),
        )

    return pl.concat(
        [
            sections_df.select("id", "role", "content"),
            pl.DataFrame(hidden_vectors).select(
                pl.concat_arr("*").alias(embedding_column)
            ),
        ],
        how="horizontal",
    )


def project_embedded_sections(
    embedded_sections_df: pl.DataFrame,
    x: str = "projection_x",
    y: str = "projection_y",
    neighbors: str = "neighbors",
    embedding_column: str = "embedding",
    umap_args: dict[str, object] | None = None,
) -> pl.DataFrame:
    vectors = np.array(
        embedded_sections_df[embedding_column].to_numpy(),
        copy=True,
        order="C",
    )

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
                    "ids": a,  # ID is always the same as the row index.
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
            embedded_sections_df,
            projection_df,
            neighbors_df,
        ],
        how="horizontal",
    )
