from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import polars as pl
import yaml

from chartcoach.retrieval.analysis.counterfactual import (
    compute_counterfactual_sensitivity,
    CounterfactualSensitivityResult,
)
from chartcoach.retrieval.analysis.pooling import compute_pool_coverage
from chartcoach.retrieval.analysis.stability import StabilityResult, compute_stability
from chartcoach.retrieval.service.eval_artifacts_schema import (
    EvalArtifactsIndexArtifact,
    EvalScenarioBundleArtifact,
)


@dataclass(frozen=True, slots=True)
class StrategyTaxonomyRow:
    id: str
    family: str
    label: str | None = None


def load_strategy_taxonomy(path: Path) -> dict[str, StrategyTaxonomyRow]:
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError("Expected YAML mapping at taxonomy path.")
    strategies = doc.get("strategies")
    if not isinstance(strategies, list):
        raise ValueError("Expected taxonomy to contain 'strategies: [...]'.")

    out: dict[str, StrategyTaxonomyRow] = {}
    for row in strategies:
        if not isinstance(row, dict):
            continue
        sid = row.get("id")
        family = row.get("family")
        if not isinstance(sid, str) or not sid.strip():
            continue
        if not isinstance(family, str) or not family.strip():
            continue
        label = row.get("label")
        out[sid] = StrategyTaxonomyRow(
            id=sid.strip(),
            family=family.strip(),
            label=str(label).strip() if isinstance(label, str) and label.strip() else None,
        )
    return out


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_index(run_dir: Path) -> EvalArtifactsIndexArtifact:
    index_path = run_dir / "index.json"
    if not index_path.exists():
        raise FileNotFoundError(f"Missing index.json under {run_dir}")
    return EvalArtifactsIndexArtifact.model_validate(_read_json(index_path))


def _iter_bundles(run_dir: Path) -> list[EvalScenarioBundleArtifact]:
    bundles_dir = run_dir / "bundles"
    if not bundles_dir.exists():
        raise FileNotFoundError(f"Missing bundles/ under {run_dir}")
    bundles: list[EvalScenarioBundleArtifact] = []
    for path in sorted(bundles_dir.glob("*.json")):
        bundles.append(EvalScenarioBundleArtifact.model_validate(_read_json(path)))
    return bundles


def _safe_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        raw = value.strip()
        if raw.isdigit():
            return int(raw)
    return None


def _safe_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return None
    return None


def _pairwise_jaccard_label_sets(label_sets: list[set[str]]) -> float:
    if len(label_sets) <= 1:
        return 0.0
    total = 0.0
    pairs = 0
    for i in range(len(label_sets)):
        for j in range(i + 1, len(label_sets)):
            a = label_sets[i]
            b = label_sets[j]
            denom = len(a | b)
            total += (len(a & b) / denom) if denom else 0.0
            pairs += 1
    return total / max(1, pairs)


