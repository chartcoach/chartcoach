from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import anywidget
import polars as pl
import traitlets

from .data import default_selection_from_registry, discover_registry
from .runtime_config import (
    ViewerRuntimeConfig,
    serialize_viewer_runtime_config,
    viewer_runtime_config_sidecar_path,
)
from .spec import ViewerConfig


class VisGroundViewerBackend(anywidget.AnyWidget):
    _esm = ""
    _css = ""
    _artifact_path: Path | None = None
    _viewer_config_path: Path | None = None

    debug = traitlets.Bool(False).tag(sync=True)
    _artifact_url = traitlets.Unicode("").tag(sync=True)
    _selection = traitlets.Dict({}).tag(sync=True)
    _viewer_config = traitlets.Dict({}).tag(sync=True)

    def __init__(
        self,
        *,
        candidates_df: pl.DataFrame,
        viewer_config: ViewerConfig,
        judgements_df: pl.DataFrame | None = None,
        judgement_runs_df: pl.DataFrame | None = None,
        initial_vis_id: str | None = None,
        initial_filters: Mapping[str, Any] | None = None,
        initial_layout: Mapping[str, Any] | None = None,
        debug: bool = False,
        show_scores: bool = True,
    ) -> None:
        if candidates_df.is_empty():
            raise ValueError("Viewer requires at least one candidate row.")

        registry = discover_registry(candidates_df, config=viewer_config)
        catalog_vis_ids = list(registry["vis_ids"])
        if not catalog_vis_ids:
            raise ValueError("Viewer requires at least one case id.")
        runtime_config: ViewerRuntimeConfig = serialize_viewer_runtime_config(
            viewer_config
        )

        from .export import export_viewer_artifact

        self._artifact_path = export_viewer_artifact(
            candidates_df=candidates_df,
            judgements_df=judgements_df,
            judgement_runs_df=judgement_runs_df,
            viewer_config=viewer_config,
            show_scores=show_scores,
        )
        self._viewer_config_path = viewer_runtime_config_sidecar_path(
            self._artifact_path
        )

        defaults = default_selection_from_registry(registry, config=viewer_config)
        chosen_vis_id = initial_vis_id or catalog_vis_ids[0]
        if chosen_vis_id not in catalog_vis_ids:
            chosen_vis_id = catalog_vis_ids[0]

        super().__init__()
        self.debug = debug
        self.set_trait("_viewer_config", runtime_config)
        self._selection = {
            "vis_id": chosen_vis_id,
            "filters": dict(initial_filters or defaults["filters"]),
            "layout": dict(initial_layout or defaults["layout"]),
        }
