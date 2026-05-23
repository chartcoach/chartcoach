from __future__ import annotations

import base64
from collections.abc import Mapping
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

import polars as pl

from .backend import VisGroundViewerBackend
from .spec import ViewerConfig

DEFAULT_VIEWER_DEV_URL = "http://127.0.0.1:5173/js/anywidget.ts?anywidget"
DEFAULT_VIEWER_ARTIFACT_DEV_URL = "http://127.0.0.1:5173/data/viewer.parquet"
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


def _resolve_viewer_esm_asset() -> Any:
    from anywidget._util import try_file_contents

    resolved_esm = _resolve_viewer_esm()
    file_contents = try_file_contents(resolved_esm)
    if file_contents is not None:
        return file_contents
    return str(resolved_esm)


def _resolve_viewer_artifact_url(path: Path) -> str:
    dev_url = os.getenv("VISGROUND_VIEWER_DEV_URL")
    if dev_url or _viewer_dev_enabled():
        from .export import viewer_dev_public_artifact_path

        public_artifact_path = viewer_dev_public_artifact_path()
        if (
            public_artifact_path is None
            or path.resolve() != public_artifact_path.resolve()
        ):
            return _resolve_runtime_artifact_url(path)
        candidate = _normalize_viewer_dev_url(dev_url or DEFAULT_VIEWER_DEV_URL)
        parts = urlsplit(candidate)
        if parts.scheme and parts.netloc:
            return urlunsplit(parts._replace(path="/data/viewer.parquet", query=""))
        return DEFAULT_VIEWER_ARTIFACT_DEV_URL
    return _resolve_runtime_artifact_url(path)


def _resolve_runtime_artifact_url(path: Path) -> str:
    if url := _resolve_marimo_virtual_file_url(path):
        return url
    return _resolve_data_url(path)


def _resolve_marimo_virtual_file_url(path: Path) -> str:
    if not path.is_file():
        return ""

    try:
        from marimo._output.data import data as mo_data
        from marimo._runtime.context import ContextNotInitializedError, get_context
    except Exception:
        return ""

    try:
        context = get_context()
    except ContextNotInitializedError:
        return ""

    if not context.virtual_files_supported:
        return ""

    return str(mo_data.any_data(path.read_bytes(), ext=path.suffix).url)


def _resolve_data_url(path: Path) -> str:
    if not path.is_file():
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:application/octet-stream;base64,{encoded}"


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
        self._esm = _resolve_viewer_esm_asset()
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
        artifact_path = self._artifact_path
        if artifact_path is None:
            raise RuntimeError("VisGround viewer did not prepare a viewer artifact.")
        artifact_url = _resolve_viewer_artifact_url(artifact_path)
        if not artifact_url:
            raise RuntimeError(
                f"VisGround viewer could not resolve a viewer artifact location for {artifact_path}."
            )
        self._artifact_url = artifact_url


__all__ = ["VisGroundViewer"]
