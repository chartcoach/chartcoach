from __future__ import annotations

import json
import logging
import threading
from collections import defaultdict
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal, cast

from joblib import Parallel, delayed
import polars as pl
from PIL import Image

from visground.datasets import VisEvalDataset, VisGroundDataset
from visground.evaluation import SCORE_FIELDS, overall_score_value, score_value
from visground.generation import VisualizationBackend
from visground.generation.backends import resolve_visualization_backend
from visground.grounding import get_audience_description
from visground.grounding.types import AUDIENCE_MODIFIER_IDS, AudienceModifierId
from visground.utils import extract_json

from .prompt import build_visjudge_prompt
from .visjudge import VisJudgeClient, VisJudgeRequest

_RAW_RUNS_ARTIFACT_NAME = "04_judgement_runs.parquet"
VisJudgeAggregationMode = Literal["average", "best"]
ProgressFn = Callable[[Iterable[Any], int], Iterable[Any]]


@dataclass(frozen=True, slots=True)
class _JudgeWorkItem:
    vis_id: str
    model: str
    grammar: str
    group: Sequence[Mapping[str, Any]]
    judge_run_index: int
    judge_run_id: str


@dataclass(frozen=True, slots=True)
class _RunSummary:
    judgement_raw: str | None
    judgement: Mapping[str, Any] | None
    overall_score: float | None
    canonical_judge_run_id: str | None
    best_overall_score: float | None
    best_judge_run_id: str | None


@dataclass(frozen=True, slots=True)
class VisJudgeRunConfig:
    repeats: int = 3
    aggregation: VisJudgeAggregationMode = "average"
    batch_size: int = 16
    parallel_jobs: int = 1

    def __post_init__(self) -> None:
        if self.repeats < 1:
            raise ValueError("repeats must be at least 1.")
        if self.aggregation not in {"average", "best"}:
            raise ValueError("aggregation must be either `average` or `best`.")
        if self.batch_size < 1:
            raise ValueError("batch_size must be at least 1.")
        if self.parallel_jobs < 1:
            raise ValueError("parallel_jobs must be at least 1.")


