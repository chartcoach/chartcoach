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
    Retrieve the highest-value visualization design guidelines for the request.

    Optimize for application value, not generic relevance. The selected guidelines
    will be handed to a later model that must actually apply them, so every chosen
    guideline must be:
    - unambiguous to apply from the advice text
    - visibly testable in the final rendered chart
    - distinct from the other chosen guidelines
    - compatible with the rest of the set
    - deeply matched to the exact situation described by the full context
    - realistically actionable and correctly implementable in Python charting
      libraries
    - realistically applicable together with the rest of the set in one chart

    Read `context["objective"]` first.
    Infer the situation from everything available in `context`, including the
    query wording, task, scope, time mode, audience, fixed chart decisions,
    retrieval stages, and data profile. Prefer guidelines that fit this full
    situation deeply rather than guidelines that only overlap on one broad topic
    or one shared keyword.
    Build the final set like a coherent playbook for one chart, not like a bag
    of separately relevant snippets.

    `guidelines` is organized into dynamic basis groups. Every basis group
    contains purpose buckets plus short group summaries. Treat each basis group
    as one retrieval lane.

    Required workflow:
    - inspect every basis group before finalizing the set
    - use the group-level summaries to quickly understand what each basis lane
      specializes in before drilling into its cards
    - within each basis group, inspect the bucket matching
      `context["objective"]` first
    - inspect the opposite-purpose bucket only when it adds a genuinely useful
      complementary item
    - compare the strongest compatible candidates across basis groups before
      taking a second item from any one basis group

    For `select`:
    - the chart type and core structure are not fixed yet
    - first retrieve decisive guidelines that make one primary design direction
      clearly preferable for this task
    - the set must converge on a single chart or structure choice rather than
      presenting several incompatible alternatives
    - use `refine` bucket items only after the main design direction is clear
      and only when they strengthen that chosen direction
    - do not return mutually exclusive chart, structure, or channel guidance

    For `refine`:
    - the chart type and core structure are already fixed and must be preserved
    - retrieve guidelines that improve the specified design's readability,
      interpretability, comparison support, ordering, labeling, annotation,
      scale choices, accessibility, or polish
    - only use `select` bucket items when they are directly applicable without
      reopening the fixed chart decision

    Global rules:
    - every selected guideline should introduce a distinct visible change to the
      chart; do not waste slots on invisible or low-impact guidance
    - the selected set must be complementary and synergetic; each guideline
      should make the others more useful rather than redundant or disconnected
    - the selected set must fit within a realistic application budget for one
      chart; do not choose so many simultaneous changes that the final result
      would become cluttered, overengineered, or hard to execute cleanly
    - prefer situation-specific guidance over generic good practice
    - prefer guidelines whose advice text specifies concrete edits
    - prefer changes that would be fully visible when applied
    - prefer guidelines that can be implemented robustly, correctly, and
      visibly in Python charting libraries rather than guidelines that are only
      theoretically good or likely to become brittle in implementation
    - balance across useful basis groups when it improves the set, but do not
      use weak guidelines just to cover a group
    - large basis groups must not dominate only because they contain more
      candidates
    - avoid near-duplicates or guidelines that collapse into the same edit
    - if two candidates conflict, keep the one that better fits the request and
      discard the other
    - if two candidates are similarly relevant, prefer the one that is more
      realistically executable in chart code and less likely to become buggy,
      fragile, or only weakly visible after implementation
    - return fewer items instead of padding with weak, ambiguous, or low-value
      guidelines

    Usually return 5-8 deeply situation-matched, complementary, synergetic
    guidelines. For `select`, rank decisive selection guidelines first and
    follow them with compatible refinements from other useful basis groups. For
    `refine`, rank the highest-value visible improvements first.
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
            "For select, order the list so decisive chart-choice guidelines come "
            "first and compatible refinements come after. For refine, order by "
            "highest-value visible improvements first."
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
            "1. Pick decisive guidelines that converge on one best chart or structure choice.",
            "2. Compare strong candidates across different basis groups before doubling up within one group.",
            "3. Add only compatible refinements once the main design direction is clear.",
        ]
        avoid = [
            "sets that imply multiple incompatible chart or structure choices",
            "generic polish before the main design choice is clear",
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
            "2. Prefer one strong compatible improvement from each useful basis group before doubling up.",
            "3. Keep only visible refinements that strengthen the current design.",
        ]
        avoid = [
            "guidelines whose main effect is to switch chart type",
            "guidelines that reopen the core chart-choice decision",
            "generic advice that is not clearly applicable to the prescribed chart",
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
