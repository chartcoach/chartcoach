from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import anywidget
import polars as pl
import traitlets
from anywidget.experimental import command

from visground.datasets import VisEvalDataset, VisGroundDataset

from .data import (
    build_catalog,
    build_overview_matrix,
    build_ui_schema,
    default_selection_from_registry,
    discover_registry,
    enrich_candidates_with_scores,
    normalize_selection,
)
from .rendering import ChartImageService


class VisGroundViewerBackend(anywidget.AnyWidget):
    _esm = ""
    _css = ""

    _selection = traitlets.Dict({}).tag(sync=True)
    _state = traitlets.Dict({}).tag(sync=True)

    def __init__(
        self,
        *,
        store: VisGroundDataset | None = None,
        dataset: VisEvalDataset | None = None,
        initial_vis_id: str | None = None,
        initial_objective: str | None = None,
        initial_audience: str | None = None,
        initial_overview_variant: str | None = None,
        show_scores: bool = True,
    ) -> None:
        self._store = store or VisGroundDataset()
        self._dataset = dataset or VisEvalDataset()

        candidates_df = self._store.read_generated_candidates_df()
        if candidates_df.is_empty():
            raise ValueError(
                "No generated candidates found. Run workbench `03_generating.py` first."
            )
        if show_scores and self._store.judgements_path().exists():
            candidates_df = enrich_candidates_with_scores(
                candidates_df,
                self._store.read_judgements_df(),
            )

        self._candidates_df = candidates_df
        self._registry = discover_registry(candidates_df)
        self._catalog_vis_ids = self._ordered_vis_ids()
        if not self._catalog_vis_ids:
            raise ValueError("Viewer requires at least one generated vis_id.")

        self._catalog = build_catalog(
            self._candidates_df,
            self._catalog_vis_ids,
            request_chart_by_vis_id=self._case_request_chart_lookup(),
        )
        self._request_chart_options = [
            None,
            *list(
                dict.fromkeys(
                    entry["request_chart"]
                    for entry in self._catalog
                    if entry["request_chart"] is not None
                )
            ),
        ]
        self._image_service = ChartImageService(self._store, self._dataset)
        self._case_cache: dict[str, pl.DataFrame] = {}
        self._view_cache: dict[tuple[Any, ...], dict[str, Any]] = {}
        self._records_by_visgen_id = {
            str(record["visgen_id"]): dict(record)
            for record in self._candidates_df.iter_rows(named=True)
        }
        self._syncing_selection = False

        super().__init__()

        defaults = default_selection_from_registry(self._registry)
        chosen_vis_id = initial_vis_id or self._catalog_vis_ids[0]
        if chosen_vis_id not in self._catalog_vis_ids:
            raise ValueError(f"Unknown initial_vis_id '{chosen_vis_id}'.")
        self._apply_selection(
            {
                "vis_id": chosen_vis_id,
                "request_chart": defaults["request_chart"],
                "objective": initial_objective or defaults["objective"],
                "overview_variant": initial_overview_variant
                or defaults["overview_variant"],
                "dimension_filters": {
                    "audience": initial_audience,
                },
            }
        )

    @traitlets.observe("_selection")
    def _on_selection_change(self, change: traitlets.Bunch) -> None:
        if self._syncing_selection:
            return
        self._apply_selection(change["new"])

    @command
    def load_assets(
        self,
        msg: object,
        buffers: list[bytes],
    ) -> tuple[dict[str, Any], list[bytes]]:
        try:
            payload = self._coerce_message_dict(msg)
            requests = payload.get("requests")
            if not isinstance(requests, list):
                raise ValueError(
                    "Asset request payload must include a list of requests."
                )

            assets = []
            for request in requests:
                if not isinstance(request, Mapping):
                    continue
                visgen_id = str(request.get("visgen_id", ""))
                variant = str(request.get("variant", ""))
                record = self._records_by_visgen_id.get(visgen_id)
                if record is None:
                    assets.append(
                        {
                            "visgen_id": visgen_id,
                            "variant": variant,
                            "image_url": None,
                            "image_meta": None,
                            "error": f"Unknown candidate '{visgen_id}'.",
                        }
                    )
                    continue
                try:
                    assets.append(
                        {
                            "visgen_id": visgen_id,
                            "variant": variant,
                            "image_url": self._image_service.image_data_url(
                                record, variant
                            ),
                            "image_meta": self._image_service.image_metadata(record),
                            "error": None,
                        }
                    )
                except Exception as exc:
                    assets.append(
                        {
                            "visgen_id": visgen_id,
                            "variant": variant,
                            "image_url": None,
                            "image_meta": None,
                            "error": str(exc),
                        }
                    )
            return (
                {
                    "ok": True,
                    "payload": {
                        "assets": assets,
                    },
                },
                buffers,
            )
        except Exception as exc:
            return (
                {
                    "ok": False,
                    "error": {
                        "message": str(exc),
                        "where": "load_assets",
                    },
                },
                buffers,
            )

    def _apply_selection(self, requested: Mapping[str, Any]) -> None:
        try:
            requested_request_chart = self._as_optional_string(
                requested.get("request_chart")
            )
            if requested_request_chart not in self._request_chart_options:
                requested_request_chart = None
            requested_vis_id = (
                self._as_optional_string(requested.get("vis_id"))
                or self._catalog_vis_ids[0]
            )
            vis_id = self._resolve_vis_id_for_request_chart(
                requested_vis_id,
                requested_request_chart,
            )
            case_df = self._case_df(vis_id)
            normalized = normalize_selection(
                case_df,
                registry=self._registry,
                request_chart=requested_request_chart,
                objective=self._as_optional_string(requested.get("objective")),
                overview_variant=self._as_optional_string(
                    requested.get("overview_variant")
                ),
                dimension_filters=self._coerce_dimension_filters(
                    requested.get("dimension_filters")
                ),
                request_chart_options=self._request_chart_options,
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
            "request_chart": selection["request_chart"],
            "objective": selection["objective"],
            "overview_variant": selection["overview_variant"],
            "dimension_filters": dict(selection["dimension_filters"]),
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
            selection["request_chart"],
            selection["objective"],
            selection["overview_variant"],
            selection["dimension_filters"].get("audience"),
        )
        if cache_key in self._view_cache:
            return self._view_cache[cache_key]

        objective_df = normalized["objective_df"]
        scoped_df = normalized["scoped_df"]
        variant = normalized["variant"]
        overview = {
            "nl_query": str(objective_df.item(0, "query")),
            "ui_schema": build_ui_schema(
                registry=self._registry,
                selection=selection,
                valid_variants=normalized["valid_variants"],
                request_chart_options=self._request_chart_options,
                variant=variant,
                audience_options=tuple(
                    objective_df.select(pl.col("audience"))
                    .unique(maintain_order=True)
                    .get_column("audience")
                    .to_list()
                ),
            ),
            "matrix": build_overview_matrix(
                objective_df=objective_df,
                scoped_df=scoped_df,
                variant=variant,
                image_loader=lambda record: self._image_service.image_data_url(
                    record, "panel"
                ),
                image_metadata_loader=self._image_service.image_metadata,
            ),
        }
        self._view_cache[cache_key] = overview
        return overview

    def _ordered_vis_ids(self) -> list[str]:
        first_seen = self._registry["vis_ids"]
        if not self._store.cohort_path().exists():
            return list(first_seen)

        cohort_ids = [
            cohort_id
            for cohort_id in self._store.read_cohort_df().get_column("id").to_list()
            if cohort_id in first_seen
        ]
        seen = set(cohort_ids)
        return [*cohort_ids, *(vis_id for vis_id in first_seen if vis_id not in seen)]

    def _case_request_chart_lookup(self) -> dict[str, str | None]:
        if self._store.cohort_path().exists():
            cohort_df = self._store.read_cohort_df().select("id", "chart")
            return {
                row["id"]: row["chart"]
                for row in cohort_df.iter_rows(named=True)
                if row["id"] in self._catalog_vis_ids
            }
        return {
            vis_id: self._candidates_df.filter(pl.col("vis_id") == vis_id)
            .get_column("request_chart")
            .drop_nulls()
            .head(1)
            .to_list()[0]
            if self._candidates_df.filter(pl.col("vis_id") == vis_id)
            .get_column("request_chart")
            .drop_nulls()
            .len()
            > 0
            else None
            for vis_id in self._catalog_vis_ids
        }

    def _resolve_vis_id_for_request_chart(
        self,
        vis_id: str,
        request_chart: str | None,
    ) -> str:
        if request_chart is None:
            filtered_vis_ids = list(self._catalog_vis_ids)
        else:
            filtered_vis_ids = [
                entry["vis_id"]
                for entry in self._catalog
                if entry["request_chart"] == request_chart
            ]
        if vis_id in filtered_vis_ids:
            return vis_id
        if filtered_vis_ids:
            return filtered_vis_ids[0]
        return vis_id

    def _case_df(self, vis_id: str) -> pl.DataFrame:
        if vis_id not in self._case_cache:
            self._case_cache[vis_id] = self._candidates_df.filter(
                pl.col("vis_id") == vis_id
            )
        return self._case_cache[vis_id]

    @staticmethod
    def _coerce_message_dict(msg: object) -> dict[str, Any]:
        if msg is None:
            return {}
        if isinstance(msg, Mapping):
            return {str(key): value for key, value in msg.items()}
        raise TypeError("Viewer command payload must be a mapping.")

    @staticmethod
    def _coerce_dimension_filters(value: object) -> dict[str, Any]:
        if value is None:
            return {}
        if isinstance(value, Mapping):
            return {str(key): item for key, item in value.items()}
        raise TypeError("Viewer dimension filters must be a mapping.")

    @staticmethod
    def _as_optional_string(value: object) -> str | None:
        if value is None:
            return None
        if isinstance(value, str):
            return value
        return str(value)
