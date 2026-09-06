from __future__ import annotations

import json
from pathlib import Path

import pytest
from chartcoach.catalog.model import Catalog
from chartcoach.cli.main import main as chartcoach_cli
from click.testing import CliRunner
from helpers import assert_cli_error


def test_catalog_validate_rejects_empty_workspace(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    (empty / "entries").mkdir()
    (empty / "MANIFEST.md").write_text(
        """# Empty

## Section Roles

### advice

Actionable guidance.

## Label Families

### chart

Chart-family labels such as `chart:bar`.
"""
    )
    result = runner.invoke(
        chartcoach_cli, ["catalog", "validate", "--source", str(empty)]
    )
    assert_cli_error(result, "No guideline entries found")


def test_catalog_build_writes_bundle(
    runner: CliRunner,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "bundle"

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "build",
            "--source",
            str(sample_workspace_path),
            "--out",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
    assert (output_path / "MANIFEST.md").is_file()
    assert (output_path / "entries.parquet").is_file()

    validate_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "validate",
            "--source",
            str(output_path),
            "--format",
            "json",
        ],
    )

    assert validate_result.exit_code == 0
    rows = {row["name"]: row["rows"] for row in json.loads(validate_result.stdout)}
    assert rows["guidelines"] == 2
    assert rows["manifest_section_roles"] == 1


def test_catalog_export_duckdb_writes_catalog_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    import duckdb

    duckdb_path = tmp_path / "duckdb" / "catalog.duckdb"

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "export",
            "duckdb",
            "--source",
            str(sample_catalog_path),
            "--out",
            str(duckdb_path),
        ],
    )

    assert result.exit_code == 0
    assert duckdb_path.exists()
    assert "Wrote DuckDB catalog" in result.output

    conn = duckdb.connect(duckdb_path, read_only=True)
    try:
        guidelines_count = conn.execute("select count(*) from guidelines").fetchone()
        labels_count = conn.execute("select count(*) from guideline_labels").fetchone()
    finally:
        conn.close()
    assert guidelines_count == (2,)
    assert labels_count == (5,)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "export",
            "duckdb",
            "--source",
            str(sample_catalog_path),
            "--out",
            str(duckdb_path),
        ],
    )
    assert_cli_error(result, "Pass --overwrite")


def test_duckdb_overwrite_preserves_existing_file_on_failure(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.duckdb as duckdb_module
    import duckdb

    duckdb_path = tmp_path / "duckdb" / "catalog.duckdb"
    duckdb_module.write_duckdb(sample_catalog, duckdb_path)

    def fail_register(*_: object, **__: object) -> None:
        raise RuntimeError("register failed")

    monkeypatch.setattr(duckdb_module, "register_catalog", fail_register)

    with pytest.raises(RuntimeError, match="register failed"):
        duckdb_module.write_duckdb(sample_catalog, duckdb_path, overwrite=True)

    conn = duckdb.connect(duckdb_path, read_only=True)
    try:
        row = conn.execute("select count(*) from guidelines").fetchone()
    finally:
        conn.close()
    assert row == (2,)
