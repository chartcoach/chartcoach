from __future__ import annotations

import pytest
from chartcoach._catalog.paths import paths

DIGEST = "8" * 64


def test_catalog_paths_navigate_release_profiles() -> None:
    release = paths.release(DIGEST)
    profile = release.profile("minilm-normalized")
    profile_root = f"catalog/releases/{DIGEST}/profiles/minilm-normalized"

    assert paths.selected() == "catalog.json"
    assert release.root() == f"catalog/releases/{DIGEST}"
    assert release.json() == f"catalog/releases/{DIGEST}/release.json"
    assert release.manifest() == f"catalog/releases/{DIGEST}/MANIFEST.md"
    assert release.entries() == f"catalog/releases/{DIGEST}/entries.parquet"
    assert profile.metadata() == f"{profile_root}/profile.json"
    assert profile.documents() == f"{profile_root}/documents.parquet"
    assert profile.index() == f"{profile_root}/index.tar.gz"
    assert profile.projection() == f"{profile_root}/projection.parquet"


@pytest.mark.parametrize(
    "call",
    [
        lambda: paths.release("invalid").json(),
        lambda: paths.release(DIGEST).artifact("../entries.parquet"),
        lambda: paths.release(DIGEST).profile("openai//model").index(),
        lambda: paths.release(DIGEST).profile("OpenAI").index(),
    ],
)
def test_catalog_paths_reject_unsafe_values(call) -> None:
    with pytest.raises(ValueError):
        call()