def build_strategy_summary_table(
    *,
    run_dir: Path,
    taxonomy: dict[str, StrategyTaxonomyRow],
    k: int | None = None,
) -> pl.DataFrame:
    """Summarize one run with paper-facing metrics (latency, tokens, redundancy)."""

    index = _load_index(run_dir)
    id_to_name = {s.id: s.name for s in index.strategies}
    bundles = _iter_bundles(run_dir)

    rows: list[dict[str, Any]] = []
    for bundle in bundles:
        scenario_id = bundle.scenario.id
        for strat in bundle.strategies:
            sid = strat.strategy_id
            meta = strat.meta or {}
            elapsed_ms = _safe_int(meta.get("elapsed_ms"))

            lm_usage: dict[str, object] = {}
            raw_lm = meta.get("lm_usage")
            if isinstance(raw_lm, dict):
                lm_usage = {k: v for k, v in raw_lm.items() if isinstance(k, str)}

            vlm_usage: dict[str, object] = {}
            raw_vlm = meta.get("vlm_usage")
            if isinstance(raw_vlm, dict):
                vlm_usage = {k: v for k, v in raw_vlm.items() if isinstance(k, str)}

            lm_calls = _safe_int(lm_usage.get("calls"))
            lm_total = _safe_int(lm_usage.get("total_tokens"))
            lm_cost = _safe_float(lm_usage.get("cost_usd"))
            vlm_calls = _safe_int(vlm_usage.get("calls"))
            vlm_total = _safe_int(vlm_usage.get("total_tokens"))
            vlm_cost = _safe_float(vlm_usage.get("cost_usd"))

            gids = []
            label_sets: list[set[str]] = []
            for g in strat.guidelines[: (k or len(strat.guidelines))]:
                gids.append(g.entry.id)
                label_sets.append(set(g.entry.guideline.labels or []))

            redundancy = _pairwise_jaccard_label_sets(label_sets)
            tax = taxonomy.get(sid)
            family = tax.family if tax is not None else "unknown"
            label = tax.label if tax is not None else None

            rows.append(
                {
                    "scenario_id": scenario_id,
                    "strategy_id": sid,
                    "strategy_name": id_to_name.get(sid) or sid,
                    "family": family,
                    "label": label or sid,
                    "k": k or len(gids),
                    "elapsed_ms": elapsed_ms,
                    "lm_calls": lm_calls,
                    "lm_total_tokens": lm_total,
                    "lm_cost_usd": lm_cost,
                    "vlm_calls": vlm_calls,
                    "vlm_total_tokens": vlm_total,
                    "vlm_cost_usd": vlm_cost,
                    "pairwise_label_jaccard": redundancy,
                }
            )

    df = pl.DataFrame(rows)
    if df.is_empty():
        return df

    return (
        df.group_by(["strategy_id", "strategy_name", "family", "label"])
        .agg(
            pl.len().alias("n_scenarios"),
            pl.mean("elapsed_ms").alias("mean_elapsed_ms"),
            pl.mean("lm_calls").alias("mean_lm_calls"),
            pl.mean("lm_total_tokens").alias("mean_lm_total_tokens"),
            pl.mean("lm_cost_usd").alias("mean_lm_cost_usd"),
            pl.mean("vlm_calls").alias("mean_vlm_calls"),
            pl.mean("vlm_total_tokens").alias("mean_vlm_total_tokens"),
            pl.mean("vlm_cost_usd").alias("mean_vlm_cost_usd"),
            pl.mean("pairwise_label_jaccard").alias("mean_pairwise_label_jaccard"),
        )
        .sort(["family", "strategy_id"])
    )


def write_paper_assets(
    *,
    runs: list[Path],
    out_dir: Path,
    taxonomy_path: Path,
    k: int | None = None,
    plots: bool = False,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    taxonomy = load_strategy_taxonomy(taxonomy_path)

    def _df_to_markdown_table(df: pl.DataFrame) -> str:
        if df.is_empty():
            return "_(no rows)_"
        cols = df.columns
        lines = [
            "| " + " | ".join(cols) + " |",
            "|" + "|".join(["---" for _ in cols]) + "|",
        ]
        for row in df.iter_rows(named=False):
            lines.append("| " + " | ".join(str(v) for v in row) + " |")
        return "\n".join(lines)

    # Per-run summaries (CSV + Markdown table).
    for run in runs:
        run_name = run.name
        summary = build_strategy_summary_table(run_dir=run, taxonomy=taxonomy, k=k)
        summary_path = out_dir / f"{run_name}.strategy-summary.csv"
        summary.write_csv(summary_path)

        md_path = out_dir / f"{run_name}.strategy-summary.md"
        md_path.write_text(_df_to_markdown_table(summary), encoding="utf-8")

        pool = compute_pool_coverage(artifacts_root=run, k=k)
        pool_md = out_dir / f"{run_name}.pool.md"
        pool_md.write_text(
            "\n".join(
                [
                    f"# Pool coverage ({run_name})",
                    "",
                    "| scenario_id | strategies | pool_size |",
                    "|---|---:|---:|",
                    *[
                        f"| {r.scenario_id} | {r.strategies} | {r.unique_guidelines} |"
                        for r in pool
                    ],
                ]
            ),
            encoding="utf-8",
        )

        cf = compute_counterfactual_sensitivity(artifacts_root=run, k=k)
        cf_md = out_dir / f"{run_name}.counterfactual.md"
        cf_md.write_text(
            "\n".join(
                [
                    f"# Counterfactual overlap ({run_name})",
                    "",
                    "| strategy_id | mean_overlap_jaccard |",
                    "|---|---:|",
                    *[f"| {r.strategy_id} | {r.mean_jaccard:.3f} |" for r in cf],
                ]
            ),
            encoding="utf-8",
        )

        if plots:
            _write_plots_for_run(
                out_dir=out_dir,
                run_name=run_name,
                summary=summary,
                counterfactual=cf,
            )

    # Cross-run stability.
    if len(runs) >= 2:
        stability = compute_stability(runs=runs, k=k)
        stab_md = out_dir / "stability.md"
        stab_md.write_text(
            "\n".join(
                [
                    "# Stability across runs",
                    "",
                    "| strategy_id | mean_jaccard |",
                    "|---|---:|",
                    *[f"| {r.strategy_id} | {r.mean_jaccard:.3f} |" for r in stability],
                ]
            ),
            encoding="utf-8",
        )

        if plots:
            _write_stability_plot(out_dir=out_dir, stability=stability)


def _require_matplotlib():
    try:
        import matplotlib.pyplot as plt  # type: ignore[import-not-found]
    except Exception as e:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "Matplotlib not available. Install with `uv sync --group paper`."
        ) from e
    return plt


