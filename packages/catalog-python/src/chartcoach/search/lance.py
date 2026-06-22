from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypeAlias, TypedDict, cast

import polars as pl

from ..catalog.collection import Catalog
from ..constants import LANCE_DOCUMENT_TABLE
from ..catalog.documents import build_docs_df

if TYPE_CHECKING:
    from lancedb import DBConnection, Table
    from lancedb.embeddings import EmbeddingFunction
    from lancedb.pydantic import LanceModel

Mode: TypeAlias = Literal["auto", "fts", "vector", "hybrid"]
Query: TypeAlias = str | list[float] | tuple[float, ...]
_BASE_QUERY_COLUMNS = [
    "id",
    "parent_id",
    "role",
    "labels",
    "content_hash",
    "text",
]
_RANKING_COLUMNS = ("_score", "_distance", "_relevance_score")


class Document(TypedDict, total=False):
    id: str
    parent_id: str
    role: str
    labels: list[str]
    content_hash: str
    text: str
    vector: list[float]
    _score: float
    _distance: float
    _relevance_score: float


def index(
    catalog: Catalog,
    uri: str | PathLike[str],
    *,
    table_name: str = LANCE_DOCUMENT_TABLE,
    embedding: "EmbeddingFunction | None" = None,
) -> "Table":
    """Create or replace a LanceDB table for catalog document search."""

    frame = documents(catalog)
    db = _connect(uri)
    if embedding is None:
        table = db.create_table(
            table_name,
            frame.to_arrow(),
            mode="overwrite",
        )
    else:
        table = db.create_table(
            table_name,
            schema=model(embedding),
            mode="overwrite",
        )
        rows = _document_rows(frame)
        if rows:
            table.add(rows)
    if frame.height:
        table.create_fts_index("text", replace=True)
    return table


def open(
    uri: str | PathLike[str],
    *,
    table_name: str = LANCE_DOCUMENT_TABLE,
) -> "Table":
    """Open an existing LanceDB catalog document table."""

    return _connect(uri).open_table(table_name)


def query(
    table: "Table",
    search_query: Query,
    *,
    limit: int = 10,
    where: str | None = None,
    mode: Mode = "auto",
    fts_columns: str | list[str] | None = "text",
    vector_column_name: str | None = None,
) -> list[Document]:
    """Run a bounded LanceDB query against catalog document rows."""

    if isinstance(search_query, str) and not search_query.strip():
        raise ValueError("query must be a non-empty string.")
    if limit < 1:
        raise ValueError("limit must be at least 1.")
    resolved_mode = _resolve_mode(table, search_query, mode)
    search = table.search(
        search_query,
        query_type=resolved_mode,
        fts_columns=fts_columns,
        vector_column_name=vector_column_name,
    )
    if where:
        search = search.where(where)
    return [_document(row) for row in search.limit(limit).to_list()]


def model(embedding: "EmbeddingFunction") -> type["LanceModel"]:
    """Return the LanceDB model for catalog document rows."""

    try:
        from lancedb.pydantic import LanceModel, Vector
    except ModuleNotFoundError as exc:
        raise _missing_lance_error(exc.name) from exc

    namespace: dict[str, object] = {
        "__module__": __name__,
        "__qualname__": "CatalogDocument",
        "__doc__": "Catalog document row stored in LanceDB.",
        "__annotations__": {
            "id": str,
            "parent_id": str,
            "role": str,
            "labels": list[str],
            "content_hash": str,
            "text": str,
            "vector": Vector(embedding.ndims()),
        },
        "text": embedding.SourceField(),
        "vector": embedding.VectorField(),
    }
    return type("CatalogDocument", (LanceModel,), namespace)


def documents(catalog: Catalog) -> pl.DataFrame:
    """Return catalog document rows ready for a LanceDB table."""

    return _document_frame(
        build_docs_df(
            catalog.guidelines(),
            catalog.references(),
        )
    )


def _missing_lance_error(name: str | None = "lancedb") -> ModuleNotFoundError:
    return ModuleNotFoundError(
        "LanceDB indexing requires the optional `chartcoach[index]` dependencies.",
        name=name,
    )


def _connect(uri: str | PathLike[str]) -> "DBConnection":
    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise _missing_lance_error(exc.name) from exc
    return lancedb.connect(Path(uri) if isinstance(uri, PathLike) else uri)


def _document_frame(docs_df: pl.DataFrame) -> pl.DataFrame:
    return docs_df.with_columns(
        parent_id=pl.col("metadata").struct.field("parent_id"),
        role=pl.col("metadata").struct.field("role"),
        labels=pl.col("metadata").struct.field("labels"),
        content_hash=pl.col("metadata").struct.field("content_hash"),
    ).select("id", "parent_id", "role", "labels", "content_hash", "text")


def _document_rows(frame: pl.DataFrame) -> list[Document]:
    return [cast(Document, row) for row in frame.to_dicts()]


def _resolve_mode(table: "Table", search_query: Query, mode: Mode) -> Mode:
    if mode == "fts":
        return "fts"
    if mode == "auto":
        if not isinstance(search_query, str):
            return "vector"
        try:
            return "vector" if _has_embedding_functions(table) else "fts"
        except ValueError:
            return "fts"
    if not isinstance(search_query, str):
        return mode
    has_embeddings = _has_embedding_functions(table)
    if (
        mode in {"vector", "hybrid"}
        and isinstance(search_query, str)
        and not has_embeddings
    ):
        raise ValueError(
            f"{mode} search requires a LanceDB table with embeddings. "
            "Rebuild the index with `chartcoach catalog index create --embedding ...` "
            "or rerun this query with `--mode fts`."
        )
    return mode


def _has_embedding_functions(table: "Table") -> bool:
    return bool(getattr(table, "embedding_functions", None))


def _document(row: dict[str, object]) -> Document:
    keys = [*_BASE_QUERY_COLUMNS, *_RANKING_COLUMNS]
    return cast(Document, {key: row[key] for key in keys if key in row})


__all__ = [
    "Document",
    "Mode",
    "Query",
    "documents",
    "index",
    "model",
    "open",
    "query",
]
