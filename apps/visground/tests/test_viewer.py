from __future__ import annotations

from pathlib import Path
from typing import cast

import polars as pl
import pytest
from PIL import Image

from visground.datasets import VisEvalDataset, VisGroundDataset
from visground.viewer import VisGroundViewer
from visground.viewer.data import (
    build_grounding_model_matrix,
    build_ui_schema,
    default_selection_from_registry,
    discover_registry,
    enrich_candidates_with_scores,
    judgement_dimensions,
    normalize_selection,
    serialize_candidate_record,
)
from visground.viewer.rendering import ChartImageService


class _FakeDataset:
    pass


def _grounding_row(
    grounding_id: str,
    *,
    vis_id: str,
    query: str,
    objective: str,
    grounding_mode: str,
    audience: str | None,
    guideline_ids: list[str],
    data_profile: dict[str, object] | None = None,
) -> dict[str, object]:
    return {
        "grounding_id": grounding_id,
        "grounding_mode": grounding_mode,
        "request": {
            "id": vis_id,
            "query": query,
            "task": "compare",
            "scope": "global",
            "time_mode": "none",
            "chart": "line",
            "objective": objective,
            "audience": audience,
            "data_profile": data_profile or {"shape": "varied"},
        },
        "result": {
            "doc_ids": [],
            "guideline_ids": guideline_ids,
            "guidance": [],
        },
    }


def _scenario_item(
    grounding_id: str,
    visgen_id: str,
    query: str,
) -> dict[str, object]:
    return {
        "visgen_id": visgen_id,
        "grounding_id": grounding_id,
        "input": {
            "id": "vis-1",
            "query": query,
            "requirements": [],
        },
    }


def _output_item(
    *,
    interpretation: str,
    chart_type: str = "line",
) -> dict[str, object]:
    return {
        "id": "vis-1",
        "code": "```python\nchart = None\n```",
        "visualization_type": chart_type,
        "query_interpretation": interpretation,
        "design_rationale": [f"Reason for {interpretation}"],
        "grounding_trace": [f"Trace for {interpretation}"],
    }


def _grounding_df() -> pl.DataFrame:
    refine_query = (
        "Find players with a overall rating greater than or equal to 75 and use line "
        "chart to show the trend in the year of birth for players with different "
        "foot preferences."
    )
    select_query = (
        "Show the trend in year of birth for players with different foot preferences "
        "among players whose overall rating is greater than or equal to 75."
    )
    rows: list[dict[str, object]] = []
    for grounding_mode, guideline_ids in (
        ("none", []),
        ("structured", ["structured-guideline", "structured-guideline"]),
    ):
        rows.append(
            _grounding_row(
                f"vis-1-refine-{grounding_mode}-none",
                vis_id="vis-1",
                query=refine_query,
                objective="refine",
                grounding_mode=grounding_mode,
                audience=None,
                guideline_ids=guideline_ids,
            )
        )
        rows.append(
            _grounding_row(
                f"vis-1-select-{grounding_mode}-none",
                vis_id="vis-1",
                query=select_query,
                objective="select",
                grounding_mode=grounding_mode,
                audience=None,
                guideline_ids=guideline_ids,
            )
        )

    for audience, suffix in (
        ("novice", "novice"),
        ("casual", "casual"),
        ("expert", "expert"),
    ):
        rows.append(
            _grounding_row(
                f"vis-1-select-none-{suffix}",
                vis_id="vis-1",
                query=select_query,
                objective="select",
                grounding_mode="none",
                audience=audience,
                guideline_ids=[f"{suffix}-none-guideline"],
            )
        )
        rows.append(
            _grounding_row(
                f"vis-1-select-structured-{suffix}",
                vis_id="vis-1",
                query=select_query,
                objective="select",
                grounding_mode="structured",
                audience=audience,
                guideline_ids=[f"{suffix}-structured-guideline"],
            )
        )
    return pl.from_dicts(rows)


