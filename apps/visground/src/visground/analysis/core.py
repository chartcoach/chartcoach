"""Assemble the comparative tables used to judge grounded vs ungrounded runs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import polars as pl

from visground.datasets import VisGroundDataset

from .cases import (
    build_analysis_cases_df,
    build_paired_case_deltas_df,
    build_score_models_df,
    build_score_summary_df,
)
from .guidelines import (
    build_guideline_associations_df,
    build_guideline_summary_df,
)
from .variance import (
    build_condition_variance_df,
    build_design_variance_deltas_df,
    build_variance_summary_df,
)


@dataclass(frozen=True, slots=True)
class VisGroundAnalysisBundle:
    """Named collection of the comparative tables built from one experiment run."""

    analysis_cases_df: pl.DataFrame
    paired_case_deltas_df: pl.DataFrame
    score_summary_df: pl.DataFrame
    condition_variance_df: pl.DataFrame
    design_variance_deltas_df: pl.DataFrame
    variance_summary_df: pl.DataFrame
    guideline_summary_df: pl.DataFrame
    guideline_associations_df: pl.DataFrame
    score_models_df: pl.DataFrame

    def artifacts(self) -> dict[str, pl.DataFrame]:
        """Return every dataframe keyed by the artifact name used on disk."""
        return {
            "analysis_cases": self.analysis_cases_df,
            "paired_case_deltas": self.paired_case_deltas_df,
            "score_summary": self.score_summary_df,
            "condition_variance": self.condition_variance_df,
            "design_variance_deltas": self.design_variance_deltas_df,
            "variance_summary": self.variance_summary_df,
            "guideline_summary": self.guideline_summary_df,
            "guideline_associations": self.guideline_associations_df,
            "score_models": self.score_models_df,
        }

    def manifest_df(self) -> pl.DataFrame:
        """Return one row per artifact so the notebook can show what was produced."""
        return pl.from_dicts(
            [
                {
                    "artifact_name": artifact_name,
                    "rows": artifact_df.height,
                    "columns": artifact_df.width,
                }
                for artifact_name, artifact_df in self.artifacts().items()
            ]
        )

    def write_all(self, store: VisGroundDataset) -> dict[str, Path]:
        """Write every dataframe to `05_analysis` and return the written paths."""
        return {
            artifact_name: store.write_analysis_artifact_df(artifact_name, artifact_df)
            for artifact_name, artifact_df in self.artifacts().items()
        }


def build_analysis_bundle(store: VisGroundDataset) -> VisGroundAnalysisBundle:
    """Build the case, delta, variance, and guideline tables from one run snapshot."""
    analysis_cases_df = build_analysis_cases_df(
        store.read_generated_candidates_df(),
        store.read_judgements_df(),
    )
    paired_case_deltas_df = build_paired_case_deltas_df(analysis_cases_df)
    condition_variance_df = build_condition_variance_df(analysis_cases_df)
    design_variance_deltas_df = build_design_variance_deltas_df(condition_variance_df)

    return VisGroundAnalysisBundle(
        analysis_cases_df=analysis_cases_df,
        paired_case_deltas_df=paired_case_deltas_df,
        score_summary_df=build_score_summary_df(paired_case_deltas_df),
        condition_variance_df=condition_variance_df,
        design_variance_deltas_df=design_variance_deltas_df,
        variance_summary_df=build_variance_summary_df(design_variance_deltas_df),
        guideline_summary_df=build_guideline_summary_df(paired_case_deltas_df),
        guideline_associations_df=build_guideline_associations_df(
            paired_case_deltas_df
        ),
        score_models_df=build_score_models_df(paired_case_deltas_df),
    )


__all__ = [
    "VisGroundAnalysisBundle",
    "build_analysis_bundle",
]
