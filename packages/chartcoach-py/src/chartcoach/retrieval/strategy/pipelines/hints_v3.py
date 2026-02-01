from __future__ import annotations

import re
from dataclasses import dataclass


_ELECTION_RE = re.compile(
    r"\b(vote|votes|voter|voters|voting|election|elections|party|parties|turnout|poll|polls)\b",
    re.IGNORECASE,
)
_GENDER_RE = re.compile(
    r"\b(gender|women|woman|men|man|female|male)\b",
    re.IGNORECASE,
)
_DEMOGRAPHICS_RE = re.compile(
    r"\b(population|demograph|age distribution|working age|elderly|children)\b",
    re.IGNORECASE,
)
_HEALTH_RE = re.compile(
    r"\b(health|patient|hospital|treatment|vaccine|disease|risk reduction)\b",
    re.IGNORECASE,
)

_MAP_RE = re.compile(
    r"\b(map|continent|continents|geograph|region|regions|choropleth|cartogram)\b",
    re.IGNORECASE,
)
_FLOW_RE = re.compile(r"\b(flow|flows|sankey|alluvial)\b", re.IGNORECASE)
_TIME_RE = re.compile(
    r"\b(over time|time series|time-series|trend|trends|quarter|q[1-4])\b",
    re.IGNORECASE,
)
_DONUT_RE = re.compile(
    r"\b(donut|pie|slice|slices|ring|radial|rose)\b", re.IGNORECASE
)
_PYRAMID_RE = re.compile(r"\b(population pyramid|pyramid)\b", re.IGNORECASE)
_BAR_RE = re.compile(
    r"\b(bar chart|column chart|rank|ranking|ranked|top|highest|lowest|most|least|largest|smallest)\b",
    re.IGNORECASE,
)


_GENERAL_CHART_LABELS = {
    "chart:any",
    "chart:general",
    "chart:generic",
    "chart:multi",
    "chart:multiple",
}

_HARD_EXCLUDE_DOMAIN_LABELS = {
    "domain:elections",
    # These domains are common false positives for general-news scenarios.
    "domain:health",
    "domain:health-risk",
    "domain:healthcare",
    "domain:risk-communication",
    "domain:hurricane",
    "domain:hurricane-forecast",
    "domain:tropical-cyclone",
    "domain:weather",
}


@dataclass(frozen=True, slots=True)
class ScenarioHintsV3:
    is_election_related: bool
    chart_labels: frozenset[str]
    active_domains: frozenset[str]


def infer_hints_v3(*, title: str | None, situation: str) -> ScenarioHintsV3:
    title = (title or "").strip()
    situation = situation.strip()
    text = f"{title}\n{situation}".strip()
    if not text:
        return ScenarioHintsV3(
            is_election_related=False,
            chart_labels=frozenset(_GENERAL_CHART_LABELS),
            active_domains=frozenset({"domain:news"}),
        )

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
    if _BAR_RE.search(text):
        chart_labels.update({"chart:bar", "chart:stacked-bar"})

    if not chart_labels:
        chart_labels.update(_GENERAL_CHART_LABELS)

    active_domains: set[str] = {"domain:news"}
    if _ELECTION_RE.search(text):
        active_domains.add("domain:elections")
    if _GENDER_RE.search(text):
        active_domains.add("domain:gender")
    if _DEMOGRAPHICS_RE.search(text):
        active_domains.add("domain:demographics")
    if _HEALTH_RE.search(text):
        active_domains.update(
            {"domain:health", "domain:health-risk", "domain:healthcare"}
        )

    return ScenarioHintsV3(
        is_election_related="domain:elections" in active_domains,
        chart_labels=frozenset(chart_labels),
        active_domains=frozenset(active_domains),
    )


def chart_bonus_v3(*, guideline_labels: list[str], hints: ScenarioHintsV3) -> float:
    chart_labels = [l for l in guideline_labels if l.startswith("chart:")]
    if not chart_labels:
        return 0.0

    if any(l in hints.chart_labels for l in chart_labels):
        return 0.12
    if any(l in _GENERAL_CHART_LABELS for l in chart_labels):
        return 0.03
    return -0.08


def domain_penalty_v3(*, guideline_labels: list[str], hints: ScenarioHintsV3) -> float:
    domains = [l for l in guideline_labels if l.startswith("domain:")]
    if not domains:
        return 0.0

    # Softly penalize off-domain material; hard-exclude a few domains separately.
    if any(d in hints.active_domains for d in domains):
        return 0.0
    return -0.10


def should_exclude_guideline_v3(*, guideline_labels: list[str], hints: ScenarioHintsV3) -> bool:
    if any(l.startswith("pipeline:") for l in guideline_labels):
        return True

    domains = [l for l in guideline_labels if l.startswith("domain:")]
    if not domains:
        return False

    for d in domains:
        if d in _HARD_EXCLUDE_DOMAIN_LABELS and d not in hints.active_domains:
            return True
    return False


def build_search_text_v3(*, title: str | None, situation: str) -> str:
    title = (title or "").strip()
    situation = situation.strip()
    if title and situation:
        base = f"{title}\n\n{situation}"
    else:
        base = title or situation

    base = base.strip()
    if not base:
        return ""

    return (
        f"{base}\n\n"
        "Task: improve the existing visualization for a general news reader audience."
    )
