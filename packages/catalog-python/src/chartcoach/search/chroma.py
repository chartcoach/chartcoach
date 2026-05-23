from __future__ import annotations

import dataclasses as dc
import hashlib
import json
import logging
import os
import shutil
import tempfile
from collections.abc import Mapping, Sequence
from functools import cached_property
from os import PathLike
from pathlib import Path
from typing import Any, Literal, TypeAlias, cast

import polars as pl

from ..constants import CACHE_APP_NAME, CACHE_DIR_ENV, DEFAULT_CHROMA_DIRNAME
from ..catalog.collection import Catalog
from .clients import create_chroma_client

EMBEDDING_COL = "embedding"
CATALOG_COLLECTION_NAME = "catalog"
CacheMode: TypeAlias = Literal["reuse_or_create", "reuse_only", "force_rebuild"]
_CACHE_MODES = frozenset({"reuse_or_create", "reuse_only", "force_rebuild"})
Metadata = dict[str, Any]

logger = logging.getLogger(__name__)


def _missing_chroma_extra_error(name: str | None = "chromadb") -> ModuleNotFoundError:
    return ModuleNotFoundError(
        "Chroma-backed indexing requires the optional `chartcoach[chroma]` or "
        "`chartcoach[search]` dependencies.",
        name=name,
    )


def _load_chroma_embedding_api() -> tuple[Any, Any]:
    try:
        from chromadb.api.types import (
            DefaultEmbeddingFunction,
            validate_embedding_function,
        )
    except ModuleNotFoundError as exc:
        raise _missing_chroma_extra_error(exc.name) from exc

    return DefaultEmbeddingFunction, validate_embedding_function


def _load_embedding_cache_api() -> tuple[Any, Any]:
    try:
        from .cached_ef import CachedEmbeddingFunction, with_embedding_cache
    except ModuleNotFoundError as exc:
        if _is_missing_chroma_dependency(exc):
            raise _missing_chroma_extra_error() from exc
        raise

    return CachedEmbeddingFunction, with_embedding_cache


def _load_tqdm() -> Any:
    try:
        from tqdm import tqdm
    except ModuleNotFoundError as exc:
        raise _missing_chroma_extra_error(exc.name) from exc

    return tqdm


@dc.dataclass(frozen=True)
class _ResolvedEmbedding:
    embedding_fn: Any
    embedding_name: str


@dc.dataclass(frozen=True)
class _Artifacts:
    root: Path
    chroma_path: Path


@dc.dataclass(frozen=True)
class _DocumentsState:
    frame: pl.DataFrame
    count: int
    digest: str
    version: str


