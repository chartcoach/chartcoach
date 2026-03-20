from __future__ import annotations

import marimo

__generated_with = "0.21.1"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # SQL Non-Determinism Fixes
    """)
    return


@app.cell(hide_code=True)
def _(discover_nondeterministic_queries):
    items_with_nondeterministic_queries = discover_nondeterministic_queries()
    items_with_nondeterministic_queries
    return


@app.cell(hide_code=True)
def _(pl, viseval_dataset):
    def discover_nondeterministic_queries(k: int = 10) -> list[str]:
        ids = []
        for id in viseval_dataset.df["id"]:
            results = []
            for _ in range(10):
                df = viseval_dataset.vis_relation(id).pl()
                df = df.sort(df.columns)
                results.append(df)

            if not items_equal(results):
                ids.append(id)

        return ids

    def items_equal(dfs: list[pl.DataFrame]) -> bool:
        if not dfs:
            return True

        first = dfs[0]
        return all(first.equals(df) for df in dfs[1:])

    return (discover_nondeterministic_queries,)


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    # SQL Execution Fixes
    """)
    return


@app.cell(hide_code=True)
def _(attempt, viseval_dataset):
    sql_exec_errors = [
        {"id": id, "error": vis_relation_result}
        for id in viseval_dataset.df["id"]
        if (
            vis_relation_result := attempt(
                lambda id: viseval_dataset.vis_relation(id).df(),
                id,
            )
        ).is_err()
    ]
    sql_exec_errors
    return (sql_exec_errors,)


@app.cell(hide_code=True)
def _(apply_sql_fixes, generate_sql_fixes, sql_exec_errors):
    sql_fixmap = generate_sql_fixes(sql_exec_errors)
    apply_sql_fixes(sql_fixmap)
    return


@app.cell(hide_code=True)
def _(
    Err,
    SQLFixer,
    dspy,
    json,
    pathlib,
    sql_exec_error_to_input,
    sql_fixer_reward_fn,
    viseval_dataset,
):
    base_sql_fixer = dspy.Predict(SQLFixer)
    sql_fixer = dspy.Refine(
        module=base_sql_fixer,
        N=3,
        reward_fn=sql_fixer_reward_fn,
        threshold=1.0,
    )

    def generate_sql_fixes(sql_exec_errors: list[Err]) -> dict[str, str]:
        if len(sql_exec_errors) == 0:
            return {}

        parallel = dspy.Parallel(num_threads=8)
        fixes = parallel(
            [
                (sql_fixer, sql_exec_error_to_input(sql_exec_error))
                for sql_exec_error in sql_exec_errors
            ]
        )
        return {
            sql_exec_error["id"]: fix.fixed_query
            for sql_exec_error, fix in zip(sql_exec_errors, fixes)
        }

    def apply_sql_fixes(sql_fixmap: dict[str, str]):
        # Patch dataset
        fixed = viseval_dataset.raw
        for id, sql_fix in sql_fixmap.items():
            fixed[id]["vis_query"]["data_part"]["sql_part"] = sql_fix

        # Write patches
        pathlib.Path(viseval_dataset.root / "visEval.json").write_text(
            json.dumps(fixed, indent=4)
        )

    return apply_sql_fixes, generate_sql_fixes


@app.cell(hide_code=True)
def _(dspy):
    class SQLFixer(dspy.Signature):
        """
        You must fix the incorrect SQL query, considering the error it threw and the tables available in the database.
        Ensure that you make absolutely minimal diff to the original incorrect_query. No need to reformat.
        """

        id: str = dspy.InputField()
        incorrect_query: str = dspy.InputField(desc="The incorrect query to fix")
        error: str = dspy.InputField(
            desc="The DuckDB error caught on execution attempt",
        )
        table_schemas: dict[str, list[dict]] = dspy.InputField(
            desc="The schema of all tables available in the queried database",
        )

        fixed_query: str = dspy.OutputField(desc="The fixed query")

    return (SQLFixer,)


