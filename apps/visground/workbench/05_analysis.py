import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import altair as alt
    import marimo as mo
    import numpy as np
    import pandas as pd
    import polars as pl
    import scipy.stats as stats
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm

    from visground.datasets import VisGroundDataset
    from visground.evaluation import SCORE_FIELDS, score_expr

    alt.data_transformers.disable_max_rows()

    ANALYSIS_ARTIFACT_NAMES = (
        "candidate",
        "score_long",
        "coverage",
        "pair_delta",
        "summary",
        "variance",
        "guideline_diagnostics",
        "label_diagnostics",
    )
    PAIR_KEY_COLUMNS = [
        "vis_id",
        "objective",
        "audience_bucket",
        "model",
        "grammar",
    ]
    PUBLICATION_BOOTSTRAP_DRAWS = 500
    DIAGNOSTIC_BOOTSTRAP_DRAWS = 250
    BOOTSTRAP_SEED = 42

    def humanize(value: str | None) -> str:
        if value is None:
            return "None"
        return str(value).replace("_", " ").title()

    def ordered_options(series: pl.Series, *, none_first: bool = False) -> list[str]:
        values = [
            value
            for value in series.drop_nulls().unique().to_list()
            if value is not None
        ]
        if none_first:
            return sorted(values, key=lambda value: (value != "none", value))
        return sorted(values)

    def apply_optional_filters(
        df: pl.DataFrame, filters: dict[str, str]
    ) -> pl.DataFrame:
        filtered = df
        for column, value in filters.items():
            if column not in filtered.columns or value == "all":
                continue
            filtered = filtered.filter(pl.col(column) == value)
        return filtered

    def cluster_bootstrap_mean_ci(
        pdf: pd.DataFrame,
        *,
        value_col: str = "delta",
        cluster_col: str = "vis_id",
        draws: int = PUBLICATION_BOOTSTRAP_DRAWS,
        seed: int = BOOTSTRAP_SEED,
    ) -> tuple[float | None, float | None, float | None]:
        valid = pdf[[cluster_col, value_col]].dropna()
        if valid.empty:
            return (None, None, None)
        clusters = valid[cluster_col].astype(str).to_numpy()
        values = valid[value_col].astype(float).to_numpy()
        unique_clusters = np.unique(clusters)
        mean_value = float(values.mean())
        if len(unique_clusters) < 2 or draws <= 0:
            return (mean_value, mean_value, mean_value)
        index_map = {
            cluster: np.flatnonzero(clusters == cluster) for cluster in unique_clusters
        }
        rng = np.random.default_rng(seed)
        boot_means = np.empty(draws, dtype=float)
        for idx in range(draws):
            sampled_clusters = rng.choice(
                unique_clusters, size=len(unique_clusters), replace=True
            )
            sampled_values = np.concatenate(
                [values[index_map[cluster]] for cluster in sampled_clusters]
            )
            boot_means[idx] = sampled_values.mean()
        ci_low, ci_high = np.quantile(boot_means, [0.025, 0.975]).tolist()
        return (mean_value, float(ci_low), float(ci_high))

    def paired_effect_size(deltas: pd.Series) -> float | None:
        valid = deltas.dropna().astype(float).to_numpy()
        if valid.size < 2:
            return None
        std = float(valid.std(ddof=1))
        if std == 0:
            return None
        return float(valid.mean() / std)

    def win_tie_loss(deltas: pd.Series):
        valid = deltas.dropna().astype(float).to_numpy()
        if valid.size == 0:
            return (0, 0, 0, None, None, None, None)
        wins = int((valid > 0).sum())
        ties = int((valid == 0).sum())
        losses = int((valid < 0).sum())
        decisive = wins + losses
        sign_test_p = (
            float(stats.binomtest(wins, decisive, 0.5).pvalue) if decisive else None
        )
        return (
            wins,
            ties,
            losses,
            wins / valid.size,
            ties / valid.size,
            losses / valid.size,
            sign_test_p,
        )

    def summarize_delta_groups(
        delta_df: pl.DataFrame,
        *,
        group_cols: list[str],
        none_col: str = "none_score",
        structured_col: str = "structured_score",
        delta_col: str = "delta",
        cluster_col: str = "vis_id",
        bootstrap_draws: int = PUBLICATION_BOOTSTRAP_DRAWS,
    ) -> pl.DataFrame:
        if delta_df.is_empty() or delta_col not in delta_df.columns:
            return pl.DataFrame()
        needed = [*group_cols, cluster_col, none_col, structured_col, delta_col]
        valid_df = delta_df.select(
            [column for column in needed if column in delta_df.columns]
        ).filter(pl.col(delta_col).is_not_null())
        if valid_df.is_empty():
            return pl.DataFrame()
        pdf = valid_df.to_pandas()
        grouped = (
            [((), pdf)]
            if not group_cols
            else pdf.groupby(group_cols, dropna=False, sort=False)
        )
        records = []
        for key, group in grouped:
            key_tuple = key if isinstance(key, tuple) else (key,)
            record = {column: value for column, value in zip(group_cols, key_tuple)}
            deltas = group[delta_col].dropna().astype(float)
            if deltas.empty:
                continue
            mean_delta, ci_low, ci_high = cluster_bootstrap_mean_ci(
                group,
                value_col=delta_col,
                cluster_col=cluster_col,
                draws=bootstrap_draws,
            )
            wins, ties, losses, win_rate, tie_rate, loss_rate, sign_test_p = (
                win_tie_loss(deltas)
            )
            non_zero = deltas[deltas != 0]
            wilcoxon_p = None
            if len(non_zero):
                try:
                    wilcoxon_p = float(stats.wilcoxon(non_zero).pvalue)
                except ValueError:
                    wilcoxon_p = None
            record.update(
                {
                    "n_pairs": int(len(deltas)),
                    "cluster_count": int(group[cluster_col].nunique(dropna=False)),
                    "none_mean": float(group[none_col].dropna().astype(float).mean())
                    if group[none_col].notna().any()
                    else None,
                    "structured_mean": float(
                        group[structured_col].dropna().astype(float).mean()
                    )
                    if group[structured_col].notna().any()
                    else None,
                    "delta_mean": mean_delta,
                    "delta_median": float(deltas.median()),
                    "delta_std": float(deltas.std(ddof=1)) if len(deltas) > 1 else None,
                    "ci_low": ci_low,
                    "ci_high": ci_high,
                    "wins": wins,
                    "ties": ties,
                    "losses": losses,
                    "win_rate": win_rate,
                    "tie_rate": tie_rate,
                    "loss_rate": loss_rate,
                    "paired_d": paired_effect_size(deltas),
                    "sign_test_p": sign_test_p,
                    "wilcoxon_p": wilcoxon_p,
                }
            )
            records.append(record)
        return (
            pl.DataFrame(records).sort(group_cols)
            if group_cols
            else pl.DataFrame(records)
        )

    def summarize_macro_from_cells(
        cell_df: pl.DataFrame, *, group_cols: list[str]
    ) -> pl.DataFrame:
        if cell_df.is_empty():
            return pl.DataFrame()
        return (
            cell_df.group_by(group_cols)
            .agg(
                pl.len().alias("n_cells"),
                pl.col("n_pairs").sum().alias("n_pairs"),
                pl.col("cluster_count").sum().alias("cluster_count"),
                pl.col("none_mean").mean().alias("none_mean"),
                pl.col("structured_mean").mean().alias("structured_mean"),
                pl.col("delta_mean").mean().alias("delta_mean"),
                pl.col("delta_mean").median().alias("delta_median"),
                pl.col("delta_mean").std().alias("delta_std"),
                pl.col("win_rate").mean().alias("win_rate"),
                pl.col("tie_rate").mean().alias("tie_rate"),
                pl.col("loss_rate").mean().alias("loss_rate"),
            )
            .with_columns(
                wins=pl.lit(None).cast(pl.Int64),
                ties=pl.lit(None).cast(pl.Int64),
                losses=pl.lit(None).cast(pl.Int64),
                ci_low=pl.lit(None).cast(pl.Float64),
                ci_high=pl.lit(None).cast(pl.Float64),
                paired_d=pl.lit(None).cast(pl.Float64),
                sign_test_p=pl.lit(None).cast(pl.Float64),
                wilcoxon_p=pl.lit(None).cast(pl.Float64),
            )
            .sort(group_cols)
        )

    def fit_clustered_delta_model(
        delta_df: pl.DataFrame, *, dimension: str = "overall_score"
    ):
        model_df = (
            delta_df.filter(
                (pl.col("dimension") == dimension) & pl.col("delta").is_not_null()
            )
            .select(
                "vis_id",
                "objective",
                "grammar",
                "model",
                "audience_bucket",
                "delta",
            )
            .to_pandas()
        )
        if model_df.empty or model_df["vis_id"].nunique() < 2:
            return pl.DataFrame(), pl.DataFrame(), pl.DataFrame()
        terms = []
        for column in ["objective", "grammar", "model", "audience_bucket"]:
            if model_df[column].nunique(dropna=False) > 1:
                terms.append(f"C({column})")
        if (
            model_df["objective"].nunique(dropna=False) > 1
            and model_df["grammar"].nunique(dropna=False) > 1
        ):
            terms.append("C(objective):C(grammar)")
        if not terms:
            return pl.DataFrame(), pl.DataFrame(), pl.DataFrame()
        formula = "delta ~ " + " + ".join(terms)
        ols_fit = smf.ols(formula, data=model_df).fit()
        covariance = "cluster"
        try:
            robust_fit = ols_fit.get_robustcov_results(
                cov_type="cluster", groups=model_df["vis_id"]
            )
        except Exception:
            robust_fit = ols_fit
            covariance = "nonrobust"
        conf_int = robust_fit.conf_int()
        coef_df = pl.DataFrame(
            {
                "term": robust_fit.model.exog_names,
                "estimate": [float(value) for value in robust_fit.params],
                "std_error": [float(value) for value in robust_fit.bse],
                "ci_low": [float(row[0]) for row in conf_int],
                "ci_high": [float(row[1]) for row in conf_int],
                "p_value": [float(value) for value in robust_fit.pvalues],
            }
        )
        total_ss = float(((model_df["delta"] - model_df["delta"].mean()) ** 2).sum())
        try:
            anova_pdf = (
                anova_lm(ols_fit, typ=2)
                .reset_index()
                .rename(columns={"index": "term", "F": "f_value", "PR(>F)": "p_value"})
            )
            anova_pdf["eta_sq"] = anova_pdf["sum_sq"] / total_ss if total_ss else np.nan
            anova_df = pl.from_pandas(
                anova_pdf[["term", "sum_sq", "df", "f_value", "p_value", "eta_sq"]]
            )
        except Exception:
            anova_df = pl.DataFrame()
        meta_df = pl.DataFrame(
            [
                {
                    "formula": formula,
                    "n_obs": int(ols_fit.nobs),
                    "cluster_count": int(model_df["vis_id"].nunique()),
                    "r_squared": float(ols_fit.rsquared),
                    "adj_r_squared": float(ols_fit.rsquared_adj),
                    "covariance": covariance,
                }
            ]
        )
        return coef_df, anova_df, meta_df

    def trace_mentions_guideline(guideline_id: str, trace_items: object) -> bool:
        if not isinstance(trace_items, list):
            return False
        return any(guideline_id in str(item) for item in trace_items)

    def diagnostic_support_threshold(n_pairs: int) -> int:
        return max(4, int(np.ceil(n_pairs * 0.05)))

    return (
        ANALYSIS_ARTIFACT_NAMES,
        DIAGNOSTIC_BOOTSTRAP_DRAWS,
        PAIR_KEY_COLUMNS,
        Path,
        SCORE_FIELDS,
        VisGroundDataset,
        alt,
        apply_optional_filters,
        diagnostic_support_threshold,
        fit_clustered_delta_model,
        humanize,
        mo,
        ordered_options,
        pl,
        score_expr,
        summarize_delta_groups,
        summarize_macro_from_cells,
        trace_mentions_guideline,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "\n".join(
            [
                "# 05 Analysis",
                "",
                "Build the publication-grade analysis cube and quantify score lift, variance, and catalog diagnostics for grounded generation.",
                "",
                "## Stage Contract",
                "",
                "- Required inputs: `01_cohort.parquet`, `03_generate.parquet`, `04_judgements.parquet`",
                "- Supporting input: `02_grounding.parquet`",
                "- Persisted outputs: `artifacts/05_analysis/*.parquet`",
                "- Responsibility: build the canonical candidate-grain analysis table, compute paired grounded-vs-ungrounded results, quantify variance, and expose catalog/retrieval diagnostics",
            ]
        )
    )
    return


