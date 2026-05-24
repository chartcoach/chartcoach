from __future__ import annotations

import dataclasses
import re
from collections import Counter, defaultdict
from typing import Literal, NotRequired, TypedDict, cast

import chartcoach as cc
import dspy
from visground.cohorts import DataProfile, profile_dataframe
from visground.datasets import VisEvalDataset
from visground.lm import make_observed_dspy_module

from ..types import (
    GroundingRecord,
    GroundingRequest,
    GroundingStrategyMode,
    get_audience_description,
)

DESCRIPTION_CHAR_LIMIT = 1000
EXCERPT_CHAR_LIMIT = 1000
GUIDELINE_LABEL_LIMIT = 16
GROUP_LABEL_LIMIT = 16
GROUP_FAMILY_LIMIT = 16
DANGLING_ROLE = "__dangling__"
WHITESPACE_RE = re.compile(r"\s+")
PurposeBucket = Literal["select", "refine"]
PURPOSE_BUCKETS: tuple[PurposeBucket, ...] = ("select", "refine")


class GuidelineCard(TypedDict):
    id: str
    title: str
    description: str
    labels: list[str]
    context_excerpt: str


class PurposeBuckets(TypedDict):
    select: list[GuidelineCard]
    refine: list[GuidelineCard]


class PurposeCounts(TypedDict):
    select: int
    refine: int


class BasisGroup(TypedDict):
    basis_label: str
    basis_subcategory: str
    counts_by_purpose: PurposeCounts
    label_families: list[str]
    common_labels: list[str]
    by_purpose: PurposeBuckets


class GuidelinesPayload(TypedDict):
    basis_groups: list[BasisGroup]


class LabelInfo(TypedDict):
    label: str
    subcategory: str


class HybridGroundingStrategyConfig(TypedDict):
    lm: dspy.LM
    num_threads: NotRequired[int]


