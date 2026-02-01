from __future__ import annotations

import re
from dataclasses import dataclass


_ELECTION_RE = re.compile(
    r"\b(vote|votes|voter|voters|voting|election|elections|party|parties|turnout)\b",
    re.IGNORECASE,
)

_MAP_RE = re.compile(
    r"\b(map|continent|continents|geograph|region|regions|choropleth|cartogram)\b",
    re.IGNORECASE,
)
_FLOW_RE = re.compile(r"\b(flow|flows|sankey|alluvial)\b", re.IGNORECASE)
_TIME_RE = re.compile(
    r"\b(over time|time series|time-series|trend|trends|developed|quarter|q[1-4])\b",
    re.IGNORECASE,
)
_DONUT_RE = re.compile(
    r"\b(donut|pie|slice|slices|ring|radial|rose)\b", re.IGNORECASE
)
_PYRAMID_RE = re.compile(r"\b(population pyramid|pyramid)\b", re.IGNORECASE)


_GENERAL_CHART_LABELS = {
    "chart:any",
    "chart:general",
    "chart:generic",
    "chart:multi",
    "chart:multiple",
}


@dataclass(frozen=True, slots=True)
class ScenarioHints:
    """Lightweight scenario signals derived from the situation text."""

    is_election_related: bool
    chart_labels: frozenset[str]


def infer_hints(*, situation: str) -> ScenarioHints:
    text = situation.strip()
    if not text:
        return ScenarioHints(is_election_related=False, chart_labels=frozenset())

    chart_labels: set[str] = set()
    if _FLOW_RE.search(text):
        chart_labels.add("chart:sankey")
    if _DONUT_RE.search(text):
        chart_labels.update({"chart:donut", "chart:pie", "chart:radial"})
    if _PYRAMID_RE.search(text):
        chart_labels.update({"chart:bar", "chart:distribution"})
    if _TIME_RE.search(text):
        chart_labels.update({"chart:line", "chart:time-series", "chart:area"})
    if _MAP_RE.search(text):
        chart_labels.update(
            {
                "chart:map",
                "chart:choropleth",
                "chart:cartogram",
                "chart:icon-array",
            }
        )

    # Default to general chart guidance when the situation text is ambiguous.
    if not chart_labels:
        chart_labels.update(_GENERAL_CHART_LABELS)

    return ScenarioHints(
        is_election_related=bool(_ELECTION_RE.search(text)),
        chart_labels=frozenset(chart_labels),
    )


def chart_bonus(*, guideline_labels: list[str], hints: ScenarioHints) -> float:
    """Small heuristic boost/penalty based on chart label compatibility."""

    chart_labels = [l for l in guideline_labels if l.startswith("chart:")]
    if not chart_labels:
        return 0.0

    if any(l in hints.chart_labels for l in chart_labels):
        return 0.12

    if any(l in _GENERAL_CHART_LABELS for l in chart_labels):
        return 0.03

    # Hard mismatches (e.g., map guidance for donut chart tasks) tend to be noise.
    return -0.08


def build_search_text(*, situation: str) -> str:
    """Build a design-focused query string for non-agentic retrieval strategies."""

    s = situation.strip()
    if not s:
        return ""

    # Keep this short: it affects both lexical matching and dense embeddings.
    return (
        f"{s}\n\n"
        "Task: improve the existing visualization for a general news reader audience."
    )

