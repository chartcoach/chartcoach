"""Embedding utilities.

This package is split into:
- dependency-light utilities (text extraction + catalog orchestration)
- optional embedding backends (e.g., `chartcoach.embedding.atlas`)

Import `chartcoach.embedding.atlas` directly if you need embedding/projecting.
"""

from __future__ import annotations

from .catalog_embedder import CatalogEmbedder
from .text_sources import (
    CatalogTextSource,
    DEFAULT_TEXT_SOURCES,
    GuidelineAbstractTextSource,
    GuidelineFieldTextSource,
    GuidelineLabelsTextSource,
    SectionsTextSource,
)
from .vectors import vector_matrix

__all__ = [
    "CatalogEmbedder",
    "CatalogTextSource",
    "DEFAULT_TEXT_SOURCES",
    "GuidelineAbstractTextSource",
    "GuidelineFieldTextSource",
    "GuidelineLabelsTextSource",
    "SectionsTextSource",
    "vector_matrix",
]

try:
    from .atlas import TextProjector, embed_text, project_embedded_text  # noqa: F401

    __all__.extend(["TextProjector", "embed_text", "project_embedded_text"])
except ImportError:  # pragma: no cover
    pass
