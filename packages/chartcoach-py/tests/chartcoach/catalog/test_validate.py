from __future__ import annotations

from pathlib import Path

import polars as pl
import pytest

from chartcoach.catalog import validate


def _write_guideline_entry(entry_dir: Path, *, gid: str) -> None:
    entry_dir.mkdir(parents=True, exist_ok=True)
    (entry_dir / "guideline.md").write_text(
        f"""---
id: {gid}
title: Title {gid}
description: Desc {gid}
labels: []
---

Body
""",
        encoding="utf-8",
    )


def test_helpers_cover_unique_and_folder_id_match() -> None:
    path = Path("g1")
    assert validate._validate_folder_ids_match_paths([(path, "g1")]) == []
    assert validate._validate_unique_ids(["g1", "g2"]) == []

    assert validate._validate_folder_ids_match_paths([(path, "mismatch")]) == [
        "Folder name 'g1' does not match guideline id 'mismatch'."
    ]
    assert validate._validate_unique_ids(["g1", "g1"]) == ["Duplicate guideline ids: ['g1']"]


def test_load_folder_ids_reports_missing_root(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    entries, errors = validate._load_folder_ids(missing)
    assert entries == []
    assert errors == [f"Catalog folder does not exist: {missing}"]


def test_load_folder_ids_skips_templates_and_collects_entry_errors(tmp_path: Path) -> None:
    root = tmp_path / "guidelines"
    root.mkdir()
    (root / "README.txt").write_text("not a dir", encoding="utf-8")
    (root / "__templates__").mkdir()

    ok_dir = root / "g1"
    _write_guideline_entry(ok_dir, gid="g1")

    bad_dir = root / "g2"
    bad_dir.mkdir()
    (bad_dir / "guideline.md").write_text("---\nid: g2\n---\nBody", encoding="utf-8")

    entries, errors = validate._load_folder_ids(root)
    assert [(p.name, gid) for p, gid in entries] == [("g1", "g1")]
    assert any("g2" in e for e in errors)


def test_load_parquet_ids_covers_error_branches(tmp_path: Path) -> None:
    missing = tmp_path / "missing.parquet"
    ids, errors = validate._load_parquet_ids(missing)
    assert ids == []
    assert errors == [f"Catalog parquet does not exist: {missing}"]

    wrong_suffix = tmp_path / "catalog.txt"
    wrong_suffix.write_text("x", encoding="utf-8")
    ids, errors = validate._load_parquet_ids(wrong_suffix)
    assert ids == []
    assert errors == [f"Catalog parquet must be a .parquet file: {wrong_suffix}"]

    no_id_col = tmp_path / "no_id.parquet"
    pl.DataFrame({"x": ["g1"]}).write_parquet(no_id_col)
    ids, errors = validate._load_parquet_ids(no_id_col)
    assert ids == []
    assert errors == [f"Catalog parquet is missing required column 'id': {no_id_col}"]

    bad_ids = tmp_path / "bad_ids.parquet"
    pl.DataFrame({"id": [None]}).write_parquet(bad_ids)
    ids, errors = validate._load_parquet_ids(bad_ids)
    assert ids == []
    assert errors == [f"Catalog parquet contains non-string or empty ids: {bad_ids}"]


def test_validate_catalog_ok_and_mismatch_reporting(tmp_path: Path) -> None:
    folder = tmp_path / "guidelines"
    folder.mkdir()
    _write_guideline_entry(folder / "g1", gid="g1")
    _write_guideline_entry(folder / "g2", gid="g2")

    parquet = tmp_path / "catalog.parquet"
    pl.DataFrame({"id": ["g1", "g2"]}).write_parquet(parquet)

    validate.validate_catalog(folder, parquet_path=parquet)

    parquet_mismatch = tmp_path / "mismatch.parquet"
    pl.DataFrame({"id": ["g1", "only-in-parquet"]}).write_parquet(parquet_mismatch)

    with pytest.raises(ValueError, match="IDs missing"):
        validate.validate_catalog(folder, parquet_path=parquet_mismatch)


def test_main_exits_nonzero_on_validation_error(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    with pytest.raises(SystemExit, match="Catalog validation failed"):
        validate.main(["--folder", str(missing)])


def test_main_succeeds_on_valid_catalog(tmp_path: Path) -> None:
    folder = tmp_path / "guidelines"
    folder.mkdir()
    _write_guideline_entry(folder / "g1", gid="g1")
    validate.main(["--folder", str(folder)])
