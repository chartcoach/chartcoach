from __future__ import annotations

import dataclasses as dc
import hashlib
import json
import logging
import shutil
import tempfile
from collections.abc import Mapping
from os import PathLike
from pathlib import Path
from typing import Any, Literal, TypeAlias, cast

import polars as pl

from ..constants import DEFAULT_CHROMA_DIRNAME
from ..catalog.collection import Catalog
from .clients import create_chroma_client

CATALOG_COLLECTION_NAME = "catalog"
CacheMode: TypeAlias = Literal["reuse_or_create", "reuse_only", "force_rebuild"]
_CACHE_MODES = frozenset({"reuse_or_create", "reuse_only", "force_rebuild"})
Metadata = dict[str, Any]

logger = logging.getLogger(__name__)


def _missing_chroma_extra_error(name: str | None = "chromadb") -> ModuleNotFoundError:
    return ModuleNotFoundError(
        "Chroma-backed indexing requires the optional `chartcoach[search]` dependencies.",
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
class _CachePaths:
    cache_root: Path
    cache_path: Path
    chroma_path: Path


@dc.dataclass(frozen=True)
class ChromaIndexPaths:
    """Native paths for a content-addressed Chroma catalog index."""

    index_root: Path
    cache_path: Path
    chroma_path: Path
    catalog_digest: str
    documents_version: str
    embedding_name: str
    collection_name: str


@dc.dataclass(frozen=True)
class _Documents:
    frame: pl.DataFrame
    count: int
    digest: str
    version: str


class ChromaIndex:
    """Optional semantic-search index layered on top of a catalog."""

    def __init__(
        self,
        catalog: Catalog,
        collection: Any,
        *,
        embedding_name: str | None = None,
        collection_name: str = CATALOG_COLLECTION_NAME,
        paths: ChromaIndexPaths | None = None,
        documents: _Documents | None = None,
    ) -> None:
        self._catalog = catalog
        self._collection = collection
        self._embedding_name = embedding_name
        self._collection_name = collection_name
        self._paths = paths
        self._documents_cache = documents

    @classmethod
    def create(
        cls,
        catalog: Catalog,
        *,
        path: str | PathLike[str],
        embedding_fn: Any | None = None,
        collection_name: str = CATALOG_COLLECTION_NAME,
        reset: bool = False,
    ) -> "ChromaIndex":
        """Build an index in a caller-owned Chroma directory."""

        resolved_embedding = _resolve_embedding(embedding_fn)
        chroma_path = Path(path)
        if reset and chroma_path.exists():
            shutil.rmtree(chroma_path, ignore_errors=True)
        chroma_path.mkdir(parents=True, exist_ok=True)

        documents = _build_documents(catalog)
        catalog_digest = catalog.digest()
        paths = ChromaIndexPaths(
            index_root=chroma_path,
            cache_path=chroma_path,
            chroma_path=chroma_path,
            catalog_digest=catalog_digest,
            documents_version=documents.version,
            embedding_name=resolved_embedding.embedding_name,
            collection_name=collection_name,
        )
        collection = create_chroma_client(chroma_path).get_or_create_collection(
            collection_name,
            embedding_function=resolved_embedding.embedding_fn,
            metadata=_collection_metadata(
                catalog,
                documents,
                embedding_name=resolved_embedding.embedding_name,
            ),
        )
        index = cls(
            catalog=catalog,
            collection=collection,
            embedding_name=resolved_embedding.embedding_name,
            collection_name=collection_name,
            paths=paths,
            documents=documents,
        )
        index.build()
        return index

    @classmethod
    def from_cache(
        cls,
        catalog: Catalog,
        *,
        cache_dir: str | PathLike[str],
        cache_mode: CacheMode = "reuse_only",
        embedding_fn: Any | None = None,
        collection_name: str = CATALOG_COLLECTION_NAME,
    ) -> "ChromaIndex":
        """Open or build an index in ChartCoach's content-addressed cache."""

        if cache_mode not in _CACHE_MODES:
            allowed = ", ".join(sorted(_CACHE_MODES))
            raise ValueError(f"cache_mode must be one of: {allowed}.")

        catalog_digest = catalog.digest()
        resolved_embedding = _resolve_embedding(embedding_fn)
        documents_version = _documents_version()
        cache_paths = _cache_paths_for(
            cache_root=_resolve_cache_root(cache_dir),
            catalog_digest=catalog_digest,
            documents_version=documents_version,
            embedding_name=resolved_embedding.embedding_name,
        )

        if cache_mode == "force_rebuild":
            documents = _build_documents(catalog)
            _rebuild_cache(
                catalog=catalog,
                documents=documents,
                embedding_fn=resolved_embedding.embedding_fn,
                embedding_name=resolved_embedding.embedding_name,
                cache_paths=cache_paths,
                collection_name=collection_name,
            )
        elif cache_mode == "reuse_only":
            _require_cache(
                cache_paths=cache_paths,
                catalog_digest=catalog_digest,
                documents_version=documents_version,
                embedding_fn=resolved_embedding.embedding_fn,
                embedding_name=resolved_embedding.embedding_name,
                collection_name=collection_name,
            )
        elif not _cache_ready(
            cache_paths=cache_paths,
            catalog_digest=catalog_digest,
            documents_version=documents_version,
            embedding_fn=resolved_embedding.embedding_fn,
            embedding_name=resolved_embedding.embedding_name,
            collection_name=collection_name,
        ):
            documents = _build_documents(catalog)
            _rebuild_cache(
                catalog=catalog,
                documents=documents,
                embedding_fn=resolved_embedding.embedding_fn,
                embedding_name=resolved_embedding.embedding_name,
                cache_paths=cache_paths,
                collection_name=collection_name,
            )

        return _open_index(
            catalog=catalog,
            embedding_fn=resolved_embedding.embedding_fn,
            embedding_name=resolved_embedding.embedding_name,
            cache_paths=cache_paths,
            collection_name=collection_name,
            catalog_digest=catalog_digest,
            documents_version=documents_version,
        )

    @classmethod
    def cache_paths(
        cls,
        catalog: Catalog,
        *,
        cache_dir: str | PathLike[str],
        embedding_fn: Any | None = None,
        collection_name: str = CATALOG_COLLECTION_NAME,
    ) -> ChromaIndexPaths:
        """Resolve the native Chroma paths for this catalog and embedding function."""

        catalog_digest = catalog.digest()
        documents_version = _documents_version()
        resolved_embedding = _resolve_embedding(embedding_fn)
        cache_root = _resolve_cache_root(cache_dir)
        cache_paths = _cache_paths_for(
            cache_root=cache_root,
            catalog_digest=catalog_digest,
            documents_version=documents_version,
            embedding_name=resolved_embedding.embedding_name,
        )
        return _index_paths(
            catalog_digest=catalog_digest,
            documents_version=documents_version,
            cache_paths=cache_paths,
            embedding_name=resolved_embedding.embedding_name,
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

    @property
    def collection_name(self) -> str:
        """Return the Chroma collection name."""

        return self._collection_name

    @property
    def embedding_name(self) -> str | None:
        """Return the embedding identity used to build this index, when known."""

        return self._embedding_name

    @property
    def paths(self) -> ChromaIndexPaths | None:
        """Return native filesystem paths for this index, when known."""

        return self._paths

    @property
    def chroma_path(self) -> Path | None:
        """Return the Chroma persistent database directory, when known."""

        if self._paths is None:
            return None
        return self._paths.chroma_path

    def build(self, *, batch_size: int = 768) -> None:
        """Populate the Chroma collection with catalog documents."""

        existing_count = self.collection.count()
        documents = self._documents()
        expected_metadata = _collection_metadata(
            self.catalog,
            documents,
            embedding_name=self._embedding_name,
        )
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
                "Chroma collection does not match this catalog. Rebuild the cache path from scratch."
            )
        if _metadata_conflicts(actual_metadata, expected_metadata):
            raise ValueError(
                "Chroma collection is empty but belongs to a different catalog. Rebuild the cache path from scratch."
            )
        _set_collection_metadata(self.collection, expected_metadata)

        ids, texts, metadatas = _chroma_add_args(documents.frame)
        _batch_add_documents(
            self.collection,
            ids,
            texts,
            metadatas,
            batch_size=batch_size,
        )

    def documents(self) -> pl.DataFrame:
        """Return the text records indexed by Chroma."""

        return self._documents().frame

    def _documents(self) -> _Documents:
        if self._documents_cache is None:
            self._documents_cache = _build_documents(self.catalog)
        return self._documents_cache


def _chroma_add_args(
    docs_df: pl.DataFrame,
) -> tuple[list[str], list[str], list[Metadata]]:
    ids = docs_df.get_column("id").to_list()
    documents = docs_df.get_column("doc").to_list()
    metadatas = [
        _chroma_metadata(metadata)
        for metadata in cast(list[Metadata], docs_df.get_column("metadata").to_list())
    ]
    return ids, documents, metadatas


def _chroma_metadata(metadata: Metadata) -> Metadata:
    return {
        key: value
        for key, value in metadata.items()
        if value is not None and not (key == "labels" and value == [])
    }


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


def _resolve_cache_root(cache_dir: str | PathLike[str]) -> Path:
    return Path(cache_dir)


def _resolve_embedding(
    embedding_fn: Any | None,
) -> _ResolvedEmbedding:
    DefaultEmbeddingFunction, validate_embedding_function = _load_chroma_embedding_api()
    resolved = DefaultEmbeddingFunction() if embedding_fn is None else embedding_fn

    validate_embedding_function(resolved)
    return _ResolvedEmbedding(
        embedding_fn=resolved,
        embedding_name=_embedding_name(resolved),
    )


def _embedding_name(embedding_fn: Any) -> str:
    cls = type(embedding_fn)
    label = f"{cls.__module__}.{cls.__qualname__}"
    get_config = getattr(embedding_fn, "get_config", None)
    config = get_config() if callable(get_config) else {}
    payload = json.dumps(
        {"class": label, "config": config},
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
    return f"{label}-{digest}"


def _embedding_dirname(embedding_name: str) -> str:
    return "".join(
        char if char.isalnum() or char in {"-", "_", "."} else "-"
        for char in embedding_name
    )


def _cache_paths_for(
    *,
    cache_root: Path,
    catalog_digest: str,
    documents_version: str,
    embedding_name: str,
) -> _CachePaths:
    cache_path = (
        cache_root
        / catalog_digest
        / documents_version
        / _embedding_dirname(embedding_name)
    )
    return _CachePaths(
        cache_root=cache_root,
        cache_path=cache_path,
        chroma_path=cache_path / DEFAULT_CHROMA_DIRNAME,
    )


def _index_paths(
    *,
    catalog_digest: str,
    documents_version: str,
    cache_paths: _CachePaths,
    embedding_name: str,
    collection_name: str,
) -> ChromaIndexPaths:
    return ChromaIndexPaths(
        index_root=cache_paths.cache_root,
        cache_path=cache_paths.cache_path,
        chroma_path=cache_paths.chroma_path,
        catalog_digest=catalog_digest,
        documents_version=documents_version,
        embedding_name=embedding_name,
        collection_name=collection_name,
    )


def _cache_ready(
    *,
    cache_paths: _CachePaths,
    catalog_digest: str,
    documents_version: str,
    embedding_fn: Any,
    embedding_name: str,
    collection_name: str,
) -> bool:
    try:
        _require_cache(
            cache_paths=cache_paths,
            catalog_digest=catalog_digest,
            documents_version=documents_version,
            embedding_fn=embedding_fn,
            embedding_name=embedding_name,
            collection_name=collection_name,
        )
    except (FileNotFoundError, ValueError):
        return False
    return True


def _require_cache(
    *,
    cache_paths: _CachePaths,
    catalog_digest: str,
    documents_version: str,
    embedding_fn: Any,
    embedding_name: str,
    collection_name: str,
) -> None:
    if not cache_paths.chroma_path.exists():
        raise FileNotFoundError(
            f"Cached Chroma directory not found at {cache_paths.chroma_path}."
        )

    try:
        from chromadb.errors import NotFoundError
    except ModuleNotFoundError as exc:
        raise _missing_chroma_extra_error(exc.name) from exc

    try:
        collection = create_chroma_client(cache_paths.chroma_path).get_collection(
            collection_name,
            embedding_function=embedding_fn,
        )
    except NotFoundError as exc:
        raise FileNotFoundError(
            f"Cached Chroma collection '{collection_name}' was not found in {cache_paths.chroma_path}."
        ) from exc

    metadata = _collection_metadata_from_collection(collection)
    expected = {
        "catalog_digest": catalog_digest,
        "documents_version": documents_version,
        "embedding_name": embedding_name,
    }
    if not _metadata_matches(metadata, expected):
        raise ValueError(
            "Cached Chroma collection does not match the catalog, document builder, or embedding function."
        )

    try:
        expected_count = int(metadata["document_count"])
    except (KeyError, ValueError) as exc:
        raise ValueError(
            "Cached Chroma collection is missing document_count metadata."
        ) from exc
    if collection.count() != expected_count:
        raise ValueError(
            "Cached Chroma collection does not match the catalog document count."
        )


def _rebuild_cache(
    *,
    catalog: Catalog,
    documents: _Documents,
    embedding_fn: Any,
    embedding_name: str,
    cache_paths: _CachePaths,
    collection_name: str,
) -> None:
    cache_paths.cache_path.parent.mkdir(parents=True, exist_ok=True)
    staged_root = Path(
        tempfile.mkdtemp(
            prefix=f".{cache_paths.cache_path.name}-",
            dir=str(cache_paths.cache_path.parent),
        )
    )
    staged_chroma_path = staged_root / DEFAULT_CHROMA_DIRNAME

    try:
        staged_root.mkdir(parents=True, exist_ok=True)
        staged_chroma_path.mkdir(parents=True, exist_ok=True)
        collection = create_chroma_client(staged_chroma_path).get_or_create_collection(
            collection_name,
            embedding_function=embedding_fn,
            metadata=_collection_metadata(
                catalog,
                documents,
                embedding_name=embedding_name,
            ),
        )
        ChromaIndex(
            catalog=catalog,
            collection=collection,
            embedding_name=embedding_name,
            collection_name=collection_name,
            paths=_index_paths(
                catalog_digest=catalog.digest(),
                documents_version=documents.version,
                cache_paths=_CachePaths(
                    cache_root=cache_paths.cache_root,
                    cache_path=staged_root,
                    chroma_path=staged_chroma_path,
                ),
                embedding_name=embedding_name,
                collection_name=collection_name,
            ),
            documents=documents,
        ).build()
    except Exception:
        shutil.rmtree(staged_root, ignore_errors=True)
        raise

    _replace_cache(staged_root, cache_paths.cache_path)


def _open_index(
    *,
    catalog: Catalog,
    embedding_fn: Any,
    embedding_name: str,
    cache_paths: _CachePaths,
    collection_name: str,
    catalog_digest: str,
    documents_version: str,
) -> ChromaIndex:
    _require_cache(
        cache_paths=cache_paths,
        catalog_digest=catalog_digest,
        documents_version=documents_version,
        embedding_fn=embedding_fn,
        embedding_name=embedding_name,
        collection_name=collection_name,
    )
    collection = create_chroma_client(cache_paths.chroma_path).get_collection(
        collection_name,
        embedding_function=embedding_fn,
    )
    return ChromaIndex(
        catalog=catalog,
        collection=collection,
        embedding_name=embedding_name,
        collection_name=collection_name,
        paths=_index_paths(
            catalog_digest=catalog_digest,
            documents_version=documents_version,
            cache_paths=cache_paths,
            embedding_name=embedding_name,
            collection_name=collection_name,
        ),
    )


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


def _build_documents(catalog: Catalog) -> _Documents:
    version, build_docs_df = _load_documents_api()
    frame = build_docs_df(
        catalog.guidelines(),
        catalog.references(),
    )
    return _Documents(
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


def _documents_version() -> str:
    version, _ = _load_documents_api()
    return str(version)


def _documents_digest(docs_df: pl.DataFrame, *, version: str) -> str:
    hasher = hashlib.sha256()
    hasher.update(version.encode("utf-8"))
    for row in docs_df.select("id", "doc", "metadata").sort("id").to_dicts():
        payload = json.dumps(row, sort_keys=True, separators=(",", ":"), default=str)
        hasher.update(payload.encode("utf-8"))
    return hasher.hexdigest()


def _collection_metadata(
    catalog: Catalog,
    documents: _Documents,
    *,
    embedding_name: str | None = None,
) -> dict[str, str]:
    metadata = {
        "catalog_digest": catalog.digest(),
        "document_count": str(documents.count),
        "documents_digest": documents.digest,
        "documents_version": documents.version,
    }
    if embedding_name is not None:
        metadata["embedding_name"] = embedding_name
    return metadata


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


def _is_missing_chroma_dependency(exc: ModuleNotFoundError) -> bool:
    name = exc.name
    if name is None:
        return False
    return name in {
        "chromadb",
        "tqdm",
    } or name.startswith("chromadb.")


__all__ = [
    "CATALOG_COLLECTION_NAME",
    "CacheMode",
    "ChromaIndex",
    "ChromaIndexPaths",
]
