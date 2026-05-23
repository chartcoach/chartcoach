from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import polars as pl

from visground.viewer.backend import VisGroundViewerBackend
from visground.viewer.export import (
    default_viewer_dev_artifact_path,
    default_viewer_dev_public_artifact_path,
    export_viewer_artifact,
)
from visground.viewer.runtime_config import (
    serialize_viewer_runtime_config,
    viewer_runtime_config_sidecar_path,
)
from visground.viewer.spec import ViewerConfig, ViewerDimensionSpec, ViewerLayout
from visground.viewer.widget import _resolve_viewer_artifact_url


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

            artifact = export_viewer_artifact(
                candidates_df=make_candidates_df(),
                viewer_config=config,
                output_path=artifact_path,
                show_scores=False,
            )

            sidecar_path = viewer_runtime_config_sidecar_path(artifact.artifact_path)
            self.assertEqual(artifact.artifact_path, artifact_path)
            self.assertTrue(artifact.artifact_path.is_file())
            self.assertEqual(sidecar_path, Path(tmp_dir) / "viewer.config.json")
            self.assertEqual(artifact.runtime_config_path, sidecar_path)
            self.assertTrue(sidecar_path.is_file())
            self.assertEqual(
                artifact.runtime_config, serialize_viewer_runtime_config(config)
            )
            self.assertEqual(
                json.loads(sidecar_path.read_text()),
                serialize_viewer_runtime_config(config),
            )

    def test_export_viewer_artifact_rejects_missing_configured_dimension(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            config = ViewerConfig(
                image_base_url="https://example.com/charts/",
                case_id_field="vis_id",
                dimensions=(
                    ViewerDimensionSpec(id="model", label="Model"),
                    ViewerDimensionSpec(id="missing_dim", label="Missing"),
                ),
                filter_dimensions=(),
                axis_dimensions=("model", "missing_dim"),
                default_filters={},
                default_layout=ViewerLayout(
                    row_dimension="model",
                    column_dimension="missing_dim",
                    group_dimension=None,
                ),
            )

            with self.assertRaisesRegex(
                ValueError,
                "missing required columns: missing_dim",
            ):
                export_viewer_artifact(
                    candidates_df=make_candidates_df(),
                    viewer_config=config,
                    output_path=Path(tmp_dir) / "viewer.parquet",
                    show_scores=False,
                )

    def test_export_viewer_artifact_restores_previous_pair_on_commit_failure(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            artifact_path = Path(tmp_dir) / "viewer.parquet"
            sidecar_path = viewer_runtime_config_sidecar_path(artifact_path)
            artifact_path.write_bytes(b"old parquet")
            sidecar_path.write_text('{"old": true}\n')
            real_replace = os.replace
            failed_sidecar_commit = False

            def failing_replace(
                src: str | os.PathLike[str],
                dst: str | os.PathLike[str],
            ) -> None:
                nonlocal failed_sidecar_commit
                src_path = Path(src)
                dst_path = Path(dst)
                if (
                    dst_path == sidecar_path
                    and src_path.name.startswith(".viewer.config.json.")
                    and not failed_sidecar_commit
                ):
                    failed_sidecar_commit = True
                    raise OSError("sidecar replace failed")
                real_replace(src, dst)

            with patch(
                "visground.viewer.export.os.replace", side_effect=failing_replace
            ):
                with self.assertRaisesRegex(OSError, "sidecar replace failed"):
                    export_viewer_artifact(
                        candidates_df=make_candidates_df(),
                        viewer_config=make_viewer_config(),
                        output_path=artifact_path,
                        show_scores=False,
                    )

            self.assertEqual(artifact_path.read_bytes(), b"old parquet")
            self.assertEqual(sidecar_path.read_text(), '{"old": true}\n')

    def test_export_viewer_artifact_preserves_previous_pair_on_backup_failure(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            artifact_path = Path(tmp_dir) / "viewer.parquet"
            sidecar_path = viewer_runtime_config_sidecar_path(artifact_path)
            artifact_path.write_bytes(b"old parquet")
            sidecar_path.write_text('{"old": true}\n')
            real_replace = os.replace
            failed_backup = False

            def failing_replace(
                src: str | os.PathLike[str],
                dst: str | os.PathLike[str],
            ) -> None:
                nonlocal failed_backup
                if Path(src) == artifact_path and not failed_backup:
                    failed_backup = True
                    raise OSError("artifact backup failed")
                real_replace(src, dst)

            with patch(
                "visground.viewer.export.os.replace", side_effect=failing_replace
            ):
                with self.assertRaisesRegex(OSError, "artifact backup failed"):
                    export_viewer_artifact(
                        candidates_df=make_candidates_df(),
                        viewer_config=make_viewer_config(),
                        output_path=artifact_path,
                        show_scores=False,
                    )

            self.assertEqual(artifact_path.read_bytes(), b"old parquet")
            self.assertEqual(sidecar_path.read_text(), '{"old": true}\n')

    def test_export_viewer_artifact_keeps_backups_when_restore_fails(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            work_dir = Path(tmp_dir)
            artifact_path = work_dir / "viewer.parquet"
            sidecar_path = viewer_runtime_config_sidecar_path(artifact_path)
            artifact_path.write_bytes(b"old parquet")
            sidecar_path.write_text('{"old": true}\n')
            real_replace = os.replace
            failed_sidecar_commit = False
            failed_artifact_restore = False

            def failing_replace(
                src: str | os.PathLike[str],
                dst: str | os.PathLike[str],
            ) -> None:
                nonlocal failed_sidecar_commit, failed_artifact_restore
                src_path = Path(src)
                dst_path = Path(dst)
                if (
                    dst_path == sidecar_path
                    and src_path.name.startswith(".viewer.config.json.")
                    and not failed_sidecar_commit
                ):
                    failed_sidecar_commit = True
                    raise OSError("sidecar replace failed")
                if (
                    failed_sidecar_commit
                    and dst_path == artifact_path
                    and src_path.name.startswith(".viewer.parquet.")
                    and not failed_artifact_restore
                ):
                    failed_artifact_restore = True
                    raise OSError("artifact restore failed")
                real_replace(src, dst)

            with patch(
                "visground.viewer.export.os.replace", side_effect=failing_replace
            ):
                with self.assertRaisesRegex(OSError, "artifact restore failed"):
                    export_viewer_artifact(
                        candidates_df=make_candidates_df(),
                        viewer_config=make_viewer_config(),
                        output_path=artifact_path,
                        show_scores=False,
                    )

            artifact_backups = list(work_dir.glob(".viewer.parquet.*.tmp"))
            sidecar_backups = list(work_dir.glob(".viewer.config.json.*.tmp"))
            self.assertTrue(
                any(path.read_bytes() == b"old parquet" for path in artifact_backups)
            )
            self.assertTrue(
                any(path.read_text() == '{"old": true}\n' for path in sidecar_backups)
            )

    def test_viewer_dev_artifact_path_matches_shared_public_viewer_root(self) -> None:
        with patch.dict(os.environ, {"VISGROUND_VIEWER_DEV": "1"}, clear=False):
            path = default_viewer_dev_artifact_path()

        self.assertEqual(path.name, "viewer.parquet")
        self.assertEqual(path.parent.name, "data")
        self.assertEqual(path.parent.parent.name, "public")
        self.assertEqual(path.parent.parent.parent.name, "visground-web")
        self.assertEqual(path, default_viewer_dev_public_artifact_path())

    def test_viewer_dev_artifact_url_uses_runtime_url_for_custom_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            artifact_path = Path(tmp_dir) / "viewer.parquet"
            artifact_path.write_bytes(b"custom artifact")

            with patch.dict(
                os.environ,
                {
                    "VISGROUND_VIEWER_DEV": "1",
                    "VISGROUND_VIEWER_DEV_ARTIFACT_PATH": str(artifact_path),
                },
                clear=False,
            ):
                artifact_url = _resolve_viewer_artifact_url(artifact_path)

            self.assertTrue(artifact_url.startswith("data:application/octet-stream;base64,"))

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
