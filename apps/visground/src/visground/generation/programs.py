from __future__ import annotations

import json
from collections.abc import Sequence
from typing import Any, Callable, TypeVar, cast

import dspy
from tenacity import retry, stop_after_attempt, wait_fixed

from visground.lm import make_observed_dspy_module

from .backends import VisualizationBackend
from .models import ImplementationReviewResult, VisGenOutput, VisGenResult
from .signatures import ReviewVisualizationImplementation, WriteVisualizationCode

DEFAULT_RETRY_ITERATIONS = 3
TRANSIENT_RETRY_ATTEMPTS = 3
TRANSIENT_RETRY_WAIT_SECONDS = 1

_RetryT = TypeVar("_RetryT")


class VisualizationGenerationProgram(dspy.Module):
    def __init__(
        self,
        backend: VisualizationBackend,
        coder_signature: type[dspy.Signature],
        review_signature: type[dspy.Signature],
        reviewer_lm: dspy.LM | None = None,
        max_iterations: int = DEFAULT_RETRY_ITERATIONS,
    ) -> None:
        super().__init__()
        if max_iterations < 1:
            raise ValueError("max_iterations must be at least 1.")
        self.backend = backend
        self.coder = dspy.Predict(coder_signature)
        self.review_signature = review_signature
        self.reviewer_lm = reviewer_lm
        self.max_iterations = max_iterations

    def deepcopy(self):
        new = self.__class__.__new__(self.__class__)
        dspy.Module.__init__(new)
        new.backend = self.backend
        new.coder = self.coder.deepcopy()
        new.review_signature = self.review_signature
        new.reviewer_lm = self.reviewer_lm
        new.max_iterations = self.max_iterations
        return new

    def forward(self, **kwargs) -> dspy.Prediction:
        base_lm = self.coder.get_lm() or dspy.settings.lm
        rollout_start = _rollout_start(base_lm)
        outer_trace = dspy.settings.trace

        best_prediction: dspy.Prediction | None = None
        best_reward = -float("inf")
        best_trace: list[tuple[Any, Any, Any]] | None = None
        feedback: str | None = None

        for attempt_index in range(self.max_iterations):
            attempt_lm = _attempt_lm(base_lm, rollout_start + attempt_index)
            with dspy.context(trace=[]):
                draft = self._run_coder_attempt(
                    inputs=kwargs,
                    feedback=feedback,
                    attempt_lm=attempt_lm,
                )
                review = _review_generated_visualization(
                    backend=self.backend,
                    review_signature=self.review_signature,
                    request_id=kwargs["id"],
                    code=draft.code,
                    query=kwargs["query"],
                    tablespec=kwargs["tablespec"],
                    requirements=kwargs["requirements"],
                    lm=self.reviewer_lm or attempt_lm or dspy.settings.lm,
                )
                prediction = dspy.Prediction(**dict(draft), **review)
                attempt_trace = dspy.settings.trace.copy()

            reward = _reward_prediction(prediction)
            if reward > best_reward:
                best_reward = reward
                best_prediction = prediction
                best_trace = attempt_trace

            if prediction.implementation_acceptable:
                break

            if attempt_index == self.max_iterations - 1:
                break

            feedback = _build_retry_feedback(prediction, attempt_index + 1)

        if best_trace:
            outer_trace.extend(best_trace)

        if best_prediction is None:
            raise ValueError("Generation loop produced no prediction.")

        return best_prediction

    def _run_coder_attempt(
        self,
        *,
        inputs: dict[str, Any],
        feedback: str | None,
        attempt_lm: dspy.LM | None,
    ) -> dspy.Prediction:
        coder = self.coder.deepcopy()
        if attempt_lm is not None:
            coder.lm = attempt_lm

        coder_inputs = dict(inputs)
        coder_inputs["feedback"] = feedback

        return _call_with_transient_retry(lambda: coder(**coder_inputs))


def build_feedback_loop_generator(
    backend: VisualizationBackend,
    coder_signature: type[dspy.Signature] = WriteVisualizationCode,
    review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
    reviewer_lm: dspy.LM | None = None,
    max_iterations: int = DEFAULT_RETRY_ITERATIONS,
) -> dspy.Module:
    return VisualizationGenerationProgram(
        backend=backend,
        coder_signature=coder_signature,
        review_signature=review_signature,
        reviewer_lm=reviewer_lm,
        max_iterations=max_iterations,
    )


