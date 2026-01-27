"""Retrieval domain layer (strategies + request/response types).

Higher-level use-cases live in `chartcoach.retrieval.service`.
Interfaces (CLI / FastAPI) live in `chartcoach.retrieval.cli` and
`chartcoach.retrieval.server`.
"""

from __future__ import annotations

from .base import RetrievalStrategy, StrategyInfo
from .dspy_adapters import (
    get_image_item_by_role,
    get_text_by_role,
    image_item_to_dspy_image,
    require_image_item_by_role,
    require_text_by_role,
)
from .guideline_browser import GuidelineBrowserStrategy
from .registry import StrategyRegistration, create_default_strategy_registrations
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
    "RetrievalRequest",
    "RetrievalResponse",
    "RetrievalStrategy",
    "require_image_item_by_role",
    "require_text_by_role",
    "StrategyInfo",
    "StrategyRegistration",
    "TableItem",
    "TextItem",
    "create_default_strategy_registrations",
]
