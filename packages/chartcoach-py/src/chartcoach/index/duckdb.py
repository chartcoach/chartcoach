from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np
import polars as pl

from .types import VectorIndex
from .utils import default_indices_root, hash_vectors_for_index

if TYPE_CHECKING:  # pragma: no cover
    import duckdb


def _sql_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


@dataclass(frozen=True, slots=True)
class DuckDBVectorIndex(VectorIndex):
    conn: duckdb.DuckDBPyConnection
    tablename: str
    embedding_column: str = "embedding"
    backend: str = "duckdb"

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

        dims = int(query.shape[0])
        query_list = [float(x) for x in query.tolist()]
        query_lit = f"[{', '.join(map(str, query_list))}]::FLOAT[{dims}]"

        where = ""
        if roles:
            role_list = ", ".join(_sql_quote(r) for r in sorted(roles))
            where = f"WHERE role IN ({role_list})"

        return self.conn.sql(
            f"""
                SELECT id,
                       role,
                       list_cosine_similarity("{self.embedding_column}", {query_lit}) AS score
                FROM "{self.tablename}"
                {where}
                ORDER BY score DESC
                LIMIT {int(k)}
                """
        ).pl()


@dataclass(frozen=True, slots=True)
class DuckDBVectorIndexBackend:
    path: Path | None = None
    tablename: str = "embeddings"
    backend: str = "duckdb"

    def index(
        self,
        embedded_text_df: pl.DataFrame,
        *,
        embedding_column: str = "embedding",
        id_column: str = "id",
        role_column: str = "role",
    ) -> DuckDBVectorIndex:
        try:
            import duckdb
        except ImportError as e:  # pragma: no cover
            raise ImportError(
                "DuckDB backend requires the optional dependency group `chartcoach[index-duckdb]`."
            ) from e

        if embedded_text_df.is_empty():
            raise ValueError("Cannot index an empty embedded text DataFrame.")

        digest, vectors = hash_vectors_for_index(
            embedded_text_df,
            embedding_column=embedding_column,
            version=1,
            extra={
                "tablename": self.tablename,
                "id_column": id_column,
                "role_column": role_column,
            },
        )
        db_path = (
            self.path
            if self.path is not None
            else default_indices_root() / "duckdb" / f"{digest}.duckdb"
        )
        db_path.parent.mkdir(parents=True, exist_ok=True)

        ndims = vectors.shape[1]
        conn = duckdb.connect(str(db_path))
        conn.register("embedded_text_df", embedded_text_df)
        conn.execute(f"""
        INSTALL vss; LOAD vss;
        SET hnsw_enable_experimental_persistence = true;
        CREATE OR REPLACE TABLE "{self.tablename}" as (
            SELECT "{id_column}" as id,
                   "{role_column}" as role,
                   "{embedding_column}"::FLOAT[{ndims}]
            AS "{embedding_column}"
            FROM embedded_text_df
        );
        CREATE INDEX idx ON "{self.tablename}" USING HNSW ("{embedding_column}");
        """)
        return DuckDBVectorIndex(
            conn=conn,
            tablename=self.tablename,
            embedding_column=embedding_column,
        )