class RetrieveGuidelines(dspy.Signature):
    """
    Retrieve the best design-guidance bundle for one visualization request.

    Goal:
    - usually return about 7-9 guidelines
    - maximize distinct design volume for one static printed chart
    - keep only guidelines that add a unique visible job
    - prefer guidelines that create noticeable visual or interpretive improvement
      over guidelines that are merely correct but low-drama
    - prefer concrete, actionable, implementable guidance over generic,
      repetitive, or warning-only guidance
    - prefer a smaller complete bundle over a larger repetitive one

    Read `context["objective"]` first. Use all of `context` to infer the real
    design problem the bundle must solve. Use `guidelines` second.

    `guidelines` is organized into dynamic basis groups. Each basis group is a
    retrieval lane with `select` and `refine` buckets plus short summaries.

    Hard filters:
    - target medium is a static printed publication, so reject guidance whose
      value depends on hover, click, tooltip, zoom, pan, toggle, brushing,
      scrolling, animation, or any other interactive behavior
    - basis groups are search lanes, not coverage quotas; do not keep a weak
      guideline merely to represent one more basis group
    - if a kept guideline already determines the same visible lever, drop the
      more generic or weaker guideline
    - if two guidelines would mostly collapse into the same code edit or same
      visible chart mutation, keep only the stronger one
    - generic hygiene guidance such as axis labels, title/caption, contrast,
      or minimum text size is fill-only; usually keep zero or one
    - low-drama maintenance guidance is lower priority than guidance that would
      noticeably change how the chart reads at a glance

    Selection procedure:
    1. Identify the primary design decision the request needs first.
    2. Sketch the minimum bundle jobs needed before selecting.
    3. Inspect every basis group, starting with the bucket matching
       `context["objective"]`.
    4. Nominate the strongest candidate from each useful basis group.
    5. Build the bundle from candidates that change different visible design
       levers such as chart family, structure, comparison geometry,
       baseline/scale, ordering, direct labeling, annotation, accessibility
       encoding, and framing/context.
    6. Keep at most one strong guideline per visible lever unless two
       guidelines create clearly different compatible edits.
    7. Stop once the main design decision plus the strongest orthogonal
       refinements are already covered.

    Keep a guideline only if:
    - it says what to do, or blocks a major failure while still implying one
      clear concrete edit
    - removing it would materially change the final chart
    - its effect would be obvious both in the final figure and in the
      implementation
    - it creates a noticeable visible or interpretive improvement, not merely a
      maintenance cleanup that readers may barely notice
    - it strengthens the other selected guidelines instead of merely repeating
      them

    For `select`:
    - choose one coherent chart or structure direction first
    - then add compatible `refine` bucket items that polish, clarify, order,
      annotate, label, or improve accessibility of that chosen design
    - do not stop at a bare chart-family decision
    - do not return mutually exclusive chart, structure, or channel guidance

    For `refine`:
    - preserve the fixed chart type and core structure
    - prefer strong upgrades that materially improve the current design without
      reopening the main chart-choice decision
    - actively favor refinements that make the figure read differently at a
      glance, such as stronger ordering, clearer grouping, better focal
      comparison, more informative labeling, sharper annotation, or more
      legible encoding
    - deprioritize bland maintenance guidance unless the chart is already
      otherwise complete
    - only use `select` bucket items when they apply directly without changing
      the fixed design direction

    Final ranking:
    - decisive structure first
    - orthogonal refinements next
    - hygiene last
    - within a tie, prefer the more specific, more actionable guideline
    - within a tie, prefer the guideline with the bigger visible impact
    - the final set should feel like one coherent publication-ready chart
      recipe and be as small as possible while still feeling complete
    """

    context: dict = dspy.InputField(
        desc=(
            "Request context for the visualization task, including the objective "
            "(select or refine), the query, chart decision state, fixed visual "
            "decisions, audience assumptions, data characteristics, and "
            "objective-specific retrieval constraints"
        )
    )

    guidelines: GuidelinesPayload = dspy.InputField(
        desc=(
            "Candidate visualization design guidelines grouped by basis label. "
            "Each basis group contains purpose buckets plus compact group "
            "summaries and compact guideline cards with labels and context excerpts."
        )
    )

    guideline_ids: list[str] = dspy.OutputField(
        desc=(
            "Ranked list of the best mutually reinforcing guideline IDs to apply. "
            "Prefer bundles where each selected guideline adds a distinct visible "
            "design move rather than repeating the same effect or collapsing into "
            "the same code edit at different levels of generality."
        )
    )


def _first_section(guideline: cc.Guideline, role: str) -> cc.Section | None:
    return next(
        (section for section in guideline.sections if section.role == role),
        None,
    )


def _first_non_dangling_section(guideline: cc.Guideline) -> cc.Section | None:
    return next(
        (section for section in guideline.sections if section.role != DANGLING_ROLE),
        None,
    )


def _normalize_and_truncate(text: str, *, limit: int) -> str:
    normalized = WHITESPACE_RE.sub(" ", text).strip()
    if len(normalized) <= limit:
        return normalized

    cutoff = max(limit - 3, 0)
    truncated = normalized[:cutoff].rstrip()
    if not truncated:
        return normalized[:limit]
    return f"{truncated}..."


def _guideline_labels(guideline: cc.Guideline) -> list[str]:
    labels: list[str] = []

    for label in guideline.labels:
        if label.startswith(("purpose:", "basis:")):
            continue
        if label in labels:
            continue
        labels.append(label)
        if len(labels) >= GUIDELINE_LABEL_LIMIT:
            break

    return labels


def _non_structural_labels(guideline: cc.Guideline) -> list[str]:
    return [
        label
        for label in guideline.labels
        if not label.startswith(("purpose:", "basis:"))
    ]


