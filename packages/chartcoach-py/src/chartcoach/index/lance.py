from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast

import numpy as np
import polars as pl

from .types import VectorIndex
from .utils import default_indices_root, hash_vectors_for_index

if TYPE_CHECKING:  # pragma: no cover
    import lancedb


@dataclass(frozen=True, slots=True)
class LanceVectorIndex(VectorIndex):
    table: lancedb.table.LanceTable
    embedding_column: str = "embedding"
    text_column: str = "text"
    metric: Literal["l2", "cosine", "dot"] = "cosine"
    backend: str = "lance"

    def search(
        self,
        query: np.ndarray,
        *,
        k: int = 10,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        query = np.asarray(query)
        if query.ndim != 1:
            raise ValueError("query must be a 1D vector.")

        q = query.astype(np.float32, copy=False)
        search = self.table.search(q).limit(int(k))
        if roles:
            roles_sorted = sorted(roles)
            role_list = ", ".join(repr(r) for r in roles_sorted)
            search = search.where(f"role IN ({role_list})")
        if ids:
            ids_sorted = sorted(ids)
            id_list = ", ".join(repr(i) for i in ids_sorted)
            search = search.where(f"id IN ({id_list})")

        # Lance returns `_distance` (lower is better). Standardize to higher-is-better `score`.
        df = pl.DataFrame(search.to_arrow())
        if "_distance" in df.columns:
            df = df.rename({"_distance": "distance"}).with_columns(
                score=(
                    1 - pl.col("distance")
                    if self.metric == "cosine"
                    else -pl.col("distance")
                )
            )
        return df

    def search_fts(
        self,
        query: str,
        *,
        k: int = 10,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        q = query.strip()
        if not q:
            return pl.DataFrame({"id": [], "role": [], "score": []})

        search = self.table.search(q, query_type="fts").limit(int(k))
        if roles:
            roles_sorted = sorted(roles)
            role_list = ", ".join(repr(r) for r in roles_sorted)
            search = search.where(f"role IN ({role_list})")
        if ids:
            ids_sorted = sorted(ids)
            id_list = ", ".join(repr(i) for i in ids_sorted)
            search = search.where(f"id IN ({id_list})")

        df = pl.DataFrame(search.to_arrow())
        if "_score" in df.columns:
            df = df.rename({"_score": "score"})
        return df

    def search_hybrid(
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,
        reranker: object | None = None,
        k: int = 10,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
        fts_columns: str | list[str] | None = None,
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        query_text = query_text.strip()
        if not query_text:
            return pl.DataFrame({"id": [], "role": [], "score": []})

        qvec = np.asarray(query_vector)
        if qvec.ndim != 1:
            raise ValueError("query_vector must be a 1D vector.")
        qvec = qvec.astype(np.float32, copy=False)

        search = (
            self.table.search(
                query_type="hybrid",
                vector_column_name=self.embedding_column,
                fts_columns=fts_columns,
            )
            .vector(qvec)
            .text(query_text)
        )

        if roles:
            roles_sorted = sorted(roles)
            role_list = ", ".join(repr(r) for r in roles_sorted)
            search = search.where(f"role IN ({role_list})")
        if ids:
            ids_sorted = sorted(ids)
            id_list = ", ".join(repr(i) for i in ids_sorted)
            search = search.where(f"id IN ({id_list})")

        if reranker is not None:
            # Lance expects a `lancedb.rerankers.Reranker` instance, but keep this
            # loosely typed to avoid importing optional reranker deps here.
            search = search.rerank(reranker)  # type: ignore[no-untyped-call]

        df = pl.DataFrame(search.limit(int(k)).to_arrow())
        if "_relevance_score" in df.columns:
            df = df.rename({"_relevance_score": "score"})
        return df


@dataclass(frozen=True, slots=True)
class EmptyLanceVectorIndex(VectorIndex):
    """A Lance-compatible index facade for empty catalogs.

    LanceDB itself doesn't need to be involved here: this object only exists so
    strategies can be instantiated and executed against empty catalogs without
    special-casing in higher layers.
    """

    embedding_column: str = "embedding"
    text_column: str = "text"
    metric: Literal["l2", "cosine", "dot"] = "cosine"
    backend: str = "lance"

    def search(
        self,
        query: np.ndarray,
        *,
        k: int = 10,
        roles: set[str] | None = None,  # noqa: ARG002
        ids: set[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        query = np.asarray(query)
        if query.ndim != 1:
            raise ValueError("query must be a 1D vector.")

        return pl.DataFrame({"id": [], "role": [], "score": []})

    def search_fts(
        self,
        query: str,
        *,
        k: int = 10,
        roles: set[str] | None = None,  # noqa: ARG002
        ids: set[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        _ = query.strip()
        return pl.DataFrame({"id": [], "role": [], "score": []})

    def search_hybrid(
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,
        reranker: object | None = None,  # noqa: ARG002
        k: int = 10,
        roles: set[str] | None = None,  # noqa: ARG002
        ids: set[str] | None = None,  # noqa: ARG002
        fts_columns: str | list[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        if not query_text.strip():
            return pl.DataFrame({"id": [], "role": [], "score": []})

        qvec = np.asarray(query_vector)
        if qvec.ndim != 1:
            raise ValueError("query_vector must be a 1D vector.")

        return pl.DataFrame({"id": [], "role": [], "score": []})


@dataclass(frozen=True, slots=True)
class LanceVectorIndexBackend:
    path: Path | None = None
    index_type: Literal[
        "IVF_FLAT",
        "IVF_SQ",
        "IVF_PQ",
        "IVF_RQ",
        "IVF_HNSW_SQ",
        "IVF_HNSW_PQ",
    ] = "IVF_PQ"
    metric: Literal["l2", "cosine", "dot"] = "cosine"
    backend: str = "lance"

    def index(
        self,
        embedded_text_df: pl.DataFrame,
        *,
        embedding_column: str = "embedding",
        id_column: str = "id",
        role_column: str = "role",
    ) -> LanceVectorIndex | EmptyLanceVectorIndex:
        try:
            import lancedb
            import pyarrow as pa
        except ImportError as e:  # pragma: no cover
            raise ImportError(
                "Lance backend requires the optional dependency group `chartcoach[index-lance]`."
            ) from e

        if embedded_text_df.is_empty():
            return EmptyLanceVectorIndex(
                embedding_column=embedding_column,
                metric=self.metric,
            )

        digest, vectors = hash_vectors_for_index(
            embedded_text_df,
            embedding_column=embedding_column,
            version=2,
            extra={
                "id_column": id_column,
                "role_column": role_column,
                "index_type": self.index_type,
                "metric": self.metric,
            },
        )
        db_dir = (
            self.path if self.path is not None else default_indices_root() / "lance"
        )
        db_dir.mkdir(parents=True, exist_ok=True)

        table_name = f"catalog_{digest}"
        ids = embedded_text_df[id_column].to_list()
        roles = embedded_text_df[role_column].to_list()
        texts = (
            embedded_text_df.get_column("content").fill_null("").to_list()
            if "content" in embedded_text_df.columns
            else [""] * embedded_text_df.height
        )
        vectors_f32 = vectors.astype("float32", copy=False)
        flat_values = pa.array(vectors_f32.ravel())
        vector_arr = pa.FixedSizeListArray.from_arrays(
            flat_values, vectors_f32.shape[1]
        )
        data = pa.table(
            {
                "id": pa.array(ids),
                "role": pa.array(roles),
                "text": pa.array(texts),
                embedding_column: vector_arr,
            }
        )

        db = lancedb.connect(str(db_dir))
        # `table_names()` is deprecated in LanceDB; use the modern `list_tables()`.
        existing = set(db.list_tables().tables)
        if table_name in existing:
            table = cast(lancedb.table.LanceTable, db.open_table(table_name))
        else:
            table = cast(
                lancedb.table.LanceTable, db.create_table(table_name, data=data)
            )

        # Enable full-text search for lexical/hybrid retrieval.
        try:
            table.create_fts_index("text", replace=False)
        except RuntimeError:
            pass

        if embedded_text_df.height >= 256:
            try:
                table.create_index(
                    metric=self.metric,
                    index_type=self.index_type,
                    vector_column_name=embedding_column,
                    replace=True,
                )
            except RuntimeError:
                pass

        return LanceVectorIndex(
            table=table,
            embedding_column=embedding_column,
            metric=self.metric,
        )
