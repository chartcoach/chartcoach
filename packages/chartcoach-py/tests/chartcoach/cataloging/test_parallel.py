from __future__ import annotations

from pathlib import Path

from chartcoach.cataloging.parallel import parallel_map, param_collapsed


def test_param_collapsed() -> None:
    def add(*, a: int, b: int) -> int:
        return a + b

    wrapped = param_collapsed(add)
    assert wrapped({"a": 1, "b": 2}) == 3


def test_parallel_map_cache_hit(tmp_path: Path) -> None:
    cache_dir = tmp_path / "cache"
    calls: list[int] = []

    def f(x: int) -> int:
        calls.append(x)
        return x + 1

    inputs = [1, 2, 3]
    assert parallel_map(
        f, inputs, n_jobs=1, backend="threading", cache_dir=str(cache_dir)
    ) == [2, 3, 4]
    calls.clear()

    # cache hit should bypass function body
    assert parallel_map(
        lambda x: (_ for _ in ()).throw(RuntimeError("should not run")),
        inputs,
        n_jobs=1,
        backend="threading",
        cache_dir=str(cache_dir),
    ) == [2, 3, 4]
    assert calls == []


def test_parallel_map_no_cache() -> None:
    assert parallel_map(
        lambda x: x * 2, [1, 2], n_jobs=1, backend="threading", cache_dir=None
    ) == [2, 4]