def _generated_df() -> pl.DataFrame:
    refine_query = (
        "Find players with a overall rating greater than or equal to 75 and use line "
        "chart to show the trend in the year of birth for players with different "
        "foot preferences."
    )
    select_query = (
        "Show the trend in year of birth for players with different foot preferences "
        "among players whose overall rating is greater than or equal to 75."
    )
    models = ("claude-sonnet-4.6", "gpt-5.4")

    rows = []
    for model in models:
        rows.append(
            {
                "run": {
                    "model": model,
                    "grammar": "altair",
                    "scenario": [
                        _scenario_item(
                            "vis-1-refine-none-none",
                            f"vis-1-refine-none-none-altair-{model}",
                            refine_query,
                        ),
                        _scenario_item(
                            "vis-1-refine-structured-none",
                            f"vis-1-refine-structured-none-altair-{model}",
                            refine_query,
                        ),
                        _scenario_item(
                            "vis-1-select-none-none",
                            f"vis-1-select-none-none-altair-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-structured-none",
                            f"vis-1-select-structured-none-altair-{model}",
                            select_query,
                        ),
                    ],
                },
                "outputs": [
                    _output_item(interpretation=f"refine none altair {model}"),
                    _output_item(interpretation=f"refine structured altair {model}"),
                    _output_item(interpretation=f"select none altair {model}"),
                    _output_item(interpretation=f"select structured altair {model}"),
                ],
            }
        )
        rows.append(
            {
                "run": {
                    "model": model,
                    "grammar": "matplotlib",
                    "scenario": [
                        _scenario_item(
                            "vis-1-refine-none-none",
                            f"vis-1-refine-none-none-matplotlib-{model}",
                            refine_query,
                        ),
                        _scenario_item(
                            "vis-1-refine-structured-none",
                            f"vis-1-refine-structured-none-matplotlib-{model}",
                            refine_query,
                        ),
                        _scenario_item(
                            "vis-1-select-none-none",
                            f"vis-1-select-none-none-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-structured-none",
                            f"vis-1-select-structured-none-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-none-novice",
                            f"vis-1-select-none-novice-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-structured-novice",
                            f"vis-1-select-structured-novice-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-none-casual",
                            f"vis-1-select-none-casual-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-structured-casual",
                            f"vis-1-select-structured-casual-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-none-expert",
                            f"vis-1-select-none-expert-matplotlib-{model}",
                            select_query,
                        ),
                        _scenario_item(
                            "vis-1-select-structured-expert",
                            f"vis-1-select-structured-expert-matplotlib-{model}",
                            select_query,
                        ),
                    ],
                },
                "outputs": [
                    _output_item(interpretation=f"refine none matplotlib {model}"),
                    _output_item(
                        interpretation=f"refine structured matplotlib {model}"
                    ),
                    _output_item(interpretation=f"select none matplotlib {model}"),
                    _output_item(
                        interpretation=f"select structured matplotlib {model}"
                    ),
                    _output_item(
                        interpretation=f"select none novice matplotlib {model}"
                    ),
                    _output_item(
                        interpretation=f"select structured novice matplotlib {model}"
                    ),
                    _output_item(
                        interpretation=f"select none casual matplotlib {model}"
                    ),
                    _output_item(
                        interpretation=f"select structured casual matplotlib {model}"
                    ),
                    _output_item(
                        interpretation=f"select none expert matplotlib {model}"
                    ),
                    _output_item(
                        interpretation=f"select structured expert matplotlib {model}"
                    ),
                ],
            }
        )
    return pl.from_dicts(rows)


def _judgements_df() -> pl.DataFrame:
    return pl.from_dicts(
        [
            {
                "visgen_id": "vis-1-refine-structured-none-altair-claude-sonnet-4.6",
                "judgement": {
                    "data_fidelity": {"score": 5, "reasoning": "accurate"},
                    "semantic_readability": {"score": 4, "reasoning": "clear"},
                    "insight_discovery": {"score": 3, "reasoning": "adequate"},
                    "design_style": {"score": 4, "reasoning": "clean"},
                    "visual_composition": {"score": 5, "reasoning": "balanced"},
                    "color_harmony": {"score": 3, "reasoning": "muted"},
                },
            }
        ]
    )


def _seed_store(root: Path, *, with_judgements: bool = False) -> VisGroundDataset:
    store = VisGroundDataset(root=root)
    store.write_grounding_df(_grounding_df())
    store.write_generated_df(_generated_df())
    if with_judgements:
        store.write_judgements_df(_judgements_df())
    return store


