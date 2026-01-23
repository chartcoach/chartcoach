"""Guideline retrieval (very minimal for now)."""

from __future__ import annotations

from .dspy_adapters import (
    get_image_item_by_role,
    get_text_by_role,
    image_item_to_dspy_image,
    require_image_item_by_role,
    require_text_by_role,
)
from .head import HeadRetrievalStrategy
from .guideline_browser import GuidelineBrowserStrategy
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
    "HeadRetrievalStrategy",
    "ImageItem",
    "image_item_to_dspy_image",
    "RetrievalRequest",
    "RetrievalResponse",
    "require_image_item_by_role",
    "require_text_by_role",
    "TableItem",
    "TextItem",
]
