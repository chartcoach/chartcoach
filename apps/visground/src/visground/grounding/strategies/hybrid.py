import dataclasses
from typing import NotRequired, TypedDict

import chartcoach as cc
import dspy
from visground.cohorts import DataProfile, profile_dataframe
from visground.datasets import VisEvalDataset

from ..types import (
    GroundingRecord,
    GroundingRequest,
    GroundingStrategyMode,
    get_audience_description,
)


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

    For `select`:
    - the chart type and core structure are not fixed yet
    - first retrieve decisive guidelines that make one primary design direction
      clearly preferable for this task
    - the set must converge on a single chart or structure choice rather than
      presenting several incompatible alternatives
    - after the design direction is clear, add only compatible refinement
      guidelines that make that chosen design richer, clearer, and more
      well-rounded
    - once the main design direction is clear, use compatible refinements from
      other relevant lanes such as annotation/detail, rhetoric/tone/wording,
      accessibility, color, and polish so the chosen design is not only correct
      but also well-rounded
    - use the remaining slots after the decisive design-choice guidelines on
      orthogonal, compatible refinements rather than on more of the same lane
    - do not spend most of the budget on generic polish, titles, captions,
      labels, or annotations before the core design choice is settled
    - do not return mutually exclusive chart, structure, or channel guidance

    For `refine`:
    - the chart type and core structure are already fixed and must be preserved
    - retrieve guidelines that improve the specified design's readability,
      interpretability, comparison support, ordering, labeling, annotation,
      scale choices, accessibility, or polish
    - exclude guidelines whose main effect is to switch chart type, change the
      core structure, or reopen the primary design decision

    Global rules:
    - every selected guideline should introduce a distinct visible change to the
      chart; do not waste slots on invisible or low-impact guidance
    - the selected set must be complementary and synergetic; each guideline
      should make the others more useful rather than redundant or disconnected
    - the selected set must fit within a realistic application budget for one
      chart; do not choose so many simultaneous changes that the final result
      would become cluttered, overengineered, or hard to execute cleanly
    - after selecting the core high-leverage guidelines, prefer orthogonal
      guidelines from different compatible lanes rather than stacking many items
      that all operate on the same narrow aspect
    - prefer situation-specific guidance over generic good practice
    - prefer guidelines whose advice text specifies concrete edits
    - prefer changes that would be fully visible when applied
    - prefer guidelines that can be implemented robustly, correctly, and
      visibly in Python charting libraries rather than guidelines that are only
      theoretically good or likely to become brittle in implementation
    - prefer strong, bounded guidance over vague, generic, or mostly cautionary
      guidance
    - when it improves the set, balance across different relevant topic lanes
      such as core design choice, rhetoric, tone, wording, accessibility,
      color, annotation/detail, and polish so the result is well-rounded rather
      than clustered in one narrow area
    - avoid near-duplicates or guidelines that collapse into the same edit
    - avoid diversity for its own sake; do not add a topic lane unless the
      guideline is truly situation-matched, compatible, and visibly useful
    - avoid over-clustering in one lane unless each additional guideline brings
      a clearly different visible contribution that the set would otherwise miss
    - avoid sets that would force too many competing visual priorities,
      annotations, embellishments, or implementation burdens into one chart
    - if two candidates conflict, keep the one that better fits the request and
      discard the other
    - if two candidates are similarly relevant, prefer the one that is more
      realistically executable in chart code and less likely to become buggy,
      fragile, or only weakly visible after implementation
    - if two candidate sets are similarly strong, prefer the more compact and
      higher-leverage set that can be applied together without overloading the chart
    - return fewer items instead of padding with weak, ambiguous, or low-value
      guidelines

    Usually return 5-8 deeply situation-matched, complementary, synergetic
    guidelines. For `select`, rank decisive selection guidelines first and
    follow them with compatible refinements from other relevant lanes. For
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

    guidelines: dict[str, str] = dspy.InputField(
        desc=(
            "Candidate visualization design guidelines keyed by guideline ID, where each "
            "value contains compatibility labels plus the guideline's context and advice "
            "markdown so actionability, visibility, deep situational fit, "
            "Python-charting implementability, and cross-guideline synergy can "
            "be judged"
        )
    )

    guideline_ids: list[str] = dspy.OutputField(
        desc=(
            "Ranked list of the best mutually reinforcing guideline IDs to apply. "
            "For select, order the list so decisive chart-choice guidelines come "
            "first and compatible refinements from other relevant lanes come "
            "after. For refine, order by highest-value visible improvements first."
        )
    )


