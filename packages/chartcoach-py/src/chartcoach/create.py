from __future__ import annotations

import dataclasses as dc
import os
import shutil
import tempfile
from os import PathLike
from pathlib import Path
from typing import Any, Literal, TypeAlias, TypedDict, Unpack, cast

import platformdirs
from chromadb.api.types import (
    DefaultEmbeddingFunction,
    Documents,
    EmbeddingFunction,
    validate_embedding_function,
)

from .catalog.cached_ef import CachedEmbeddingFunction, with_embedding_cache
from .catalog.clients import create_chroma_client, create_duckdb_conn
from .catalog.collection import Catalog
from .catalog.index import Index, PERSISTED_DUCKDB_RELATIONS
from .coach import Coach
from .constants import CACHE_APP_NAME, DEFAULT_CHROMA_DIRNAME, DEFAULT_DUCKDB_FILENAME

CATALOG_COLLECTION_NAME = "catalog"
DEFAULT_CATALOG_URI = (
    "https://files.peter.gy/projects/chartcoach/artifacts/catalog.parquet"
)
CacheMode: TypeAlias = Literal["reuse_or_create", "reuse_only", "force_rebuild"]
_CACHE_MODES = frozenset({"reuse_or_create", "reuse_only", "force_rebuild"})


class Settings(TypedDict, total=False):
    """Small set of options used to open or build a ready coach."""

    catalog: Catalog | str | PathLike[str]
    cache_dir: str | PathLike[str]
    cache_mode: CacheMode
    cache_embeddings: bool
    embedding_fn: EmbeddingFunction[Any] | None


@dc.dataclass(frozen=True)
class _ResolvedSettings:
    catalog: Catalog
    cache_root: Path
    cache_mode: CacheMode
    embedding_fn: EmbeddingFunction[Any]
    embedding_name: str


@dc.dataclass(frozen=True)
class _ResolvedEmbedding:
    embedding_fn: EmbeddingFunction[Any]
    embedding_name: str


@dc.dataclass(frozen=True)
class _Artifacts:
    root: Path
    chroma_path: Path
    duckdb_path: Path


def create(**settings: Unpack[Settings]) -> Coach:
    """Open or build a ready coach from a catalog, Chroma, and DuckDB."""

    resolved = _resolve_settings(cast(Settings, settings))

    artifacts = _artifacts_for(
        cache_root=resolved.cache_root,
        catalog_digest=resolved.catalog.hexdigest(),
        embedding_name=resolved.embedding_name,
    )

    if resolved.cache_mode == "force_rebuild":
        _rebuild_namespace(
            catalog=resolved.catalog,
            embedding_fn=resolved.embedding_fn,
            artifacts=artifacts,
        )
    elif resolved.cache_mode == "reuse_only":
        _require_artifacts(
            artifacts=artifacts,
            catalog=resolved.catalog,
            embedding_fn=resolved.embedding_fn,
        )
    else:
        if not _artifacts_ready(
            artifacts=artifacts,
            catalog=resolved.catalog,
            embedding_fn=resolved.embedding_fn,
        ):
            _rebuild_namespace(
                catalog=resolved.catalog,
                embedding_fn=resolved.embedding_fn,
                artifacts=artifacts,
            )

    index = _open_index(
        catalog=resolved.catalog,
        embedding_fn=resolved.embedding_fn,
        artifacts=artifacts,
    )
    return Coach(resolved.catalog, index=index)


def _resolve_settings(settings: Settings) -> _ResolvedSettings:
    raw_catalog = settings.get("catalog")
    if raw_catalog is None:
        raw_catalog = os.getenv("CHARTCOACH_CATALOG_PATH") or DEFAULT_CATALOG_URI

    catalog = (
        raw_catalog
        if isinstance(raw_catalog, Catalog)
        else Catalog.from_uri(raw_catalog)
    )

    raw_cache_dir = settings.get("cache_dir")
    cache_root = (
        Path(raw_cache_dir)
        if raw_cache_dir is not None
        else Path(
            os.getenv("CHARTCOACH_CACHE_DIR")
            or platformdirs.user_cache_dir(CACHE_APP_NAME)
        )
    )

    raw_cache_mode = settings.get("cache_mode", "reuse_or_create")
    if raw_cache_mode not in _CACHE_MODES:
        allowed = ", ".join(sorted(_CACHE_MODES))
        raise ValueError(f"cache_mode must be one of: {allowed}.")

    raw_cache_embeddings = settings.get("cache_embeddings", True)
    if not isinstance(raw_cache_embeddings, bool):
        raise ValueError("cache_embeddings must be a bool.")

    resolved_embedding = _resolve_effective_embedding_fn(
        settings.get("embedding_fn"),
        cache_embeddings=raw_cache_embeddings,
    )

    return _ResolvedSettings(
        catalog=catalog,
        cache_root=cache_root,
        cache_mode=raw_cache_mode,
        embedding_fn=resolved_embedding.embedding_fn,
        embedding_name=resolved_embedding.embedding_name,
    )


def _resolve_effective_embedding_fn(
    embedding_fn: EmbeddingFunction[Any] | None,
    *,
    cache_embeddings: bool,
) -> _ResolvedEmbedding:
    resolved = (
        cast(EmbeddingFunction[Any], DefaultEmbeddingFunction())
        if embedding_fn is None
        else cast(EmbeddingFunction[Any], embedding_fn)
    )
    if cache_embeddings and not isinstance(resolved, CachedEmbeddingFunction):
        resolved = cast(
            EmbeddingFunction[Any],
            with_embedding_cache(
                cast(EmbeddingFunction[Documents], resolved),
                app_name=CACHE_APP_NAME,
            ),
        )

    validate_embedding_function(cast(Any, resolved))
    return _ResolvedEmbedding(
        embedding_fn=resolved,
        embedding_name=_embedding_name(resolved),
    )


