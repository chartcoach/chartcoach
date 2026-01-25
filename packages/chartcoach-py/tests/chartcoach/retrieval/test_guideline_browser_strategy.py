from __future__ import annotations

import base64
from pathlib import Path

import pytest

import dspy

from chartcoach.catalog.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval import (
    GuidelineBrowserStrategy,
    ImageItem,
    RetrievalRequest,
    TextItem,
)
from chartcoach.retrieval.dspy_adapters import (
    get_image_item_by_role,
    get_text_by_role,
    image_item_to_dspy_image,
    require_image_item_by_role,
    require_text_by_role,
)
from chartcoach.retrieval.guideline_browser import (
    GuidelineBrowserTools,
    guideline_browser_inputs_from_request,
)


_PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+0pV0AAAAASUVORK5CYII="
)


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use accessible colors",
                    description="Ensure color choices are accessible.",
                    labels=["topic:color", "audience:senior"],
                    body="Body 1",
                ),
                references=["@article{a, title={A}}"],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axes clearly",
                    description="Axis labels should be clear.",
                    labels=["topic:annotation"],
                    body="Body 2",
                ),
                references=["@book{b, title={B}}"],
            ),
        ]
    )


def test_guideline_catalog_tools_support_filters(catalog: Catalog) -> None:
    tools = GuidelineBrowserTools(catalog=catalog)
    csv = tools.list_guideline_abstracts(
        where_labels=["topic:color"],
        where_reftypes=["article"],
    )
    assert "g1" in csv
    assert "g2" not in csv


def test_guideline_catalog_tools_lists_taxonomy_and_reftypes(catalog: Catalog) -> None:
    tools = GuidelineBrowserTools(catalog=catalog)
    assert tools.list_guideline_labels() == [
        "audience:senior",
        "topic:annotation",
        "topic:color",
    ]
    assert sorted(tools.list_reftypes()) == ["article", "book"]


def test_guideline_catalog_tools_can_read_by_id(catalog: Catalog) -> None:
    tools = GuidelineBrowserTools(catalog=catalog)
    out = tools.read_guidelines_by_id(["g2", "missing"])
    assert out == [
        {"id": "g2", "body": "Body 2", "references": ["@book{b, title={B}}"]}
    ]


def test_dspy_adapters_get_require_by_role(catalog: Catalog) -> None:
    request = RetrievalRequest(
        context=[
            ImageItem(role="chart", data=_PNG_1X1, mime="image/png"),
            TextItem(role="situation", text="S"),
            TextItem(role="chart_spec", text="{}"),
        ]
    )

    assert get_text_by_role(request, role="situation") == "S"
    assert get_text_by_role(request, role="missing") is None
    assert require_text_by_role(request, role="chart_spec") == "{}"
    with pytest.raises(ValueError):
        require_text_by_role(request, role="missing")

    assert get_image_item_by_role(request, role="chart") is not None
    assert get_image_item_by_role(request, role="missing") is None
    assert require_image_item_by_role(request, role="chart").mime == "image/png"
    with pytest.raises(ValueError):
        require_image_item_by_role(request, role="missing")


def test_image_item_to_dspy_image_supports_data_file_uri_and_path(
    tmp_path: Path,
) -> None:
    # `data`
    assert isinstance(
        image_item_to_dspy_image(ImageItem(role="chart", data=_PNG_1X1)), dspy.Image
    )

    # missing `data`/`uri`
    with pytest.raises(ValueError):
        image_item_to_dspy_image(ImageItem(role="chart"))

    # `file://...`
    file_uri_path = tmp_path / "chart_file_uri.png"
    file_uri_path.write_bytes(_PNG_1X1)
    assert isinstance(
        image_item_to_dspy_image(
            ImageItem(role="chart", uri=f"file://{file_uri_path}")
        ),
        dspy.Image,
    )

    # plain path string
    plain_path = tmp_path / "chart_plain.png"
    plain_path.write_bytes(_PNG_1X1)
    assert isinstance(
        image_item_to_dspy_image(ImageItem(role="chart", uri=str(plain_path))),
        dspy.Image,
    )


def test_image_item_to_dspy_image_supports_url() -> None:
    img = image_item_to_dspy_image(
        ImageItem(role="chart", uri="https://example.com/chart.png")
    )
    assert isinstance(img, dspy.Image)
    assert img.url == "https://example.com/chart.png"


def test_grounded_vis_feedback_inputs_from_request_defaults_existing_feedback() -> None:
    request = RetrievalRequest(
        context=[
            ImageItem(role="chart", data=_PNG_1X1, mime="image/png"),
            TextItem(role="situation", text="S"),
            TextItem(role="chart_spec", text="{}"),
        ]
    )
    inputs = guideline_browser_inputs_from_request(request)
    assert inputs.situation == "S"
    assert inputs.chart_spec == "{}"
    assert inputs.existing_chart_feedback == ""


def test_strategy_requires_either_lm_or_llm_config(catalog: Catalog) -> None:
    with pytest.raises(TypeError):
        GuidelineBrowserStrategy(catalog=catalog)  # type: ignore[call-arg]


def test_strategy_instantiates_default_react_program_without_calling_llm(
    catalog: Catalog,
) -> None:
    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strategy = GuidelineBrowserStrategy(catalog=catalog, lm=lm)
    assert isinstance(strategy, dspy.Module)
    assert isinstance(strategy.tools, GuidelineBrowserTools)


def test_strategy_forward_calls_program_with_adapted_inputs(catalog: Catalog) -> None:
    class DummyProgram(dspy.Module):
        def __init__(self) -> None:
            super().__init__()
            self.last_kwargs: dict[str, object] | None = None

        def forward(self, **kwargs):
            self.last_kwargs = kwargs
            return dspy.Prediction(used_guideline_ids=["g1"], feedback="OK")

    program = DummyProgram()
    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strategy = GuidelineBrowserStrategy(catalog=catalog, lm=lm)
    strategy._program = program  # type: ignore[assignment]

    request = RetrievalRequest(
        context=[
            ImageItem(role="chart", data=_PNG_1X1, mime="image/png"),
            TextItem(role="situation", text="S"),
            TextItem(role="chart_spec", text="{}"),
            TextItem(role="existing_chart_feedback", text="E"),
        ]
    )
    out = strategy(request=request)
    assert out.meta["used_guideline_ids"] == ["g1"]
    assert len(out.catalog) == 1
    assert out.catalog.entries[0].guideline.id == "g1"
    assert program.last_kwargs is not None
    assert isinstance(program.last_kwargs["chart"], dspy.Image)
    assert program.last_kwargs["situation"] == "S"
    assert program.last_kwargs["chart_spec"] == "{}"
    assert program.last_kwargs["existing_chart_feedback"] == "E"