@app.cell(hide_code=True)
def _(attempt, dspy, find_db_id_by_vis_id, viseval_dataset):
    def sql_fixer_reward_fn(args: dict, pred: dspy.Prediction) -> float:
        vis_id = args["id"]
        db_id = find_db_id_by_vis_id(vis_id)
        conn = viseval_dataset.database(db_id)
        result = attempt(conn.query, pred.fixed_query)

        # Only perfection is acceptable outcome
        if result.is_ok():
            return 1.0

        return 0.0

    return (sql_fixer_reward_fn,)


@app.cell(hide_code=True)
def _(Err, dspy, find_db_id_by_vis_id, find_sql_by_vis_id, viseval_dataset):
    def sql_exec_error_to_input(sql_exec_error: Err) -> dspy.Example:
        vis_id = sql_exec_error["id"]
        db_id = find_db_id_by_vis_id(vis_id)
        tables = viseval_dataset.databases[db_id]
        conn = viseval_dataset.database(db_id)
        table_schemas = {
            table: conn.query(f'describe table "{table}"')
            .pl()
            .select("column_name", "column_type")
            .to_dicts()
            for table in tables
        }

        return dspy.Example(
            id=vis_id,
            incorrect_query=find_sql_by_vis_id(vis_id),
            error=sql_exec_error["error"].error,
            table_schemas=table_schemas,
        ).with_inputs(
            "id",
            "incorrect_query",
            "error",
            "table_schemas",
        )

    return (sql_exec_error_to_input,)


@app.cell(hide_code=True)
def _(pl, viseval_dataset):
    def find_db_id_by_vis_id(vis_id: str) -> str:
        return (
            viseval_dataset.df.filter(id=vis_id)
            .select(pl.col("data").struct.field("db_id"))
            .row(0)[0]
        )

    def find_sql_by_vis_id(vis_id: str) -> str:
        return (
            viseval_dataset.df.filter(id=vis_id)
            .select(
                pl.col("data")
                .struct.field("vis_query")
                .struct.field("data_part")
                .struct.field("sql_part")
            )
            .row(0)[0]
        )

    return find_db_id_by_vis_id, find_sql_by_vis_id


@app.cell(hide_code=True)
def _():
    import json
    import pathlib

    return json, pathlib


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    # Database Fixes
    """)
    return


@app.cell(hide_code=True)
def _(attempt, viseval_dataset):
    db_setup_errors = [
        {"db_id": db_id, "error": database_result}
        for db_id in viseval_dataset.databases
        if (database_result := attempt(viseval_dataset.database, db_id)).is_err()
    ]
    db_setup_errors
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    # VisEval Dataset
    """)
    return


@app.cell(hide_code=True)
def _(VisEvalDataset):
    # viseval_dataset = VisEvalDataset("./apps/visground/nogit/visEval_dataset")
    viseval_dataset = VisEvalDataset()
    return (viseval_dataset,)


@app.cell(hide_code=True)
def _():
    from dataclasses import dataclass
    from typing import Callable, Generic, ParamSpec, TypeVar

    T = TypeVar("T")
    E = TypeVar("E", bound=BaseException)
    P = ParamSpec("P")

    class Result(Generic[T, E]):
        def is_ok(self) -> bool:
            return isinstance(self, Ok)

        def is_err(self) -> bool:
            return isinstance(self, Err)

    @dataclass(frozen=True)
    class Ok(Result[T, E]):
        value: T

    @dataclass(frozen=True)
    class Err(Result[T, E]):
        error: E

    def attempt(
        fn: Callable[P, T], *args: P.args, **kwargs: P.kwargs
    ) -> Result[T, Exception]:
        try:
            return Ok(fn(*args, **kwargs))
        except Exception as exc:
            return Err(exc)

    return Err, attempt


@app.cell(hide_code=True)
def _():
    import dspy

    dspy.configure_cache(
        enable_disk_cache=True,
        enable_memory_cache=True,
    )

    def lm(model: str) -> dspy.LM:
        return dspy.LM(
            f"openai/{model}",
            api_base="http://localhost:8317/v1",
            api_key="sk-",
        )

    dspy.configure(
        lm=lm("gpt-5.4"),
        track_usage=True,
    )
    return (dspy,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl
    from visground.datasets import VisEvalDataset

    return VisEvalDataset, mo, pl


if __name__ == "__main__":
    app.run()
