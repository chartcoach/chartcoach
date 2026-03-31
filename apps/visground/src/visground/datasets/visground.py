from __future__ import annotations

import os
import tempfile
from os import PathLike
from pathlib import Path
from typing import Final

import polars as pl
from PIL import Image

from .paths import VISGROUND_DATA_ROOT

_GENERATED_CANDIDATE_COLUMNS: Final[tuple[str, ...]] = (
    "visgen_id",
    "grounding_id",
    "grounding_mode",
    "objective",
    "vis_id",
    "query",
    "request_chart",
    "audience",
    "guideline_ids",
    "model",
    "grammar",
    "code",
    "visualization_type",
    "grounding_trace",
)

_GENERATED_ATTEMPT_COLUMNS: Final[tuple[str, ...]] = (
    *_GENERATED_CANDIDATE_COLUMNS,
    "generation_error",
)


def flatten_generated_attempts_df(
    generated_df: pl.DataFrame,
    grounding_df: pl.DataFrame,
) -> pl.DataFrame:
    """Normalize scenario-batched generation output into one row per attempt."""
    if generated_df.is_empty():
        return pl.DataFrame(
            schema=[
                ("visgen_id", pl.String),
                ("grounding_id", pl.String),
                ("grounding_mode", pl.String),
                ("objective", pl.String),
                ("vis_id", pl.String),
                ("query", pl.String),
                ("request_chart", pl.String),
                ("audience", pl.String),
                ("guideline_ids", pl.List(pl.String)),
                ("model", pl.String),
                ("grammar", pl.String),
                ("code", pl.String),
                ("visualization_type", pl.String),
                ("grounding_trace", pl.Struct({})),
                ("generation_error", pl.String),
            ]
        )

    attempts_df = (
        generated_df.unnest("run")
        .explode("scenario", "outputs")
        .unnest("scenario")
        .unnest("input")
        .drop("id")
        .unnest("outputs")
        .join(
            grounding_df.select(
                "grounding_id",
                "grounding_mode",
                objective=pl.when(
                    pl.col("request").struct.field("objective").is_not_null()
                )
                .then(pl.col("request").struct.field("objective"))
                .when(pl.col("grounding_id").str.contains("-refine-"))
                .then(pl.lit("refine"))
                .when(pl.col("grounding_id").str.contains("-select-"))
                .then(pl.lit("select"))
                .otherwise(pl.lit(None).cast(pl.String)),
                request_chart=pl.col("request").struct.field("chart"),
                audience=pl.col("request").struct.field("audience"),
                guideline_ids=pl.col("result").struct.field("guideline_ids"),
            ),
            on="grounding_id",
            how="left",
        )
    )

    if "generation_error" not in attempts_df.columns:
        attempts_df = attempts_df.with_columns(
            pl.lit(None).cast(pl.String).alias("generation_error")
        )

    return attempts_df.select(
        "visgen_id",
        "grounding_id",
        "grounding_mode",
        "objective",
        pl.col("id").alias("vis_id"),
        "query",
        "request_chart",
        "audience",
        "guideline_ids",
        "model",
        "grammar",
        "code",
        "visualization_type",
        "grounding_trace",
        "generation_error",
    ).select(*_GENERATED_ATTEMPT_COLUMNS)


def flatten_generated_candidates_df(
    generated_df: pl.DataFrame,
    grounding_df: pl.DataFrame,
) -> pl.DataFrame:
    """Normalize scenario-batched generation output into one row per candidate."""
    return (
        flatten_generated_attempts_df(generated_df, grounding_df)
        .filter(pl.col("generation_error").is_null())
        .select(*_GENERATED_CANDIDATE_COLUMNS)
    )


