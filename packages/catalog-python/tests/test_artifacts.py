from __future__ import annotations

from pathlib import Path

import pytest

from chartcoach import Catalog
from chartcoach.artifacts import catalog_artifact_rows
from chartcoach.paths import (
    default_artifact_dir,
    default_cache_dir,
    default_duckdb_path,
    default_index_dir,
)


def _rows_by_name(rows: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    return {str(row["name"]): row for row in rows}


def test_default_artifact_paths_use_platform_cache_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.paths as paths

    cache_root = tmp_path / "platform-cache"

    def fake_user_cache_path(appname: str, *, appauthor: bool) -> Path:
        assert appname == "chartcoach"
        assert appauthor is False
        return cache_root

    monkeypatch.setattr(paths, "user_cache_path", fake_user_cache_path)

    assert default_cache_dir() == cache_root
    assert default_artifact_dir() == cache_root / "artifacts"
    assert default_duckdb_path() == cache_root / "artifacts" / "duckdb_catalog.db"
    assert default_index_dir() == cache_root / "index"
    assert not cache_root.exists()


def test_catalog_artifact_rows_use_default_platform_paths_without_creating_them(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.paths as paths

    cache_root = tmp_path / "platform-cache"
    monkeypatch.setattr(
        paths,
        "user_cache_path",
        lambda appname, *, appauthor: cache_root,
    )

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=tmp_path / "catalog.parquet",
    )
    paths_by_name = {str(row["name"]): Path(str(row["path"])) for row in rows}
    index_root = paths_by_name["index_root"]

    assert paths_by_name["duckdb_catalog"] == (
        cache_root / "artifacts" / "duckdb_catalog.db"
    )
    assert index_root.is_relative_to(cache_root / "index")
    assert sample_catalog.digest() in index_root.parts
    assert paths_by_name["index_table"] == index_root / "catalog_documents.lance"
    assert not (cache_root / "artifacts").exists()
    assert not (cache_root / "index").exists()


def test_catalog_artifact_rows_keep_explicit_path_overrides(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    explicit_index_dir = tmp_path / "explicit-index"
    explicit_duckdb_path = tmp_path / "explicit.duckdb"

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=tmp_path / "catalog.parquet",
        index_dir=explicit_index_dir,
        duckdb_path=explicit_duckdb_path,
    )
    paths_by_name = {str(row["name"]): Path(str(row["path"])) for row in rows}
    index_root = paths_by_name["index_root"]

    assert paths_by_name["duckdb_catalog"] == explicit_duckdb_path
    assert index_root.is_relative_to(explicit_index_dir)
    assert sample_catalog.digest() in index_root.parts
    assert paths_by_name["index_table"] == index_root / "catalog_documents.lance"
    assert not explicit_duckdb_path.exists()
    assert not explicit_index_dir.exists()


@pytest.mark.search
def test_catalog_artifact_rows_expose_exact_parquet_contract(
    sample_catalog: Catalog,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    index_dir = tmp_path / "index"
    duckdb_path = tmp_path / "catalog.duckdb"

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=sample_catalog_path,
        index_dir=index_dir,
        duckdb_path=duckdb_path,
    )
    by_name = _rows_by_name(rows)

    assert set(by_name) == {
        "catalog_manifest",
        "catalog_source",
        "catalog_parquet",
        "duckdb_catalog",
        "index_root",
        "index_table",
    }
    assert {row["catalog_digest"] for row in rows} == {sample_catalog.digest()}
    assert by_name["catalog_manifest"]["path"] == str(
        sample_catalog_path.parent / "MANIFEST.md"
    )
    assert by_name["catalog_manifest"]["exists"] is False
    assert by_name["catalog_manifest"]["kind"] == "manifest"
    assert by_name["catalog_source"]["path"] == str(sample_catalog_path)
    assert by_name["catalog_source"]["exists"] is True
    assert by_name["catalog_source"]["kind"] == "catalog"
    assert by_name["catalog_parquet"]["kind"] == "parquet"
    assert by_name["catalog_parquet"]["exists"] is True
    assert by_name["duckdb_catalog"]["path"] == str(duckdb_path)
    assert by_name["duckdb_catalog"]["kind"] == "duckdb"
    assert by_name["duckdb_catalog"]["exists"] is False
    index_root = Path(str(by_name["index_root"]["path"]))
    assert index_root.is_relative_to(index_dir)
    assert sample_catalog.digest() in index_root.parts
    assert by_name["index_root"]["kind"] == "directory"
    assert by_name["index_root"]["exists"] is False
    assert by_name["index_root"]["table_name"] == "catalog_documents"
    assert isinstance(by_name["index_root"]["documents_version"], str)
    assert by_name["index_table"]["path"] == str(index_root / "catalog_documents.lance")
    assert by_name["index_table"]["kind"] == "lance_table"
    assert by_name["index_table"]["table_name"] == "catalog_documents"


@pytest.mark.search
def test_catalog_artifact_rows_expose_exact_folder_contract(
    sample_catalog: Catalog,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=sample_workspace_path,
        index_dir=tmp_path / "index",
    )
    by_name = _rows_by_name(rows)

    assert set(by_name) == {
        "catalog_manifest",
        "catalog_source",
        "duckdb_catalog",
        "index_root",
        "index_table",
    }
    assert by_name["catalog_source"]["kind"] == "catalog"
    assert by_name["catalog_manifest"]["path"] == str(
        sample_workspace_path / "MANIFEST.md"
    )
    assert by_name["catalog_manifest"]["exists"] is True


@pytest.mark.search
def test_catalog_artifact_rows_locate_built_lance_index(
    sample_catalog: Catalog,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    index_dir = tmp_path / "index"
    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=index_dir,
        cache_mode="reuse_or_create",
    )

    rows = _rows_by_name(
        catalog_artifact_rows(
            sample_catalog,
            source_path=sample_catalog_path,
            index_dir=index_dir,
        )
    )

    assert rows["index_root"]["path"] == str(index.index_root)
    assert rows["index_root"]["exists"] is True
    assert rows["index_table"]["path"] == str(index.table_path)
    assert rows["index_table"]["exists"] is True
    assert rows["index_table"]["table_name"] == "catalog_documents"
