from __future__ import annotations

import builtins
from pathlib import Path
from typing import Callable

import numpy as np
import polars as pl
import pytest

from chartcoach.index.duckdb import DuckDBVectorIndexBackend


def test_duckdb_backend_import_error(monkeypatch: pytest.MonkeyPatch) -> None:
    backend = DuckDBVectorIndexBackend(path=Path(":memory:"))

    orig_import: Callable = builtins.__import__

    def fake_import(name: str, *args, **kwargs):
        if name == "duckdb":
            raise ImportError("no duckdb")
        return orig_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    df = pl.DataFrame({"id": ["a"], "role": ["x"], "embedding": [[0.0, 1.0]]})
    with pytest.raises(ImportError):
        backend.index(df)


def test_duckdb_backend_empty_df_raises() -> None:
    backend = DuckDBVectorIndexBackend(path=Path(":memory:"))
    empty = pl.DataFrame(
        schema={"id": pl.String, "role": pl.String, "embedding": pl.List(pl.Float64)}
    )
    with pytest.raises(ValueError):
        backend.index(empty)


def test_duckdb_backend_path_branches_and_search(
    embedding_atlas_cache_dir: Path,
) -> None:
    df = pl.DataFrame(
        {
            "id": ["a", "b"],
            "role": ["x", "y"],
            "embedding": [[1.0, 0.0], [0.0, 1.0]],
        }
    )
    index1 = DuckDBVectorIndexBackend(path=Path(":memory:")).index(df)
    row1 = index1.conn.sql("select count(*) as n from embeddings").fetchone()
    assert row1 is not None
    assert row1[0] == 2

    hits = index1.search(np.array([1.0, 0.0]), k=1)
    assert hits.select("id").to_series().to_list() == ["a"]

    hits_x = index1.search(np.array([1.0, 0.0]), k=10, roles={"x"})
    assert hits_x.select("role").to_series().to_list() == ["x"]

    with pytest.raises(ValueError):
        index1.search(np.array([1.0, 0.0]), k=0)

    with pytest.raises(ValueError):
        index1.search(np.array([[1.0, 0.0]]), k=1)

    index2 = DuckDBVectorIndexBackend(path=None).index(df)
    row2 = index2.conn.sql("select count(*) as n from embeddings").fetchone()
    assert row2 is not None
    assert row2[0] == 2
