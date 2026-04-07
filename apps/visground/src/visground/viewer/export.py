from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import platformdirs
import polars as pl

from visground.datasets import VisGroundDataset

from .data import (
    enrich_candidates_with_judge_runs,
    enrich_candidates_with_scores,
    serialize_candidate_record,
)
from .defaults import build_default_viewer_config
from .spec import ViewerConfig

_TRUTHY_ENV_VALUES = {"1", "true", "yes", "on"}


def _viewer_dev_enabled() -> bool:
    return os.getenv("VISGROUND_VIEWER_DEV", "").strip().lower() in _TRUTHY_ENV_VALUES


def default_viewer_dev_artifact_path() -> Path:
    override = os.getenv("VISGROUND_VIEWER_DEV_ARTIFACT_PATH")
    if override:
        return Path(override).expanduser()

    return (
        Path(__file__).resolve().parents[5]
        / "apps"
        / "visground"
        / "public"
        / "data"
        / "viewer.parquet"
    )


def default_viewer_runtime_artifact_path() -> Path:
    override = os.getenv("VISGROUND_VIEWER_ARTIFACT_PATH")
    if override:
        return Path(override).expanduser()

    return Path(platformdirs.user_cache_dir("visground")) / "viewer" / "viewer.parquet"


def default_viewer_artifact_path() -> Path:
    if _viewer_dev_enabled():
        return default_viewer_dev_artifact_path()
    return default_viewer_runtime_artifact_path()


def build_viewer_artifact_df(
    *,
    candidates_df: pl.DataFrame,
    viewer_config: ViewerConfig,
    judgements_df: pl.DataFrame | None = None,
    judgement_runs_df: pl.DataFrame | None = None,
    show_scores: bool = True,
) -> pl.DataFrame:
    enriched_df = candidates_df
    if show_scores and judgements_df is not None:
        enriched_df = enrich_candidates_with_scores(enriched_df, judgements_df)
    if judgement_runs_df is not None:
        enriched_df = enrich_candidates_with_judge_runs(enriched_df, judgement_runs_df)

    rows: list[dict[str, Any]] = []
    for record in enriched_df.to_dicts():
        vis_id = str(record.get("vis_id") or "")
        query = str(record.get("query") or "")
        candidate = serialize_candidate_record(record, config=viewer_config)
        rows.append(
            {
                "visgen_id": str(record.get("visgen_id") or ""),
                "vis_id": vis_id,
                "query": query,
                "search_text": " ".join(
                    value for value in [vis_id, query] if value
                ).strip(),
                "objective": record.get("objective"),
                "request_chart": record.get("request_chart"),
                "audience": record.get("audience"),
                "grammar": record.get("grammar"),
                "grounding_mode": record.get("grounding_mode"),
                "model": record.get("model"),
                "overall_score": record.get("overall_score"),
                "candidate_json": json.dumps(candidate),
            }
        )

    return pl.DataFrame(rows)


def export_viewer_artifact(
    *,
    candidates_df: pl.DataFrame,
    viewer_config: ViewerConfig,
    judgements_df: pl.DataFrame | None = None,
    judgement_runs_df: pl.DataFrame | None = None,
    output_path: str | Path | None = None,
    show_scores: bool = True,
) -> Path:
    path = (
        Path(output_path) if output_path is not None else default_viewer_artifact_path()
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    artifact_df = build_viewer_artifact_df(
        candidates_df=candidates_df,
        viewer_config=viewer_config,
        judgements_df=judgements_df,
        judgement_runs_df=judgement_runs_df,
        show_scores=show_scores,
    )
    artifact_df.write_parquet(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(default_viewer_artifact_path()))
    args = parser.parse_args()

    store = VisGroundDataset()
    export_viewer_artifact(
        candidates_df=store.read_generated_candidates_df(),
        judgements_df=store.read_judgements_df()
        if store.judgements_path().exists()
        else None,
        judgement_runs_df=store.read_judgement_runs_df()
        if store.judgement_runs_path().exists()
        else None,
        viewer_config=build_default_viewer_config(),
        output_path=args.output,
    )
    print(Path(args.output).resolve())


if __name__ == "__main__":
    main()
