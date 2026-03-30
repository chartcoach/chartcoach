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
    - return 7-10 guidelines that maximize distinct design volume for one chart
    - every kept guideline must add a different visible design move
    - think in terms of bundle slots: every slot must pay for itself
    - prefer concrete, situation-matched guidance that is clearly implementable
      in Python charting libraries
    - return fewer items instead of weak, generic, or redundant extras

    Read `context["objective"]` first. Use all of `context` to infer the real
    design problem the bundle must solve. Use `guidelines` second.

    `guidelines` is organized into dynamic basis groups. Each basis group is one
    retrieval lane with `select` and `refine` buckets plus short summaries.

    Selection procedure:
    1. Identify the primary design decision the request needs first.
    2. Inspect every basis group. In each group, inspect the bucket matching
       `context["objective"]` first.
    3. Nominate only the strongest candidate from each useful basis group.
    4. Remove same-effect candidates before final ranking.
    5. Build the final bundle from candidates that change different visible
       design levers.
    6. Only after distinct design volume is strong may you add low-priority
       generic hygiene guidance.

    Design-lever rule:
    - think in visible design levers such as chart family, view structure,
      comparison geometry, baseline/scale strategy, ordering, direct-labeling,
      annotation, accessibility encoding, and framing/context
    - usually keep at most one guideline per visible design lever
    - keep two guidelines on the same lever only when both produce clearly
      different visible edits that can coexist without collapsing into the same
      code change

    Dominance test:
    - before keeping any guideline, ask: what unique visible chart change would
      disappear if this guideline were removed?
    - if the answer is "almost nothing" or is already covered by another kept
      guideline, drop it
    - do not keep both a specific structural decision and a more generic
      heuristic that merely endorses the same decision

    Bundle budget:
    - usually spend most slots on decisive structure plus orthogonal
      refinements
    - reserve at most one slot for generic hygiene guidance
    - never spend multiple slots on broad reminders that mostly say "make the
      chart clear"
    - if two selected guidelines would mostly turn into the same code edit,
      keep only the stronger one

    Same-effect rule:
    - if one kept guideline already determines the chart family, arrangement,
      baseline strategy, ordering, direct-labeling strategy, annotation
      strategy, or accessibility treatment, drop any more generic guideline
      that would produce the same visible result
    - prefer the more specific, higher-leverage, more situation-matched
      guideline
    - example: if a kept guideline already says to use grouped bars for
      within-category comparison, do not also keep a generic guideline about
      choosing a familiar basic chart type

    Hygiene rule:
    - axis labels, descriptive title/caption, contrast, minimum text size, and
      similar universal chart hygiene guidance are fill-only
    - usually include zero or one hygiene guideline
    - prefer the single hygiene guideline with the broadest useful effect if
      one is needed at all
    - never let hygiene dominate the bundle when stronger structural,
      comparison, ordering, annotation, or accessibility moves are available

    Basis rule:
    - inspect every basis group
    - prefer cross-basis coverage when it increases design volume
    - skip a basis group when its best candidate is weak, redundant, or
      incompatible
    - large basis groups must not dominate only because they contain more items

    Final bundle audit:
    - each selected guideline must have one clear unique job in the bundle
    - no pair of selected guidelines should mostly collapse into the same chart
      mutation or same implementation step
    - if removing one selected guideline would leave the chart essentially the
      same, drop it

    For `select`:
    - choose one coherent chart or structure direction first
    - use `refine` bucket items only after that direction is clear
    - do not return mutually exclusive chart, structure, or channel guidance

    For `refine`:
    - preserve the fixed chart type and core structure
    - prefer strong improvements that make the current design better without
      reopening the primary chart-choice decision
    - only use `select` bucket items when they are directly applicable without
      changing the fixed design direction

    Ranking:
    - decisive structure first
    - orthogonal refinements next
    - hygiene last
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
            "summaries and compact guideline cards with labels, context, and "
            "advice excerpts."
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

    for row in catalog.guideline_labels_df.to_dicts():
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

    for entry in catalog.entries:
        guideline_id = entry.guideline.id
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

    for entry in catalog.entries:
        guideline = entry.guideline
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
            "only compatible refinements that strengthen that chosen direction."
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
            "3. Add orthogonal guidelines from other useful basis groups, with at most one hygiene fill slot at the end.",
        ]
        avoid = [
            "sets that imply multiple incompatible chart or structure choices",
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
            "The final chart will be implemented in Python charting libraries. "
            "Prefer guidance that can be executed robustly, correctly, and with "
            "clearly visible effect in that medium."
        ),
        "application_budget": (
            "The final guideline set should be compact enough to apply together "
            "in one chart without clutter, overengineering, or too many "
            "simultaneous moving parts."
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
            entry.guideline.id: entry.guideline for entry in self.catalog.entries
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
            num_threads=self.config.get("num_threads", 4),
            disable_progress_bar=False,
        )
        with dspy.context(lm=self.config["lm"]):
            results = parallel(exec_pairs)

        return [self._prediction_to_record(res) for res in results]
