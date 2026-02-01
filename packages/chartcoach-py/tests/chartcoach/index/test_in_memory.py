from __future__ import annotations

import numpy as np
import polars as pl
import pytest

from chartcoach.index import InMemoryVectorIndexBackend


def test_in_memory_backend_empty_df_returns_empty_index() -> None:
    empty = pl.DataFrame(
        schema={"id": pl.String, "role": pl.String, "embedding": pl.List(pl.Float64)}
    )
    index = InMemoryVectorIndexBackend().index(empty)
    hits = index.search(np.array([1.0, 0.0]), k=10)
    assert hits.is_empty()


def test_in_memory_index_search_orders_and_filters() -> None:
    df = pl.DataFrame(
        {
            "id": ["a", "b", "c"],
            "role": ["x", "x", "y"],
            "embedding": [[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]],
        }
    )
    index = InMemoryVectorIndexBackend().index(df)

    hits = index.search(np.array([1.0, 0.0]), k=2)
    assert hits.select("id").to_series().to_list() == ["a", "b"]

    hits_x = index.search(np.array([1.0, 0.0]), k=10, roles={"x"})
    assert set(hits_x.select("role").to_series().to_list()) == {"x"}


def test_in_memory_index_search_validates_inputs() -> None:
    df = pl.DataFrame({"id": ["a"], "role": ["x"], "embedding": [[0.0, 1.0]]})
    index = InMemoryVectorIndexBackend().index(df)

    with pytest.raises(ValueError):
        index.search(np.array([[0.0, 1.0]]))

    with pytest.raises(ValueError):
        index.search(np.array([0.0, 1.0]), k=0)
