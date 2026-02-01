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
_DONUT_RE = re.compile(r"\b(donut|pie|slice|slices|ring|radial|rose)\b", re.IGNORECASE)
_PYRAMID_RE = re.compile(r"\b(population pyramid|pyramid)\b", re.IGNORECASE)
_BAR_RE = re.compile(
    r"\b(bar chart|column chart|rank|ranking|ranked|top|highest|lowest|most|least|largest|smallest)\b",
    re.IGNORECASE,
)
_DOT_RE = re.compile(r"\b(dot|dots|dotplot|dot plot|icon array|pictograph)\b", re.IGNORECASE)

_COMPARE_RE = re.compile(r"\b(compare|contrast|vs|versus|compared to|in comparison)\b", re.IGNORECASE)
_RANK_RE = re.compile(r"\b(rank|ranking|top|largest|most|least)\b", re.IGNORECASE)
_CHANGE_RE = re.compile(r"\b(change|changed|delta|difference|recovering|increase|decrease)\b", re.IGNORECASE)
_PART_WHOLE_RE = re.compile(r"\b(share|shares|percent|percentage|100%|part-to-whole|proportion)\b", re.IGNORECASE)
_MULTIVARIATE_RE = re.compile(r"\b(two variables|two measures|two metrics|bivariate|multivariate|multi-variate|on average|ratio)\b", re.IGNORECASE)

_TIMEPOINT_RE = re.compile(
    r"\b(?:q[1-4][\s/-]?(?:19\d{2}|20\d{2})|(?:19\d{2}|20\d{2}))\b",
    re.IGNORECASE,
)
_TWO_TIMEPOINT_CUE_RE = re.compile(
    r"\b(vs|versus|compares?|compared to|one year earlier|year earlier)\b",
    re.IGNORECASE,
)


_GENERAL_CHART_LABELS = {
    "chart:any",
    "chart:general",
    "chart:generic",
    "chart:multi",
    "chart:multiple",
}

_GENERAL_TASK_LABELS = {"task:any", "task:interpret", "task:communicate"}

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


_CHART_LABEL_HINT = {
    "chart:area": "area chart",
    "chart:bar": "bar chart",
    "chart:cartogram": "cartogram",
    "chart:choropleth": "choropleth map",
    "chart:donut": "donut chart",
    "chart:dot": "dot plot",
    "chart:icon-array": "icon array",
    "chart:line": "line chart",
    "chart:map": "map",
    "chart:pie": "pie chart",
    "chart:radial": "radial chart",
    "chart:sankey": "sankey/alluvial",
    "chart:slope": "slope chart",
    "chart:time-series": "time series",
    "chart:distribution": "distribution plot",
}

_TASK_LABEL_HINT = {
    "task:compare": "compare",
    "task:rank": "rank/sort",
    "task:trend": "trend over time",
    "task:track-change": "track change",
    "task:detect-change": "detect change",
    "task:flow": "follow flows",
    "task:part-to-whole": "part-to-whole",
    "task:characterize-distribution": "characterize distribution",
    "task:encode-multivariate": "multivariate encoding",
    "task:annotate": "annotations",
    "task:highlight": "highlighting",
}


@dataclass(frozen=True, slots=True)
class ScenarioHintsV4:
    chart_labels: frozenset[str]
    task_labels: frozenset[str]
    active_domains: frozenset[str]


def infer_hints_v4(*, title: str | None, situation: str) -> ScenarioHintsV4:
    title = (title or "").strip()
    situation = situation.strip()
    text = f"{title}\n{situation}".strip()
    if not text:
        return ScenarioHintsV4(
            chart_labels=frozenset(_GENERAL_CHART_LABELS),
            task_labels=frozenset(_GENERAL_TASK_LABELS),
            active_domains=frozenset({"domain:news"}),
        )

    chart_labels: set[str] = set()
    task_labels: set[str] = set()

    # High-salience chart forms.
    if _FLOW_RE.search(text):
        chart_labels.add("chart:sankey")
        task_labels.add("task:flow")

    if _MAP_RE.search(text):
        chart_labels.update(
            {"chart:map", "chart:choropleth", "chart:cartogram", "chart:icon-array"}
        )
        task_labels.add("task:locate")

    if _DONUT_RE.search(text):
        chart_labels.update({"chart:donut", "chart:pie", "chart:radial"})
        task_labels.add("task:part-to-whole")

    if _DOT_RE.search(text):
        chart_labels.update({"chart:dot", "chart:icon-array", "chart:pictograph"})
        task_labels.add("task:proportion")

    if _PYRAMID_RE.search(text):
        # Population pyramids are effectively paired distributions (mirrored bars).
        chart_labels.update({"chart:bar", "chart:distribution"})
        task_labels.add("task:characterize-distribution")

    # Time cues: differentiate two-time-point comparisons vs full time-series.
    if _TIME_RE.search(text):
        timepoints = {m.group(0).lower() for m in _TIMEPOINT_RE.finditer(text)}
        is_two_timepoint = bool(_TWO_TIMEPOINT_CUE_RE.search(text) and len(timepoints) >= 2)
        if is_two_timepoint and not _PYRAMID_RE.search(text):
            chart_labels.update({"chart:slope", "chart:dot", "chart:bar"})
            task_labels.update({"task:compare", "task:detect-change", "task:track-change"})
        else:
            chart_labels.update({"chart:line", "chart:time-series", "chart:area"})
            task_labels.update({"task:trend", "task:track-change"})

    if _BAR_RE.search(text):
        chart_labels.update({"chart:bar", "chart:stacked-bar"})
        task_labels.update({"task:rank", "task:compare"})

    # Task cues (chart-agnostic).
    if _COMPARE_RE.search(text):
        task_labels.add("task:compare")
    if _RANK_RE.search(text):
        task_labels.add("task:rank")
    if _CHANGE_RE.search(text):
        task_labels.add("task:detect-change")
    if _PART_WHOLE_RE.search(text):
        task_labels.add("task:part-to-whole")
    if _MULTIVARIATE_RE.search(text):
        task_labels.add("task:encode-multivariate")

    if not chart_labels:
        chart_labels.update(_GENERAL_CHART_LABELS)
    if not task_labels:
        task_labels.update(_GENERAL_TASK_LABELS)

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

    return ScenarioHintsV4(
        chart_labels=frozenset(chart_labels),
        task_labels=frozenset(task_labels),
        active_domains=frozenset(active_domains),
    )