def _guideline_card(guideline: cc.Guideline) -> GuidelineCard:
    context = _first_section(guideline, "context")

    return {
        "id": guideline.id,
        "title": guideline.title.strip(),
        "description": _normalize_and_truncate(
            guideline.description,
            limit=DESCRIPTION_CHAR_LIMIT,
        ),
        "labels": _guideline_labels(guideline),
        "context_excerpt": (
            _normalize_and_truncate(context.content, limit=EXCERPT_CHAR_LIMIT)
            if context is not None
            else ""
        ),
    }


def _top_group_label_families(labels: list[str]) -> list[str]:
    family_counts = Counter(label.split(":", 1)[0] for label in labels)
    return [
        family
        for family, _ in sorted(
            family_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )[:GROUP_FAMILY_LIMIT]
    ]


def _top_group_labels(labels: list[str]) -> list[str]:
    label_counts = Counter(labels)
    return [
        label
        for label, _ in sorted(
            label_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )[:GROUP_LABEL_LIMIT]
    ]


def _single_label_info_by_guideline(
    catalog: cc.Catalog,
    *,
    category: str,
    allowed_subcategories: set[str] | None = None,
) -> dict[str, LabelInfo]:
    labels_by_guideline: dict[str, list[LabelInfo]] = defaultdict(list)

    for row in catalog.guideline_labels().to_dicts():
        if cast(str, row["category"]) != category:
            continue
        labels_by_guideline[cast(str, row["guideline_id"])].append(
            {
                "label": cast(str, row["label"]),
                "subcategory": cast(str, row["subcategory"]),
            }
        )

    invalid: list[str] = []
    label_info_by_guideline: dict[str, LabelInfo] = {}

    for guideline_id in catalog.guidelines().get_column("id").to_list():
        label_infos = labels_by_guideline.get(guideline_id, [])

        if len(label_infos) != 1:
            invalid.append(
                f"{guideline_id}: expected exactly one {category} label, "
                f"got {len(label_infos)}"
            )
            continue

        label_info = label_infos[0]
        if (
            allowed_subcategories is not None
            and label_info["subcategory"] not in allowed_subcategories
        ):
            invalid.append(
                f"{guideline_id}: invalid {category} subcategory "
                f"{label_info['subcategory']!r}"
            )
            continue

        label_info_by_guideline[guideline_id] = label_info

    if invalid:
        raise ValueError(
            f"Invalid guideline {category} labels:\n" + "\n".join(sorted(invalid))
        )

    return label_info_by_guideline


def _build_guidelines_payload(catalog: cc.Catalog) -> GuidelinesPayload:
    basis_by_guideline = _single_label_info_by_guideline(
        catalog,
        category="basis",
    )
    purpose_by_guideline = _single_label_info_by_guideline(
        catalog,
        category="purpose",
        allowed_subcategories=set(PURPOSE_BUCKETS),
    )

    groups_by_basis: dict[str, BasisGroup] = {}
    labels_by_basis: dict[str, list[str]] = defaultdict(list)

    for row in catalog.guidelines().iter_rows(named=True):
        guideline = cc.Guideline.from_mapping(row)
        basis_info = basis_by_guideline[guideline.id]
        purpose_info = purpose_by_guideline[guideline.id]
        purpose = cast(PurposeBucket, purpose_info["subcategory"])

        group = groups_by_basis.setdefault(
            basis_info["label"],
            {
                "basis_label": basis_info["label"],
                "basis_subcategory": basis_info["subcategory"],
                "counts_by_purpose": {
                    "select": 0,
                    "refine": 0,
                },
                "label_families": [],
                "common_labels": [],
                "by_purpose": {
                    "select": [],
                    "refine": [],
                },
            },
        )
        group["counts_by_purpose"][purpose] += 1
        group["by_purpose"][purpose].append(_guideline_card(guideline))
        labels_by_basis[basis_info["label"]].extend(_non_structural_labels(guideline))

    basis_groups = [
        groups_by_basis[basis_label] for basis_label in sorted(groups_by_basis)
    ]

    for basis_group in basis_groups:
        basis_labels = labels_by_basis[basis_group["basis_label"]]
        basis_group["label_families"] = _top_group_label_families(basis_labels)
        basis_group["common_labels"] = _top_group_labels(basis_labels)
        for purpose in PURPOSE_BUCKETS:
            basis_group["by_purpose"][purpose].sort(key=lambda card: card["id"])

    return {"basis_groups": basis_groups}


