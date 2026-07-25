from __future__ import annotations

import pytest

from chartcoach.catalog.paths import paths


DIGEST = "8" * 64


def test_catalog_paths_navigate_release_profiles() -> None:
    release = paths.release(DIGEST)
    profile = release.profile("sentence-transformers/all-MiniLM-L6-v2")

    assert paths.selected() == "catalog.json"
    assert release.root() == f"catalog/releases/{DIGEST}"
    assert release.json() == f"catalog/releases/{DIGEST}/release.json"
    assert release.manifest() == f"catalog/releases/{DIGEST}/MANIFEST.md"
    assert release.entries() == f"catalog/releases/{DIGEST}/entries.parquet"
    assert profile.documents().endswith(
        "profiles/sentence-transformers/all-MiniLM-L6-v2/documents.parquet"
    )
    assert profile.index().endswith(
        "profiles/sentence-transformers/all-MiniLM-L6-v2/index.tar.gz"
    )


@pytest.mark.parametrize(
    "call",
    [
        lambda: paths.release("invalid").json(),
        lambda: paths.release(DIGEST).artifact("../entries.parquet"),
        lambda: paths.release(DIGEST).profile("openai//model").index(),
    ],
)
def test_catalog_paths_reject_unsafe_values(call) -> None:
    with pytest.raises(ValueError):
        call()