def _is_map_hint(hints: ScenarioHintsV4) -> bool:
    return any(
        l in hints.chart_labels for l in ("chart:map", "chart:choropleth", "chart:cartogram")
    )


def chart_bonus_v4(*, guideline_labels: list[str], hints: ScenarioHintsV4) -> float:
    chart_labels = [l for l in guideline_labels if l.startswith("chart:")]
    if not chart_labels:
        return 0.0

    if any(l in hints.chart_labels for l in chart_labels):
        return 0.12
    if any(l in _GENERAL_CHART_LABELS for l in chart_labels):
        return 0.03

    # Only penalize clear incompatibilities; allow alternate chart suggestions.
    if _is_map_hint(hints) and not any(
        l in chart_labels for l in ("chart:map", "chart:choropleth", "chart:cartogram")
    ):
        return -0.05
    if "chart:sankey" in hints.chart_labels and "chart:sankey" not in chart_labels:
        return -0.05
    return 0.0


def task_bonus_v4(*, guideline_labels: list[str], hints: ScenarioHintsV4) -> float:
    task_labels = [l for l in guideline_labels if l.startswith("task:")]
    if not task_labels:
        return 0.0
    if any(l in hints.task_labels for l in task_labels):
        return 0.06
    if any(l in _GENERAL_TASK_LABELS for l in task_labels):
        return 0.02
    return 0.0


def domain_penalty_v4(*, guideline_labels: list[str], hints: ScenarioHintsV4) -> float:
    domains = [l for l in guideline_labels if l.startswith("domain:")]
    if not domains:
        return 0.0

    if any(d in hints.active_domains for d in domains):
        return 0.0
    return -0.10


def should_exclude_guideline_v4(*, guideline_labels: list[str], hints: ScenarioHintsV4) -> bool:
    if any(l.startswith("pipeline:") for l in guideline_labels):
        return True

    domains = [l for l in guideline_labels if l.startswith("domain:")]
    if not domains:
        return False

    for d in domains:
        if d in _HARD_EXCLUDE_DOMAIN_LABELS and d not in hints.active_domains:
            return True
    return False


def build_search_text_v4(*, title: str | None, situation: str, hints: ScenarioHintsV4) -> str:
    title = (title or "").strip()
    situation = situation.strip()
    if title and situation:
        base = f"{title}\n\n{situation}"
    else:
        base = title or situation

    base = base.strip()
    if not base:
        return ""

    chart_terms = [
        _CHART_LABEL_HINT[label]
        for label in sorted(hints.chart_labels)
        if label in _CHART_LABEL_HINT
    ]
    task_terms = [
        _TASK_LABEL_HINT[label]
        for label in sorted(hints.task_labels)
        if label in _TASK_LABEL_HINT
    ]

    facets: list[str] = []
    if chart_terms and not any(l in _GENERAL_CHART_LABELS for l in hints.chart_labels):
        facets.append(f"Likely chart forms: {', '.join(chart_terms)}.")
    if task_terms and not any(l in _GENERAL_TASK_LABELS for l in hints.task_labels):
        facets.append(f"Key tasks: {', '.join(task_terms)}.")

    facet_text = "\n".join(facets).strip()
    if facet_text:
        base = f"{base}\n\n{facet_text}"

    return (
        f"{base}\n\n"
        "Task: improve the existing visualization for a general news reader audience."
    )
