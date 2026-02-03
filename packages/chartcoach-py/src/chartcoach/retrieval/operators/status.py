from __future__ import annotations

from dataclasses import dataclass

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.strategy.pipelines.focus import FocusMode
from chartcoach.retrieval.strategy.pipelines.guideline_status import (
    StatusScorer,
    filter_guidelines_by_status,
)
from chartcoach.retrieval.strategy.types import RetrievalRequest


@dataclass(frozen=True, slots=True)
class StatusFilterPlan:
    use_status_filter: bool
    candidate_k: int


def plan_status_filter(
    *,
    focus_mode: FocusMode,
    requested_k: int,
    base_candidate_k: int | None = None,
    status_scorer: StatusScorer | None,
    status_filter_enabled: bool,
) -> StatusFilterPlan:
    """Plan if/when a pipeline should apply the guideline-status filter.

    The filter is only meaningful when:
    - the focus mode is not "all",
    - the strategy is configured to use status filtering, and
    - a status scorer/module is available.
    """

    output_k = max(0, int(requested_k))
    candidate_k = max(output_k, int(base_candidate_k or output_k))
    if (
        focus_mode == "all"
        or not status_filter_enabled
        or status_scorer is None
        or output_k <= 0
    ):
        return StatusFilterPlan(use_status_filter=False, candidate_k=candidate_k)

    cfg = status_scorer.config
    candidate_k = max(candidate_k, output_k * int(cfg.candidate_multiplier))
    return StatusFilterPlan(use_status_filter=True, candidate_k=candidate_k)


def apply_status_filter(
    *,
    request: RetrievalRequest,
    entries: list[CatalogEntry],
    output_k: int,
    focus_mode: FocusMode,
    status_scorer: StatusScorer,
) -> tuple[list[CatalogEntry], dict[str, object]]:
    """Apply the guideline-status filter and return (selected_entries, meta)."""

    return filter_guidelines_by_status(
        request=request,
        entries=entries,
        output_k=int(output_k),
        focus=focus_mode,
        status_module=status_scorer.module,
        config=status_scorer.config,
    )