def build_observed_feedback_loop_generator(
    backend: VisualizationBackend,
    coder_signature: type[dspy.Signature] = WriteVisualizationCode,
    review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
    reviewer_lm: dspy.LM | None = None,
    max_iterations: int = DEFAULT_RETRY_ITERATIONS,
) -> dspy.Module:
    generator = build_feedback_loop_generator(
        backend=backend,
        coder_signature=coder_signature,
        review_signature=review_signature,
        reviewer_lm=reviewer_lm,
        max_iterations=max_iterations,
    )
    return make_observed_dspy_module(
        generator,
        classname="VisualizationCodeGenerator",
        observe_kwargs={
            "name": "vis-code-generator",
            "as_type": "agent",
        },
        attributes={"tags": ["generating"]},
    )


def build_refine_generator(
    backend: VisualizationBackend,
    coder_signature: type[dspy.Signature] = WriteVisualizationCode,
    review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
    reviewer_lm: dspy.LM | None = None,
    max_iterations: int = DEFAULT_RETRY_ITERATIONS,
) -> dspy.Module:
    return build_feedback_loop_generator(
        backend=backend,
        coder_signature=coder_signature,
        review_signature=review_signature,
        reviewer_lm=reviewer_lm,
        max_iterations=max_iterations,
    )


def build_observed_refine_generator(
    backend: VisualizationBackend,
    coder_signature: type[dspy.Signature] = WriteVisualizationCode,
    review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
    reviewer_lm: dspy.LM | None = None,
    max_iterations: int = DEFAULT_RETRY_ITERATIONS,
) -> dspy.Module:
    return build_observed_feedback_loop_generator(
        backend=backend,
        coder_signature=coder_signature,
        review_signature=review_signature,
        reviewer_lm=reviewer_lm,
        max_iterations=max_iterations,
    )


def run_generation(
    generator: dspy.Module,
    examples: Sequence[dspy.Example],
    *,
    num_threads: int = 20,
) -> list[VisGenResult]:
    if not examples:
        return []

    parallel = dspy.Parallel(
        num_threads=num_threads,
        max_errors=len(examples) + 1,
        return_failed_examples=True,
    )
    predictions, failed_examples, exceptions = parallel(
        [(generator, example) for example in examples]
    )
    failed_errors_by_example_id = {
        id(example): exc
        for example, exc in zip(failed_examples, exceptions, strict=True)
    }

    results: list[VisGenResult] = []
    for example, prediction in zip(examples, predictions, strict=True):
        if prediction is None:
            exc = failed_errors_by_example_id.get(id(example))
            reason = "Generation returned no prediction."
            if exc is not None:
                reason = f"Generation failed after retries: {_summarize_exception(exc)}"
            results.append(failed_example_to_result(example, reason))
            continue

        try:
            output = prediction_to_output(example, prediction)
        except Exception as exc:
            results.append(
                failed_example_to_result(
                    example,
                    f"Prediction normalization failed: {_summarize_exception(exc)}",
                )
            )
            continue

        results.append(output_to_result(output))
    return results


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
            "grounding_trace": prediction.grounding_trace,
        },
    )


def output_to_result(output: VisGenOutput) -> VisGenResult:
    return {
        "id": output["id"],
        "code": output["code"],
        "visualization_type": output["visualization_type"],
        "grounding_trace": output["grounding_trace"],
        "generation_error": None,
    }


def result_to_output(result: VisGenResult) -> VisGenOutput | None:
    if result["generation_error"] is not None:
        return None

    code = result["code"]
    visualization_type = result["visualization_type"]
    grounding_trace = result["grounding_trace"]
    if code is None or visualization_type is None or grounding_trace is None:
        return None

    return {
        "id": result["id"],
        "code": code,
        "visualization_type": visualization_type,
        "grounding_trace": grounding_trace,
    }


def failed_example_to_result(
    example: dspy.Example,
    reason: str,
) -> VisGenResult:
    example_inputs = example.inputs().toDict()
    return {
        "id": cast(str, example_inputs["id"]),
        "code": None,
        "visualization_type": None,
        "grounding_trace": None,
        "generation_error": reason,
    }