@app.cell
def _(
    Path,
    SCORE_FIELDS,
    VisGroundDataset,
    mo,
    ordered_options,
    pl,
    score_expr,
):
    mo.md("## Inputs, Controls, And Canonical Analysis Table")
    store = VisGroundDataset()
    artifact_specs = [
        ("cohort", store.cohort_path()),
        ("grounding", store.grounding_path()),
        ("generated", store.generate_path()),
        ("judgements", store.judgements_path()),
    ]
    input_status_df = pl.DataFrame(
        {
            "artifact": [name for name, _ in artifact_specs],
            "path": [str(path) for _, path in artifact_specs],
            "exists": [path.exists() for _, path in artifact_specs],
            "size_bytes": [
                path.stat().st_size if path.exists() else None
                for _, path in artifact_specs
            ],
        }
    )
    REPO_ROOT = Path(__file__).resolve().parents[3]
    catalog_path = REPO_ROOT / "guidelines" / "catalog.parquet"
    cohort_df = store.read_cohort_df()
    generated_candidates_df = store.read_generated_candidates_df()
    judgements_df = store.read_judgements_df()
    catalog_guideline_df = (
        pl.read_parquet(catalog_path)
        .select("guideline")
        .unnest("guideline")
        .select("id", "title", "labels")
    )
    catalog_label_df = (
        catalog_guideline_df.select(
            guideline_id=pl.col("id"),
            guideline_title=pl.col("title"),
            label=pl.col("labels"),
        )
        .explode("label")
        .drop_nulls("label")
        .with_columns(parts=pl.col("label").str.split(":"))
        .select(
            "guideline_id",
            "guideline_title",
            "label",
            label_category=pl.col("parts").list.get(0),
            label_subcategory=pl.col("parts").list.get(1),
            label_polarity=pl.col("parts").list.get(2, null_on_oob=True),
            label_key=pl.concat_str(
                [pl.col("parts").list.get(0), pl.col("parts").list.get(1)],
                separator=":",
            ),
        )
    )
    candidate_base_df = generated_candidates_df.join(
        judgements_df.select("visgen_id", "judgement", "judgement_raw"),
        on="visgen_id",
        how="left",
    ).join(
        cohort_df.select(
            cohort_id=pl.col("id"),
            db_id=pl.col("db_id"),
            chart=pl.col("chart"),
            hardness=pl.col("hardness"),
            task=pl.col("task"),
            scope=pl.col("scope"),
            time_mode=pl.col("time_mode"),
        ),
        left_on="vis_id",
        right_on="cohort_id",
        how="left",
    )
    candidate_df = candidate_base_df.with_columns(
        audience_bucket=pl.col("audience").fill_null("none"),
        has_judgement=pl.col("judgement").is_not_null(),
        empty_judgement=(pl.col("judgement_raw") == "{}").fill_null(False),
        n_guidelines_raw=pl.col("guideline_ids").list.len().fill_null(0),
        n_guidelines=pl.col("guideline_ids").list.unique().list.len().fill_null(0),
        trace_count=pl.col("grounding_trace").list.len().fill_null(0),
        *(
            score_expr(score_field, source_columns=candidate_base_df.columns).alias(
                score_field
            )
            for score_field in SCORE_FIELDS
        ),
    ).with_columns(
        complete_score=pl.all_horizontal(
            *(pl.col(score_field).is_not_null() for score_field in SCORE_FIELDS)
        ),
        overall_score=pl.when(
            pl.all_horizontal(
                *(pl.col(score_field).is_not_null() for score_field in SCORE_FIELDS)
            )
        )
        .then(
            pl.mean_horizontal(
                *(pl.col(score_field) for score_field in SCORE_FIELDS)
            ).round(4)
        )
        .otherwise(pl.lit(None).cast(pl.Float64)),
        guideline_duplication_count=(
            pl.col("n_guidelines_raw") - pl.col("n_guidelines")
        ).fill_null(0),
        trace_density=pl.when(pl.col("n_guidelines") > 0)
        .then((pl.col("trace_count") / pl.col("n_guidelines")).round(4))
        .otherwise(pl.lit(0.0)),
    )
    objective_options = (
        ["all", *ordered_options(candidate_df.get_column("objective"))]
        if candidate_df.height
        else ["all"]
    )
    audience_options = (
        [
            "all",
            *ordered_options(
                candidate_df.get_column("audience_bucket"), none_first=True
            ),
        ]
        if candidate_df.height
        else ["all"]
    )
    model_options = (
        ["all", *ordered_options(candidate_df.get_column("model"))]
        if candidate_df.height
        else ["all"]
    )
    grammar_options = (
        ["all", *ordered_options(candidate_df.get_column("grammar"))]
        if candidate_df.height
        else ["all"]
    )
    view_mode = mo.ui.dropdown(options=["paper", "debug"], value="paper", label="View")
    objective_filter = mo.ui.dropdown(
        options=objective_options, value="all", label="Objective"
    )
    audience_filter = mo.ui.dropdown(
        options=audience_options, value="all", label="Audience"
    )
    model_filter = mo.ui.dropdown(options=model_options, value="all", label="Model")
    grammar_filter = mo.ui.dropdown(
        options=grammar_options, value="all", label="Grammar"
    )
    mo.vstack(
        [
            input_status_df,
            mo.vstack(
                [
                    view_mode,
                    objective_filter,
                    audience_filter,
                    model_filter,
                    grammar_filter,
                ]
            ),
            candidate_df.select(
                "visgen_id",
                "vis_id",
                "objective",
                "audience_bucket",
                "grounding_mode",
                "model",
                "grammar",
                "n_guidelines",
                "trace_count",
                "has_judgement",
                "complete_score",
                "overall_score",
            ).sort(
                "objective",
                "audience_bucket",
                "grounding_mode",
                "model",
                "grammar",
            ),
        ]
    )
    return (
        audience_filter,
        candidate_df,
        catalog_guideline_df,
        catalog_label_df,
        grammar_filter,
        input_status_df,
        model_filter,
        objective_filter,
        store,
        view_mode,
    )