class ChromaIndex:
    """Optional semantic-search index layered on top of a catalog."""

    def __init__(self, catalog: Catalog, collection: Any) -> None:
        self._catalog = catalog
        self._collection = collection

    @classmethod
    def from_collection(cls, catalog: Catalog, collection: Any) -> "ChromaIndex":
        """Wrap an existing Chroma collection for this catalog."""

        return cls(catalog=catalog, collection=collection)

    @classmethod
    def create(
        cls,
        catalog: Catalog,
        *,
        path: str | PathLike[str],
        embedding_fn: Any | None = None,
        collection_name: str = CATALOG_COLLECTION_NAME,
        reset: bool = False,
        cache_embeddings: bool = False,
    ) -> "ChromaIndex":
        """Build an index in a caller-owned Chroma directory."""

        resolved_embedding = _resolve_effective_embedding_fn(
            embedding_fn,
            cache_embeddings=cache_embeddings,
        )
        chroma_path = Path(path)
        if reset and chroma_path.exists():
            shutil.rmtree(chroma_path, ignore_errors=True)
        chroma_path.mkdir(parents=True, exist_ok=True)

        documents = _documents_state(catalog)
        collection = create_chroma_client(chroma_path).get_or_create_collection(
            collection_name,
            embedding_function=resolved_embedding.embedding_fn,
            metadata=_collection_metadata(catalog, documents),
        )
        index = cls(catalog=catalog, collection=collection)
        index.build()
        return index

    @classmethod
    def from_cache(
        cls,
        catalog: Catalog,
        *,
        cache_dir: str | PathLike[str] | None = None,
        cache_mode: CacheMode = "reuse_or_create",
        cache_embeddings: bool = True,
        embedding_fn: Any | None = None,
        collection_name: str = CATALOG_COLLECTION_NAME,
    ) -> "ChromaIndex":
        """Open or build an index in ChartCoach's content-addressed cache."""

        if cache_mode not in _CACHE_MODES:
            allowed = ", ".join(sorted(_CACHE_MODES))
            raise ValueError(f"cache_mode must be one of: {allowed}.")

        resolved_embedding = _resolve_effective_embedding_fn(
            embedding_fn,
            cache_embeddings=cache_embeddings,
        )
        artifacts = _artifacts_for(
            cache_root=_resolve_cache_root(cache_dir),
            catalog_digest=catalog.hexdigest(),
            embedding_name=resolved_embedding.embedding_name,
        )

        if cache_mode == "force_rebuild":
            _rebuild_namespace(
                catalog=catalog,
                embedding_fn=resolved_embedding.embedding_fn,
                artifacts=artifacts,
                collection_name=collection_name,
            )
        elif cache_mode == "reuse_only":
            _require_artifacts(
                artifacts=artifacts,
                catalog=catalog,
                embedding_fn=resolved_embedding.embedding_fn,
                collection_name=collection_name,
            )
        elif not _artifacts_ready(
            artifacts=artifacts,
            catalog=catalog,
            embedding_fn=resolved_embedding.embedding_fn,
            collection_name=collection_name,
        ):
            _rebuild_namespace(
                catalog=catalog,
                embedding_fn=resolved_embedding.embedding_fn,
                artifacts=artifacts,
                collection_name=collection_name,
            )

        return _open_index(
            catalog=catalog,
            embedding_fn=resolved_embedding.embedding_fn,
            artifacts=artifacts,
            collection_name=collection_name,
        )

    @property
    def catalog(self) -> Catalog:
        """Return the catalog this index was built from."""

        return self._catalog

    @property
    def collection(self) -> Any:
        """Return the Chroma collection used for semantic lookup."""

        return self._collection

    def build(self, *, batch_size: int = 768) -> None:
        """Populate the Chroma collection with catalog documents."""

        existing_count = self.collection.count()
        documents = _documents_state(self.catalog)
        expected_metadata = _collection_metadata(self.catalog, documents)
        actual_metadata = _collection_metadata_from_collection(self.collection)

        if existing_count == documents.count and _metadata_matches(
            actual_metadata, expected_metadata
        ):
            logger.debug(
                "Skipping Chroma indexing; collection already has %s documents",
                existing_count,
            )
            return
        if existing_count != 0:
            raise ValueError(
                "Chroma collection does not match this catalog. Rebuild the cache namespace from scratch."
            )
        if _metadata_conflicts(actual_metadata, expected_metadata):
            raise ValueError(
                "Chroma collection is empty but belongs to a different catalog. Rebuild the cache namespace from scratch."
            )
        _set_collection_metadata(self.collection, expected_metadata)

        ids, texts, metadatas = _collection_payload(documents.frame)
        _batch_add_documents(
            self.collection,
            ids,
            texts,
            metadatas,
            batch_size=batch_size,
        )

    @cached_property
    def embeddings_df(self) -> pl.DataFrame:
        """Return the embedded text rows stored in the Chroma collection."""

        res = self.collection.get(include=["documents", "embeddings", "metadatas"])
        return _embeddings_response_to_frame(cast(Mapping[str, Sequence[object]], res))

    @cached_property
    def documents_df(self) -> pl.DataFrame:
        """Return the text records indexed by Chroma."""

        return _documents_state(self.catalog).frame


def _collection_payload(
    docs_df: pl.DataFrame,
) -> tuple[list[str], list[str], list[Metadata]]:
    ids = docs_df.get_column("id").to_list()
    documents = docs_df.get_column("doc").to_list()
    metadatas = cast(list[Metadata], docs_df.get_column("metadata").to_list())
    return ids, documents, metadatas


