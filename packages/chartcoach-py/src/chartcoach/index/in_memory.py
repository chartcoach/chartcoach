from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import polars as pl

from chartcoach.embedding.vectors import vector_matrix

from .types import VectorIndex


def _cosine_similarity_matrix(
    query: np.ndarray,
    vectors: np.ndarray,
) -> np.ndarray:
    q = query.astype(np.float32, copy=False)
    v = vectors.astype(np.float32, copy=False)
    qn = np.linalg.norm(q)
    vn = np.linalg.norm(v, axis=1)
    denom = (vn * qn) + 1e-12
    return (v @ q) / denom


@dataclass(frozen=True, slots=True)
class InMemoryVectorIndex(VectorIndex):
    ids: list[str]
    roles: list[str]
    vectors: np.ndarray
    backend: str = "in_memory"

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

        mask = None
        if roles is not None:
            roles_sorted = sorted(roles)
            mask = np.isin(np.asarray(self.roles), np.asarray(roles_sorted))

        vectors = self.vectors if mask is None else self.vectors[mask]
        ids = self.ids if mask is None else list(np.asarray(self.ids)[mask])
        rs = self.roles if mask is None else list(np.asarray(self.roles)[mask])

        sims = _cosine_similarity_matrix(query, vectors)
        topk = int(min(k, sims.shape[0]))
        idx = np.argsort(-sims)[:topk]

        return pl.DataFrame(
            {
                "id": [ids[i] for i in idx],
                "role": [rs[i] for i in idx],
                "score": [float(sims[i]) for i in idx],
            }
        )


@dataclass(frozen=True, slots=True)
class InMemoryVectorIndexBackend:
    backend: str = "in_memory"

    def index(
        self,
        embedded_text_df: pl.DataFrame,
        *,
        embedding_column: str = "embedding",
        id_column: str = "id",
        role_column: str = "role",
    ) -> InMemoryVectorIndex:
        if embedded_text_df.is_empty():
            raise ValueError("Cannot index an empty embedded text DataFrame.")

        vectors = vector_matrix(embedded_text_df.get_column(embedding_column))
        return InMemoryVectorIndex(
            ids=embedded_text_df[id_column].to_list(),
            roles=embedded_text_df[role_column].to_list(),
            vectors=vectors,
        )