@app.cell
def _(audience_filter, grammar_filter, model_filter, objective_filter):
    display_filters = {
        "objective": objective_filter.value,
        "audience_bucket": audience_filter.value,
        "model": model_filter.value,
        "grammar": grammar_filter.value,
    }
    display_filters
    return (display_filters,)


@app.cell
def _(
    PAIR_KEY_COLUMNS,
    SCORE_FIELDS,
    apply_optional_filters,
    candidate_df,
    display_filters,
    humanize,
    input_status_df,
    mo,
    pl,
):
    mo.md("## Validation, Coverage, And Pair Completeness")
    duplicate_candidate_rows = (
        candidate_df.group_by(
            "vis_id",
            "objective",
            "audience_bucket",
            "grounding_mode",
            "model",
            "grammar",
        )
        .agg(pl.len().alias("count"))
        .filter(pl.col("count") > 1)
        .height
    )
    gate_results_df = pl.DataFrame(
        [
            {
                "gate": "all_required_artifacts_present",
                "severity": "hard",
                "status": "pass"
                if input_status_df.select(pl.col("exists").all()).item()
                else "fail",
                "value": int(input_status_df.select(pl.col("exists").sum()).item()),
                "detail": "All upstream artifacts required for analysis must exist.",
            },
            {
                "gate": "candidate_rows_are_unique_by_scenario",
                "severity": "hard",
                "status": "pass" if duplicate_candidate_rows == 0 else "fail",
                "value": duplicate_candidate_rows,
                "detail": "Expected at most one candidate per vis/objective/audience/grounding/model/grammar cell.",
            },
            {
                "gate": "judgement_join_coverage",
                "severity": "soft",
                "status": "pass"
                if candidate_df.select(pl.col("has_judgement").mean()).item() == 1
                else "warn",
                "value": float(
                    candidate_df.select(pl.col("has_judgement").mean()).item()
                ),
                "detail": "Candidate cube should retain all generated rows while making missing judgements explicit.",
            },
            {
                "gate": "cohort_join_coverage",
                "severity": "soft",
                "status": "pass"
                if candidate_df.select(pl.col("db_id").is_not_null().mean()).item() == 1
                else "warn",
                "value": float(
                    candidate_df.select(pl.col("db_id").is_not_null().mean()).item()
                ),
                "detail": "Cohort metadata should join back to every candidate row by vis_id.",
            },
            {
                "gate": "empty_judgement_payloads",
                "severity": "soft",
                "status": "pass"
                if candidate_df.filter(pl.col("empty_judgement")).height == 0
                else "warn",
                "value": candidate_df.filter(pl.col("empty_judgement")).height,
                "detail": "Explicitly track rows whose judgement payload is empty JSON.",
            },
        ]
    )
    coverage_df = (
        candidate_df.group_by(
            "objective", "audience_bucket", "grounding_mode", "model", "grammar"
        )
        .agg(
            pl.len().alias("n_candidates"),
            pl.col("has_judgement").sum().alias("judged_candidates"),
            pl.col("complete_score").sum().alias("complete_scores"),
            pl.col("empty_judgement").sum().alias("empty_judgements"),
            pl.col("n_guidelines").mean().alias("mean_guidelines"),
            pl.col("guideline_duplication_count")
            .mean()
            .alias("mean_guideline_duplication"),
            pl.col("trace_density").mean().alias("mean_trace_density"),
        )
        .with_columns(
            judgement_rate=(pl.col("judged_candidates") / pl.col("n_candidates")).round(
                4
            ),
            complete_score_rate=(
                pl.col("complete_scores") / pl.col("n_candidates")
            ).round(4),
        )
        .sort("objective", "audience_bucket", "grounding_mode", "model", "grammar")
    )
    score_long_df = (
        candidate_df.select(
            "visgen_id",
            "vis_id",
            "objective",
            "audience_bucket",
            "grounding_mode",
            "model",
            "grammar",
            "db_id",
            "chart",
            "hardness",
            "task",
            "scope",
            "time_mode",
            *SCORE_FIELDS,
            "overall_score",
        )
        .unpivot(
            index=[
                "visgen_id",
                "vis_id",
                "objective",
                "audience_bucket",
                "grounding_mode",
                "model",
                "grammar",
                "db_id",
                "chart",
                "hardness",
                "task",
                "scope",
                "time_mode",
            ],
            variable_name="dimension",
            value_name="score",
        )
        .with_columns(
            dimension_label=pl.col("dimension").map_elements(
                humanize, return_dtype=pl.String
            )
        )
    )
    pair_meta_df = candidate_df.group_by(PAIR_KEY_COLUMNS).agg(
        query=pl.first("query"),
        db_id=pl.first("db_id"),
        chart=pl.first("chart"),
        hardness=pl.first("hardness"),
        task=pl.first("task"),
        scope=pl.first("scope"),
        time_mode=pl.first("time_mode"),
    )
    score_columns = [*SCORE_FIELDS, "overall_score", "complete_score"]
    none_pair_df = candidate_df.filter(pl.col("grounding_mode") == "none").select(
        *PAIR_KEY_COLUMNS,
        *(pl.col(column).alias(f"none_{column}") for column in score_columns),
    )
    structured_pair_df = candidate_df.filter(
        pl.col("grounding_mode") == "structured"
    ).select(
        *PAIR_KEY_COLUMNS,
        *(pl.col(column).alias(f"structured_{column}") for column in score_columns),
        structured_guideline_ids=pl.col("guideline_ids").list.unique(),
        structured_grounding_trace=pl.col("grounding_trace"),
        structured_n_guidelines=pl.col("n_guidelines"),
        structured_guideline_duplication_count=pl.col("guideline_duplication_count"),
        structured_trace_density=pl.col("trace_density"),
    )
    pair_base_df = (
        pair_meta_df.join(none_pair_df, on=PAIR_KEY_COLUMNS, how="left")
        .join(structured_pair_df, on=PAIR_KEY_COLUMNS, how="left")
        .with_columns(
            has_none=pl.col("none_complete_score").fill_null(False),
            has_structured=pl.col("structured_complete_score").fill_null(False),
            has_complete_pair=pl.col("none_complete_score").fill_null(False)
            & pl.col("structured_complete_score").fill_null(False),
            pair_id=pl.concat_str(PAIR_KEY_COLUMNS, separator="::"),
        )
    )
    pair_completeness_df = (
        pair_base_df.group_by("objective", "audience_bucket", "model", "grammar")
        .agg(
            pl.len().alias("expected_pairs"),
            pl.col("has_none").sum().alias("none_pairs"),
            pl.col("has_structured").sum().alias("structured_pairs"),
            pl.col("has_complete_pair").sum().alias("complete_pairs"),
        )
        .with_columns(
            complete_pair_rate=(
                pl.col("complete_pairs") / pl.col("expected_pairs")
            ).round(4)
        )
        .sort("objective", "audience_bucket", "model", "grammar")
    )
    pair_metric_frames = []
    for dimension in [*SCORE_FIELDS, "overall_score"]:
        pair_metric_frames.append(
            pair_base_df.select(
                *PAIR_KEY_COLUMNS,
                "pair_id",
                "db_id",
                "chart",
                "hardness",
                "task",
                "scope",
                "time_mode",
                "structured_guideline_ids",
                "structured_grounding_trace",
                "structured_n_guidelines",
                "structured_guideline_duplication_count",
                "structured_trace_density",
                pl.lit(dimension).alias("dimension"),
                pl.lit(humanize(dimension)).alias("dimension_label"),
                pl.col(f"none_{dimension}").alias("none_score"),
                pl.col(f"structured_{dimension}").alias("structured_score"),
                pl.col("has_complete_pair"),
            )
        )
    pairwise_delta_df = pl.concat(pair_metric_frames, how="vertical").with_columns(
        delta=pl.col("structured_score") - pl.col("none_score")
    )
    coverage_display_df = apply_optional_filters(coverage_df, display_filters)
    pair_completeness_display_df = apply_optional_filters(
        pair_completeness_df, display_filters
    )
    mo.vstack([gate_results_df, coverage_display_df, pair_completeness_display_df])
    return coverage_df, pair_base_df, pairwise_delta_df, score_long_df