def _review_generated_visualization(
    backend: VisualizationBackend,
    review_signature: type[dspy.Signature],
    request_id: str,
    code: str,
    query: str,
    tablespec: str,
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
            review = _call_with_transient_retry(
                lambda: reviewer(
                    vis=dspy.Image(image),
                    code=code,
                    query=query,
                    tablespec=tablespec,
                    requirements=requirements,
                )
            )
    except Exception as exc:
        return _failed_implementation_review(
            f"Code executed and rasterization succeeded, but the implementation reviewer failed: {_summarize_exception(exc)}"
        )

    feedback = [item.strip() for item in review.feedback if item.strip()]
    requirements_followed = review.requirements_followed
    requirement_trace = review.requirement_trace
    implementation_acceptable = (
        requirements_followed
        and review.no_truncation
        and review.no_overlap
        and review.text_readable
        and review.data_readable
    )
    if (
        not implementation_acceptable
        or not review.no_truncation
        or not review.no_overlap
        or not review.text_readable
        or not review.data_readable
        or not requirements_followed
    ):
        reasoning = review.reasoning.strip()
        explicit_reason = (
            "Code executed and rasterization succeeded, but the implementation "
            f"reviewer flagged requirement, code, or visible-quality issues. {reasoning}"
        ).strip()
        return {
            "no_truncation": review.no_truncation,
            "no_overlap": review.no_overlap,
            "text_readable": review.text_readable,
            "data_readable": review.data_readable,
            "implementation_acceptable": implementation_acceptable,
            "requirements_followed": requirements_followed,
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
        "requirement_trace": {},
        "implementation_reasoning": reason,
        "implementation_feedback": [reason],
    }


def _reward_prediction(prediction: dspy.Prediction) -> float:
    return float(
        (
            prediction.no_truncation
            + prediction.no_overlap
            + prediction.text_readable
            + prediction.data_readable
            + prediction.requirements_followed
        )
        / 5
    )


def _build_retry_feedback(
    prediction: dspy.Prediction,
    attempt_number: int,
) -> str:
    payload = {
        "source_attempt": attempt_number,
        "failed_checks": _failed_review_checks(prediction),
        "retry_instruction": (
            "Fix only the issues listed here. Preserve already-correct "
            "behavior unless a listed issue requires changing it."
        ),
        "review": {
            "implementation_acceptable": prediction.implementation_acceptable,
            "requirements_followed": prediction.requirements_followed,
            "no_truncation": prediction.no_truncation,
            "no_overlap": prediction.no_overlap,
            "text_readable": prediction.text_readable,
            "data_readable": prediction.data_readable,
            "implementation_reasoning": prediction.implementation_reasoning,
            "implementation_feedback": prediction.implementation_feedback,
            "requirement_trace": prediction.requirement_trace,
        },
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)


def _failed_review_checks(prediction: dspy.Prediction) -> list[str]:
    failed_checks: list[str] = []
    if not prediction.requirements_followed:
        failed_checks.append("requirements_followed")
    if not prediction.no_truncation:
        failed_checks.append("no_truncation")
    if not prediction.no_overlap:
        failed_checks.append("no_overlap")
    if not prediction.text_readable:
        failed_checks.append("text_readable")
    if not prediction.data_readable:
        failed_checks.append("data_readable")
    if not prediction.implementation_acceptable:
        failed_checks.append("implementation_acceptable")
    return failed_checks


def _rollout_start(lm: dspy.LM | None) -> int:
    if lm is None:
        return 0
    return int(lm.kwargs.get("rollout_id", 0) or 0)


def _attempt_lm(
    base_lm: dspy.LM | None,
    rollout_id: int,
) -> dspy.LM | None:
    if base_lm is None:
        return None
    return base_lm.copy(rollout_id=rollout_id, temperature=1.0)


def _summarize_exception(exc: Exception) -> str:
    message = " ".join(str(exc).split()).strip()
    if not message:
        return type(exc).__name__
    message = f"{type(exc).__name__}: {message}"
    return message[:240]


def _call_with_transient_retry(func: Callable[[], _RetryT]) -> _RetryT:
    @retry(
        stop=stop_after_attempt(TRANSIENT_RETRY_ATTEMPTS),
        wait=wait_fixed(TRANSIENT_RETRY_WAIT_SECONDS),
        reraise=True,
    )
    def _invoke() -> _RetryT:
        return func()

    return _invoke()
