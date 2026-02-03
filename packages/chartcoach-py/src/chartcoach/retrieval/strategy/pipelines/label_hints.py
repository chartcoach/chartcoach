from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

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
    mode: Literal["typed", "substring"] = "typed",
    min_candidate_ids: int = 25,
    value_token_match_threshold: float = 0.6,
) -> tuple[set[str], dict[str, list[str]]]:
    """Return (candidate_ids, matched_labels_by_hint).

    Two matching modes are supported:
    - typed: interpret hints as key:value labels when possible and match by facet/value
      overlap (higher precision; more controlled candidate pools).
    - substring: permissive substring matching over normalized labels (higher recall).

    For robustness, typed matching falls back to substring matching when it yields
    too few candidates.
    """

    hints = [_normalize_label(h) for h in label_hints if _normalize_label(h)]
    if not hints:
        return set(), {}

    mode = mode if mode in {"typed", "substring"} else "typed"
    min_candidate_ids = max(0, int(min_candidate_ids))
    value_token_match_threshold = max(0.0, min(1.0, float(value_token_match_threshold)))

    def _match_substring() -> tuple[set[str], dict[str, list[str]]]:
        matched_labels_by_hint: dict[str, list[str]] = {h: [] for h in hints}
        candidate_ids: set[str] = set()

        for entry in catalog.entries:
            labels = entry.guideline.labels or []
            norm_labels = [
                _normalize_label(lbl) for lbl in labels if _normalize_label(lbl)
            ]
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

        matched_labels_by_hint = {
            hint: sorted(set(labels)) for hint, labels in matched_labels_by_hint.items()
        }
        return candidate_ids, matched_labels_by_hint

    def _split_kv(text: str) -> tuple[str | None, str]:
        if ":" not in text:
            return None, text
        key, value = text.split(":", 1)
        key = key.strip()
        value = value.strip()
        return (key or None), value

    def _tokens(value: str) -> set[str]:
        # Normalize to dash-separated tokens, then split (treat ':' as separator too).
        cleaned = _normalize_label(value).replace(":", "-")
        return set(t for t in cleaned.split("-") if t)

    def _match_typed() -> tuple[set[str], dict[str, list[str]]]:
        matched_labels_by_hint: dict[str, list[str]] = {h: [] for h in hints}
        candidate_ids: set[str] = set()

        parsed_hints: list[tuple[str, str | None, set[str]]] = []
        for hint in hints:
            key, value = _split_kv(hint)
            parsed_hints.append((hint, key, _tokens(value)))

        for entry in catalog.entries:
            labels = entry.guideline.labels or []
            norm_labels = [
                _normalize_label(lbl) for lbl in labels if _normalize_label(lbl)
            ]
            if not norm_labels:
                continue

            hit = False
            for hint_raw, hint_key, hint_tokens in parsed_hints:
                for lbl in norm_labels:
                    lbl_key, lbl_value = _split_kv(lbl)
                    if hint_key is not None:
                        if lbl_key != hint_key:
                            continue
                        if not hint_tokens:
                            matched_labels_by_hint[hint_raw].append(lbl)
                            hit = True
                            continue
                        lbl_tokens = _tokens(lbl_value)
                        if not lbl_tokens:
                            continue
                        overlap = len(hint_tokens & lbl_tokens) / max(
                            1, len(hint_tokens)
                        )
                        if overlap >= value_token_match_threshold:
                            matched_labels_by_hint[hint_raw].append(lbl)
                            hit = True
                    else:
                        # Unkeyed hint: only match against label values (not keys).
                        if not hint_tokens:
                            continue
                        lbl_tokens = _tokens(lbl_value)
                        if not lbl_tokens:
                            continue
                        overlap = len(hint_tokens & lbl_tokens) / max(
                            1, len(hint_tokens)
                        )
                        if overlap >= value_token_match_threshold:
                            matched_labels_by_hint[hint_raw].append(lbl)
                            hit = True

            if hit:
                candidate_ids.add(entry.id)

        matched_labels_by_hint = {
            hint: sorted(set(labels)) for hint, labels in matched_labels_by_hint.items()
        }
        return candidate_ids, matched_labels_by_hint

    if mode == "substring":
        return _match_substring()

    typed_ids, typed_matches = _match_typed()
    if min_candidate_ids and len(typed_ids) < min_candidate_ids:
        return _match_substring()
    return typed_ids, typed_matches


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