def _write_stability_plot(*, out_dir: Path, stability: list[StabilityResult]) -> None:
    plt = _require_matplotlib()
    ids: list[str] = [r.strategy_id for r in stability]
    vals: list[float] = [float(r.mean_jaccard) for r in stability]
    if not ids:
        return

    fig_h = max(4.0, 0.25 * len(ids))
    fig, ax = plt.subplots(figsize=(10, fig_h))
    ax.barh(range(len(ids)), vals)
    ax.set_yticks(range(len(ids)))
    ax.set_yticklabels(ids)
    ax.invert_yaxis()
    ax.set_xlim(0.0, 1.0)
    ax.set_xlabel("Mean Jaccard@k (higher = more stable)")
    ax.set_title("Stability Across Runs")
    fig.tight_layout()
    fig.savefig(out_dir / "stability.png", dpi=200)
    plt.close(fig)


def _write_plots_for_run(
    *,
    out_dir: Path,
    run_name: str,
    summary: pl.DataFrame,
    counterfactual: list[CounterfactualSensitivityResult],
) -> None:
    plt = _require_matplotlib()

    # Counterfactual overlap (lower = more sensitive).
    if counterfactual:
        ids = [r.strategy_id for r in counterfactual]
        vals = [float(r.mean_jaccard) for r in counterfactual]
        fig_h = max(4.0, 0.25 * len(ids))
        fig, ax = plt.subplots(figsize=(10, fig_h))
        ax.barh(range(len(ids)), vals)
        ax.set_yticks(range(len(ids)))
        ax.set_yticklabels(ids)
        ax.invert_yaxis()
        ax.set_xlim(0.0, 1.0)
        ax.set_xlabel("Mean Jaccard@k across counterfactual variants (lower = more change)")
        ax.set_title(f"Counterfactual Overlap ({run_name})")
        fig.tight_layout()
        fig.savefig(out_dir / f"{run_name}.counterfactual.png", dpi=200)
        plt.close(fig)

    # Latency vs redundancy proxy.
    if not summary.is_empty() and "mean_elapsed_ms" in summary.columns:
        df = summary.select(
            [
                pl.col("strategy_id"),
                pl.col("mean_elapsed_ms"),
                pl.col("mean_pairwise_label_jaccard"),
            ]
        ).drop_nulls()
        if df.height:
            ids = df["strategy_id"].to_list()
            x = df["mean_elapsed_ms"].to_list()
            y = df["mean_pairwise_label_jaccard"].to_list()
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.scatter(x, y)
            for i, sid in enumerate(ids):
                ax.annotate(sid, (x[i], y[i]), fontsize=7, alpha=0.75)
            ax.set_xlabel("Mean elapsed ms (lower = faster)")
            ax.set_ylabel("Mean pairwise label Jaccard (lower = less redundant)")
            ax.set_title(f"Latency vs Redundancy Proxy ({run_name})")
            fig.tight_layout()
            fig.savefig(out_dir / f"{run_name}.latency-vs-redundancy.png", dpi=200)
            plt.close(fig)
