from __future__ import annotations

from collections.abc import Mapping
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

import polars as pl

from .backend import VisGroundViewerBackend
from .spec import ViewerConfig

DEFAULT_VIEWER_DEV_URL = "http://127.0.0.1:5173/js/anywidget.ts?anywidget"
_TRUTHY_ENV_VALUES = {"1", "true", "yes", "on"}


def _viewer_dev_enabled() -> bool:
    return os.getenv("VISGROUND_VIEWER_DEV", "").strip().lower() in _TRUTHY_ENV_VALUES


def _normalize_viewer_dev_url(value: str) -> str:
    candidate = value.strip()
    parts = urlsplit(candidate)
    if not parts.scheme or not parts.netloc:
        return candidate
    if parts.query == "anywidget":
        return candidate
    return urlunsplit(parts._replace(query="anywidget"))


def _resolve_viewer_esm() -> str | Path:
    dev_url = os.getenv("VISGROUND_VIEWER_DEV_URL")
    if dev_url:
        return _normalize_viewer_dev_url(dev_url)
    if _viewer_dev_enabled():
        return DEFAULT_VIEWER_DEV_URL
    return Path(__file__).parent / "_static" / "anywidget" / "index.js"


class VisGroundViewer(VisGroundViewerBackend):
    _esm = ""
    _css = ""

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
        from anywidget._util import try_file_contents

        resolved_esm = _resolve_viewer_esm()
        self._esm = try_file_contents(resolved_esm) or resolved_esm
        super().__init__(
            candidates_df=candidates_df,
            viewer_config=viewer_config,
            judgements_df=judgements_df,
            judgement_runs_df=judgement_runs_df,
            initial_vis_id=initial_vis_id,
            initial_filters=initial_filters,
            initial_layout=initial_layout,
            debug=debug,
            show_scores=show_scores,
        )


__all__ = ["VisGroundViewer"]
