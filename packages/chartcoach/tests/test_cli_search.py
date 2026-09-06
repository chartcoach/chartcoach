from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach.catalog.curation import EmbeddingProfile, build_release
from chartcoach.catalog.model import Catalog
from chartcoach.cli.main import main as chartcoach_cli
from click.testing import CliRunner, Result
from helpers import json_value

_PROFILE = "test-deterministic"
_EMBEDDING = "chartcoach-cli-search-test"


def _search_args(source: Path) -> list[str]:
    return [
        "catalog",
        "search",
        "--source",
        str(source),
        "--profile",
        _PROFILE,
        "direct labels",
    ]


def _json_matches(result: Result) -> list[dict[str, object]]:
    return cast(list[dict[str, object]], json_value(result)["matches"])


@pytest.mark.curation
@pytest.mark.search
def test_catalog_search_supports_fts_filters_and_vector_mode(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _search_release(sample_catalog, tmp_path)

    default = runner.invoke(chartcoach_cli, _search_args(release))
    filtered = runner.invoke(
        chartcoach_cli,
        [*_search_args(release), "--where", "role = 'section.advice'"],
    )
    vector = runner.invoke(
        chartcoach_cli,
        [*_search_args(release), "--mode", "vector"],
    )

    assert default.exit_code == 0, default.output
    assert _json_matches(default)[0]["id"] == "direct-labels"
    assert json_value(default)["match_count"] == len(_json_matches(default))
    assert json_value(default)["score_kind"] == "relevance"
    assert filtered.exit_code == 0, filtered.output
    assert _json_matches(filtered)[0]["matched_role"] == "section.advice"
    assert vector.exit_code == 0, vector.output
    assert _json_matches(vector)
    assert json_value(vector)["mode"] == "vector"
    assert json_value(vector)["score_kind"] == "distance"


def _search_release(catalog: Catalog, tmp_path: Path) -> Path:
    root = tmp_path / "release"
    build_release(
        catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
            )
        },
    )
    return root