@app.cell
def _(
    apply_optional_filters,
    display_filters,
    fit_clustered_delta_model,
    humanize,
    mo,
    pairwise_delta_df,
    pl,
    score_long_df,
    summarize_delta_groups,
    summarize_macro_from_cells,
    view_mode,
):
    mo.md("## Primary Results: Score Lift, Variance, And Heterogeneity")
    overall_pair_df = pairwise_delta_df.filter(pl.col("dimension") == "overall_score")
    overall_cell_summary_df = summarize_delta_groups(
        overall_pair_df,
        group_cols=["objective", "audience_bucket", "model", "grammar"],
    ).with_columns(
        pooling=pl.lit("cell"),
        dimension=pl.lit("overall_score"),
        dimension_label=pl.lit(humanize("overall_score")),
    )
    overall_micro_summary_df = summarize_delta_groups(
        overall_pair_df, group_cols=["objective", "audience_bucket"]
    ).with_columns(
        pooling=pl.lit("micro"),
        dimension=pl.lit("overall_score"),
        dimension_label=pl.lit(humanize("overall_score")),
        n_cells=pl.lit(None).cast(pl.Int64),
    )
    overall_macro_summary_df = summarize_macro_from_cells(
        overall_cell_summary_df, group_cols=["objective", "audience_bucket"]
    ).with_columns(
        pooling=pl.lit("macro"),
        dimension=pl.lit("overall_score"),
        dimension_label=pl.lit(humanize("overall_score")),
    )
    publication_overall_df = pl.concat(
        [
            overall_cell_summary_df,
            overall_micro_summary_df,
            overall_macro_summary_df,
        ],
        how="diagonal_relaxed",
    ).sort("objective", "audience_bucket", "pooling", "model", "grammar")
    dimension_cell_summary_df = summarize_delta_groups(
        pairwise_delta_df,
        group_cols=[
            "dimension",
            "dimension_label",
            "objective",
            "audience_bucket",
            "model",
            "grammar",
        ],
    ).with_columns(pooling=pl.lit("cell"))
    dimension_micro_summary_df = summarize_delta_groups(
        pairwise_delta_df,
        group_cols=[
            "dimension",
            "dimension_label",
            "objective",
            "audience_bucket",
        ],
    ).with_columns(pooling=pl.lit("micro"), n_cells=pl.lit(None).cast(pl.Int64))
    publication_dimension_df = pl.concat(
        [dimension_cell_summary_df, dimension_micro_summary_df],
        how="diagonal_relaxed",
    ).sort("dimension", "objective", "audience_bucket", "pooling", "model", "grammar")
    summary_df = pl.concat(
        [
            publication_overall_df.with_columns(summary_level=pl.lit("overall")),
            publication_dimension_df.with_columns(summary_level=pl.lit("dimension")),
        ],
        how="diagonal_relaxed",
    )
    scenario_spread_df = (
        score_long_df.filter(pl.col("score").is_not_null())
        .group_by(
            "vis_id",
            "objective",
            "audience_bucket",
            "grounding_mode",
            "dimension",
            "dimension_label",
        )
        .agg(
            pl.len().alias("n_candidates"),
            pl.col("score").std().alias("spread_std"),
            pl.col("score").var().alias("spread_var"),
        )
        .filter(pl.col("n_candidates") > 1)
    )
    scenario_none_df = scenario_spread_df.filter(
        pl.col("grounding_mode") == "none"
    ).select(
        "vis_id",
        "objective",
        "audience_bucket",
        "dimension",
        none_spread=pl.col("spread_std"),
        none_var=pl.col("spread_var"),
    )
    scenario_structured_df = scenario_spread_df.filter(
        pl.col("grounding_mode") == "structured"
    ).select(
        "vis_id",
        "objective",
        "audience_bucket",
        "dimension",
        structured_spread=pl.col("spread_std"),
        structured_var=pl.col("spread_var"),
    )
    scenario_spread_pair_df = scenario_none_df.join(
        scenario_structured_df,
        on=["vis_id", "objective", "audience_bucket", "dimension"],
        how="inner",
    ).with_columns(
        spread_delta=pl.col("structured_spread") - pl.col("none_spread"),
        variance_ratio=pl.when(pl.col("none_var") > 0)
        .then(pl.col("structured_var") / pl.col("none_var"))
        .otherwise(pl.lit(None).cast(pl.Float64)),
        variance_reduction_pct=pl.when(pl.col("none_var") > 0)
        .then(((1 - (pl.col("structured_var") / pl.col("none_var"))) * 100).round(4))
        .otherwise(pl.lit(None).cast(pl.Float64)),
    )
    variance_df = (
        summarize_delta_groups(
            scenario_spread_pair_df,
            group_cols=["dimension", "objective", "audience_bucket"],
            none_col="none_spread",
            structured_col="structured_spread",
            delta_col="spread_delta",
        )
        .join(
            scenario_spread_pair_df.group_by(
                "dimension", "objective", "audience_bucket"
            ).agg(
                variance_ratio_mean=pl.col("variance_ratio").mean(),
                variance_reduction_pct_mean=pl.col("variance_reduction_pct").mean(),
            ),
            on=["dimension", "objective", "audience_bucket"],
            how="left",
        )
        .with_columns(
            variance_kind=pl.lit("scenario_spread"),
            dimension_label=pl.col("dimension").map_elements(
                humanize, return_dtype=pl.String
            ),
        )
    )
    heterogeneity_coef_df, heterogeneity_anova_df, heterogeneity_meta_df = (
        fit_clustered_delta_model(pairwise_delta_df, dimension="overall_score")
    )
    overall_display_df = apply_optional_filters(publication_overall_df, display_filters)
    if view_mode.value == "paper":
        overall_display_df = overall_display_df.filter(pl.col("pooling") != "cell")
    variance_display_df = apply_optional_filters(variance_df, display_filters)
    if view_mode.value == "paper":
        variance_display_df = variance_display_df.filter(
            pl.col("dimension") == "overall_score"
        )
    mo.vstack(
        [
            overall_display_df,
            variance_display_df,
            heterogeneity_meta_df,
            heterogeneity_coef_df,
            heterogeneity_anova_df,
        ]
    )
    return publication_overall_df, summary_df, variance_df


