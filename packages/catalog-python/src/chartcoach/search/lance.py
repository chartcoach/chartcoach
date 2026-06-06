from __future__ import annotations

import dataclasses as dc
import json
import logging
import shutil
import tempfile
from os import PathLike
from pathlib import Path
from typing import Any, Literal, TypeAlias, cast

import polars as pl

from ..catalog.collection import Catalog
from ..constants import LANCE_DOCUMENT_TABLE

CacheMode: TypeAlias = Literal["reuse_or_create", "reuse_only", "force_rebuild"]
_CACHE_MODES = frozenset({"reuse_or_create", "reuse_only", "force_rebuild"})
_MANIFEST_FILENAME = "_chartcoach_index.json"

logger = logging.getLogger(__name__)


@dc.dataclass(frozen=True)
class _IndexPaths:
    """Filesystem paths for one content-addressed LanceDB catalog index."""

    cache_dir: Path
    index_root: Path
    table_path: Path
    manifest_path: Path
    catalog_digest: str
    documents_version: str
    table_name: str


@dc.dataclass(frozen=True)
class _Documents:
    frame: pl.DataFrame
    count: int
    version: str


class LanceIndex:
    """Full-text search index over ChartCoach catalog documents."""

    def __init__(
        self,
        catalog: Catalog,
        table: Any,
        *,
        paths: _IndexPaths,
    ) -> None:
        self._catalog = catalog
        self._table = table
        self._paths = paths

    @classmethod
    def from_cache(
        cls,
        catalog: Catalog,
        *,
        cache_dir: str | PathLike[str],
        cache_mode: CacheMode = "reuse_only",
        table_name: str = LANCE_DOCUMENT_TABLE,
    ) -> "LanceIndex":
        """Open or build a content-addressed LanceDB index."""

        if cache_mode not in _CACHE_MODES:
            allowed = ", ".join(sorted(_CACHE_MODES))
            raise ValueError(f"cache_mode must be one of: {allowed}.")

        paths = _cache_index_paths(
            catalog,
            cache_dir=Path(cache_dir),
            documents_version=_documents_version(),
            table_name=table_name,
        )
        if cache_mode == "force_rebuild":
            documents = _build_documents(catalog)
            _rebuild_cache(catalog=catalog, documents=documents, paths=paths)
            return _open_index(catalog, paths=paths)
        elif cache_mode == "reuse_only":
            return _open_index(catalog, paths=paths)
        if not _cache_ready(paths):
            documents = _build_documents(catalog)
            _rebuild_cache(catalog=catalog, documents=documents, paths=paths)
        return _open_index(catalog, paths=paths)

    @classmethod
    def cache_paths(
        cls,
        catalog: Catalog,
        *,
        cache_dir: str | PathLike[str],
        table_name: str = LANCE_DOCUMENT_TABLE,
    ) -> _IndexPaths:
        """Resolve the content-addressed LanceDB paths for this catalog."""

        return _cache_index_paths(
            catalog,
            cache_dir=Path(cache_dir),
            documents_version=_documents_version(),
            table_name=table_name,
        )

    @property
    def catalog(self) -> Catalog:
        return self._catalog

    @property
    def table(self) -> Any:
        return self._table

    @property
    def table_name(self) -> str:
        return self._paths.table_name

    @property
    def index_root(self) -> Path:
        """Return the LanceDB root that DuckDB can attach as a Lance namespace."""

        return self._paths.index_root

    @property
    def table_path(self) -> Path:
        return self._paths.table_path

    def document_count(self) -> int:
        return int(self.table.count_rows())

    def query_documents(
        self,
        query: str,
        *,
        limit: int = 10,
        where: str | None = None,
    ) -> list[dict[str, Any]]:
        """Run a LanceDB full-text query against indexed catalog documents."""

        if not query.strip():
            raise ValueError("query must be a non-empty string.")
        if limit < 1:
            raise ValueError("limit must be at least 1.")
        search = self.table.search(query, query_type="fts", fts_columns="doc")
        if where:
            search = search.where(where)
        return [dict(row) for row in search.limit(limit).to_list()]


def _missing_lance_error(name: str | None = "lancedb") -> ModuleNotFoundError:
    return ModuleNotFoundError(
        "LanceDB indexing requires the optional `chartcoach[search]` dependencies.",
        name=name,
    )


def _load_lancedb() -> Any:
    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise _missing_lance_error(exc.name) from exc
    return lancedb


def _build_documents(catalog: Catalog) -> _Documents:
    version, build_docs_df = _load_documents_api()
    frame = _index_frame(
        build_docs_df(
            catalog.guidelines(),
            catalog.references(),
        )
    )
    return _Documents(
        frame=frame,
        count=frame.height,
        version=version,
    )


def _load_documents_api() -> tuple[str, Any]:
    from .documents import DOCUMENTS_VERSION, build_docs_df

    return DOCUMENTS_VERSION, build_docs_df


def _documents_version() -> str:
    from .documents import DOCUMENTS_VERSION

    return DOCUMENTS_VERSION


def _index_frame(docs_df: pl.DataFrame) -> pl.DataFrame:
    return docs_df.with_columns(
        parent_id=pl.col("metadata").struct.field("parent_id"),
        role=pl.col("metadata").struct.field("role"),
        labels=pl.col("metadata").struct.field("labels"),
        content_hash=pl.col("metadata").struct.field("content_hash"),
    ).select("id", "parent_id", "role", "labels", "content_hash", "doc")


