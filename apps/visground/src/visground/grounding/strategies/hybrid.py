import dataclasses
from typing import NotRequired, TypedDict

import chartcoach as cc
import dspy
from visground.cohorts import profile_dataframe
from visground.datasets import VisEvalDataset

from ..types import (
    GroundingRecord,
    GroundingRequest,
    GroundingStrategyMode,
)


class HybridGroundingStrategyConfig(TypedDict):
    lm: dspy.LM
    num_threads: NotRequired[int]


class RetrieveGuidelines(dspy.Signature):
    """
    Select the most relevant visualization design guidelines for a given analytical context.

    Use the user's analytical intent and any explicitly fixed visualization decisions as
    binding constraints. Do not select guidelines whose main effect would be to redirect,
    contradict, or replace already-decided choices such as the analytical framing, chosen
    chart form, required encodings, or presentation requirements. Instead, prioritize
    complementary guidelines that help the chosen approach succeed.

    Prefer guidelines that:
    - are directly applicable to the given context
    - prescribe clear implementation actions rather than mostly offering cautions
    - would create visible changes in the final visualization if applied
    - strengthen the design through refinements such as encoding, ordering, labeling,
      annotation, comparison support, accessibility, interaction, layout, or polish
    - can make the result more distinctive or memorable without violating user intent

    Favor a compact, high-signal, non-redundant set. When possible, choose complementary
    guidelines from different lanes so the final set is well-rounded rather than clustered
    in one area. Typically return 5-7 guidelines.

    Exclude guidelines that are irrelevant, overlapping, vague, generic, weakly actionable,
    low-visibility, mostly cautionary, or that would override explicit user intent or fixed
    visualization decisions.
    """

    context: dict = dspy.InputField(
        desc=(
            "Analytical context for the visualization task, including the user's goal, "
            "data characteristics, audience, constraints, preferences, and any explicit "
            "choices that are already fixed"
        )
    )

    guidelines: dict[str, str] = dspy.InputField(
        desc=(
            "Candidate visualization design guidelines keyed by guideline ID, where each "
            "value contains the full markdown text of that guideline"
        )
    )

    guideline_ids: list[str] = dspy.OutputField(
        desc=("Ranked list of the most relevant guideline IDs to apply to this context")
    )


def guideline_to_selection_md(guideline: cc.Guideline) -> str:
    context = [s for s in guideline.sections if s.role == "context"][0]
    return "\n".join(
        [
            "---",
            f"id: {guideline.id}",
            f"labels: {guideline.labels}",
            "---",
            "",
            f"# {guideline.title}",
            "",
            f"> {guideline.description}",
            "",
            f"## {context.title}",
            context.content,
        ]
    )


class GuidelineRetriever(dspy.Module):
    def __init__(
        self,
        viseval_dataset: VisEvalDataset,
        catalog: cc.Catalog,
    ):
        self._retrieve = dspy.Predict(RetrieveGuidelines)
        self._viseval_dataset = viseval_dataset
        self._catalog = catalog

    def forward(self, *, req: dict) -> dspy.Prediction:
        df = self._viseval_dataset.vis_relation(req["id"]).pl()
        profile = profile_dataframe(df)
        return self._retrieve(
            context={
                "request": req,
                "data_profile": profile,
            },
            guidelines={
                entry.guideline.id: guideline_to_selection_md(entry.guideline)
                for entry in self._catalog.entries
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
        guideline_ids = pred.guideline_ids
        guidelines = [
            e.guideline for e in self.catalog.entries if e.guideline.id in guideline_ids
        ]
        guidance = [guideline_to_guidance(guideline) for guideline in guidelines]
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
