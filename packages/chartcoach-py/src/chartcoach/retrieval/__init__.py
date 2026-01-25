"""Guideline retrieval (very minimal for now)."""

from __future__ import annotations

from .dspy_adapters import (
    get_image_item_by_role,
    get_text_by_role,
    image_item_to_dspy_image,
    require_image_item_by_role,
    require_text_by_role,
)
from .guideline_browser import GuidelineBrowserStrategy
from .strategy import RetrievalStrategy
from .types import (
    ContextItem,
    FileItem,
    ImageItem,
    RetrievalRequest,
    RetrievalResponse,
    TableItem,
    TextItem,
)

__all__ = [
    "ContextItem",
    "FileItem",
    "get_image_item_by_role",
    "get_text_by_role",
    "GuidelineBrowserStrategy",
    "ImageItem",
    "image_item_to_dspy_image",
    "RetrievalStrategy",
    "RetrievalRequest",
    "RetrievalResponse",
    "require_image_item_by_role",
    "require_text_by_role",
    "TableItem",
    "TextItem",
]
