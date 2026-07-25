from __future__ import annotations

from pathlib import Path
from typing import cast

from click.testing import CliRunner, Result
import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation import EmbeddingProfile, build_release
from chartcoach.cli.main import main as chartcoach_cli
from catalog_testkit import deterministic_embedding

from helpers import json_value

_PROFILE = "test/deterministic"
_EMBEDDING = "chartcoach-cli-find-test"


def _find_args(source: Path) -> list[str]:
    return [
        "catalog",
        "find",
        "--source",
        str(source),
        "--profile",
        _PROFILE,
        "direct labels",
    ]


def _json_rows(result: Result) -> list[dict[str, object]]:
    return cast(list[dict[str, object]], json_value(result)["rows"])


@pytest.mark.curation
@pytest.mark.search
def test_catalog_find_returns_guidelines_as_json(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _search_release(sample_catalog, tmp_path)

    result = runner.invoke(
        chartcoach_cli,
        [*_find_args(release), "--format", "json"],
    )

    assert result.exit_code == 0, result.output
    assert _json_rows(result)[0]["id"] == "direct-labels"


@pytest.mark.curation
@pytest.mark.search
def test_catalog_find_forwards_native_filters(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _search_release(sample_catalog, tmp_path)

    result = runner.invoke(
        chartcoach_cli,
        [
            *_find_args(release),
            "--where",
            "role = 'section.advice'",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    assert _json_rows(result)[0]["matched_role"] == "section.advice"


@pytest.mark.curation
@pytest.mark.search
def test_catalog_find_accepts_a_caller_provided_vector(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _search_release(sample_catalog, tmp_path)

    result = runner.invoke(
        chartcoach_cli,
        [
            *_find_args(release),
            "--mode",
            "vector",
            "--vector",
            "1",
            "--vector",
            "1",
            "--vector",
            "0",
            "--vector",
            "0",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    assert _json_rows(result)
    assert json_value(result)["mode"] == "vector"


def _search_release(catalog: Catalog, tmp_path: Path) -> Path:
    root = tmp_path / "release"
    build_release(
        catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
            )
        },
    )
    return root
