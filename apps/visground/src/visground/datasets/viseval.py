import json
import pathlib
from functools import cached_property
from os import PathLike

import duckdb
import polars as pl

from .paths import VISGROUND_DATA_ROOT

VISEVAL_DATASET_ROOT = VISGROUND_DATA_ROOT / "vis-eval" / "VisEval" / "dataset"


class VisEvalDataset:
    def __init__(
        self,
        dataset_root: str | PathLike[str] = VISEVAL_DATASET_ROOT,
    ):
        self._root = pathlib.Path(dataset_root)

    @property
    def root(self) -> pathlib.Path:
        return self._root

    @cached_property
    def databases(self) -> dict[str, list[str]]:
        path = self._root / "databases" / "db_tables.json"
        return json.loads(path.read_text(encoding="utf-8"))

    @cached_property
    def databases_df(self) -> pl.DataFrame:
        return pl.from_dicts(
            [
                {"db_id": db_id, "tables": tables}
                for db_id, tables in self.databases.items()
            ]
        )

    @cached_property
    def df(self) -> pl.DataFrame:
        return (
            duckdb.query(f"""select * from '{self._root / "visEval.json"}'""")
            .pl()
            .transpose(
                include_header=True,
                header_name="id",
                column_names=["data"],
            )
        )

    @cached_property
    def queries_df(self) -> pl.DataFrame:
        return (
            self.df.unnest("data")
            .explode("nl_queries")
            .rename({"nl_queries": "nl_query"})
        )

    def _table_path(self, db: str, table: str) -> pathlib.Path:
        path = self._root / "databases" / db / f"{table}.csv"
        if not path.exists():
            raise ValueError(f"Table '{table}' does not exist in database '{db}'")
        return path
