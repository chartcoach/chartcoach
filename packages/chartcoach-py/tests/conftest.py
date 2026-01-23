from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture()
def embedding_atlas_cache_dir(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    import embedding_atlas.utils

    cache_root = tmp_path / "embedding_atlas"
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setattr(
        embedding_atlas.utils,
        "user_cache_path",
        lambda *args, **kwargs: cache_root,
    )
    return cache_root
