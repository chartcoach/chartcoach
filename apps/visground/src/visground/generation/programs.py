from __future__ import annotations

from collections.abc import Sequence
from typing import cast

import dspy

from .backends import VisualizationBackend
from .models import ImplementationReviewResult, VisGenOutput
from .signatures import ReviewVisualizationImplementation, WriteVisualizationCode

DEFAULT_REFINE_ROLLOUTS = 5
DEFAULT_REFINE_THRESHOLD = 1.0


class VisualizationGenerationProgram(dspy.Module):
    def __init__(
        self,
        backend: VisualizationBackend,
        coder_signature: type[dspy.Signature],
        review_signature: type[dspy.Signature],
        reviewer_lm: dspy.LM | None = None,
    ) -> None:
        super().__init__()
        self.backend = backend
        self.coder = dspy.Predict(coder_signature)
        self.review_signature = review_signature
        self.reviewer_lm = reviewer_lm

    def deepcopy(self):
        new = self.__class__.__new__(self.__class__)
        dspy.Module.__init__(new)
        new.backend = self.backend
        new.coder = self.coder.deepcopy()
        new.review_signature = self.review_signature
        new.reviewer_lm = self.reviewer_lm
        return new

    def forward(self, **kwargs) -> dspy.Prediction:
        draft = self.coder(**kwargs)
        review = _review_generated_visualization(
            backend=self.backend,
            review_signature=self.review_signature,
            request_id=kwargs["id"],
            code=draft.code,
            requirements=kwargs["requirements"],
            lm=self.reviewer_lm or self.coder.get_lm(),
        )
        return dspy.Prediction(**dict(draft), **review)


def build_refine_generator(
    backend: VisualizationBackend,
    coder_signature: type[dspy.Signature] = WriteVisualizationCode,
    review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
    reviewer_lm: dspy.LM | None = None,
) -> dspy.Module:
    program = VisualizationGenerationProgram(
        backend=backend,
        coder_signature=coder_signature,
        review_signature=review_signature,
        reviewer_lm=reviewer_lm,
    )
    return dspy.Refine(
        module=program,
        N=DEFAULT_REFINE_ROLLOUTS,
        reward_fn=lambda args, pred: float(
            (
                pred.no_truncation
                + pred.no_overlap
                + pred.text_readable
                + pred.data_readable
                + pred.implementation_acceptable
                + pred.requirements_followed
                + pred.no_unprescribed_design
            )
            / 7
        ),
        threshold=DEFAULT_REFINE_THRESHOLD,
    )


def run_generation(
    generator: dspy.Module,
    examples: Sequence[dspy.Example],
    *,
    num_threads: int = 20,
) -> list[VisGenOutput]:
    if not examples:
        return []

    parallel = dspy.Parallel(num_threads=num_threads)
    predictions = parallel([(generator, example) for example in examples])
    return [
        prediction_to_output(example, prediction)
        for example, prediction in zip(examples, predictions)
    ]


def prediction_to_output(
    example: dspy.Example,
    prediction: dspy.Prediction,
) -> VisGenOutput:
    example_inputs = example.inputs().toDict()
    return cast(
        VisGenOutput,
        {
            "id": example_inputs["id"],
            "code": prediction.code,
            "visualization_type": prediction.visualization_type,
            "query_interpretation": prediction.query_interpretation,
            "design_rationale": prediction.design_rationale,
            "grounding_trace": prediction.grounding_trace,
        },
    )


def _review_generated_visualization(
    backend: VisualizationBackend,
    review_signature: type[dspy.Signature],
    request_id: str,
    code: str,
    requirements: list[str],
    lm: object | None,
) -> ImplementationReviewResult:
    try:
        vis = backend.materialize_visualization(request_id, code)
    except Exception as exc:
        return _failed_implementation_review(
            f"Code did not execute successfully, so no chart object was produced: {_summarize_exception(exc)}"
        )

    try:
        image = backend.rasterize(vis)
        image.load()
    except Exception as exc:
        return _failed_implementation_review(
            f"Code executed and produced a chart object, but rasterization failed: {_summarize_exception(exc)}"
        )

    reviewer = dspy.Predict(review_signature, temperature=0.0)
    try:
        context_kwargs: dict[str, object] = {"trace": []}
        if lm is not None:
            context_kwargs["lm"] = lm
        with dspy.context(**context_kwargs):
            review = reviewer(vis=dspy.Image(image), requirements=requirements)
    except Exception as exc:
        return _failed_implementation_review(
            f"Code executed and rasterization succeeded, but the implementation reviewer failed: {_summarize_exception(exc)}"
        )

    feedback = [item.strip() for item in review.feedback if item.strip()]
    requirements_followed = review.requirements_followed
    no_unprescribed_design = review.no_unprescribed_design
    requirement_trace = review.requirement_trace
    implementation_acceptable = (
        review.implementation_acceptable
        and requirements_followed
        and no_unprescribed_design
    )
    if (
        not implementation_acceptable
        or not review.no_truncation
        or not review.no_overlap
        or not review.text_readable
        or not review.data_readable
        or not requirements_followed
        or not no_unprescribed_design
    ):
        reasoning = review.reasoning.strip()
        explicit_reason = (
            "Code executed and rasterization succeeded, but the implementation "
            f"reviewer flagged visible quality issues. {reasoning}"
        ).strip()
        return {
            "no_truncation": review.no_truncation,
            "no_overlap": review.no_overlap,
            "text_readable": review.text_readable,
            "data_readable": review.data_readable,
            "implementation_acceptable": implementation_acceptable,
            "requirements_followed": requirements_followed,
            "no_unprescribed_design": no_unprescribed_design,
            "requirement_trace": requirement_trace,
            "implementation_reasoning": explicit_reason,
            "implementation_feedback": feedback or [explicit_reason],
        }

    return {
        "no_truncation": review.no_truncation,
        "no_overlap": review.no_overlap,
        "text_readable": review.text_readable,
        "data_readable": review.data_readable,
        "implementation_acceptable": implementation_acceptable,
        "requirements_followed": requirements_followed,
        "no_unprescribed_design": no_unprescribed_design,
        "requirement_trace": requirement_trace,
        "implementation_reasoning": review.reasoning.strip(),
        "implementation_feedback": feedback,
    }


def _failed_implementation_review(reason: str) -> ImplementationReviewResult:
    return {
        "no_truncation": False,
        "no_overlap": False,
        "text_readable": False,
        "data_readable": False,
        "implementation_acceptable": False,
        "requirements_followed": False,
        "no_unprescribed_design": False,
        "requirement_trace": {},
        "implementation_reasoning": reason,
        "implementation_feedback": [reason],
    }


def _summarize_exception(exc: Exception) -> str:
    message = " ".join(str(exc).split()).strip()
    if not message:
        return type(exc).__name__
    message = f"{type(exc).__name__}: {message}"
    return message[:240]
