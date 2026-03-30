from __future__ import annotations

import unittest

import polars as pl

from visground.viewer import ViewerConfig, ViewerDimensionSpec, ViewerLayout
from visground.viewer.data import (
    build_overview_matrix,
    build_ui_schema,
    default_selection_from_registry,
    discover_registry,
    normalize_selection,
)


def make_viewer_config(*, axis_dimensions: tuple[str, ...]) -> ViewerConfig:
    return ViewerConfig(
        case_id_field="vis_id",
        case_label_field="query",
        dimensions=(
            ViewerDimensionSpec(id="objective", label="Objective"),
            ViewerDimensionSpec(
                id="request_chart", label="Chart type", null_label="All"
            ),
            ViewerDimensionSpec(id="audience", label="Audience", null_label="None"),
            ViewerDimensionSpec(
                id="grammar",
                label="Grammar",
                aliases={
                    "altair": "Altair",
                    "matplotlib": "Matplotlib",
                    "plotly": "Plotly",
                },
            ),
            ViewerDimensionSpec(
                id="grounding_mode",
                label="Grounding",
                aliases={"none": "Ungrounded", "hybrid": "Hybrid"},
                order={"none": 0, "hybrid": 1},
            ),
            ViewerDimensionSpec(id="model", label="Model"),
            ViewerDimensionSpec(
                id="temperature",
                label="Temperature",
                aliases={"cold": "Cold", "warm": "Warm"},
                order={"cold": 0, "warm": 1},
            ),
        ),
        filter_dimensions=("objective", "request_chart", "audience"),
        axis_dimensions=axis_dimensions,
        default_filters={
            "objective": "select",
            "request_chart": None,
            "audience": None,
        },
        default_layout=ViewerLayout(
            row_dimension=axis_dimensions[0],
            column_dimension=axis_dimensions[1],
            group_dimension=axis_dimensions[2] if len(axis_dimensions) > 2 else None,
        ),
        image_base_url="http://127.0.0.1:8000",
    )


def make_candidates_df() -> pl.DataFrame:
    records: list[dict[str, object]] = []
    for grounding_mode in ("none", "hybrid"):
        for grammar in ("altair", "matplotlib", "plotly"):
            records.append(
                {
                    "visgen_id": f"case-1-{grounding_mode}-{grammar}",
                    "vis_id": "case-1",
                    "query": "Compare outputs",
                    "objective": "select",
                    "request_chart": None,
                    "audience": None,
                    "model": "gpt-5.4",
                    "grounding_mode": grounding_mode,
                    "grammar": grammar,
                    "guideline_ids": (
                        []
                        if grounding_mode == "none"
                        else {
                            "altair": ["g-1", "g-2"],
                            "matplotlib": ["g-2", "g-3"],
                            "plotly": ["g-1", "g-3"],
                        }[grammar]
                    ),
                    "overall_score": {
                        "altair": 0.81,
                        "matplotlib": 0.83,
                        "plotly": 0.8,
                    }[grammar],
                }
            )
    return pl.from_dicts(records)


def make_four_axis_df() -> pl.DataFrame:
    records: list[dict[str, object]] = []
    for temperature in ("cold", "warm"):
        for grounding_mode in ("none", "hybrid"):
            for grammar in ("altair", "matplotlib"):
                records.append(
                    {
                        "visgen_id": f"case-2-{temperature}-{grounding_mode}-{grammar}",
                        "vis_id": "case-2",
                        "query": "Compare four axes",
                        "objective": "select",
                        "request_chart": None,
                        "audience": None,
                        "model": "gpt-5.4",
                        "temperature": temperature,
                        "grounding_mode": grounding_mode,
                        "grammar": grammar,
                        "guideline_ids": [],
                        "overall_score": 0.75,
                    }
                )
    return pl.from_dicts(records)


class ViewerDataTests(unittest.TestCase):
    def test_default_selection_honors_configured_group_dimension(self) -> None:
        config = make_viewer_config(
            axis_dimensions=("model", "grounding_mode", "grammar")
        )
        registry = discover_registry(make_candidates_df(), config=config)

        selection = default_selection_from_registry(registry, config=config)

        self.assertEqual(selection["layout"]["group_dimension"], "grammar")

    def test_normalize_selection_preserves_explicit_no_grouping(self) -> None:
        config = make_viewer_config(
            axis_dimensions=("model", "grounding_mode", "grammar")
        )
        candidates_df = make_candidates_df()
        registry = discover_registry(candidates_df, config=config)
        case_df = candidates_df.filter(pl.col("vis_id") == "case-1")

        normalized = normalize_selection(
            case_df,
            registry=registry,
            config=config,
            filters={"objective": "select", "request_chart": None, "audience": None},
            layout={
                "row_dimension": "model",
                "column_dimension": "grounding_mode",
                "group_dimension": None,
            },
        )

        self.assertIsNone(normalized["selection"]["layout"]["group_dimension"])
        schema = build_ui_schema(
            selection=normalized["selection"],
            axis_dimensions=normalized["axis_dimensions"],
            filter_controls=normalized["filter_controls"],
            layout_controls=normalized["layout_controls"],
            config=config,
        )
        self.assertEqual(schema["matrix_axes"]["hidden_labels"], ["Grammar"])

    def test_hidden_grammar_becomes_variants_in_no_grouping_layout(self) -> None:
        config = make_viewer_config(
            axis_dimensions=("model", "grounding_mode", "grammar")
        )

        overview = build_overview_matrix(
            scoped_df=make_candidates_df(),
            layout={
                "row_dimension": "model",
                "column_dimension": "grounding_mode",
                "group_dimension": None,
            },
            config=config,
        )

        self.assertEqual(overview["kind"], "flat")
        first_cell = overview["rows"][0]["cells"][0]
        self.assertEqual(first_cell["hidden_axes"], ["grammar"])
        self.assertEqual(first_cell["variant_count"], 3)
        self.assertEqual(
            [entry["variant_label"] for entry in first_cell["variants"]],
            [
                "Grammar: Matplotlib",
                "Grammar: Altair",
                "Grammar: Plotly",
            ],
        )
        grounded_column = overview["columns"][1]
        self.assertEqual(grounded_column["label"], "Hybrid")
        self.assertEqual(grounded_column["meta_kind"], "guidelines")
        self.assertEqual(grounded_column["meta_label"], "3 guidelines")
        ungrounded_column = overview["columns"][0]
        self.assertIsNone(ungrounded_column["meta_label"])

    def test_two_hidden_axes_are_preserved_for_future_inner_layouts(self) -> None:
        config = make_viewer_config(
            axis_dimensions=("model", "temperature", "grounding_mode", "grammar")
        )

        overview = build_overview_matrix(
            scoped_df=make_four_axis_df(),
            layout={
                "row_dimension": "model",
                "column_dimension": "temperature",
                "group_dimension": None,
            },
            config=config,
        )

        first_cell = overview["rows"][0]["cells"][0]
        self.assertEqual(first_cell["hidden_axes"], ["grounding_mode", "grammar"])
        self.assertEqual(first_cell["variant_count"], 4)
        self.assertEqual(
            first_cell["variants"][0]["variant_label"],
            "Grounding: Ungrounded · Grammar: Altair",
        )


if __name__ == "__main__":
    unittest.main()