class VisGroundDataset:
    """Typed read/write API for workbench artifacts."""

    def __init__(self, root: str | PathLike[str] | None = None) -> None:
        self._root = (
            Path(root) if root is not None else VISGROUND_DATA_ROOT / "artifacts"
        )

    def cohort_path(self) -> Path:
        return self._root / "01_cohort.parquet"

    def grounding_path(self) -> Path:
        return self._root / "02_grounding.parquet"

    def generate_path(self) -> Path:
        return self._root / "03_generate.parquet"

    def judgements_path(self) -> Path:
        return self._root / "04_judgements.parquet"

    def judgement_runs_path(self) -> Path:
        return self._root / "04_judgement_runs.parquet"

    def analysis_dir(self) -> Path:
        return self._root / "05_analysis"

    def analysis_artifact_path(self, artifact_name: str) -> Path:
        return self.analysis_dir() / f"{artifact_name}.parquet"

    def charts_dir(self) -> Path:
        return self._root / "charts"

    def chart_path(self, visgen_id: str, suffix: str = ".png") -> Path:
        return self.charts_dir() / f"{visgen_id}{suffix}"

    def read_cohort_df(self) -> pl.DataFrame:
        return self._read_df(
            self.cohort_path(),
            label="01_cohort.parquet",
            producer="01_cohort.py",
        )

    def write_cohort_df(self, df: pl.DataFrame) -> Path:
        return self._write_df(df, self.cohort_path())

    def read_grounding_df(self) -> pl.DataFrame:
        return self._read_df(
            self.grounding_path(),
            label="02_grounding.parquet",
            producer="02_grounding.py",
        )

    def write_grounding_df(self, df: pl.DataFrame) -> Path:
        return self._write_df(df, self.grounding_path())

    def read_generated_df(self) -> pl.DataFrame:
        return self._read_df(
            self.generate_path(),
            label="03_generate.parquet",
            producer="03_generating.py",
        )

    def write_generated_df(self, df: pl.DataFrame) -> Path:
        return self._write_df(df, self.generate_path())

    def read_generated_candidates_df(self) -> pl.DataFrame:
        return flatten_generated_candidates_df(
            self.read_generated_df(),
            self.read_grounding_df(),
        )

    def read_generated_attempts_df(self) -> pl.DataFrame:
        return flatten_generated_attempts_df(
            self.read_generated_df(),
            self.read_grounding_df(),
        )

    def read_judgements_df(self) -> pl.DataFrame:
        return self._read_df(
            self.judgements_path(),
            label="04_judgements.parquet",
            producer="04_judging.py",
        )

    def write_judgements_df(self, df: pl.DataFrame) -> Path:
        return self._write_df(df, self.judgements_path())

    def read_judgement_runs_df(self) -> pl.DataFrame:
        return self._read_df(
            self.judgement_runs_path(),
            label="04_judgement_runs.parquet",
            producer="04_judging.py",
        )

    def write_judgement_runs_df(self, df: pl.DataFrame) -> Path:
        return self._write_df(df, self.judgement_runs_path())

    def read_analysis_artifact_df(self, artifact_name: str) -> pl.DataFrame:
        return self._read_df(
            self.analysis_artifact_path(artifact_name),
            label=f"05_analysis/{artifact_name}.parquet",
            producer="05_analysis.py",
        )

    def write_analysis_artifact_df(
        self,
        artifact_name: str,
        df: pl.DataFrame,
    ) -> Path:
        return self._write_df(df, self.analysis_artifact_path(artifact_name))

    def chart_exists(self, visgen_id: str) -> bool:
        return self.chart_path(visgen_id).exists()

    def read_chart_image(self, visgen_id: str) -> Image.Image:
        path = self.chart_path(visgen_id)
        if not path.exists():
            raise FileNotFoundError(
                f"Missing chart image for visgen_id '{visgen_id}' at {path}. "
                "Generate or save the chart image first."
            )
        with Image.open(path) as image:
            return image.copy()

    def write_chart_image(self, visgen_id: str, image: Image.Image) -> Path:
        path = self.chart_path(visgen_id)
        self._ensure_parent(path)
        fd, temp_name = tempfile.mkstemp(
            dir=path.parent,
            prefix=f".{path.stem}-",
            suffix=path.suffix,
        )
        os.close(fd)
        temp_path = Path(temp_name)
        try:
            image.save(temp_path)
            os.replace(temp_path, path)
        except Exception:
            temp_path.unlink(missing_ok=True)
            raise
        return path

    def delete_chart_image(self, visgen_id: str) -> None:
        self.chart_path(visgen_id).unlink(missing_ok=True)

    @staticmethod
    def _ensure_parent(path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)

    def _read_df(self, path: Path, *, label: str, producer: str) -> pl.DataFrame:
        if not path.exists():
            raise FileNotFoundError(
                f"Missing `{label}` at {path}; run workbench `{producer}` first."
            )
        return pl.read_parquet(path)

    def _write_df(self, df: pl.DataFrame, path: Path) -> Path:
        self._ensure_parent(path)
        df.write_parquet(path)
        return path
