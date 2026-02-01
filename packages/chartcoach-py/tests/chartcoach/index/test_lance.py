from __future__ import annotations

import builtins
from pathlib import Path
from typing import Callable

import numpy as np
import polars as pl
import pytest

from chartcoach.index.lance import LanceVectorIndex, LanceVectorIndexBackend


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


def test_lance_backend_empty_df_returns_empty_index(
    embedding_atlas_cache_dir: Path, tmp_path: Path
) -> None:
    backend = LanceVectorIndexBackend(path=tmp_path / "lance")
    empty = pl.DataFrame(
        schema={"id": pl.String, "role": pl.String, "embedding": pl.List(pl.Float64)}
    )
    index = backend.index(empty)
    assert index.search(np.array([0.0, 1.0]), k=10).is_empty()
    assert index.search_fts("row 1", k=10).is_empty()
    assert index.search_hybrid(
        query_text="row 1", query_vector=np.array([0.0, 1.0]), k=10
    ).is_empty()

    with pytest.raises(ValueError, match="k must be positive"):
        index.search(np.array([0.0, 1.0]), k=0)

    with pytest.raises(ValueError, match="query must be a 1D vector"):
        index.search(np.array([[0.0, 1.0]]), k=1)

    with pytest.raises(ValueError, match="k must be positive"):
        index.search_fts("row 1", k=0)

    with pytest.raises(ValueError, match="k must be positive"):
        index.search_hybrid(query_text="row 1", query_vector=np.array([0.0, 1.0]), k=0)

    assert index.search_hybrid(
        query_text=" ", query_vector=np.array([0.0, 1.0]), k=10
    ).is_empty()

    with pytest.raises(ValueError, match="query_vector must be a 1D vector"):
        index.search_hybrid(
            query_text="row 1",
            query_vector=np.array([[0.0, 1.0]]),
            k=10,
        )


def test_lance_backend_path_and_create_index_error_is_swallowed(
    embedding_atlas_cache_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import lancedb
    from lancedb.rerankers import RRFReranker

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
            "content": [f"row {i}" for i in range(n)],
            "embedding": [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]] * n,
        }
    )

    index1 = LanceVectorIndexBackend(
        path=tmp_path / "lance", index_type="IVF_FLAT"
    ).index(df)
    assert isinstance(index1, LanceVectorIndex)
    assert index1.table.count_rows() == n

    query = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    hits = index1.search(query, k=1)
    assert hits.height == 1

    hits_x = index1.search(query, k=10, roles={"x"})
    assert set(hits_x.select("role").to_series().to_list()) == {"x"}

    hits_ids = index1.search(query, k=10, ids={"1", "2"})
    assert set(hits_ids.select("id").to_series().to_list()) <= {"1", "2"}

    with pytest.raises(ValueError):
        index1.search(np.array([query]), k=1)

    with pytest.raises(ValueError):
        index1.search(query, k=0)

    fts_hits = index1.search_fts("row 1", k=5)
    assert "score" in fts_hits.columns
    assert fts_hits.height >= 1

    with pytest.raises(ValueError, match="k must be positive"):
        index1.search_fts("row 1", k=0)

    assert index1.search_fts(" ", k=5).is_empty()

    fts_hits_x = index1.search_fts("row 1", k=5, roles={"x"})
    assert set(fts_hits_x.select("role").to_series().to_list()) == {"x"}

    fts_hits_ids = index1.search_fts("row 1", k=5, ids={"1"})
    assert set(fts_hits_ids.select("id").to_series().to_list()) <= {"1"}

    hybrid_hits = index1.search_hybrid(
        query_text="row 1",
        query_vector=query.astype(np.float32),
        reranker=RRFReranker(),
        k=5,
    )
    assert "score" in hybrid_hits.columns
    assert hybrid_hits.height >= 1

    with pytest.raises(ValueError, match="k must be positive"):
        index1.search_hybrid(
            query_text="row 1",
            query_vector=query.astype(np.float32),
            reranker=RRFReranker(),
            k=0,
        )

    assert index1.search_hybrid(
        query_text=" ",
        query_vector=query.astype(np.float32),
        reranker=RRFReranker(),
        k=5,
    ).is_empty()

    with pytest.raises(ValueError, match="query_vector must be a 1D vector"):
        index1.search_hybrid(
            query_text="row 1",
            query_vector=np.array([query], dtype=np.float32),
            reranker=RRFReranker(),
            k=5,
        )

    hybrid_hits_x = index1.search_hybrid(
        query_text="row 1",
        query_vector=query.astype(np.float32),
        reranker=RRFReranker(),
        k=5,
        roles={"x"},
    )
    assert "score" in hybrid_hits_x.columns
    assert hybrid_hits_x.height >= 1

    hybrid_hits_ids = index1.search_hybrid(
        query_text="row 1",
        query_vector=query.astype(np.float32),
        reranker=RRFReranker(),
        k=5,
        ids={"1"},
    )
    assert set(hybrid_hits_ids.select("id").to_series().to_list()) <= {"1"}

    index1_again = LanceVectorIndexBackend(
        path=tmp_path / "lance", index_type="IVF_FLAT"
    ).index(df)
    assert isinstance(index1_again, LanceVectorIndex)
    assert index1_again.table.count_rows() == n

    index2 = LanceVectorIndexBackend(path=None, index_type="IVF_FLAT").index(df.head(1))
    assert isinstance(index2, LanceVectorIndex)
    assert index2.table.count_rows() == 1


def test_lance_backend_create_fts_index_error_is_swallowed(
    embedding_atlas_cache_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import lancedb

    monkeypatch.setattr(
        lancedb.table.LanceTable,
        "create_fts_index",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("boom")),
    )

    df = pl.DataFrame(
        {
            "id": ["1"],
            "role": ["x"],
            "content": ["row 1"],
            "embedding": [[0.0, 1.0, 2.0, 3.0]],
        }
    )
    index = LanceVectorIndexBackend(
        path=tmp_path / "lance", index_type="IVF_FLAT"
    ).index(df)
    assert isinstance(index, LanceVectorIndex)
    assert index.table.count_rows() == 1