def build_retrieval_context(*, req: GroundingRequest, profile: DataProfile) -> dict:
    audience_description = (
        get_audience_description(req["audience"])
        if req["audience"] is not None
        else None
    )

    if req["objective"] == "select":
        objective_summary = (
            "Choose the best primary chart or structure for the task, then add "
            "compatible refinements that strengthen, polish, and clarify that "
            "chosen direction."
        )
        chart_state = "Chart type is not fixed yet."
        must_preserve = [
            f"task={req['task']}",
            f"scope={req['scope']}",
            f"time_mode={req['time_mode']}",
        ]
        retrieval_stages = [
            "1. Lock one coherent chart or structure direction first.",
            "2. Keep only the strongest candidate per visible design lever; drop generic restatements of more specific kept guidelines.",
            "3. Add orthogonal refine-style touches from other useful basis groups so the chosen design is already polished and publication-ready, with at most one hygiene fill slot at the end.",
        ]
        avoid = [
            "sets that imply multiple incompatible chart or structure choices",
            "interactive-only guidance whose value depends on hover, click, zoom, toggles, tooltips, or animation",
            "same-effect generic guidance that adds no new visible design decision beyond a more specific kept guideline",
            "multiple selected guidelines that would mostly collapse into the same code edit",
            "more than one low-priority hygiene reminder in the same bundle",
            "bundles dominated by generic chart hygiene before the main design choice is clear",
            "low-visibility communication boilerplate that does not help choose or improve the chosen design",
        ]
    else:
        objective_summary = (
            "Improve an already-prescribed chart without changing its chart type or "
            "core structure."
        )
        chart_state = f"Chart type is fixed to {req['chart']!r}."
        must_preserve = [
            f"chart={req['chart']}",
            f"task={req['task']}",
            f"scope={req['scope']}",
            f"time_mode={req['time_mode']}",
        ]
        retrieval_stages = [
            "1. Preserve the prescribed chart and core structure.",
            "2. Keep only the strongest improvement per visible design lever; drop generic restatements of more specific kept guidelines.",
            "3. Prefer orthogonal refinements from useful basis groups before doubling up, with at most one hygiene fill slot at the end.",
        ]
        avoid = [
            "guidelines whose main effect is to switch chart type",
            "interactive-only guidance whose value depends on hover, click, zoom, toggles, tooltips, or animation",
            "guidelines that reopen the core chart-choice decision",
            "same-effect generic guidance that adds no new visible design decision beyond a more specific kept guideline",
            "multiple selected guidelines that would mostly collapse into the same code edit",
            "more than one low-priority hygiene reminder in the same bundle",
            "bundles dominated by generic hygiene instead of stronger design changes",
        ]

    return {
        "objective": req["objective"],
        "objective_summary": objective_summary,
        "chart_state": chart_state,
        "must_preserve": must_preserve,
        "audience_description": audience_description,
        "request": req,
        "retrieval_stages": retrieval_stages,
        "implementation_medium": (
            "The final chart will be implemented in Python charting libraries "
            "as a static figure for printed publication. Prefer guidance that "
            "can be executed robustly, correctly, and with a clearly visible "
            "effect in one non-interactive published chart. Reject guidance "
            "whose value depends on hover, click, tooltips, zoom, toggles, "
            "animation, or other interactive behavior."
        ),
        "application_budget": (
            "The final guideline set should be compact enough to apply together "
            "in one chart without clutter, overengineering, or too many "
            "simultaneous moving parts. A strong bundle usually maps to only "
            "about 3-6 concrete implementation moves; if that already feels "
            "complete, return fewer guidelines."
        ),
        "avoid": avoid,
        "data_profile": profile,
    }


