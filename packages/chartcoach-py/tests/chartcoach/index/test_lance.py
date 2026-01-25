from __future__ import annotations

import builtins
from pathlib import Path
from typing import Callable

import numpy as np
import polars as pl
import pytest

from chartcoach.index.lance import LanceVectorIndexBackend


def test_lance_backend_import_error(monkeypatch: pytest.MonkeyPatch) -> None:
    backend = LanceVectorIndexBackend(path=Path("/tmp/does-not-matter"))

    orig_import: Callable = builtins.__import__

    def fake_import(name: str, *args, **kwargs):
        if name == "lancedb":
            raise ImportError("no lancedb")
        return orig_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)
    df = pl.DataFrame({"id": ["a"], "role": ["x"], "embedding": [[0.0, 1.0]]})
    with pytest.raises(ImportError):
        backend.index(df)


def test_lance_backend_empty_df_raises(
    embedding_atlas_cache_dir: Path, tmp_path: Path
) -> None:
    backend = LanceVectorIndexBackend(path=tmp_path / "lance")
    empty = pl.DataFrame(
        schema={"id": pl.String, "role": pl.String, "embedding": pl.List(pl.Float64)}
    )
    with pytest.raises(ValueError):
        backend.index(empty)


def test_lance_backend_path_and_create_index_error_is_swallowed(
    embedding_atlas_cache_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import lancedb

    monkeypatch.setattr(
        lancedb.table.LanceTable,
        "create_index",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("boom")),
    )

    n = 256
    df = pl.DataFrame(
        {
            "id": [str(i) for i in range(n)],
            "role": ["x"] * n,
            "embedding": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]] * n,
        }
    )

    index1 = LanceVectorIndexBackend(
        path=tmp_path / "lance", index_type="IVF_FLAT"
    ).index(df)
    assert index1.table.count_rows() == n

    query = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    hits = index1.search(query, k=1)
    assert hits.height == 1

    hits_x = index1.search(query, k=10, roles={"x"})
    assert set(hits_x.select("role").to_series().to_list()) == {"x"}

    with pytest.raises(ValueError):
        index1.search(np.array([query]), k=1)

    with pytest.raises(ValueError):
        index1.search(query, k=0)

    index2 = LanceVectorIndexBackend(path=None, index_type="IVF_FLAT").index(df.head(1))
    assert index2.table.count_rows() == 1