def _embedding_name(embedding_fn: EmbeddingFunction[Any]) -> str:
    model_name = getattr(embedding_fn, "model_name", None)
    if isinstance(model_name, str) and model_name:
        return model_name

    name = embedding_fn.name()
    if not isinstance(name, str) or not name:
        raise ValueError("embedding_fn must expose a non-empty model_name or name().")
    return name


def _embedding_dirname(embedding_name: str) -> str:
    return embedding_name.replace("/", "-")


def _artifacts_for(
    *,
    cache_root: Path,
    catalog_digest: str,
    embedding_name: str,
) -> _Artifacts:
    root = cache_root / catalog_digest / _embedding_dirname(embedding_name)
    return _Artifacts(
        root=root,
        chroma_path=root / DEFAULT_CHROMA_DIRNAME,
        duckdb_path=root / DEFAULT_DUCKDB_FILENAME,
    )


def _artifacts_ready(
    *,
    artifacts: _Artifacts,
    catalog: Catalog,
    embedding_fn: EmbeddingFunction[Any],
) -> bool:
    if not artifacts.chroma_path.exists():
        return False
    if not artifacts.duckdb_path.exists():
        return False
    if not _has_required_duckdb_relations(artifacts.duckdb_path):
        return False

    try:
        collection = create_chroma_client(artifacts.chroma_path).get_collection(
            CATALOG_COLLECTION_NAME,
            embedding_function=embedding_fn,
        )
    except Exception:
        return False

    return collection.count() == catalog.docs_df.height


def _require_artifacts(
    *,
    artifacts: _Artifacts,
    catalog: Catalog,
    embedding_fn: EmbeddingFunction[Any],
) -> None:
    if not artifacts.chroma_path.exists():
        raise FileNotFoundError(
            f"Cached Chroma directory not found at {artifacts.chroma_path}."
        )
    if not artifacts.duckdb_path.exists():
        raise FileNotFoundError(
            f"Cached DuckDB file not found at {artifacts.duckdb_path}."
        )
    if not _has_required_duckdb_relations(artifacts.duckdb_path):
        raise ValueError(
            "Cached DuckDB file does not expose the expected ChartCoach tables."
        )

    try:
        collection = create_chroma_client(artifacts.chroma_path).get_collection(
            CATALOG_COLLECTION_NAME,
            embedding_function=embedding_fn,
        )
    except Exception as exc:
        raise FileNotFoundError(
            f"Cached Chroma collection '{CATALOG_COLLECTION_NAME}' was not found in {artifacts.chroma_path}."
        ) from exc

    expected_count = catalog.docs_df.height
    if collection.count() != expected_count:
        raise ValueError(
            "Cached Chroma collection does not match the catalog document count."
        )


def _rebuild_namespace(
    *,
    catalog: Catalog,
    embedding_fn: EmbeddingFunction[Any],
    artifacts: _Artifacts,
) -> None:
    if artifacts.root.exists():
        shutil.rmtree(artifacts.root, ignore_errors=True)

    artifacts.root.parent.mkdir(parents=True, exist_ok=True)
    staged_root = Path(
        tempfile.mkdtemp(
            prefix=f".{artifacts.root.name}-",
            dir=str(artifacts.root.parent),
        )
    )
    staged_artifacts = _Artifacts(
        root=staged_root,
        chroma_path=staged_root / DEFAULT_CHROMA_DIRNAME,
        duckdb_path=staged_root / DEFAULT_DUCKDB_FILENAME,
    )

    conn = None
    try:
        staged_artifacts.root.mkdir(parents=True, exist_ok=True)
        staged_artifacts.chroma_path.mkdir(parents=True, exist_ok=True)

        collection = create_chroma_client(
            staged_artifacts.chroma_path
        ).get_or_create_collection(
            CATALOG_COLLECTION_NAME,
            embedding_function=embedding_fn,
        )
        conn = create_duckdb_conn(staged_artifacts.duckdb_path)
        Index(catalog, collection=collection, conn=conn).build()
    except Exception:
        shutil.rmtree(staged_root, ignore_errors=True)
        raise
    finally:
        if conn is not None:
            conn.close()

    artifacts.root.parent.mkdir(parents=True, exist_ok=True)
    staged_root.rename(artifacts.root)


def _open_index(
    *,
    catalog: Catalog,
    embedding_fn: EmbeddingFunction[Any],
    artifacts: _Artifacts,
) -> Index:
    _require_artifacts(
        artifacts=artifacts,
        catalog=catalog,
        embedding_fn=embedding_fn,
    )
    collection = create_chroma_client(artifacts.chroma_path).get_collection(
        CATALOG_COLLECTION_NAME,
        embedding_function=embedding_fn,
    )
    conn = create_duckdb_conn(artifacts.duckdb_path)
    return Index(catalog, collection=collection, conn=conn)


def _has_required_duckdb_relations(path: Path) -> bool:
    if not path.exists():
        return False

    conn = None
    try:
        conn = create_duckdb_conn(path)
        relation_rows = conn.execute("show all tables").fetchall()
    except Exception:
        return False
    finally:
        if conn is not None:
            conn.close()

    relation_names = {str(row[2]) for row in relation_rows}
    return PERSISTED_DUCKDB_RELATIONS.issubset(relation_names)


__all__ = [
    "CacheMode",
    "Settings",
    "create",
]
