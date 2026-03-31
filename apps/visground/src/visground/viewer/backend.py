from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import anywidget
import polars as pl
import traitlets

from .data import (
    build_catalog,
    build_overview_matrix,
    build_ui_schema,
    default_selection_from_registry,
    discover_registry,
    enrich_candidates_with_judge_runs,
    enrich_candidates_with_scores,
    normalize_selection,
)
from .spec import ViewerConfig, resolved_case_label_field


class VisGroundViewerBackend(anywidget.AnyWidget):
    _esm = ""
    _css = ""

    debug = traitlets.Bool(False).tag(sync=True)
    _selection = traitlets.Dict({}).tag(sync=True)
    _state = traitlets.Dict({}).tag(sync=True)

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

        if show_scores and judgements_df is not None:
            candidates_df = enrich_candidates_with_scores(candidates_df, judgements_df)
        if judgement_runs_df is not None:
            candidates_df = enrich_candidates_with_judge_runs(
                candidates_df, judgement_runs_df
            )

        self._candidates_df = candidates_df
        self._config = viewer_config
        self._registry = discover_registry(candidates_df, config=viewer_config)
        self._catalog_vis_ids = list(self._registry["vis_ids"])
        if not self._catalog_vis_ids:
            raise ValueError("Viewer requires at least one case id.")

        self._catalog = build_catalog(
            self._candidates_df,
            self._catalog_vis_ids,
            config=self._config,
        )
        self._case_cache: dict[str, pl.DataFrame] = {}
        self._view_cache: dict[tuple[Any, ...], dict[str, Any]] = {}
        self._syncing_selection = False

        super().__init__()
        self.debug = debug

        defaults = default_selection_from_registry(self._registry, config=self._config)
        chosen_vis_id = initial_vis_id or self._catalog_vis_ids[0]
        if chosen_vis_id not in self._catalog_vis_ids:
            raise ValueError(f"Unknown initial_vis_id '{chosen_vis_id}'.")

        self._apply_selection(
            {
                "vis_id": chosen_vis_id,
                "filters": dict(initial_filters or defaults["filters"]),
                "layout": dict(initial_layout or defaults["layout"]),
            }
        )

    @traitlets.observe("_selection")
    def _on_selection_change(self, change: traitlets.Bunch) -> None:
        if self._syncing_selection:
            return
        self._apply_selection(change["new"])

    def _apply_selection(self, requested: Mapping[str, Any]) -> None:
        try:
            vis_id = self._resolve_vis_id(requested.get("vis_id"))
            case_df = self._case_df(vis_id)
            normalized = normalize_selection(
                case_df,
                registry=self._registry,
                config=self._config,
                filters=self._coerce_filters(requested.get("filters")),
                layout=self._coerce_layout(requested.get("layout")),
            )
            selection = normalized["selection"]
            overview = self._build_overview(
                case_df,
                selection=selection,
                normalized=normalized,
            )
            self._set_synced_view(
                selection=selection,
                overview=overview,
                error=None,
            )
        except Exception as exc:
            self._state = {
                "catalog": self._catalog,
                "overview": None,
                "error": str(exc),
            }

    def _set_synced_view(
        self,
        *,
        selection: Mapping[str, Any],
        overview: Mapping[str, Any],
        error: str | None,
    ) -> None:
        next_value = {
            "vis_id": selection["vis_id"],
            "filters": dict(selection["filters"]),
            "layout": dict(selection["layout"]),
        }

        self._syncing_selection = True
        try:
            if self._selection != next_value:
                self._selection = next_value
            self._state = {
                "catalog": self._catalog,
                "overview": dict(overview),
                "error": error,
            }
        finally:
            self._syncing_selection = False

    def _build_overview(
        self,
        case_df: pl.DataFrame,
        *,
        selection: Mapping[str, Any],
        normalized: Mapping[str, Any],
    ) -> dict[str, Any]:
        cache_key = (
            selection["vis_id"],
            tuple(sorted(selection["filters"].items())),
            selection["layout"]["row_dimension"],
            selection["layout"]["column_dimension"],
            selection["layout"]["group_dimension"],
        )
        if cache_key in self._view_cache:
            return self._view_cache[cache_key]

        scoped_df = normalized["scoped_df"]
        label_source_df = scoped_df if not scoped_df.is_empty() else case_df
        label = str(label_source_df.item(0, resolved_case_label_field(self._config)))
        overview = {
            "label": label,
            "ui_schema": build_ui_schema(
                selection=selection,
                axis_dimensions=normalized["axis_dimensions"],
                filter_controls=normalized["filter_controls"],
                layout_controls=normalized["layout_controls"],
                config=self._config,
            ),
            "matrix": build_overview_matrix(
                scoped_df=scoped_df,
                layout=selection["layout"],
                config=self._config,
            ),
        }
        self._view_cache[cache_key] = overview
        return overview

    def _resolve_vis_id(self, value: object) -> str:
        vis_id = self._as_optional_string(value) or self._catalog_vis_ids[0]
        if vis_id in self._catalog_vis_ids:
            return vis_id
        return self._catalog_vis_ids[0]

    def _case_df(self, vis_id: str) -> pl.DataFrame:
        if vis_id not in self._case_cache:
            self._case_cache[vis_id] = self._candidates_df.filter(
                pl.col(self._config.case_id_field) == vis_id
            )
        return self._case_cache[vis_id]

    @staticmethod
    def _coerce_filters(value: object) -> dict[str, Any]:
        if value is None:
            return {}
        if isinstance(value, Mapping):
            return {str(key): item for key, item in value.items()}
        raise TypeError("Viewer filters must be a mapping.")

    @staticmethod
    def _coerce_layout(value: object) -> dict[str, Any]:
        if value is None:
            return {}
        if isinstance(value, Mapping):
            return {str(key): item for key, item in value.items()}
        raise TypeError("Viewer layout must be a mapping.")

    @staticmethod
    def _as_optional_string(value: object) -> str | None:
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return str(value)
