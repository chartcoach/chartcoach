from __future__ import annotations

from pathlib import Path
from typing import cast

from click.testing import CliRunner, Result
import polars as pl
import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.cli.main import main as chartcoach_cli

from helpers import json_value


def _find_args(catalog: Path, index: Path) -> list[str]:
    return [
        "catalog",
        "find",
        "--source",
        str(catalog),
        "--index",
        str(index),
        "direct labels",
    ]


def _json_rows(result: Result) -> list[dict[str, object]]:
    return cast(list[dict[str, object]], json_value(result)["rows"])


@pytest.mark.search
def test_catalog_find_returns_guidelines_as_json(
    runner: CliRunner,
    sample_catalog: Catalog,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    index = tmp_path / "index"
    _build_index(sample_catalog, index)

    result = runner.invoke(
        chartcoach_cli,
        [*_find_args(sample_catalog_path, index), "--format", "json"],
    )

    assert result.exit_code == 0, result.output
    assert _json_rows(result)[0]["id"] == "direct-labels"


@pytest.mark.search
def test_catalog_find_forwards_native_filters(
    runner: CliRunner,
    sample_catalog: Catalog,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    index = tmp_path / "index"
    _build_index(sample_catalog, index)

    result = runner.invoke(
        chartcoach_cli,
        [
            *_find_args(sample_catalog_path, index),
            "--where",
            "role = 'section.advice'",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    assert _json_rows(result)[0]["matched_role"] == "section.advice"


@pytest.mark.search
def test_catalog_find_accepts_a_caller_provided_vector(
    runner: CliRunner,
    sample_catalog: Catalog,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    index = tmp_path / "index"
    _build_index(sample_catalog, index)

    result = runner.invoke(
        chartcoach_cli,
        [
            *_find_args(sample_catalog_path, index),
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
    assert _json_rows(result)[0]["id"] == "direct-labels"


def _build_index(catalog: Catalog, path: Path) -> None:
    import lancedb
    from lancedb.index import FTS

    from chartcoach.catalog.documents import document_rows

    frame = (
        document_rows(catalog)
        .with_row_index("row_id")
        .with_columns(
            pl.col("text")
            .map_elements(
                lambda text: [float(len(text)), 1.0, 0.0, 0.0],
                return_dtype=pl.List(pl.Float32),
            )
            .alias("vector")
        )
    )
    table = lancedb.connect(path).create_table("documents", frame.to_arrow())
    table.create_index("text", config=FTS())