def test_discover_registry_scans_concrete_dimensions_from_artifacts(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    registry = discover_registry(store.read_generated_candidates_df())

    assert registry["vis_ids"] == ["vis-1"]
    assert registry["grounding_modes"] == ["none", "structured"]
    assert registry["models"] == ["claude-sonnet-4.6", "gpt-5.4"]
    assert registry["grammars_by_objective"]["select"] == ["altair", "matplotlib"]
    assert registry["audiences_by_objective"]["refine"] == [None]
    assert registry["audiences_by_objective"]["select"] == [
        None,
        "novice",
        "casual",
        "expert",
    ]


def test_normalize_selection_defaults_to_select_matplotlib_none(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    case_df = store.read_generated_candidates_df().filter(pl.col("vis_id") == "vis-1")
    registry = discover_registry(case_df)

    assert default_selection_from_registry(registry) == {
        "objective": "select",
        "grammar": "matplotlib",
        "audience": None,
    }

    normalized = normalize_selection(
        case_df,
        registry=registry,
        objective=None,
        grammar=None,
        audience=None,
    )

    assert normalized["selection"] == {
        "objective": "select",
        "grammar": "matplotlib",
        "audience": None,
    }


def test_normalize_selection_keeps_audience_stable_for_sparse_slice(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    case_df = store.read_generated_candidates_df().filter(pl.col("vis_id") == "vis-1")
    registry = discover_registry(case_df)

    normalized = normalize_selection(
        case_df,
        registry=registry,
        objective="select",
        grammar="altair",
        audience="expert",
    )

    assert normalized["selection"] == {
        "objective": "select",
        "grammar": "altair",
        "audience": "expert",
    }
    assert normalized["selection_df"].is_empty()


def test_normalize_selection_disables_audience_for_refine(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    case_df = store.read_generated_candidates_df().filter(pl.col("vis_id") == "vis-1")
    registry = discover_registry(case_df)

    normalized = normalize_selection(
        case_df,
        registry=registry,
        objective="refine",
        grammar="altair",
        audience="expert",
    )

    assert normalized["selection"] == {
        "objective": "refine",
        "grammar": "altair",
        "audience": None,
    }
    assert normalized["options"]["audience_enabled"] is False


def test_build_grounding_model_matrix_uses_discovered_dimensions(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    case_df = store.read_generated_candidates_df().filter(pl.col("vis_id") == "vis-1")
    registry = discover_registry(case_df)
    normalized = normalize_selection(
        case_df,
        registry=registry,
        objective="select",
        grammar="matplotlib",
        audience="expert",
    )

    matrix = build_grounding_model_matrix(
        objective_grammar_df=normalized["objective_grammar_df"],
        selection_df=normalized["selection_df"],
        audience=normalized["selection"]["audience"],
    )

    assert [column["value"] for column in matrix["columns"]] == [
        "claude-sonnet-4.6",
        "gpt-5.4",
    ]
    assert [row["grounding_label"] for row in matrix["rows"]] == [
        "Ungrounded",
        "Grounded",
    ]


def test_build_ui_schema_emits_filters_axes_labels_and_defaults(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    registry = discover_registry(store.read_generated_candidates_df())
    selection = {
        "objective": "refine",
        "grammar": "altair",
        "audience": None,
    }

    schema = build_ui_schema(
        registry=registry,
        selection=selection,
        asset_version="abc123",
    )

    assert schema["asset_version"] == "abc123"
    assert schema["defaults"] == {
        "objective": "select",
        "grammar": "matplotlib",
        "audience": None,
    }
    assert schema["matrix_axes"]["row_dimension"] == "grounding_mode"
    assert schema["matrix_axes"]["column_dimension"] == "model"
    assert [filter_config["id"] for filter_config in schema["filters"]] == [
        "objective",
        "grammar",
        "audience",
    ]
    assert schema["filters"][-1]["disabled"] is True
    assert schema["display_labels"]["grounding_mode"]["none"] == "Ungrounded"


def test_placeholder_reason_is_specific_for_sparse_audience_slice(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path)
    case_df = store.read_generated_candidates_df().filter(pl.col("vis_id") == "vis-1")
    registry = discover_registry(case_df)
    normalized = normalize_selection(
        case_df,
        registry=registry,
        objective="select",
        grammar="altair",
        audience="expert",
    )

    matrix = build_grounding_model_matrix(
        objective_grammar_df=normalized["objective_grammar_df"],
        selection_df=normalized["selection_df"],
        audience=normalized["selection"]["audience"],
    )

    assert all(
        cell["placeholder_reason"] == "not run for this audience"
        for row in matrix["rows"]
        for cell in row["cells"]
    )


def test_query_provenance_switches_by_objective(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path, with_judgements=True)
    viewer = VisGroundViewer(store=store, dataset=cast(VisEvalDataset, _FakeDataset()))

    refine_payload, _ = viewer.load_view({"objective": "refine"}, [])
    select_payload, _ = viewer.load_view({"objective": "select"}, [])

    assert "use line chart" in refine_payload["overview"]["nl_query"]
    assert "use line chart" not in select_payload["overview"]["nl_query"]
    assert "different foot preferences" in select_payload["overview"]["nl_query"]


def test_enrich_candidates_with_scores_joins_optional_badges() -> None:
    candidates_df = pl.from_dicts(
        [
            {"visgen_id": "candidate-1", "vis_id": "vis-1"},
            {"visgen_id": "candidate-2", "vis_id": "vis-1"},
        ]
    )
    judgements_df = pl.from_dicts(
        [
            {
                "visgen_id": "candidate-1",
                "judgement": _judgements_df().item(0, "judgement"),
            }
        ]
    )

    enriched = enrich_candidates_with_scores(candidates_df, judgements_df).sort(
        "visgen_id"
    )

    assert enriched.row(0, named=True)["overall_score"] == 4.0
    assert enriched.row(1, named=True)["overall_score"] is None


def test_judgement_dimensions_preserve_reasoning() -> None:
    dimensions = judgement_dimensions(_judgements_df().item(0, "judgement"))
    assert dimensions[0]["reasoning"] == "accurate"


def test_serialize_candidate_record_includes_guidelines_and_trace_for_hover() -> None:
    candidate = {
        "visgen_id": "candidate-1",
        "vis_id": "vis-1",
        "query": "Show the analytical intent.",
        "grounding_mode": "structured",
        "objective": "select",
        "model": "claude-sonnet-4.6",
        "grammar": "matplotlib",
        "audience": "expert",
        "guideline_ids": ["g-1", "g-1", "g-2"],
        "visualization_type": "line",
        "query_interpretation": "Interpretation",
        "design_rationale": ["Reason"],
        "grounding_trace": ["Trace"],
        "code": "chart = None",
        "judgement": _judgements_df().item(0, "judgement"),
        "overall_score": 4.0,
    }

    payload = serialize_candidate_record(
        candidate,
        image_loader=lambda record, variant: "data:image/jpeg;base64,AAA",
        image_variant="panel",
        include_detail=False,
    )

    assert payload["grounding_label"] == "Grounded"
    assert payload["guideline_ids"] == ["g-1", "g-2"]
    assert payload["grounding_story"] == ["Trace"]


def test_serialize_candidate_record_exposes_judge_reasoning_in_detail() -> None:
    candidate = {
        "visgen_id": "candidate-1",
        "vis_id": "vis-1",
        "query": "Show the analytical intent.",
        "grounding_mode": "structured",
        "objective": "select",
        "model": "claude-sonnet-4.6",
        "grammar": "matplotlib",
        "audience": "expert",
        "guideline_ids": ["g-1", "g-2"],
        "visualization_type": "line",
        "query_interpretation": "Interpretation",
        "design_rationale": ["Reason"],
        "grounding_trace": ["Trace"],
        "code": "chart = None",
        "judgement": _judgements_df().item(0, "judgement"),
        "overall_score": 4.0,
    }

    payload = serialize_candidate_record(
        candidate,
        image_loader=lambda record, variant: "data:image/jpeg;base64,AAA",
        image_variant="detail",
        include_detail=True,
    )

    assert payload["nl_query"] == "Show the analytical intent."
    assert payload["judgement_dimensions"][0]["reasoning"] == "accurate"


def test_chart_image_service_uses_cached_chart_bytes_deterministically(
    tmp_path: Path,
) -> None:
    store = VisGroundDataset(root=tmp_path)
    store.write_chart_image("cached", Image.new("RGB", (80, 40), "white"))
    service = ChartImageService(store, cast(VisEvalDataset, _FakeDataset()))

    first = service.image_data_url(
        {
            "visgen_id": "cached",
            "vis_id": "vis-1",
            "grammar": "altair",
            "code": "chart = None",
        },
        "panel",
    )
    second = service.image_data_url(
        {
            "visgen_id": "cached",
            "vis_id": "vis-1",
            "grammar": "altair",
            "code": "chart = None",
        },
        "panel",
    )

    assert first == second
    assert first.startswith("data:image/jpeg;base64,")


def test_chart_image_service_renders_and_persists_missing_chart(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    store = VisGroundDataset(root=tmp_path)
    service = ChartImageService(store, cast(VisEvalDataset, _FakeDataset()))

    class _FakeBackend:
        def materialize_visualization(self, vis_id: str, code: str) -> str:
            assert vis_id == "vis-1"
            assert code == "chart = None"
            return "chart"

        def rasterize(self, chart: str) -> Image.Image:
            assert chart == "chart"
            return Image.new("RGB", (120, 80), "navy")

    monkeypatch.setattr(
        "visground.viewer.rendering.resolve_visualization_backend",
        lambda grammar, dataset: _FakeBackend(),
    )

    image_url = service.image_data_url(
        {
            "visgen_id": "missing",
            "vis_id": "vis-1",
            "grammar": "plotly",
            "code": "chart = None",
        },
        "detail",
    )

    assert image_url.startswith("data:image/jpeg;base64,")
    assert store.chart_exists("missing")


def test_chart_image_service_supports_hover_variant(tmp_path: Path) -> None:
    store = VisGroundDataset(root=tmp_path)
    store.write_chart_image("cached", Image.new("RGB", (80, 40), "white"))
    service = ChartImageService(store, cast(VisEvalDataset, _FakeDataset()))

    image_url = service.image_data_url(
        {
            "visgen_id": "cached",
            "vis_id": "vis-1",
            "grammar": "altair",
            "code": "chart = None",
        },
        "hover",
    )

    assert image_url.startswith("data:image/jpeg;base64,")


def test_visground_viewer_uses_dynamic_defaults(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path, with_judgements=True)
    viewer = VisGroundViewer(store=store, dataset=cast(VisEvalDataset, _FakeDataset()))

    init_payload, _ = viewer.initialize({}, [])

    assert init_payload["value"]["objective"] == "select"
    assert init_payload["value"]["grammar"] == "matplotlib"
    assert init_payload["value"]["audience"] is None
    assert init_payload["overview"]["ui_schema"]["defaults"] == {
        "objective": "select",
        "grammar": "matplotlib",
        "audience": None,
    }
    assert init_payload["config"]["asset_version"]


def test_visground_viewer_keeps_sparse_matrix_frame_for_audience_slice(
    tmp_path: Path,
) -> None:
    store = _seed_store(tmp_path, with_judgements=True)
    viewer = VisGroundViewer(store=store, dataset=cast(VisEvalDataset, _FakeDataset()))

    payload, _ = viewer.load_view(
        {
            "vis_id": "vis-1",
            "objective": "select",
            "grammar": "altair",
            "audience": "expert",
        },
        [],
    )

    assert payload["overview"]["selection"]["audience"] == "expert"
    assert [column["value"] for column in payload["overview"]["matrix"]["columns"]] == [
        "claude-sonnet-4.6",
        "gpt-5.4",
    ]
    assert payload["overview"]["matrix"]["rows"][0]["grounding_label"] == "Ungrounded"
    assert payload["overview"]["matrix"]["rows"][1]["grounding_label"] == "Grounded"
    assert (
        payload["overview"]["matrix"]["rows"][0]["cells"][0]["placeholder_reason"]
        == "not run for this audience"
    )


def test_visground_viewer_rejects_unknown_initial_vis_id(tmp_path: Path) -> None:
    store = _seed_store(tmp_path)

    with pytest.raises(ValueError, match="Unknown initial_vis_id"):
        VisGroundViewer(
            store=store,
            dataset=cast(VisEvalDataset, _FakeDataset()),
            initial_vis_id="missing",
        )
