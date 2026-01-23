from __future__ import annotations

import numpy as np
import polars as pl


def vector_matrix(series: pl.Series, *, dtype: np.dtype | None = None) -> np.ndarray:
    if series.len() == 0:
        raise ValueError("Cannot convert an empty embedding column to a vector matrix.")

    as_numpy = series.to_numpy()
    if as_numpy.ndim == 1 or as_numpy.dtype == object:
        vectors = np.stack(series.to_list())
    else:
        vectors = np.array(
            as_numpy,
            copy=True,
            order="C",
        )

    if vectors.ndim != 2:
        raise ValueError(
            f"Expected a 2D vector matrix, got shape={vectors.shape} dtype={vectors.dtype}."
        )

    if dtype is not None:
        return vectors.astype(dtype, copy=False)
    return vectors
