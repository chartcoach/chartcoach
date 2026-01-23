from __future__ import annotations

from pathlib import Path

import numpy as np
import polars as pl
import pytest

from chartcoach.index.utils import (
    cache_path,
    cache_root,
    default_indices_root,
    hash_vectors_for_index,
)


def test_cache_root_env_override(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "ccache"))
    assert cache_root() == tmp_path / "ccache"


def test_cache_root_platform_branches(monkeypatch: pytest.MonkeyPatch) -> None:
    import chartcoach.index.utils as u

    monkeypatch.delenv("CHARTCOACH_CACHE_DIR", raising=False)
    monkeypatch.setattr(u.Path, "home", classmethod(lambda cls: Path("/home/test")))

    monkeypatch.setattr(u.sys, "platform", "darwin")
    assert u.cache_root() == Path("/home/test/Library/Caches/chartcoach")

    monkeypatch.setattr(u.sys, "platform", "linux")
    monkeypatch.setenv("XDG_CACHE_HOME", "/xdg")
    assert u.cache_root() == Path("/xdg/chartcoach")

    monkeypatch.delenv("XDG_CACHE_HOME", raising=False)

    class DummyOS:
        def __init__(self, *, name: str, localappdata: str | None) -> None:
            self.name = name
            self._localappdata = localappdata

        def getenv(self, key: str) -> str | None:
            if key in {"CHARTCOACH_CACHE_DIR", "XDG_CACHE_HOME"}:
                return None
            if key == "LOCALAPPDATA":
                return self._localappdata
            return None

    monkeypatch.setattr(u, "os", DummyOS(name="nt", localappdata="/local"))
    monkeypatch.setattr(u.sys, "platform", "win32")
    assert u.cache_root() == Path("/local/chartcoach/Cache")

    monkeypatch.setattr(u, "os", DummyOS(name="nt", localappdata=None))
    assert u.cache_root() == Path("/home/test/AppData/Local/chartcoach/Cache")

    monkeypatch.setattr(u, "os", DummyOS(name="posix", localappdata=None))
    assert u.cache_root() == Path("/home/test/.cache/chartcoach")


def test_cache_path_and_default_indices_root(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", "/tmp/ccache")
    assert cache_path("indices") == Path("/tmp/ccache/indices")
    assert default_indices_root() == Path("/tmp/ccache/indices")


def test_hash_vectors_for_index_is_stable() -> None:
    df = pl.DataFrame(
        {
            "id": ["a", "b"],
            "role": ["x", "y"],
            "embedding": [[0.0, 1.0], [1.0, 0.0]],
        }
    )
    d1, v1 = hash_vectors_for_index(df, embedding_column="embedding", version=1)
    d2, v2 = hash_vectors_for_index(df, embedding_column="embedding", version=1)
    assert d1 == d2
    assert np.allclose(v1, v2)

