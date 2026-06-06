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
    import chartcoach.search.chroma as chroma

    cache_root = tmp_path / "platform-cache"
    monkeypatch.setattr(
        paths,
        "user_cache_path",
        lambda appname, *, appauthor: cache_root,
    )

    def fake_cache_paths(
        catalog: Catalog,
        *,
        cache_dir: str | Path,
        collection_name: str = "catalog",
        **_: object,
    ) -> chroma.ChromaIndexPaths:
        index_root = Path(cache_dir)
        return chroma.ChromaIndexPaths(
            index_root=index_root,
            cache_path=index_root / catalog.digest() / "documents-v1" / "tiny",
            chroma_path=index_root
            / catalog.digest()
            / "documents-v1"
            / "tiny"
            / "chroma_db",
            catalog_digest=catalog.digest(),
            documents_version="documents-v1",
            embedding_name="tiny",
            collection_name=collection_name,
        )

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(fake_cache_paths),
    )

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=tmp_path / "catalog.parquet",
    )
    paths_by_name = {str(row["name"]): Path(str(row["path"])) for row in rows}

    assert paths_by_name["duckdb_catalog"] == (
        cache_root / "artifacts" / "duckdb_catalog.db"
    )
    assert paths_by_name["index_root"] == cache_root / "index"
    assert paths_by_name["chroma"].is_relative_to(cache_root / "index")
    assert not (cache_root / "artifacts").exists()
    assert not (cache_root / "index").exists()


def test_catalog_artifact_rows_keep_explicit_path_overrides(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    explicit_index_dir = tmp_path / "explicit-index"
    explicit_duckdb_path = tmp_path / "explicit.duckdb"

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(
            lambda catalog, *, cache_dir, collection_name="catalog", **_: (
                chroma.ChromaIndexPaths(
                    index_root=Path(cache_dir),
                    cache_path=Path(cache_dir)
                    / catalog.digest()
                    / "documents-v1"
                    / "tiny",
                    chroma_path=Path(cache_dir)
                    / catalog.digest()
                    / "documents-v1"
                    / "tiny"
                    / "chroma_db",
                    catalog_digest=catalog.digest(),
                    documents_version="documents-v1",
                    embedding_name="tiny",
                    collection_name=collection_name,
                )
            )
        ),
    )

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=tmp_path / "catalog.parquet",
        index_dir=explicit_index_dir,
        duckdb_path=explicit_duckdb_path,
    )
    paths_by_name = {str(row["name"]): Path(str(row["path"])) for row in rows}

    assert paths_by_name["duckdb_catalog"] == explicit_duckdb_path
    assert paths_by_name["index_root"] == explicit_index_dir
    assert paths_by_name["chroma"].is_relative_to(explicit_index_dir)
    assert not explicit_duckdb_path.exists()
    assert not explicit_index_dir.exists()


@pytest.mark.search
def test_catalog_artifact_rows_expose_exact_parquet_contract(
    sample_catalog: Catalog,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    pytest.importorskip("chromadb")
    from chartcoach.search.chroma import ChromaIndex

    index_dir = tmp_path / "index"
    duckdb_path = tmp_path / "catalog.duckdb"
    paths = ChromaIndex.cache_paths(sample_catalog, cache_dir=index_dir)

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=sample_catalog_path,
        index_dir=index_dir,
        duckdb_path=duckdb_path,
    )
    by_name = _rows_by_name(rows)

    assert list(by_name) == [
        "catalog_manifest",
        "catalog_source",
        "catalog_parquet",
        "duckdb_catalog",
        "index_root",
        "chroma",
    ]
    assert {row["catalog_digest"] for row in rows} == {sample_catalog.digest()}
    assert by_name["catalog_manifest"] == {
        "name": "catalog_manifest",
        "path": str(sample_catalog_path.parent / "MANIFEST.md"),
        "exists": False,
        "kind": "manifest",
        "catalog_digest": sample_catalog.digest(),
        "embedding_name": None,
        "collection_name": None,
        "note": "Catalog manifest that defines section roles and label families.",
        "error": None,
    }
    assert by_name["catalog_source"] == {
        "name": "catalog_source",
        "path": str(sample_catalog_path),
        "exists": True,
        "kind": "catalog",
        "catalog_digest": sample_catalog.digest(),
        "embedding_name": None,
        "collection_name": None,
        "note": "Source path passed to ChartCoach.",
        "error": None,
    }
    assert by_name["catalog_parquet"]["kind"] == "parquet"
    assert by_name["catalog_parquet"]["exists"] is True
    assert by_name["duckdb_catalog"]["path"] == str(duckdb_path)
    assert by_name["duckdb_catalog"]["kind"] == "duckdb"
    assert by_name["duckdb_catalog"]["exists"] is False
    assert by_name["index_root"]["path"] == str(paths.index_root)
    assert by_name["index_root"]["kind"] == "directory"
    assert by_name["index_root"]["exists"] is False
    assert by_name["index_root"]["collection_name"] == "catalog"
    assert by_name["chroma"]["path"] == str(paths.chroma_path)
    assert by_name["chroma"]["kind"] == "chroma"
    assert by_name["chroma"]["collection_name"] == "catalog"


@pytest.mark.search
def test_catalog_artifact_rows_expose_exact_folder_contract(
    sample_catalog: Catalog,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    pytest.importorskip("chromadb")

    rows = catalog_artifact_rows(
        sample_catalog,
        source_path=sample_workspace_path,
        index_dir=tmp_path / "index",
    )
    by_name = _rows_by_name(rows)

    assert list(by_name) == [
        "catalog_manifest",
        "catalog_source",
        "duckdb_catalog",
        "index_root",
        "chroma",
    ]
    assert by_name["catalog_source"]["kind"] == "catalog"
    assert by_name["catalog_manifest"]["path"] == str(
        sample_workspace_path / "MANIFEST.md"
    )
    assert by_name["catalog_manifest"]["exists"] is True


def test_catalog_artifact_rows_report_missing_search_extra(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    def raise_missing_search_extra(*_: object, **__: object) -> object:
        raise ModuleNotFoundError("missing tqdm", name="tqdm")

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(raise_missing_search_extra),
    )

    rows = _rows_by_name(
        catalog_artifact_rows(
            sample_catalog,
            source_path=tmp_path / "catalog.parquet",
            index_dir=tmp_path / "index",
        )
    )

    assert list(rows) == [
        "catalog_manifest",
        "catalog_source",
        "catalog_parquet",
        "duckdb_catalog",
        "index_root",
    ]
    assert rows["index_root"]["kind"] == "directory"
    assert rows["index_root"]["error"] == "missing tqdm"
    assert "Search extras are required" in str(rows["index_root"]["note"])


def test_catalog_artifact_rows_reraise_unrelated_import_errors(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    def raise_unrelated_import_error(*_: object, **__: object) -> object:
        raise ModuleNotFoundError("missing not_search", name="not_search")

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(raise_unrelated_import_error),
    )

    with pytest.raises(ModuleNotFoundError, match="missing not_search"):
        catalog_artifact_rows(
            sample_catalog,
            source_path=tmp_path / "catalog.parquet",
            index_dir=tmp_path / "index",
        )


def test_catalog_artifact_rows_only_swallows_missing_search_extras(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    def raise_unrelated_missing_module(*_: object, **__: object) -> object:
        raise ModuleNotFoundError("missing internal dependency", name="internal_dep")

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(raise_unrelated_missing_module),
    )

    with pytest.raises(ModuleNotFoundError, match="missing internal dependency"):
        catalog_artifact_rows(
            sample_catalog,
            source_path=tmp_path / "catalog.parquet",
        )