def _batch_add_documents(
    collection: Any,
    ids: list[str],
    documents: list[str],
    metadatas: list[Metadata],
    *,
    batch_size: int,
) -> None:
    logger.debug(
        "Adding %s documents to Chroma in batches of %s",
        len(ids),
        batch_size,
    )
    tqdm = _load_tqdm()
    for i in tqdm(
        range(0, len(ids), batch_size),
        desc=f"Indexing catalog in batches of {batch_size}",
    ):
        collection.add(
            ids=ids[i : i + batch_size],
            documents=documents[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )


def _embeddings_response_to_frame(
    res: Mapping[str, Sequence[object]],
) -> pl.DataFrame:
    return pl.from_dict(
        cast(
            Mapping[str, Sequence[object]],
            {
                "id": res["ids"],
                "doc": res["documents"],
                "embedding": res["embeddings"],
                "metadata": res["metadatas"],
            },
        )
    ).unnest("metadata")


def _resolve_cache_root(cache_dir: str | PathLike[str] | None) -> Path:
    if cache_dir is not None:
        return Path(cache_dir)
    raw_cache_dir = os.getenv(CACHE_DIR_ENV)
    if raw_cache_dir:
        return Path(raw_cache_dir)
    try:
        import platformdirs
    except ModuleNotFoundError as exc:
        raise _missing_chroma_extra_error(exc.name) from exc

    return Path(platformdirs.user_cache_dir(CACHE_APP_NAME))


def _resolve_effective_embedding_fn(
    embedding_fn: Any | None,
    *,
    cache_embeddings: bool,
) -> _ResolvedEmbedding:
    DefaultEmbeddingFunction, validate_embedding_function = _load_chroma_embedding_api()
    CachedEmbeddingFunction, with_embedding_cache = _load_embedding_cache_api()
    resolved = DefaultEmbeddingFunction() if embedding_fn is None else embedding_fn
    if cache_embeddings and not isinstance(resolved, CachedEmbeddingFunction):
        resolved = with_embedding_cache(
            resolved,
            app_name=CACHE_APP_NAME,
        )

    validate_embedding_function(resolved)
    return _ResolvedEmbedding(
        embedding_fn=resolved,
        embedding_name=_embedding_name(resolved),
    )


def _embedding_name(embedding_fn: Any) -> str:
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
    )


def _artifacts_ready(
    *,
    artifacts: _Artifacts,
    catalog: Catalog,
    embedding_fn: Any,
    collection_name: str,
) -> bool:
    if not artifacts.chroma_path.exists():
        return False

    documents = _documents_state(catalog)
    try:
        collection = create_chroma_client(artifacts.chroma_path).get_collection(
            collection_name,
            embedding_function=embedding_fn,
        )
    except Exception:
        return False

    return collection.count() == documents.count and _metadata_matches(
        _collection_metadata_from_collection(collection),
        _collection_metadata(catalog, documents),
    )


def _require_artifacts(
    *,
    artifacts: _Artifacts,
    catalog: Catalog,
    embedding_fn: Any,
    collection_name: str,
) -> None:
    if not artifacts.chroma_path.exists():
        raise FileNotFoundError(
            f"Cached Chroma directory not found at {artifacts.chroma_path}."
        )

    try:
        collection = create_chroma_client(artifacts.chroma_path).get_collection(
            collection_name,
            embedding_function=embedding_fn,
        )
    except Exception as exc:
        raise FileNotFoundError(
            f"Cached Chroma collection '{collection_name}' was not found in {artifacts.chroma_path}."
        ) from exc

    documents = _documents_state(catalog)
    if collection.count() != documents.count:
        raise ValueError(
            "Cached Chroma collection does not match the catalog document count."
        )
    if not _metadata_matches(
        _collection_metadata_from_collection(collection),
        _collection_metadata(catalog, documents),
    ):
        raise ValueError(
            "Cached Chroma collection does not match the catalog documents."
        )


