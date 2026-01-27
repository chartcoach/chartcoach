"""Retrieval domain layer (strategies + request/response types).

Higher-level use-cases live in `chartcoach.retrieval.service`.
Interfaces (CLI / FastAPI) live in `chartcoach.retrieval.cli` and
`chartcoach.retrieval.server`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .optional import is_dspy_available
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
    "ImageItem",
    "RetrievalRequest",
    "RetrievalResponse",
    "TableItem",
    "TextItem",
]

_DSPY_AVAILABLE = is_dspy_available()

if TYPE_CHECKING or _DSPY_AVAILABLE:
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

    if _DSPY_AVAILABLE:
        __all__ = [
            "ContextItem",
            "FileItem",
            "ImageItem",
            "RetrievalRequest",
            "RetrievalResponse",
            "TableItem",
            "TextItem",
            "GuidelineBrowserStrategy",
            "RetrievalStrategy",
            "StrategyInfo",
            "StrategyRegistration",
            "create_default_strategy_registrations",
            "get_image_item_by_role",
            "get_text_by_role",
            "image_item_to_dspy_image",
            "require_image_item_by_role",
            "require_text_by_role",
        ]