def _index_paths(
    *,
    cache_dir: Path,
    index_root: Path,
    catalog_digest: str,
    documents_version: str,
    table_name: str,
) -> _IndexPaths:
    return _IndexPaths(
        cache_dir=cache_dir,
        index_root=index_root,
        table_path=index_root / f"{table_name}.lance",
        manifest_path=index_root / _MANIFEST_FILENAME,
        catalog_digest=catalog_digest,
        documents_version=documents_version,
        table_name=table_name,
    )


def _cache_index_paths(
    catalog: Catalog,
    *,
    cache_dir: Path,
    documents_version: str,
    table_name: str,
) -> _IndexPaths:
    return _index_paths(
        cache_dir=cache_dir,
        index_root=cache_dir / catalog.digest() / documents_version,
        catalog_digest=catalog.digest(),
        documents_version=documents_version,
        table_name=table_name,
    )


def _manifest(paths: _IndexPaths, documents: _Documents) -> dict[str, object]:
    return {
        "catalog_digest": paths.catalog_digest,
        "document_count": documents.count,
        "documents_version": paths.documents_version,
        "table_name": paths.table_name,
    }


def _write_index(
    *,
    catalog: Catalog,
    documents: _Documents,
    paths: _IndexPaths,
) -> None:
    lancedb = _load_lancedb()
    paths.index_root.mkdir(parents=True, exist_ok=True)
    db = lancedb.connect(paths.index_root)
    table = db.create_table(
        paths.table_name,
        documents.frame.to_arrow(),
        mode="overwrite",
    )
    if documents.count:
        table.create_fts_index("doc", replace=True)
    paths.manifest_path.write_text(
        json.dumps(_manifest(paths, documents), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    logger.debug("Built LanceDB index for %s at %s", catalog.digest(), paths.index_root)


def _read_manifest(paths: _IndexPaths) -> dict[str, object]:
    try:
        value = json.loads(paths.manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Cached LanceDB index manifest not found at {paths.manifest_path}."
        ) from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Cached LanceDB index manifest is invalid: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("Cached LanceDB index manifest must be a JSON object.")
    return cast(dict[str, object], value)


def _require_cache(paths: _IndexPaths) -> dict[str, object]:
    if not paths.table_path.exists():
        raise FileNotFoundError(
            f"Cached LanceDB table not found at {paths.table_path}."
        )
    manifest = _read_manifest(paths)
    expected: dict[str, object] = {
        "catalog_digest": paths.catalog_digest,
        "documents_version": paths.documents_version,
        "table_name": paths.table_name,
    }
    mismatches = [
        key
        for key, expected_value in expected.items()
        if manifest.get(key) != expected_value
    ]
    if mismatches:
        joined = ", ".join(mismatches)
        raise ValueError(f"Cached LanceDB index does not match: {joined}.")
    return manifest


def _cache_ready(paths: _IndexPaths) -> bool:
    try:
        _open_table(paths)
    except (FileNotFoundError, ValueError):
        return False
    return True


def _rebuild_cache(
    *,
    catalog: Catalog,
    documents: _Documents,
    paths: _IndexPaths,
) -> None:
    paths.index_root.parent.mkdir(parents=True, exist_ok=True)
    staged_root = Path(
        tempfile.mkdtemp(
            prefix=f".{paths.index_root.name}-",
            dir=str(paths.index_root.parent),
        )
    )
    staged_paths = dc.replace(
        paths,
        index_root=staged_root,
        table_path=staged_root / f"{paths.table_name}.lance",
        manifest_path=staged_root / _MANIFEST_FILENAME,
    )
    try:
        _write_index(catalog=catalog, documents=documents, paths=staged_paths)
    except Exception:
        shutil.rmtree(staged_root, ignore_errors=True)
        raise

    _replace_cache(staged_root, paths.index_root)


def _replace_cache(staged_root: Path, target_root: Path) -> None:
    if not target_root.exists():
        staged_root.rename(target_root)
        return

    backup_root = Path(
        tempfile.mkdtemp(
            prefix=f".{target_root.name}-backup-",
            dir=str(target_root.parent),
        )
    )
    shutil.rmtree(backup_root)
    target_root.rename(backup_root)
    try:
        staged_root.rename(target_root)
    except Exception:
        backup_root.rename(target_root)
        raise
    shutil.rmtree(backup_root, ignore_errors=True)


def _open_index(
    catalog: Catalog,
    *,
    paths: _IndexPaths,
) -> LanceIndex:
    table = _open_table(paths)
    return LanceIndex(catalog, table, paths=paths)


def _open_table(paths: _IndexPaths) -> Any:
    manifest = _require_cache(paths)
    lancedb = _load_lancedb()
    table = lancedb.connect(paths.index_root).open_table(paths.table_name)
    _validate_document_count(table, manifest=manifest, paths=paths)
    return table


def _validate_document_count(
    table: Any,
    *,
    manifest: dict[str, object],
    paths: _IndexPaths,
) -> None:
    document_count = manifest.get("document_count")
    if isinstance(document_count, bool) or not isinstance(document_count, int):
        raise ValueError("Cached LanceDB index manifest is missing document_count.")

    actual_count = int(table.count_rows())
    if actual_count != document_count:
        raise ValueError(
            "Cached LanceDB table row count does not match the manifest: "
            f"expected {document_count}, found {actual_count} at {paths.table_path}."
        )


__all__ = ["CacheMode", "LanceIndex"]