def _rebuild_namespace(
    *,
    catalog: Catalog,
    embedding_fn: Any,
    artifacts: _Artifacts,
    collection_name: str,
) -> None:
    artifacts.root.parent.mkdir(parents=True, exist_ok=True)
    staged_root = Path(
        tempfile.mkdtemp(
            prefix=f".{artifacts.root.name}-",
            dir=str(artifacts.root.parent),
        )
    )
    staged_chroma_path = staged_root / DEFAULT_CHROMA_DIRNAME
    documents = _documents_state(catalog)

    try:
        staged_root.mkdir(parents=True, exist_ok=True)
        staged_chroma_path.mkdir(parents=True, exist_ok=True)
        collection = create_chroma_client(staged_chroma_path).get_or_create_collection(
            collection_name,
            embedding_function=embedding_fn,
            metadata=_collection_metadata(catalog, documents),
        )
        ChromaIndex(catalog=catalog, collection=collection).build()
    except Exception:
        shutil.rmtree(staged_root, ignore_errors=True)
        raise

    _replace_artifact_root(staged_root, artifacts.root)


def _open_index(
    *,
    catalog: Catalog,
    embedding_fn: Any,
    artifacts: _Artifacts,
    collection_name: str,
) -> ChromaIndex:
    _require_artifacts(
        artifacts=artifacts,
        catalog=catalog,
        embedding_fn=embedding_fn,
        collection_name=collection_name,
    )
    collection = create_chroma_client(artifacts.chroma_path).get_collection(
        collection_name,
        embedding_function=embedding_fn,
    )
    return ChromaIndex(catalog=catalog, collection=collection)


def _collection_metadata_from_collection(collection: Any) -> dict[str, str]:
    metadata = getattr(collection, "metadata", None)
    if not isinstance(metadata, Mapping):
        return {}
    return {
        str(key): str(value) for key, value in metadata.items() if value is not None
    }


def _set_collection_metadata(collection: Any, metadata: Mapping[str, str]) -> None:
    modify = getattr(collection, "modify", None)
    if not callable(modify):
        return
    existing = getattr(collection, "metadata", None)
    next_metadata = dict(existing) if isinstance(existing, Mapping) else {}
    next_metadata.update(metadata)
    modify(metadata=next_metadata)


def _document_count(catalog: Catalog) -> int:
    return _documents_state(catalog).count


def _documents_state(catalog: Catalog) -> _DocumentsState:
    version, build_docs_df = _load_documents_api()
    frame = build_docs_df(catalog.guidelines_df, catalog.references_df)
    return _DocumentsState(
        frame=frame,
        count=frame.height,
        digest=_documents_digest(frame, version=version),
        version=version,
    )


def _load_documents_api() -> tuple[str, Any]:
    try:
        from .documents import DOCUMENTS_VERSION, build_docs_df
    except ModuleNotFoundError as exc:
        if _is_missing_chroma_dependency(exc):
            raise _missing_chroma_extra_error(exc.name) from exc
        raise

    return DOCUMENTS_VERSION, build_docs_df


def _documents_digest(docs_df: pl.DataFrame, *, version: str) -> str:
    hasher = hashlib.sha256()
    hasher.update(version.encode("utf-8"))
    for row in docs_df.select("id", "doc", "metadata").sort("id").to_dicts():
        payload = json.dumps(row, sort_keys=True, separators=(",", ":"), default=str)
        hasher.update(payload.encode("utf-8"))
    return hasher.hexdigest()


def _collection_metadata(
    catalog: Catalog,
    documents: _DocumentsState,
) -> dict[str, str]:
    return {
        "catalog_digest": catalog.hexdigest(),
        "documents_digest": documents.digest,
        "documents_version": documents.version,
    }


def _metadata_matches(
    actual: Mapping[str, str],
    expected: Mapping[str, str],
) -> bool:
    return all(actual.get(key) == value for key, value in expected.items())


def _metadata_conflicts(
    actual: Mapping[str, str],
    expected: Mapping[str, str],
) -> bool:
    return any(
        key in actual and actual[key] != value for key, value in expected.items()
    )


def _replace_artifact_root(staged_root: Path, target_root: Path) -> None:
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


def _is_missing_chroma_dependency(exc: ModuleNotFoundError) -> bool:
    name = exc.name
    if name is None:
        return False
    return name in {
        "chromadb",
        "platformdirs",
        "polars_hash",
        "tqdm",
    } or name.startswith("chromadb.")


__all__ = [
    "CATALOG_COLLECTION_NAME",
    "CacheMode",
    "ChromaIndex",
    "EMBEDDING_COL",
]
