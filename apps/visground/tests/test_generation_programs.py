from types import SimpleNamespace
from typing import cast

import dspy
import PIL.Image

from visground.generation.backends.base import VisualizationBackend
from visground.generation.programs import (
    _review_generated_visualization,
    build_refine_generator,
)
from visground.generation.models import VisualizationRequestRecord
from visground.generation.signatures import ReviewVisualizationImplementation


class DummyBackend(VisualizationBackend[object]):
    dataset = None

    def __init__(self) -> None:
        self.materialize_args: tuple[str, str] | None = None
        self.rasterize_arg: object | None = None

    def build_requirements(
        self,
        req: VisualizationRequestRecord,
    ) -> list[str]:
        raise NotImplementedError

    def materialize_visualization(self, id: str, code: str) -> object:
        self.materialize_args = (id, code)
        return {"request_id": id, "code": code}

    def rasterize(self, chart: object) -> PIL.Image.Image:
        self.rasterize_arg = chart
        return PIL.Image.new("RGB", (16, 16), "white")


def _review_prediction(**overrides: object) -> SimpleNamespace:
    payload: dict[str, object] = {
        "feedback": [],
        "requirements_followed": True,
        "no_unprescribed_design": True,
        "requirement_trace": {
            "requirement_1": "Explicitly implemented in code and visible in the chart."
        },
        "implementation_acceptable": True,
        "no_truncation": True,
        "no_overlap": True,
        "text_readable": True,
        "data_readable": True,
        "layout_balanced": True,
        "data_operations_correct": True,
        "self_explanatory": True,
        "reasoning": "Looks correct.",
    }
    payload.update(overrides)
    return SimpleNamespace(**payload)


def _patch_predict(
    monkeypatch,
    *,
    returned_prediction: SimpleNamespace,
    capture: dict[str, object],
) -> None:
    class FakePredict:
        def __init__(self, signature, temperature: float = 0.0) -> None:
            capture["signature"] = signature
            capture["temperature"] = temperature

        def __call__(self, **kwargs):
            capture["kwargs"] = kwargs
            return returned_prediction

    monkeypatch.setattr(dspy, "Predict", FakePredict)


def test_review_generated_visualization_passes_code_and_context_to_reviewer(
    monkeypatch,
) -> None:
    capture: dict[str, object] = {}
    _patch_predict(
        monkeypatch,
        returned_prediction=_review_prediction(),
        capture=capture,
    )
    backend = DummyBackend()
    code = "```python\nchart = df\n```"
    query = "Show average sales by region."
    tablespec = '{"fields":{"region":{"dtype":"str"}}}'
    requirements = ["Use a bar chart."]

    result = _review_generated_visualization(
        backend=backend,
        review_signature=ReviewVisualizationImplementation,
        request_id="case-1",
        code=code,
        query=query,
        tablespec=tablespec,
        requirements=requirements,
        lm=None,
    )

    assert backend.materialize_args == ("case-1", code)
    assert capture["signature"] is ReviewVisualizationImplementation
    kwargs = cast(dict[str, object], capture["kwargs"])
    assert kwargs["code"] == code
    assert kwargs["query"] == query
    assert kwargs["tablespec"] == tablespec
    assert kwargs["requirements"] == requirements
    assert isinstance(kwargs["vis"], dspy.Image)
    assert result["implementation_acceptable"] is True
    assert result["layout_balanced"] is True
    assert result["data_operations_correct"] is True


def test_review_generated_visualization_rejects_new_strictness_failures(
    monkeypatch,
) -> None:
    capture: dict[str, object] = {}
    _patch_predict(
        monkeypatch,
        returned_prediction=_review_prediction(
            layout_balanced=False,
            data_operations_correct=False,
            reasoning="Layout is cramped and required aggregation is missing.",
        ),
        capture=capture,
    )

    result = _review_generated_visualization(
        backend=DummyBackend(),
        review_signature=ReviewVisualizationImplementation,
        request_id="case-2",
        code="```python\nchart = df\n```",
        query="Show average sales by region.",
        tablespec='{"fields":{"region":{"dtype":"str"}}}',
        requirements=["Aggregate by region before plotting."],
        lm=None,
    )

    assert result["layout_balanced"] is False
    assert result["data_operations_correct"] is False
    assert result["implementation_acceptable"] is False
    assert (
        "requirement, code, or visible-quality issues"
        in result["implementation_reasoning"]
    )


def test_build_refine_generator_reward_fn_counts_new_strictness_fields() -> None:
    reward_fn = build_refine_generator(DummyBackend()).reward_fn
    good_pred = SimpleNamespace(
        no_truncation=True,
        no_overlap=True,
        text_readable=True,
        data_readable=True,
        layout_balanced=True,
        data_operations_correct=True,
        self_explanatory=True,
        implementation_acceptable=True,
        requirements_followed=True,
        no_unprescribed_design=True,
    )

    assert reward_fn({}, good_pred) == 1.0

    cramped_pred = SimpleNamespace(**{**good_pred.__dict__, "layout_balanced": False})
    assert reward_fn({}, cramped_pred) == 0.9

    wrong_ops_pred = SimpleNamespace(
        **{**good_pred.__dict__, "data_operations_correct": False}
    )
    assert reward_fn({}, wrong_ops_pred) == 0.9