class VisJudgeRunner:
    def __init__(
        self,
        *,
        store: VisGroundDataset,
        viseval_dataset: VisEvalDataset,
        visjudge_client: VisJudgeClient,
        logger: logging.Logger | None = None,
        backend_resolver: Callable[
            [str, VisEvalDataset],
            VisualizationBackend[Any],
        ] = resolve_visualization_backend,
    ) -> None:
        self._store = store
        self._viseval_dataset = viseval_dataset
        self._visjudge_client = visjudge_client
        self._logger = logger or logging.getLogger(__name__)
        self._backend_resolver = backend_resolver
        self._backend_cache: dict[str, VisualizationBackend[Any]] = {}
        self._chart_locks: dict[str, threading.Lock] = {}
        self._chart_locks_guard = threading.Lock()

    def judge_candidates(
        self,
        candidates_df: pl.DataFrame,
        *,
        config: VisJudgeRunConfig | None = None,
        progress: ProgressFn | None = None,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        if candidates_df.is_empty():
            return (
                _empty_judgements_df(candidates_df),
                _empty_judgement_runs_df(candidates_df),
            )

        cfg = config or VisJudgeRunConfig()
        raw_rows: list[dict[str, Any]] = []

        work_items = self._build_work_items(candidates_df, repeats=cfg.repeats)
        raw_rows.extend(
            self._run_work_items(
                work_items,
                batch_size=cfg.batch_size,
                parallel_jobs=cfg.parallel_jobs,
                progress=progress,
            )
        )

        raw_runs_df = pl.from_dicts(raw_rows)
        judgements_df = self._aggregate_runs(
            candidates_df=candidates_df,
            raw_rows=raw_rows,
            aggregation=cfg.aggregation,
        )
        return judgements_df, raw_runs_df

    def _build_work_items(
        self,
        candidates_df: pl.DataFrame,
        *,
        repeats: int,
    ) -> list[_JudgeWorkItem]:
        group_df = (
            candidates_df.group_by("vis_id", "model", "grammar")
            .agg(group=pl.struct(pl.all()))
            .sort("vis_id", "model", "grammar")
        )

        work_items: list[_JudgeWorkItem] = []
        for row in group_df.iter_rows(named=True):
            for run_index in range(1, repeats + 1):
                work_items.append(
                    _JudgeWorkItem(
                        vis_id=str(row["vis_id"]),
                        model=str(row["model"]),
                        grammar=str(row["grammar"]),
                        group=row["group"],
                        judge_run_index=run_index,
                        judge_run_id=f"{run_index:02d}",
                    )
                )
        return work_items

    def _run_work_items(
        self,
        work_items: Sequence[_JudgeWorkItem],
        *,
        batch_size: int,
        parallel_jobs: int,
        progress: ProgressFn | None,
    ) -> list[dict[str, Any]]:
        if parallel_jobs == 1 or len(work_items) <= 1:
            results_iter: Iterable[list[dict[str, Any]]] = (
                self._run_group(item, batch_size=batch_size) for item in work_items
            )
        else:
            results_iter = Parallel(
                n_jobs=min(parallel_jobs, len(work_items)),
                prefer="threads",
                return_as="generator",
            )(
                delayed(self._run_group)(item, batch_size=batch_size)
                for item in work_items
            )

        iterator = (
            progress(results_iter, len(work_items))
            if progress is not None
            else results_iter
        )
        raw_rows: list[dict[str, Any]] = []
        for group_rows in iterator:
            raw_rows.extend(group_rows)
        return raw_rows

    def _run_group(
        self,
        item: _JudgeWorkItem,
        *,
        batch_size: int,
    ) -> list[dict[str, Any]]:
        raw_rows: list[dict[str, Any]] = []
        requests: list[VisJudgeRequest] = []
        request_templates: list[dict[str, Any]] = []

        for candidate in item.group:
            candidate_record = {
                **candidate,
                "vis_id": item.vis_id,
                "model": item.model,
                "grammar": item.grammar,
            }
            template = {
                **candidate_record,
                "judge_run_index": item.judge_run_index,
                "judge_run_id": item.judge_run_id,
                "judge_prompt_suffix": _build_prompt_suffix(item.judge_run_id),
                "judgement_raw": None,
                "judgement": None,
                "overall_score": None,
                "judge_error": None,
            }

            try:
                request = self._build_request(
                    candidate_record,
                    run_id=item.judge_run_id,
                )
            except Exception as exc:
                template["judge_error"] = str(exc)
                raw_rows.append(template)
                self._logger.error(
                    "Error building VisJudge request for visgen_id %s run %s: %s",
                    candidate_record["visgen_id"],
                    item.judge_run_id,
                    exc,
                )
                continue

            requests.append(request)
            request_templates.append(template)

        if not requests:
            self._logger.warning(
                "No valid VisJudge requests for vis_id %s run %s, skipping.",
                item.vis_id,
                item.judge_run_id,
            )
            return raw_rows

        self._logger.info(
            "Built %s VisJudge requests for vis_id %s run %s",
            len(requests),
            item.vis_id,
            item.judge_run_id,
        )

        try:
            judgements_raw = self._visjudge_client.run_many(
                requests,
                batch_size=batch_size,
            )
        except Exception as exc:
            self._logger.error(
                "VisJudge batch failed for vis_id %s run %s: %s",
                item.vis_id,
                item.judge_run_id,
                exc,
            )
            for template in request_templates:
                raw_rows.append(template | {"judge_error": str(exc)})
            return raw_rows

        if len(judgements_raw) != len(request_templates):
            message = (
                "VisJudge returned the wrong number of results for "
                f"vis_id {item.vis_id} run {item.judge_run_id}."
            )
            self._logger.error(message)
            for template in request_templates:
                raw_rows.append(template | {"judge_error": message})
            return raw_rows

        for template, judgement_raw in zip(request_templates, judgements_raw):
            judgement, error = self._parse_judgement(judgement_raw)
            raw_rows.append(
                template
                | {
                    "judgement_raw": judgement_raw,
                    "judgement": judgement,
                    "overall_score": overall_score_value(judgement),
                    "judge_error": error,
                }
            )

        return raw_rows

    def _build_request(
        self,
        candidate: Mapping[str, Any],
        *,
        run_id: str,
    ) -> VisJudgeRequest:
        chart_image = self._read_or_create_chart_image(candidate)

        context: dict[str, str] = {
            "Judge run id": _build_prompt_suffix(run_id),
        }
        if (
            audience := candidate.get("audience")
        ) is not None and audience in AUDIENCE_MODIFIER_IDS:
            context["The intended audience for this visualization is"] = (
                get_audience_description(cast(AudienceModifierId, audience))
            )

        return {
            "image": chart_image,
            "prompt": build_visjudge_prompt(context),
        }

    def _read_or_create_chart_image(self, candidate: Mapping[str, Any]) -> Image.Image:
        visgen_id = str(candidate["visgen_id"])
        if self._store.chart_exists(visgen_id):
            return self._store.read_chart_image(visgen_id)

        with self._chart_lock(visgen_id):
            if self._store.chart_exists(visgen_id):
                return self._store.read_chart_image(visgen_id)

            grammar = str(candidate["grammar"])
            vis_backend = self._get_backend(grammar)
            chart = vis_backend.materialize_visualization(
                str(candidate["vis_id"]),
                str(candidate["code"]),
            )
            chart_image = vis_backend.rasterize(chart)
            self._store.write_chart_image(visgen_id, chart_image)
            return chart_image

    def _chart_lock(self, visgen_id: str) -> threading.Lock:
        with self._chart_locks_guard:
            return self._chart_locks.setdefault(visgen_id, threading.Lock())

    def _get_backend(self, grammar: str) -> VisualizationBackend[Any]:
        backend = self._backend_cache.get(grammar)
        if backend is None:
            backend = self._backend_resolver(grammar, self._viseval_dataset)
            self._backend_cache[grammar] = backend
        return backend

    def _parse_judgement(
        self,
        judgement_raw: str | None,
    ) -> tuple[dict[str, Any] | None, str | None]:
        if judgement_raw is None:
            return None, "VisJudge returned no result."

        try:
            return extract_json(judgement_raw), None
        except Exception as exc:
            return None, str(exc)

    def _aggregate_runs(
        self,
        *,
        candidates_df: pl.DataFrame,
        raw_rows: Sequence[Mapping[str, Any]],
        aggregation: VisJudgeAggregationMode,
    ) -> pl.DataFrame:
        rows_by_visgen_id: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
        for row in raw_rows:
            rows_by_visgen_id[str(row["visgen_id"])].append(row)

        aggregate_rows: list[dict[str, Any]] = []
        for candidate in candidates_df.iter_rows(named=True):
            candidate_runs = rows_by_visgen_id.get(str(candidate["visgen_id"]), [])
            successful_runs = [
                row
                for row in candidate_runs
                if isinstance(row.get("judgement"), Mapping)
            ]
            run_summary = _summarize_candidate_runs(
                successful_runs,
                aggregation=aggregation,
            )
            aggregate_rows.append(
                candidate
                | {
                    "judgement_raw": run_summary.judgement_raw,
                    "judgement": run_summary.judgement,
                    "overall_score": run_summary.overall_score,
                    "judgement_aggregation": aggregation,
                    "canonical_judge_run_id": run_summary.canonical_judge_run_id,
                    "judgement_run_count": len(candidate_runs),
                    "judgement_success_count": len(successful_runs),
                    "best_overall_score": run_summary.best_overall_score,
                    "best_judge_run_id": run_summary.best_judge_run_id,
                    "judge_error_count": sum(
                        1
                        for row in candidate_runs
                        if row.get("judge_error") is not None
                    ),
                }
            )

        return pl.from_dicts(aggregate_rows)


def _build_prompt_suffix(run_id: str) -> str:
    return (
        f"{run_id}. This identifier only distinguishes repeated identical "
        "evaluations for aggregation. Do not change the rubric because of it."
    )


def _empty_judgement_runs_df(candidates_df: pl.DataFrame) -> pl.DataFrame:
    return candidates_df.head(0).with_columns(
        pl.lit(None, dtype=pl.Int64).alias("judge_run_index"),
        pl.lit(None, dtype=pl.String).alias("judge_run_id"),
        pl.lit(None, dtype=pl.String).alias("judge_prompt_suffix"),
        pl.lit(None, dtype=pl.String).alias("judgement_raw"),
        pl.lit(None).alias("judgement"),
        pl.lit(None, dtype=pl.Float64).alias("overall_score"),
        pl.lit(None, dtype=pl.String).alias("judge_error"),
    )


def _empty_judgements_df(candidates_df: pl.DataFrame) -> pl.DataFrame:
    return candidates_df.head(0).with_columns(
        pl.lit(None, dtype=pl.String).alias("judgement_raw"),
        pl.lit(None).alias("judgement"),
        pl.lit(None, dtype=pl.Float64).alias("overall_score"),
        pl.lit(None, dtype=pl.String).alias("judgement_aggregation"),
        pl.lit(None, dtype=pl.String).alias("canonical_judge_run_id"),
        pl.lit(None, dtype=pl.Int64).alias("judgement_run_count"),
        pl.lit(None, dtype=pl.Int64).alias("judgement_success_count"),
        pl.lit(None, dtype=pl.Float64).alias("best_overall_score"),
        pl.lit(None, dtype=pl.String).alias("best_judge_run_id"),
        pl.lit(None, dtype=pl.Int64).alias("judge_error_count"),
    )


def _summarize_candidate_runs(
    successful_runs: Sequence[Mapping[str, Any]],
    *,
    aggregation: VisJudgeAggregationMode,
) -> _RunSummary:
    best_run = _best_run(successful_runs)

    if aggregation == "best":
        if best_run is None:
            return _RunSummary(
                judgement_raw=None,
                judgement=None,
                overall_score=None,
                canonical_judge_run_id=None,
                best_overall_score=None,
                best_judge_run_id=None,
            )
        return _RunSummary(
            judgement_raw=cast(str | None, best_run.get("judgement_raw")),
            judgement=cast(Mapping[str, Any] | None, best_run.get("judgement")),
            overall_score=cast(float | None, best_run.get("overall_score")),
            canonical_judge_run_id=cast(str | None, best_run.get("judge_run_id")),
            best_overall_score=cast(float | None, best_run.get("overall_score")),
            best_judge_run_id=cast(str | None, best_run.get("judge_run_id")),
        )

    judgement = _average_judgements(successful_runs)
    return _RunSummary(
        judgement_raw=(
            json.dumps(judgement, ensure_ascii=False, default=str)
            if judgement is not None
            else None
        ),
        judgement=judgement,
        overall_score=overall_score_value(judgement),
        canonical_judge_run_id=None,
        best_overall_score=cast(float | None, best_run.get("overall_score"))
        if best_run
        else None,
        best_judge_run_id=cast(str | None, best_run.get("judge_run_id"))
        if best_run
        else None,
    )


def _average_judgements(
    successful_runs: Sequence[Mapping[str, Any]],
) -> dict[str, dict[str, Any]] | None:
    if not successful_runs:
        return None

    success_count = len(successful_runs)
    note = (
        f"Average of {success_count} successful judge runs; see "
        f"{_RAW_RUNS_ARTIFACT_NAME} for per-run rationale."
    )
    averaged: dict[str, dict[str, Any]] = {}
    for score_field in SCORE_FIELDS:
        scores: list[float] = []
        for row in successful_runs:
            judgement = row.get("judgement")
            if not isinstance(judgement, Mapping):
                continue
            score = score_value(judgement, score_field)
            if score is not None:
                scores.append(score)
        averaged[score_field] = {
            "score": (sum(scores) / len(scores)) if scores else None,
            "reasoning": note,
        }
    return averaged


def _best_run(
    successful_runs: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any] | None:
    best: Mapping[str, Any] | None = None
    best_score = float("-inf")

    for row in successful_runs:
        overall_score = row.get("overall_score")
        if overall_score is None:
            continue
        score = float(overall_score)
        if score > best_score:
            best = row
            best_score = score

    return best


__all__ = [
    "VisJudgeAggregationMode",
    "VisJudgeRunConfig",
    "VisJudgeRunner",
]
