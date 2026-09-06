from __future__ import annotations

import pytest
from chartcoach.catalog.profile_layout import (
    discover_profile_artifacts,
    profile_artifact_path,
)


def test_profiles_use_flat_ids_and_optional_exports() -> None:
    artifacts = discover_profile_artifacts(
        [
            "MANIFEST.md",
            "entries.parquet",
            "profiles/minilm-normalized/profile.json",
            "profiles/minilm-normalized/index.tar.gz",
            "profiles/minilm-normalized/projection.parquet",
        ],
    )

    assert artifacts["minilm-normalized"].documents is None
    assert artifacts["minilm-normalized"].projection == (
        "profiles/minilm-normalized/projection.parquet"
    )
    assert profile_artifact_path("english-small", "profile.json") == (
        "profiles/english-small/profile.json"
    )


@pytest.mark.parametrize(
    ("paths", "message"),
    [
        (
            [
                "profiles/provider/model/profile.json",
                "profiles/provider/model/index.tar.gz",
            ],
            "single-component",
        ),
        (["profiles/minilm/profile.json"], "missing index.tar.gz"),
        (["profiles/minilm/unknown.bin"], "Unknown profile artifact"),
        (["profiles/minilm/index.tar.gz"], "missing profile.json"),
    ],
)
def test_profile_layout_rejects_invalid_inventories(
    paths: list[str], message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        discover_profile_artifacts(paths)
