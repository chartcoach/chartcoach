from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import polars as pl

from visground.viewer.backend import VisGroundViewerBackend
from visground.viewer.export import export_viewer_artifact
from visground.viewer.runtime_config import (
    serialize_viewer_runtime_config,
    viewer_runtime_config_sidecar_path,
)
from visground.viewer.spec import ViewerConfig, ViewerDimensionSpec, ViewerLayout


def make_viewer_config() -> ViewerConfig:
    return ViewerConfig(
        image_base_url="https://example.com/charts/",
        case_id_field="vis_id",
        case_label_field="query",
        dimensions=(
            ViewerDimensionSpec(
                id="objective",
                label="Objective",
                aliases={"select": "Select", "refine": "Refine"},
                order={"select": 0, "refine": 1},
            ),
            ViewerDimensionSpec(
                id="model",
                label="Model",
            ),
            ViewerDimensionSpec(
                id="grammar",
                label="Grammar",
                null_label="No grammar",
            ),
        ),
        filter_dimensions=("objective",),
        axis_dimensions=("model", "grammar"),
        default_filters={"objective": "select"},
        default_layout=ViewerLayout(
            row_dimension="model",
            column_dimension="grammar",
            group_dimension=None,
        ),
        guideline_details_by_id={"g-1": {"title": "Ignored by runtime serializer"}},
        search_fields=("query", "objective"),
    )


def make_candidates_df() -> pl.DataFrame:
    return pl.DataFrame(
        [
            {
                "visgen_id": "vg-1",
                "vis_id": "case-1",
                "query": "Show sales by month",
                "objective": "select",
                "model": "gpt-5.4",
                "grammar": "altair",
                "guideline_ids": ["g-1"],
            }
        ]
    )


class ViewerRuntimeConfigTests(unittest.TestCase):
    maxDiff = None

    def test_runtime_config_serializer_keeps_only_browser_fields(self) -> None:
        runtime_config = serialize_viewer_runtime_config(make_viewer_config())

        self.assertEqual(
            set(runtime_config),
            {
                "dimensions",
                "filter_dimensions",
                "axis_dimensions",
                "default_filters",
                "default_layout",
            },
        )
        self.assertEqual(runtime_config["filter_dimensions"], ["objective"])
        self.assertEqual(runtime_config["axis_dimensions"], ["model", "grammar"])
        self.assertEqual(runtime_config["default_filters"], {"objective": "select"})
        self.assertEqual(
            runtime_config["default_layout"],
            {
                "row_dimension": "model",
                "column_dimension": "grammar",
                "group_dimension": None,
            },
        )
        self.assertEqual(
            runtime_config["dimensions"],
            [
                {
                    "id": "objective",
                    "label": "Objective",
                    "nullLabel": "None",
                    "noneValueMode": "null",
                    "aliases": {"select": "Select", "refine": "Refine"},
                    "order": {"select": 0, "refine": 1},
                },
                {
                    "id": "model",
                    "label": "Model",
                    "nullLabel": "None",
                    "noneValueMode": "null",
                    "aliases": {},
                    "order": {},
                },
                {
                    "id": "grammar",
                    "label": "Grammar",
                    "nullLabel": "No grammar",
                    "noneValueMode": "null",
                    "aliases": {},
                    "order": {},
                },
            ],
        )

    def test_export_viewer_artifact_writes_runtime_config_sidecar(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            artifact_path = Path(tmp_dir) / "viewer.parquet"
            config = make_viewer_config()

            exported_path = export_viewer_artifact(
                candidates_df=make_candidates_df(),
                viewer_config=config,
                output_path=artifact_path,
                show_scores=False,
            )

            sidecar_path = viewer_runtime_config_sidecar_path(exported_path)
            self.assertEqual(exported_path, artifact_path)
            self.assertTrue(exported_path.is_file())
            self.assertEqual(sidecar_path, Path(tmp_dir) / "viewer.config.json")
            self.assertTrue(sidecar_path.is_file())
            self.assertEqual(
                json.loads(sidecar_path.read_text()),
                serialize_viewer_runtime_config(config),
            )

    def test_backend_exposes_runtime_config_for_anywidget_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            artifact_path = Path(tmp_dir) / "widget-viewer.parquet"
            config = make_viewer_config()

            with patch.dict(
                os.environ,
                {"VISGROUND_VIEWER_ARTIFACT_PATH": str(artifact_path)},
                clear=False,
            ):
                backend = VisGroundViewerBackend(
                    candidates_df=make_candidates_df(),
                    viewer_config=config,
                    show_scores=False,
                )

            self.assertEqual(backend._artifact_path, artifact_path)
            self.assertEqual(
                backend._viewer_config_path,
                Path(tmp_dir) / "widget-viewer.config.json",
            )
            self.assertEqual(
                backend._viewer_config,
                serialize_viewer_runtime_config(config),
            )


if __name__ == "__main__":
    unittest.main()
