from __future__ import annotations

import numpy as np
import polars as pl
import pytest

from chartcoach.embedding.vectors import vector_matrix


def test_vector_matrix_validations() -> None:
    with pytest.raises(ValueError):
        vector_matrix(pl.Series("embedding", []))

    bad = pl.Series("embedding", [[1.0], [1.0, 2.0]])
    with pytest.raises(ValueError):
        vector_matrix(bad)

    scalar = pl.Series("embedding", [1.0, 2.0])
    with pytest.raises(ValueError):
        vector_matrix(scalar)

    df = pl.DataFrame(np.array([[1, 2], [3, 4]], dtype=np.float32))
    array_series = df.select(pl.concat_arr("*").alias("embedding")).get_column(
        "embedding"
    )
    v = vector_matrix(array_series, dtype=np.dtype(np.float32))
    assert v.dtype == np.float32
