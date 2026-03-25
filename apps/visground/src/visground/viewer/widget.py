from __future__ import annotations

from pathlib import Path
from typing import Any, cast

import anywidget
import polars as pl
import traitlets
from anywidget.experimental import command

from visground.datasets import VisEvalDataset, VisGroundDataset

from .data import (
    GROUNDING_MODES,
    build_catalog,
    build_grounding_model_matrix,
    enrich_candidates_with_scores,
    normalize_selection,
    resolve_focus_key,
    serialize_candidate_record,
)
from .rendering import ChartImageService


class VisGroundViewer(anywidget.AnyWidget):
    _esm = Path(__file__).with_name("widget.js")
    _css = Path(__file__).with_name("widget.css")

    value = traitlets.Dict().tag(sync=True)

    def __init__(
        self,
        *,
        store: VisGroundDataset | None = None,
        dataset: VisEvalDataset | None = None,
        initial_vis_id: str | None = None,
        initial_objective: str = "refine",
        initial_grammar: str | None = None,
        initial_audience: str | None = None,
        show_scores: bool = True,
    ) -> None:
        self._store = store or VisGroundDataset()
        self._dataset = dataset or VisEvalDataset()
        self._show_scores = show_scores

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
        self._catalog_vis_ids = self._ordered_vis_ids()
        if not self._catalog_vis_ids:
            raise ValueError("Viewer requires at least one generated vis_id.")

        chosen_vis_id = initial_vis_id or self._catalog_vis_ids[0]
        if chosen_vis_id not in self._catalog_vis_ids:
            raise ValueError(f"Unknown initial_vis_id '{chosen_vis_id}'.")

        self._catalog = build_catalog(self._candidates_df, self._catalog_vis_ids)
        self._image_service = ChartImageService(self._store, self._dataset)
        self._case_cache: dict[str, pl.DataFrame] = {}
        self._overview_cache: dict[tuple[Any, ...], dict[str, Any]] = {}
        self._record_cache: dict[
            tuple[Any, ...],
            dict[tuple[str, str], dict[str, Any]],
        ] = {}

        super().__init__()

        selection = self._normalized_selection(
            chosen_vis_id,
            objective=initial_objective,
            grammar=initial_grammar,
            audience=initial_audience,
        )
        self.value = self._build_value(
            vis_id=chosen_vis_id,
            view_mode="overview",
            objective=selection["selection"]["objective"],
            grammar=selection["selection"]["grammar"],
            audience=selection["selection"]["audience"],
            focused_model=None,
            focused_grounding_mode=None,
        )

    @command
    def initialize(
        self,
        msg: object,
        buffers: list[bytes],
    ) -> tuple[dict[str, Any], list[bytes]]:
        del msg
        payload, value = self._build_view_payload(
            vis_id=str(self.value["vis_id"]),
            objective=self._as_optional_string(self.value.get("objective")),
            grammar=self._as_optional_string(self.value.get("grammar")),
            audience=self._as_optional_string(self.value.get("audience")),
            view_mode=str(self.value["view_mode"]),
            focused_model=self._as_optional_string(self.value.get("focused_model")),
            focused_grounding_mode=self._as_optional_string(
                self.value.get("focused_grounding_mode")
            ),
        )
        return (
            {
                "catalog": self._catalog,
                **payload,
                "value": value,
                "config": {
                    "grounding_modes": list(GROUNDING_MODES),
                    "scores_enabled": bool(
                        self._show_scores
                        and "overall_score" in self._candidates_df.columns
                    ),
                },
            },
            buffers,
        )

    @command
    def load_view(
        self,
        msg: object,
        buffers: list[bytes],
    ) -> tuple[dict[str, Any], list[bytes]]:
        payload = self._coerce_message_dict(msg)
        view_payload, value = self._build_view_payload(
            vis_id=str(payload.get("vis_id", self.value["vis_id"])),
            objective=self._as_optional_string(
                payload.get("objective", self.value.get("objective"))
            ),
            grammar=self._as_optional_string(
                payload.get("grammar", self.value.get("grammar"))
            ),
            audience=self._as_optional_string(
                payload.get("audience", self.value.get("audience"))
            ),
            view_mode=str(
                payload.get("view_mode", self.value.get("view_mode", "overview"))
            ),
            focused_model=self._as_optional_string(
                payload.get("focused_model", self.value.get("focused_model"))
            ),
            focused_grounding_mode=self._as_optional_string(
                payload.get(
                    "focused_grounding_mode",
                    self.value.get("focused_grounding_mode"),
                )
            ),
        )
        return ({**view_payload, "value": value}, buffers)

    def _build_view_payload(
        self,
        *,
        vis_id: str,
        objective: str | None,
        grammar: str | None,
        audience: str | None,
        view_mode: str,
        focused_model: str | None,
        focused_grounding_mode: str | None,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        if vis_id not in self._catalog_vis_ids:
            raise ValueError(f"Unknown vis_id '{vis_id}'.")

        overview = self._overview_payload(
            vis_id,
            objective=objective,
            grammar=grammar,
            audience=audience,
        )
        selection = overview["selection"]

        normalized_view_mode = "inspect" if view_mode == "inspect" else "overview"
        inspect = None
        normalized_model = None
        normalized_grounding_mode = None
        if normalized_view_mode == "inspect":
            inspect = self._inspect_payload(
                overview,
                focused_model=focused_model,
                focused_grounding_mode=focused_grounding_mode,
            )
            normalized_model = inspect["focused_model"]
            normalized_grounding_mode = inspect["focused_grounding_mode"]

        value = self._build_value(
            vis_id=vis_id,
            view_mode=normalized_view_mode,
            objective=selection["objective"],
            grammar=selection["grammar"],
            audience=selection["audience"],
            focused_model=normalized_model,
            focused_grounding_mode=normalized_grounding_mode,
        )
        return (
            {
                "overview": overview,
                "inspect": inspect,
            },
            value,
        )

    def _overview_payload(
        self,
        vis_id: str,
        *,
        objective: str | None,
        grammar: str | None,
        audience: str | None,
    ) -> dict[str, Any]:
        normalized = self._normalized_selection(
            vis_id,
            objective=objective,
            grammar=grammar,
            audience=audience,
        )
        selection = normalized["selection"]
        selection_key = self._selection_key(vis_id, selection)
        if selection_key in self._overview_cache:
            return self._overview_cache[selection_key]

        matrix = build_grounding_model_matrix(
            objective_grammar_df=normalized["objective_grammar_df"],
            selection_df=normalized["selection_df"],
            audience=selection["audience"],
        )
        record_map = matrix["record_map"]
        rows = []
        for row in matrix["rows"]:
            cells = []
            for cell in row["cells"]:
                record = cell["record"]
                cells.append(
                    {
                        "grounding_mode": cell["grounding_mode"],
                        "model": cell["model"],
                        "missing": record is None,
                        "placeholder_reason": cell["placeholder_reason"],
                        "candidate": (
                            None
                            if record is None
                            else serialize_candidate_record(
                                record,
                                image_loader=self._image_service.image_data_url,
                                image_variant="panel",
                                include_detail=False,
                            )
                        ),
                    }
                )
            rows.append({"grounding_mode": row["grounding_mode"], "cells": cells})

        payload = {
            "vis_id": vis_id,
            "page_index": self._catalog_vis_ids.index(vis_id),
            "page_count": len(self._catalog_vis_ids),
            "nl_query": normalized["objective_df"].item(0, "query"),
            "selection": selection,
            "options": normalized["options"],
            "models": matrix["models"],
            "rows": rows,
        }
        self._overview_cache[selection_key] = payload
        self._record_cache[selection_key] = record_map
        return payload

    def _inspect_payload(
        self,
        overview: dict[str, Any],
        *,
        focused_model: str | None,
        focused_grounding_mode: str | None,
    ) -> dict[str, Any]:
        selection_key = self._selection_key(overview["vis_id"], overview["selection"])
        record_map = self._record_cache[selection_key]

        focused_key = resolve_focus_key(
            record_map,
            focused_grounding_mode=focused_grounding_mode,
            focused_model=focused_model,
        )
        if focused_key is None:
            return {
                **overview,
                "focused_model": None,
                "focused_grounding_mode": None,
                "focused_candidate": None,
            }

        grounding_mode, model = focused_key
        focused_candidate = serialize_candidate_record(
            record_map[focused_key],
            image_loader=self._image_service.image_data_url,
            image_variant="detail",
            include_detail=True,
        )
        return {
            **overview,
            "focused_model": model,
            "focused_grounding_mode": grounding_mode,
            "focused_candidate": focused_candidate,
        }

    def _normalized_selection(
        self,
        vis_id: str,
        *,
        objective: str | None,
        grammar: str | None,
        audience: str | None,
    ) -> dict[str, Any]:
        return normalize_selection(
            self._case_df(vis_id),
            objective=objective,
            grammar=grammar,
            audience=audience,
        )

    def _ordered_vis_ids(self) -> list[str]:
        first_seen = (
            self._candidates_df.select("vis_id")
            .unique(maintain_order=True)
            .get_column("vis_id")
            .to_list()
        )
        if not self._store.cohort_path().exists():
            return first_seen

        cohort_ids = [
            cohort_id
            for cohort_id in self._store.read_cohort_df().get_column("id").to_list()
            if cohort_id in first_seen
        ]
        seen = set(cohort_ids)
        return [*cohort_ids, *(vis_id for vis_id in first_seen if vis_id not in seen)]

    def _case_df(self, vis_id: str) -> pl.DataFrame:
        if vis_id not in self._case_cache:
            self._case_cache[vis_id] = self._candidates_df.filter(
                pl.col("vis_id") == vis_id
            )
        return self._case_cache[vis_id]

    def _selection_key(
        self,
        vis_id: str,
        selection: dict[str, Any],
    ) -> tuple[Any, ...]:
        return (
            vis_id,
            selection["objective"],
            selection["grammar"],
            selection["audience"],
        )

    def _build_value(
        self,
        *,
        vis_id: str,
        view_mode: str,
        objective: str,
        grammar: str,
        audience: str | None,
        focused_model: str | None,
        focused_grounding_mode: str | None,
    ) -> dict[str, Any]:
        return {
            "vis_id": vis_id,
            "page_index": self._catalog_vis_ids.index(vis_id),
            "view_mode": view_mode,
            "objective": objective,
            "grammar": grammar,
            "audience": audience,
            "focused_model": focused_model,
            "focused_grounding_mode": focused_grounding_mode,
        }

    def _coerce_message_dict(self, msg: object) -> dict[str, Any]:
        if not isinstance(msg, dict):
            raise ValueError(f"Expected dict message, got {type(msg).__name__}.")
        return cast(dict[str, Any], msg)

    @staticmethod
    def _as_optional_string(value: object) -> str | None:
        if value is None:
            return None
        return str(value)
