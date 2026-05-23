from __future__ import annotations

import argparse
import dataclasses as dc
import json
import os
import tempfile
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
from .runtime_config import (
    ViewerRuntimeConfig,
    serialize_viewer_runtime_config,
    viewer_runtime_config_sidecar_path,
)
from .spec import ViewerConfig

_TRUTHY_ENV_VALUES = {"1", "true", "yes", "on"}


@dc.dataclass(frozen=True, slots=True)
class ViewerArtifact:
    artifact_path: Path
    runtime_config_path: Path
    runtime_config: ViewerRuntimeConfig


def _viewer_dev_enabled() -> bool:
    return os.getenv("VISGROUND_VIEWER_DEV", "").strip().lower() in _TRUTHY_ENV_VALUES


def default_viewer_dev_artifact_path() -> Path:
    override = os.getenv("VISGROUND_VIEWER_DEV_ARTIFACT_PATH")
    if override:
        return Path(override).expanduser()

    return default_viewer_dev_public_artifact_path()


def default_viewer_dev_public_artifact_path() -> Path:
    return (
        Path(__file__).resolve().parents[5]
        / "apps"
        / "visground-web"
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
    _validate_viewer_artifact_source_columns(enriched_df, viewer_config)

    rows: list[dict[str, Any]] = []
    for record in enriched_df.to_dicts():
        vis_id = str(record.get(viewer_config.case_id_field) or "")
        query = str(record.get("query") or "")
        candidate = serialize_candidate_record(record, config=viewer_config)
        row = {
            "visgen_id": str(record.get("visgen_id") or ""),
            "vis_id": vis_id,
            "query": query,
            "search_text": " ".join(value for value in [vis_id, query] if value).strip(),
            "overall_score": record.get("overall_score"),
            "candidate_json": json.dumps(candidate),
        }
        for dimension in viewer_config.dimensions:
            row[dimension.id] = record.get(dimension.id)
        rows.append(row)

    return pl.DataFrame(rows)


def _validate_viewer_artifact_source_columns(
    candidates_df: pl.DataFrame,
    viewer_config: ViewerConfig,
) -> None:
    required = {
        "visgen_id",
        viewer_config.case_id_field,
        *(dimension.id for dimension in viewer_config.dimensions),
    }
    missing = sorted(required - set(candidates_df.columns))
    if missing:
        raise ValueError(
            "Viewer artifact source data is missing required columns: "
            + ", ".join(missing)
            + "."
        )


def export_viewer_artifact(
    *,
    candidates_df: pl.DataFrame,
    viewer_config: ViewerConfig,
    judgements_df: pl.DataFrame | None = None,
    judgement_runs_df: pl.DataFrame | None = None,
    output_path: str | Path | None = None,
    show_scores: bool = True,
) -> ViewerArtifact:
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
    runtime_config = serialize_viewer_runtime_config(viewer_config)
    runtime_config_path = viewer_runtime_config_sidecar_path(path)
    _replace_artifact_pair(
        artifact_df=artifact_df,
        artifact_path=path,
        runtime_config_path=runtime_config_path,
        runtime_config=runtime_config,
    )
    return ViewerArtifact(
        artifact_path=path,
        runtime_config_path=runtime_config_path,
        runtime_config=runtime_config,
    )


def _temporary_sibling(path: Path) -> Path:
    fd, name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    os.close(fd)
    return Path(name)


def _replace_artifact_pair(
    *,
    artifact_df: pl.DataFrame,
    artifact_path: Path,
    runtime_config_path: Path,
    runtime_config: ViewerRuntimeConfig,
) -> None:
    artifact_tmp = _temporary_sibling(artifact_path)
    runtime_config_tmp = _temporary_sibling(runtime_config_path)
    artifact_backup = _temporary_sibling(artifact_path)
    runtime_config_backup = _temporary_sibling(runtime_config_path)
    artifact_had_previous = artifact_path.exists()
    runtime_config_had_previous = runtime_config_path.exists()
    artifact_backup_created = False
    runtime_config_backup_created = False
    artifact_committed = False
    runtime_config_committed = False
    transaction_succeeded = False

    try:
        artifact_df.write_parquet(artifact_tmp)
        runtime_config_tmp.write_text(
            json.dumps(runtime_config, indent=2, sort_keys=True) + "\n"
        )
        if artifact_had_previous:
            os.replace(artifact_path, artifact_backup)
            artifact_backup_created = True
        else:
            artifact_backup.unlink(missing_ok=True)
        if runtime_config_had_previous:
            os.replace(runtime_config_path, runtime_config_backup)
            runtime_config_backup_created = True
        else:
            runtime_config_backup.unlink(missing_ok=True)
        os.replace(artifact_tmp, artifact_path)
        artifact_committed = True
        os.replace(runtime_config_tmp, runtime_config_path)
        runtime_config_committed = True
        transaction_succeeded = True
    except Exception:
        if artifact_committed or artifact_backup_created:
            artifact_path.unlink(missing_ok=True)
        if runtime_config_committed or runtime_config_backup_created:
            runtime_config_path.unlink(missing_ok=True)
        if artifact_backup_created:
            os.replace(artifact_backup, artifact_path)
        if runtime_config_backup_created:
            os.replace(runtime_config_backup, runtime_config_path)
        raise
    finally:
        artifact_tmp.unlink(missing_ok=True)
        runtime_config_tmp.unlink(missing_ok=True)
        if transaction_succeeded or not artifact_backup_created:
            artifact_backup.unlink(missing_ok=True)
        if transaction_succeeded or not runtime_config_backup_created:
            runtime_config_backup.unlink(missing_ok=True)


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