class GuidelineRetriever(dspy.Module):
    def __init__(
        self,
        viseval_dataset: VisEvalDataset,
        guidelines: GuidelinesPayload,
    ):
        self._retrieve = dspy.ChainOfThought(RetrieveGuidelines)
        self._viseval_dataset = viseval_dataset
        self._guidelines = guidelines

    def forward(self, *, req: GroundingRequest) -> dspy.Prediction:
        df = self._viseval_dataset.vis_relation(req["id"]).pl()
        profile = profile_dataframe(df)
        return self._retrieve(
            context=build_retrieval_context(req=req, profile=profile),
            guidelines=self._guidelines,
        )


def guideline_to_guidance(guideline: cc.Guideline) -> str:
    section = _first_section(guideline, "advice") or _first_non_dangling_section(
        guideline
    )
    if section is None:
        return "\n".join(
            [
                f"# {guideline.title}",
                "",
                f"> {guideline.description}",
                "",
                guideline.body,
            ]
        )

    return "\n".join(
        [
            f"# {guideline.title}",
            "",
            f"> {guideline.description}",
            "",
            f"## {section.title}",
            f"{section.content}",
        ]
    )


@dataclasses.dataclass(slots=True)
class HybridGroundingStrategy:
    catalog: cc.Catalog
    config: HybridGroundingStrategyConfig
    viseval_dataset: VisEvalDataset
    mode: GroundingStrategyMode = "hybrid"
    retriever: GuidelineRetriever = dataclasses.field(init=False, repr=False)
    _guidelines_by_id: dict[str, cc.Guideline] = dataclasses.field(
        init=False,
        repr=False,
    )

    def __post_init__(self):
        self._guidelines_by_id = {
            guideline.id: guideline
            for guideline in (
                cc.Guideline.from_mapping(row)
                for row in self.catalog.guidelines().iter_rows(named=True)
            )
        }
        self.retriever = GuidelineRetriever(
            viseval_dataset=self.viseval_dataset,
            guidelines=_build_guidelines_payload(self.catalog),
        )

    @property
    def observed_retriever(self) -> dspy.Module:
        return make_observed_dspy_module(
            self.retriever,
            classname="HybridGrounder",
            observe_kwargs={
                "name": "hybrid-grounder",
                "as_type": "retriever",
                "capture_input": False,
            },
            attributes={"tags": ["grounding"]},
        )

    def _prediction_to_record(self, pred: dspy.Prediction) -> GroundingRecord:
        guideline_ids = [
            guideline_id
            for guideline_id in dict.fromkeys(pred.guideline_ids)
            if guideline_id in self._guidelines_by_id
        ]
        guidance = [
            guideline_to_guidance(self._guidelines_by_id[guideline_id])
            for guideline_id in guideline_ids
        ]
        return {
            "doc_ids": guideline_ids,
            "guideline_ids": guideline_ids,
            "guidance": guidance,
        }

    def retrieve(self, req: GroundingRequest) -> GroundingRecord:
        with dspy.context(lm=self.config["lm"]):
            res = self.observed_retriever(req=req)

        return self._prediction_to_record(res)

    def retrieve_many(self, reqs: list[GroundingRequest]) -> list[GroundingRecord]:
        examples = [{"req": req} for req in reqs]
        exec_pairs = [(self.observed_retriever, example) for example in examples]
        parallel = dspy.Parallel(
            num_threads=self.config.get("num_threads", 8),
            disable_progress_bar=False,
        )
        with dspy.context(lm=self.config["lm"]):
            results = parallel(exec_pairs)

        return [self._prediction_to_record(res) for res in results]
