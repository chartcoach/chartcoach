"""Composable retrieval operators (shared pipeline stages).

These utilities exist to keep strategy implementations small and readable by
factoring out common retrieval mechanics (role-aware fallback, status filtering,
etc.) while preserving strategy-level composition.
"""

from .search import (
    search_dense_with_focus,
    search_fts_with_focus,
    search_hybrid_with_focus,
)
from .status import apply_status_filter, plan_status_filter

__all__ = [
    "apply_status_filter",
    "plan_status_filter",
    "search_dense_with_focus",
    "search_fts_with_focus",
    "search_hybrid_with_focus",
]
