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
    backend: str = "lance"

    def search(
        self,
        query: np.ndarray,
        *,
        k: int = 10,
        roles: set[str] | None = None,
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

        # Lance returns `_distance` (lower is better). Standardize to higher-is-better `score`.
        df = pl.DataFrame(search.to_arrow())
        if "_distance" in df.columns:
            df = df.rename({"_distance": "distance"}).with_columns(
                score=-pl.col("distance")
            )
        return df


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
    metric: Literal["l2", "cosine", "dot"] = "l2"
    backend: str = "lance"

    def index(
        self,
        embedded_text_df: pl.DataFrame,
        *,
        embedding_column: str = "embedding",
        id_column: str = "id",
        role_column: str = "role",
    ) -> LanceVectorIndex:
        try:
            import lancedb
            import pyarrow as pa
        except ImportError as e:  # pragma: no cover
            raise ImportError(
                "Lance backend requires the optional dependency group `chartcoach[index-lance]`."
            ) from e

        if embedded_text_df.is_empty():
            raise ValueError("Cannot index an empty embedded text DataFrame.")

        digest, vectors = hash_vectors_for_index(
            embedded_text_df,
            embedding_column=embedding_column,
            version=1,
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
        vectors_f32 = vectors.astype("float32", copy=False)
        flat_values = pa.array(vectors_f32.ravel())
        vector_arr = pa.FixedSizeListArray.from_arrays(
            flat_values, vectors_f32.shape[1]
        )
        data = pa.table(
            {
                "id": pa.array(ids),
                "role": pa.array(roles),
                embedding_column: vector_arr,
            }
        )

        db = lancedb.connect(str(db_dir))
        table = cast(
            lancedb.table.LanceTable,
            db.create_table(table_name, data=data, mode="overwrite"),
        )

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

        return LanceVectorIndex(table=table, embedding_column=embedding_column)