@app.cell
def _(
    ANALYSIS_ARTIFACT_NAMES,
    DIAGNOSTIC_BOOTSTRAP_DRAWS,
    alt,
    apply_optional_filters,
    candidate_df,
    catalog_guideline_df,
    catalog_label_df,
    coverage_df,
    diagnostic_support_threshold,
    display_filters,
    humanize,
    mo,
    pair_base_df,
    pairwise_delta_df,
    pl,
    publication_overall_df,
    score_long_df,
    store,
    summarize_delta_groups,
    summary_df,
    trace_mentions_guideline,
    variance_df,
    view_mode,
):
    mo.md("## Catalog Diagnostics, Publication Visuals, And Persisted Outputs")
    overall_delta_baseline_df = pairwise_delta_df.group_by("dimension").agg(
        baseline_delta_std=pl.col("delta").std()
    )
    diagnostic_support_min = diagnostic_support_threshold(
        pair_base_df.filter(pl.col("has_complete_pair")).height
    )
    pair_guideline_df = (
        pairwise_delta_df.filter(pl.col("has_complete_pair"))
        .select(
            "pair_id",
            "vis_id",
            "objective",
            "audience_bucket",
            "model",
            "grammar",
            "dimension",
            "dimension_label",
            "none_score",
            "structured_score",
            "delta",
            "structured_guideline_ids",
            "structured_grounding_trace",
        )
        .explode("structured_guideline_ids")
        .drop_nulls("structured_guideline_ids")
        .rename({"structured_guideline_ids": "guideline_id"})
        .with_columns(
            trace_hit=pl.struct(
                "guideline_id", "structured_grounding_trace"
            ).map_elements(
                lambda row: trace_mentions_guideline(
                    row["guideline_id"], row["structured_grounding_trace"]
                ),
                return_dtype=pl.Boolean,
            )
        )
        .join(
            catalog_guideline_df.select(
                guideline_id=pl.col("id"), guideline_title=pl.col("title")
            ),
            on="guideline_id",
            how="left",
        )
    )
    guideline_support_df = pair_guideline_df.group_by(
        "guideline_id", "guideline_title", "dimension"
    ).agg(
        support_pairs=pl.n_unique("pair_id"),
        support_vis_ids=pl.n_unique("vis_id"),
        trace_adoption_rate=pl.col("trace_hit").mean(),
    )
    global_trace_adoption_rate = (
        pair_guideline_df.select(pl.col("trace_hit").mean()).item()
        if pair_guideline_df.height
        else None
    )
    guideline_diagnostics_df = (
        summarize_delta_groups(
            pair_guideline_df,
            group_cols=[
                "guideline_id",
                "guideline_title",
                "dimension",
                "dimension_label",
            ],
            bootstrap_draws=DIAGNOSTIC_BOOTSTRAP_DRAWS,
        )
        .join(
            guideline_support_df,
            on=["guideline_id", "guideline_title", "dimension"],
            how="left",
        )
        .join(overall_delta_baseline_df, on="dimension", how="left")
        .with_columns(
            diagnostic_level=pl.lit("guideline"),
            meets_support_threshold=pl.col("support_pairs") >= diagnostic_support_min,
            harmful_stable=(
                (pl.col("support_pairs") >= diagnostic_support_min)
                & pl.col("ci_high").is_not_null()
                & (pl.col("ci_high") < 0)
            ),
            unstable=pl.col("delta_std") > pl.col("baseline_delta_std"),
            low_trace_adoption=pl.when(pl.lit(global_trace_adoption_rate).is_not_null())
            .then(pl.col("trace_adoption_rate") < pl.lit(global_trace_adoption_rate))
            .otherwise(pl.lit(False)),
        )
    )
    pair_label_df = pair_guideline_df.join(
        catalog_label_df, on="guideline_id", how="left"
    ).drop_nulls("label")
    label_diagnostics_df = summarize_delta_groups(
        pair_label_df,
        group_cols=[
            "label_category",
            "label_subcategory",
            "label_key",
            "dimension",
            "dimension_label",
        ],
        bootstrap_draws=DIAGNOSTIC_BOOTSTRAP_DRAWS,
    ).with_columns(diagnostic_level=pl.lit("subcategory"))
    score_chart_source = apply_optional_filters(
        publication_overall_df.filter(pl.col("pooling") == "cell"), display_filters
    ).with_columns(
        cell_label=pl.concat_str(["model", "grammar"], separator=" · "),
        audience_label=pl.col("audience_bucket").map_elements(
            humanize, return_dtype=pl.String
        ),
    )
    if score_chart_source.is_empty():
        score_lift_chart = mo.md(
            "No cell-level score data available for the current filter selection."
        )
    else:
        score_lift_chart = (
            alt.Chart(score_chart_source.to_pandas())
            .mark_bar()
            .encode(
                x=alt.X("cell_label:N", title="Model · Grammar"),
                y=alt.Y("delta_mean:Q", title="Mean grounded - ungrounded score"),
                color=alt.condition(
                    alt.datum.delta_mean >= 0,
                    alt.value("#2e8b57"),
                    alt.value("#c0392b"),
                ),
                tooltip=[
                    "objective",
                    "audience_bucket",
                    "model",
                    "grammar",
                    "n_pairs",
                    "delta_mean",
                    "ci_low",
                    "ci_high",
                ],
                column=alt.Column("objective:N", title="Objective"),
                row=alt.Row("audience_label:N", title="Audience"),
            )
            .properties(width=180, height=110)
        )
    persisted_artifacts = {
        "candidate": candidate_df,
        "score_long": score_long_df,
        "coverage": coverage_df,
        "pair_delta": pairwise_delta_df,
        "summary": summary_df,
        "variance": variance_df,
        "guideline_diagnostics": guideline_diagnostics_df,
        "label_diagnostics": label_diagnostics_df,
    }
    persisted_rows = []
    for artifact_name in ANALYSIS_ARTIFACT_NAMES:
        artifact_df = persisted_artifacts[artifact_name]
        artifact_path = store.write_analysis_artifact_df(artifact_name, artifact_df)
        persisted_rows.append(
            {
                "artifact": artifact_name,
                "path": str(artifact_path),
                "rows": artifact_df.height,
                "columns": len(artifact_df.columns),
            }
        )
    persisted_artifacts_df = pl.DataFrame(persisted_rows).sort("artifact")
    guideline_display_df = apply_optional_filters(
        guideline_diagnostics_df.filter(pl.col("dimension") == "overall_score"),
        display_filters,
    )
    if view_mode.value == "paper":
        guideline_display_df = guideline_display_df.filter(
            pl.col("meets_support_threshold")
        ).select(
            "guideline_id",
            "guideline_title",
            "support_pairs",
            "trace_adoption_rate",
            "delta_mean",
            "ci_low",
            "ci_high",
            "delta_std",
            "harmful_stable",
            "unstable",
        )
    mo.vstack([guideline_display_df.head(25), score_lift_chart, persisted_artifacts_df])
    return


if __name__ == "__main__":
    app.run()