def _first_section(guideline: cc.Guideline, role: str) -> cc.Section | None:
    return next(
        (section for section in guideline.sections if section.role == role), None
    )


def _selection_labels(guideline: cc.Guideline) -> list[str]:
    prefixes = (
        "purpose:",
        "chart:",
        "structure:",
        "channel:",
        "task:",
        "scope:",
        "time:",
        "literacy:",
        "audience:",
        "needs:",
    )
    return sorted(label for label in guideline.labels if label.startswith(prefixes))


def guideline_to_selection_md(guideline: cc.Guideline) -> str:
    context = _first_section(guideline, "context")
    selection_labels = _selection_labels(guideline)

    parts = [
        "---",
        f"id: {guideline.id}",
        f"labels: {guideline.labels}",
        f"selection_labels: {selection_labels}",
        "---",
        "",
        f"# {guideline.title}",
        "",
        f"> {guideline.description}",
    ]

    if context is not None:
        parts.extend(
            [
                "",
                f"## {context.title}",
                context.content,
            ]
        )

    return "\n".join(parts)


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
            "2. Add only compatible refinement guidelines once that choice is clear.",
            "3. Spend the remaining slots on orthogonal refinements from other relevant lanes so the final set is well-rounded.",
        ]
        topic_lanes = [
            "core design choice",
            "annotation/detail",
            "rhetoric/tone/wording",
            "accessibility",
            "color",
            "polish",
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
            "2. Choose only visible refinements that make the current design stronger.",
            "3. Prefer orthogonal refinements from different useful lanes when they make the final chart more well-rounded.",
        ]
        topic_lanes = [
            "readability/detail",
            "annotation/wording",
            "rhetoric/tone",
            "accessibility",
            "color",
            "polish",
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
        "topic_lanes": topic_lanes,
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
        catalog: cc.Catalog,
    ):
        self._retrieve = dspy.ChainOfThought(RetrieveGuidelines)
        self._viseval_dataset = viseval_dataset
        self._catalog = catalog

    def forward(self, *, req: GroundingRequest) -> dspy.Prediction:
        df = self._viseval_dataset.vis_relation(req["id"]).pl()
        profile = profile_dataframe(df)
        return self._retrieve(
            context=build_retrieval_context(req=req, profile=profile),
            guidelines={
                entry.guideline.id: guideline_to_selection_md(entry.guideline)
                for entry in self._catalog.entries
                if "avoid" not in entry.id
            },
        )


def guideline_to_guidance(guideline: cc.Guideline) -> str:
    advice = [s for s in guideline.sections if s.role == "advice"][0]
    return "\n".join(
        [
            f"# {guideline.title}",
            "",
            f"> {guideline.description}",
            "",
            f"## {advice.title}",
            f"{advice.content}",
        ]
    )


@dataclasses.dataclass
class HybridGroundingStrategy:
    catalog: cc.Catalog
    config: HybridGroundingStrategyConfig
    viseval_dataset: VisEvalDataset
    mode: GroundingStrategyMode = "hybrid"

    def __post_init__(self):
        self.retriever = GuidelineRetriever(
            viseval_dataset=self.viseval_dataset,
            catalog=self.catalog,
        )

    def _prediction_to_record(self, pred: dspy.Prediction) -> GroundingRecord:
        guidelines_by_id = {
            entry.guideline.id: entry.guideline for entry in self.catalog.entries
        }
        guideline_ids = [
            guideline_id
            for guideline_id in dict.fromkeys(pred.guideline_ids)
            if guideline_id in guidelines_by_id
        ]
        guidance = [
            guideline_to_guidance(guidelines_by_id[guideline_id])
            for guideline_id in guideline_ids
        ]
        return {
            "doc_ids": guideline_ids,
            "guideline_ids": guideline_ids,
            "guidance": guidance,
        }

    def retrieve(self, req: GroundingRequest) -> GroundingRecord:
        with dspy.context(lm=self.config["lm"]):
            res = self.retriever(req=req)

        return self._prediction_to_record(res)

    def retrieve_many(self, reqs: list[GroundingRequest]) -> list[GroundingRecord]:
        examples = [{"req": req} for req in reqs]
        exec_pairs = [(self.retriever, example) for example in examples]
        parallel = dspy.Parallel(
            num_threads=self.config.get("num_threads", 4),
            disable_progress_bar=False,
        )
        with dspy.context(lm=self.config["lm"]):
            results = parallel(exec_pairs)

        return [self._prediction_to_record(res) for res in results]
