from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.optional import require_dspy

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


def _normalize_label(text: str) -> str:
    norm = (text or "").strip().lower()
    if not norm:
        return ""
    # Keep ":" to preserve key:value label structure; normalize other punctuation.
    norm = re.sub(r"[^a-z0-9:]+", "-", norm)
    return norm.strip("-")


def match_catalog_ids_by_label_hints(
    *,
    catalog: Catalog,
    label_hints: list[str],
) -> tuple[set[str], dict[str, list[str]]]:
    """Return (candidate_ids, matched_labels_by_hint).

    Matching is intentionally permissive (substring-based) to preserve recall when
    the LM produces approximate label strings.
    """

    hints = [_normalize_label(h) for h in label_hints if _normalize_label(h)]
    if not hints:
        return set(), {}

    matched_labels_by_hint: dict[str, list[str]] = {h: [] for h in hints}
    candidate_ids: set[str] = set()

    for entry in catalog.entries:
        labels = entry.guideline.labels or []
        norm_labels = [_normalize_label(lbl) for lbl in labels if _normalize_label(lbl)]
        if not norm_labels:
            continue

        hit = False
        for hint in hints:
            for lbl in norm_labels:
                if hint in lbl:
                    matched_labels_by_hint[hint].append(lbl)
                    hit = True
        if hit:
            candidate_ids.add(entry.id)

    # Deduplicate matched labels for readability.
    matched_labels_by_hint = {
        hint: sorted(set(labels)) for hint, labels in matched_labels_by_hint.items()
    }
    return candidate_ids, matched_labels_by_hint


class LabelHintsSignature(dspy.Signature):
    """Predict label-like hints to prune the catalog before retrieval."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "It may include optional chart image notes. "
            "Produce label-like hints that help find relevant visualization design guidelines."
        )
    )
    focus: str = dspy.InputField(
        desc="One of: all, violations, satisfied. Use it to bias hints toward what to retrieve."
    )
    n: int = dspy.InputField(
        desc="Number of label hints to return.", ge=1, le=12, default=8
    )

    canonical_query: str = dspy.OutputField(
        desc=(
            "A short retrieval query that captures the main chart intent and likely design concerns. "
            "Keep key domain nouns/variables and chart-type terms if known."
        )
    )
    label_hints: list[str] = dspy.OutputField(
        desc=(
            "A compact list of label-like hints to restrict the guideline catalog. "
            "Prefer key:value forms (e.g., 'audience:general', 'topic:accessibility') when sensible, "
            "but short keywords are also acceptable."
        )
    )


@dataclass(frozen=True, slots=True)
class LabelHintsConfig:
    n: int = 8

