from __future__ import annotations

from typing import Protocol

import numpy as np
import polars as pl


class VectorIndex(Protocol):
    backend: str

    def search(
        self,
        query: np.ndarray,
        *,
        k: int = 10,
        roles: set[str] | None = None,
    ) -> pl.DataFrame: ...


class VectorIndexBackend(Protocol):
    backend: str

    def index(
        self,
        embedded_text_df: pl.DataFrame,
        *,
        embedding_column: str = "embedding",
        id_column: str = "id",
        role_column: str = "role",
    ) -> VectorIndex: ...
