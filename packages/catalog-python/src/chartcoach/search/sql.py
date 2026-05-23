from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Any

import polars as pl

from ..catalog.collection import Catalog

if TYPE_CHECKING:
    from .chroma import ChromaIndex

EMBEDDING_COL = "embedding"

CATALOG_RELATION = "catalog"
SECTIONS_RELATION = "sections"
GUIDELINE_LABELS_RELATION = "guideline_labels"
REFERENCES_RELATION = "reference_entries"
GUIDELINE_REFERENCES_RELATION = "guideline_references"
EMBEDDINGS_RELATION = "embeddings"
STRUCTURED_RELATIONS = (
    (CATALOG_RELATION, "guidelines_df"),
    (SECTIONS_RELATION, "sections_df"),
    (GUIDELINE_LABELS_RELATION, "guideline_labels_df"),
    (REFERENCES_RELATION, "references_df"),
    (GUIDELINE_REFERENCES_RELATION, "guideline_references_df"),
)


def connect_catalog(
    catalog: Catalog,
    *,
    search: "ChromaIndex | None" = None,
    path: str | PathLike[str] = ":memory:",
) -> Any:
    """Open a DuckDB connection populated with catalog tables."""

    conn = _connect_duckdb(path=path)
    register_catalog(conn, catalog, search=search)
    return conn


def register_catalog(
    conn: Any,
    catalog: Catalog,
    *,
    search: "ChromaIndex | None" = None,
) -> None:
    """Create or replace DuckDB tables for catalog data and optional embeddings."""

    for relation_name, frame_attr in STRUCTURED_RELATIONS:
        _replace_table(conn, relation_name, getattr(catalog, frame_attr))

    if search is not None:
        _replace_embeddings_table(conn, search.embeddings_df)


def _connect_duckdb(
    *,
    path: str | PathLike[str],
) -> Any:
    try:
        import duckdb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "DuckDB catalog SQL requires the optional `chartcoach[sql]` dependencies."
        ) from exc

    duckdb_path: str | Path = ":memory:" if path == ":memory:" else Path(path)
    return duckdb.connect(duckdb_path)


def _replace_table(conn: Any, relation_name: str, frame: pl.DataFrame) -> None:
    source_relation = f"{relation_name}_source"
    conn.register(source_relation, frame)
    try:
        conn.execute(
            f'create or replace table "{relation_name}" as (select * from "{source_relation}")'
        )
    finally:
        conn.unregister(source_relation)


def _replace_embeddings_table(conn: Any, embeddings_df: pl.DataFrame) -> None:
    if embeddings_df.is_empty():
        _replace_table(conn, EMBEDDINGS_RELATION, embeddings_df)
        return

    ndims = _embedding_dimensions(embeddings_df)
    source_relation = "embeddings_source"
    conn.register(source_relation, embeddings_df)
    try:
        conn.execute(
            f'''
            create or replace table "{EMBEDDINGS_RELATION}" as (
                select
                    id as slug,
                    parent_id as id,
                    doc,
                    role,
                    "{EMBEDDING_COL}"::float[{ndims}] as "{EMBEDDING_COL}"
                from "{source_relation}"
            )
            '''
        )
    finally:
        conn.unregister(source_relation)


def _embedding_dimensions(embeddings_df: pl.DataFrame) -> int:
    dtype = embeddings_df.limit(1)[EMBEDDING_COL].dtype
    shape = getattr(dtype, "shape", None)
    if shape is not None:
        return shape[0]

    first_embedding = embeddings_df.get_column(EMBEDDING_COL).to_list()[0]
    return len(first_embedding)


__all__ = [
    "CATALOG_RELATION",
    "EMBEDDINGS_RELATION",
    "GUIDELINE_LABELS_RELATION",
    "GUIDELINE_REFERENCES_RELATION",
    "REFERENCES_RELATION",
    "SECTIONS_RELATION",
    "connect_catalog",
    "register_catalog",
]
