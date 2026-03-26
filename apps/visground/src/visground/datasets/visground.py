from __future__ import annotations

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
    "audience",
    "data_profile",
    "guideline_ids",
    "model",
    "grammar",
    "code",
    "visualization_type",
    "query_interpretation",
    "design_rationale",
    "grounding_trace",
)


def flatten_generated_candidates_df(
    generated_df: pl.DataFrame,
    grounding_df: pl.DataFrame,
) -> pl.DataFrame:
    """Normalize scenario-batched generation output into one row per candidate."""
    if generated_df.is_empty():
        return pl.DataFrame(
            schema=[
                ("visgen_id", pl.String),
                ("grounding_id", pl.String),
                ("grounding_mode", pl.String),
                ("objective", pl.String),
                ("vis_id", pl.String),
                ("query", pl.String),
                ("audience", pl.String),
                ("guideline_ids", pl.List(pl.String)),
                ("model", pl.String),
                ("grammar", pl.String),
                ("code", pl.String),
                ("visualization_type", pl.String),
                ("query_interpretation", pl.String),
                ("design_rationale", pl.List(pl.String)),
                ("grounding_trace", pl.List(pl.String)),
            ]
        )

    return (
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
                audience=pl.col("request").struct.field("audience"),
                data_profile=pl.col("request").struct.field("data_profile"),
                guideline_ids=pl.col("result").struct.field("guideline_ids"),
            ),
            on="grounding_id",
            how="left",
        )
        .select(
            "visgen_id",
            "grounding_id",
            "grounding_mode",
            "objective",
            pl.col("id").alias("vis_id"),
            "query",
            "audience",
            "data_profile",
            "guideline_ids",
            "model",
            "grammar",
            "code",
            "visualization_type",
            "query_interpretation",
            "design_rationale",
            "grounding_trace",
        )
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

    def read_judgements_df(self) -> pl.DataFrame:
        return self._read_df(
            self.judgements_path(),
            label="04_judgements.parquet",
            producer="04_judging.py",
        )

    def write_judgements_df(self, df: pl.DataFrame) -> Path:
        return self._write_df(df, self.judgements_path())

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
        return Image.open(path)

    def write_chart_image(self, visgen_id: str, image: Image.Image) -> Path:
        path = self.chart_path(visgen_id)
        self._ensure_parent(path)
        image.save(path)
        return path

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
