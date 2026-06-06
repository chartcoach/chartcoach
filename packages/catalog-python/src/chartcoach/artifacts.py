from __future__ import annotations

from collections.abc import Mapping
from os import PathLike
from pathlib import Path

from .catalog.collection import Catalog
from .paths import default_duckdb_path, default_index_dir


def resolve_duckdb_path(path: str | PathLike[str] | None = None) -> Path:
    """Resolve the conventional DuckDB artifact path."""

    if path is not None:
        return Path(path)
    return default_duckdb_path()


def catalog_artifact_rows(
    catalog: Catalog,
    *,
    source_path: str | PathLike[str],
    index_dir: str | PathLike[str] | None = None,
    duckdb_path: str | PathLike[str] | None = None,
) -> list[dict[str, object]]:
    """Return rows for catalog, DuckDB, and LanceDB artifact paths."""

    source = Path(source_path)
    catalog_digest = catalog.digest()
    rows = [
        _artifact_row(
            name="catalog_manifest",
            path=_manifest_path_for_source(source),
            kind="manifest",
            catalog_digest=catalog_digest,
            note="Catalog manifest that defines section roles and label families.",
        ),
        _artifact_row(
            name="catalog_source",
            path=source,
            kind="catalog",
            catalog_digest=catalog_digest,
            note="Source path passed to ChartCoach.",
        ),
    ]

    if source.suffix == ".parquet":
        rows.append(
            _artifact_row(
                name="catalog_parquet",
                path=source,
                kind="parquet",
                catalog_digest=catalog_digest,
                note="Native catalog parquet file.",
            )
        )

    resolved_duckdb_path = resolve_duckdb_path(duckdb_path)
    rows.append(
        _artifact_row(
            name="duckdb_catalog",
            path=resolved_duckdb_path,
            kind="duckdb",
            catalog_digest=catalog_digest,
            note="Native DuckDB file with derived catalog tables.",
        )
    )

    rows.extend(_lance_artifact_rows(catalog, index_dir=index_dir))
    return rows


def _manifest_path_for_source(source: Path) -> Path:
    if source.is_dir():
        return source / "MANIFEST.md"
    return source.parent / "MANIFEST.md"


def _lance_artifact_rows(
    catalog: Catalog,
    *,
    index_dir: str | PathLike[str] | None,
) -> list[dict[str, object]]:
    resolved_index_dir = (
        Path(index_dir) if index_dir is not None else default_index_dir()
    )
    from .search import LanceIndex

    paths = LanceIndex.cache_paths(catalog, cache_dir=resolved_index_dir)
    return [
        _artifact_row(
            name="index_root",
            path=paths.index_root,
            kind="directory",
            catalog_digest=paths.catalog_digest,
            table_name=paths.table_name,
            documents_version=paths.documents_version,
            note="LanceDB namespace root for content-addressed search artifacts.",
        ),
        _artifact_row(
            name="index_table",
            path=paths.table_path,
            kind="lance_table",
            catalog_digest=paths.catalog_digest,
            table_name=paths.table_name,
            documents_version=paths.documents_version,
            note="Lance table with indexed catalog documents.",
        ),
    ]


def _artifact_row(
    *,
    name: str,
    path: str | PathLike[str] | None,
    kind: str,
    catalog_digest: str,
    table_name: str | None = None,
    documents_version: str | None = None,
    note: str | None = None,
    error: str | None = None,
) -> dict[str, object]:
    resolved = Path(path) if path is not None else None
    values: Mapping[str, object] = {
        "name": name,
        "path": str(resolved) if resolved is not None else None,
        "exists": resolved.exists() if resolved is not None else False,
        "kind": kind,
        "catalog_digest": catalog_digest,
        "table_name": table_name,
        "documents_version": documents_version,
        "note": note,
        "error": error,
    }
    return dict(values)


__all__ = [
    "catalog_artifact_rows",
    "resolve_duckdb_path",
]
