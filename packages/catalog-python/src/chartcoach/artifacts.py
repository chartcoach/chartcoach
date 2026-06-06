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
    """Return rows for catalog, DuckDB, and Chroma artifact paths."""

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

    rows.extend(_chroma_artifact_rows(catalog, source=source, index_dir=index_dir))
    return rows


def _manifest_path_for_source(source: Path) -> Path:
    if source.is_dir():
        return source / "MANIFEST.md"
    return source.parent / "MANIFEST.md"


def _chroma_artifact_rows(
    catalog: Catalog,
    *,
    source: Path,
    index_dir: str | PathLike[str] | None,
) -> list[dict[str, object]]:
    resolved_index_dir = (
        Path(index_dir) if index_dir is not None else default_index_dir()
    )
    try:
        from .search.chroma import ChromaIndex

        paths = ChromaIndex.cache_paths(catalog, cache_dir=resolved_index_dir)
    except ModuleNotFoundError as exc:
        if not _is_missing_search_extra(exc):
            raise
        return [
            _artifact_row(
                name="index_root",
                path=resolved_index_dir,
                kind="directory",
                catalog_digest=catalog.digest(),
                error=str(exc),
                note="Search extras are required to resolve the content-addressed Chroma path.",
            )
        ]

    return [
        _artifact_row(
            name="index_root",
            path=paths.index_root,
            kind="directory",
            catalog_digest=paths.catalog_digest,
            embedding_name=paths.embedding_name,
            collection_name=paths.collection_name,
            note="Root directory for content-addressed search artifacts.",
        ),
        _artifact_row(
            name="chroma",
            path=paths.chroma_path,
            kind="chroma",
            catalog_digest=paths.catalog_digest,
            embedding_name=paths.embedding_name,
            collection_name=paths.collection_name,
            note="Native Chroma persistent database for indexed catalog documents.",
        ),
    ]


def _is_missing_search_extra(exc: ModuleNotFoundError) -> bool:
    name = exc.name
    return name in {"chromadb", "tqdm"} or (
        name is not None and name.startswith("chromadb.")
    )


def _artifact_row(
    *,
    name: str,
    path: str | PathLike[str] | None,
    kind: str,
    catalog_digest: str,
    embedding_name: str | None = None,
    collection_name: str | None = None,
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
        "embedding_name": embedding_name,
        "collection_name": collection_name,
        "note": note,
        "error": error,
    }
    return dict(values)


__all__ = [
    "catalog_artifact_rows",
    "resolve_duckdb_path",
]
