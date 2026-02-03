from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Literal, NotRequired, Required, Sequence, TypedDict, cast

import numpy as np
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.embedding import (
    CatalogEmbedder,
    CatalogTextSource,
    GuidelineAbstractTextSource,
    GuidelineFieldTextSource,
    GuidelineLabelsTextSource,
    SectionsTextSource,
    SectionsWithTitleTextSource,
    vector_matrix,
)
from chartcoach.index import (
    InMemoryVectorIndexBackend,
    LanceVectorIndex,
    VectorIndex,
    VectorIndexBackend,
)


_SECRET_EMBEDDING_ARG_KEYS = {
    "api_key",
    "api_base",
    # Common alternate spellings seen in client code.
    "apiKey",
    "apiBase",
}


def _sha256_hexdigest(payload: object) -> str:
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), default=str
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class EmbeddingMeta(TypedDict):
    model: str
    text_projector_type: str
    embedding_column: str
    args: dict[str, object]
    digest: str


class TextSourceMeta(TypedDict):
    type: Required[str]
    roles: NotRequired[list[str] | None]
    field: NotRequired[str]
    role: NotRequired[str | None]


class CatalogVectorIndexMeta(TypedDict):
    embedding: EmbeddingMeta
    index_backend: str
    text_sources: list[TextSourceMeta]


def describe_text_source(source: object) -> TextSourceMeta:
    if isinstance(source, SectionsTextSource):
        roles = None if source.roles is None else sorted(source.roles)
        return cast(TextSourceMeta, {"type": "sections", "roles": roles})
    if isinstance(source, SectionsWithTitleTextSource):
        roles = None if source.roles is None else sorted(source.roles)
        return cast(
            TextSourceMeta,
            {
                "type": "sections_with_title",
                "roles": roles,
            },
        )
    if isinstance(source, GuidelineAbstractTextSource):
        return cast(
            TextSourceMeta,
            {"type": "guideline_abstract", "role": source.role},
        )
    if isinstance(source, GuidelineFieldTextSource):
        return cast(
            TextSourceMeta,
            {"type": "guideline_field", "field": source.field, "role": source.role},
        )
    if isinstance(source, GuidelineLabelsTextSource):
        return cast(
            TextSourceMeta,
            {"type": "guideline_labels", "role": source.role},
        )
    return cast(TextSourceMeta, {"type": source.__class__.__name__})


@dataclass(frozen=True, slots=True)
class EmbeddingConfig:
    model: str = "all-MiniLM-L6-v2"
    text_projector_type: Literal["sentence_transformers", "litellm"] = (
        "sentence_transformers"
    )
    embedding_column: str = "embedding"
    text_projector_args: dict[str, object] = field(default_factory=dict)

    def safe_args(self) -> dict[str, object]:
        return {
            k: v
            for k, v in self.text_projector_args.items()
            if k not in _SECRET_EMBEDDING_ARG_KEYS
        }

    def digest(self) -> str:
        return _sha256_hexdigest(
            {
                "version": 1,
                "model": self.model,
                "text_projector_type": self.text_projector_type,
                "embedding_column": self.embedding_column,
                "args": self.safe_args(),
            }
        )[:16]

    def meta(self) -> EmbeddingMeta:
        return EmbeddingMeta(
            model=self.model,
            text_projector_type=self.text_projector_type,
            embedding_column=self.embedding_column,
            args=self.safe_args(),
            digest=self.digest(),
        )


def _resolve_index_backend_label(index: VectorIndex) -> str:
    backend = getattr(index, "backend", None)
    return backend if isinstance(backend, str) else "unknown"


@dataclass(slots=True)
class CatalogVectorIndex:
    """Embedded catalog + backend-agnostic vector index."""

    catalog: Catalog
    sources: tuple[CatalogTextSource, ...]
    config: EmbeddingConfig
    embedded_text_df: pl.DataFrame
    index: VectorIndex

    @classmethod
    def from_catalog(
        cls,
        catalog: Catalog,
        *,
        sources: Sequence[CatalogTextSource],
        config: EmbeddingConfig,
        index_backend: VectorIndexBackend | None = None,
    ) -> "CatalogVectorIndex":
        embedder = CatalogEmbedder(catalog)
        text_df = embedder.text_df(sources=sources)

        try:
            from chartcoach.embedding import embed_text
        except ImportError as e:  # pragma: no cover
            raise RuntimeError(
                "Embedding backend is not available. Install `chartcoach[embedding]`."
            ) from e

        embedded_text_df = embed_text(
            text_df,
            model=config.model,
            batch_size=256,
            text_projector_type=config.text_projector_type,
            embedding_column=config.embedding_column,
            **config.text_projector_args,
        )

        backend = (
            InMemoryVectorIndexBackend() if index_backend is None else index_backend
        )
        index = backend.index(
            embedded_text_df, embedding_column=config.embedding_column
        )

        return cls(
            catalog=catalog,
            sources=tuple(sources),
            config=config,
            embedded_text_df=embedded_text_df,
            index=index,
        )

    def embed_query(self, text: str) -> np.ndarray:
        try:
            from chartcoach.embedding import embed_text
        except ImportError as e:  # pragma: no cover
            raise RuntimeError(
                "Embedding backend is not available. Install `chartcoach[embedding]`."
            ) from e

        query_df = pl.DataFrame(
            {
                "id": ["__query__"],
                "role": ["__query__"],
                "content": [text],
            }
        )
        embedded_query_df = embed_text(
            query_df,
            model=self.config.model,
            batch_size=1,
            text_projector_type=self.config.text_projector_type,
            embedding_column=self.config.embedding_column,
            **self.config.text_projector_args,
        )
        vectors = vector_matrix(
            embedded_query_df.get_column(self.config.embedding_column)
        )
        return vectors[0]

    def search(
        self,
        query: np.ndarray,
        *,
        k: int,
        roles: set[str] | None = None,
    ) -> pl.DataFrame:
        return self.index.search(query, k=k, roles=roles)

    def lance(self):
        """Return the underlying Lance index (or raise if a different backend is used)."""

        if getattr(self.index, "backend", None) != "lance":
            raise RuntimeError(
                "This operation requires the Lance backend. "
                "Instantiate CatalogVectorIndex with LanceVectorIndexBackend."
            )
        return cast(LanceVectorIndex, self.index)

    def meta(self) -> CatalogVectorIndexMeta:
        return CatalogVectorIndexMeta(
            embedding=self.config.meta(),
            index_backend=_resolve_index_backend_label(self.index),
            text_sources=[describe_text_source(s) for s in self.sources],
        )
