import json
import pathlib
from functools import cached_property
from os import PathLike
from typing import Sequence

import duckdb
import polars as pl

from ..data_profile import compact_profile, interestingness_score, profile_dataframe
from .paths import VISGROUND_DATA_ROOT

VISEVAL_DATASET_ROOT = VISGROUND_DATA_ROOT / "vis-eval" / "VisEval" / "dataset"
VISEVAL_ENRICHMENT_ROOT = VISGROUND_DATA_ROOT / "vis-eval" / "enrichment"


class VisEvalDataset:
    def __init__(
        self,
        dataset_root: str | PathLike[str] = VISEVAL_DATASET_ROOT,
        enrichment_root: str | PathLike[str] = VISEVAL_ENRICHMENT_ROOT,
    ):
        self._root = pathlib.Path(dataset_root)
        self._enrichment_root = pathlib.Path(enrichment_root)
        self._db_connections: dict[str, duckdb.DuckDBPyConnection] = {}
        self._profile_cache: dict[str, dict] = {}

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
        ).sort("db_id")

    @cached_property
    def raw(self) -> dict[str, dict]:
        return json.loads((self._root / "visEval.json").read_text(encoding="utf-8"))

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

    @cached_property
    def queries_enriched_df(self) -> pl.DataFrame:
        enrichment_columns = self.vis_tasks_df.columns
        return (
            self.queries_df.join(
                self.nl_query_canonical_df,
                on="nl_query",
                how="left",
            )
            .join(
                self.vis_tasks_df,
                on="nl_query_canonical",
                how="left",
            )
            .select(
                pl.exclude(enrichment_columns),
                enrichment=pl.struct(enrichment_columns),
            )
        )

    @cached_property
    def nl_query_canonical_df(self) -> pl.DataFrame:
        filepath = self._get_enrichment_path("nl_query_canonical.json")
        return pl.read_json(filepath)

    @cached_property
    def vis_tasks_df(self) -> pl.DataFrame:
        filepath = self._get_enrichment_path("vis_tasks.json")
        return pl.read_json(filepath)

    def _get_enrichment_path(self, filename: str) -> pathlib.Path:
        filepath = self._enrichment_root / filename
        if not filepath.exists():
            raise ValueError(f"File '{filepath}' does not exist")
        return filepath

    def _table_path(self, db: str, table: str) -> pathlib.Path:
        path = self._root / "databases" / db / f"{table}.csv"
        if not path.exists():
            raise ValueError(f"Table '{table}' does not exist in database '{db}'")
        return path

    def database(self, db_id: str) -> duckdb.DuckDBPyConnection:
        if db_id in self._db_connections:
            return self._db_connections[db_id]

        conn = duckdb.connect()
        tables = self.databases.get(db_id, [])
        stmts = [
            f"""CREATE TABLE IF NOT EXISTS "{table}" AS SELECT * FROM read_csv('{self._root / "databases" / db_id / f"{table}.csv"}', sample_size = -1);"""
            for table in tables
        ]
        conn.execute("\n".join(stmts))
        self._db_connections[db_id] = conn

        return conn

    def vis_relation(self, id: str) -> duckdb.DuckDBPyRelation:
        matched_df = self.df.filter(id=id)
        if matched_df.is_empty():
            raise ValueError(f"No chart found for id '{id}'")

        id, data = matched_df.row(0)
        db_id = data["db_id"]
        sql = data["vis_query"]["data_part"]["sql_part"]

        db = self.database(db_id)

        return db.query(sql)

    def profile(
        self,
        vis_id: str,
        *,
        compact: bool = True,
        use_cache: bool = True,
    ) -> dict:
        if use_cache and vis_id in self._profile_cache:
            return dict(self._profile_cache[vis_id])

        profile = profile_dataframe(self.vis_relation(vis_id).pl())
        payload = {
            "id": vis_id,
            "interestingness_score": interestingness_score(profile),
            "data_profile": compact_profile(profile) if compact else profile,
        }
        if use_cache:
            self._profile_cache[vis_id] = payload
        return dict(payload)

    def profiles_df(
        self,
        vis_ids: Sequence[str],
        *,
        compact: bool = True,
        use_cache: bool = True,
    ) -> pl.DataFrame:
        return pl.from_dicts(
            [
                self.profile(
                    vis_id,
                    compact=compact,
                    use_cache=use_cache,
                )
                for vis_id in vis_ids
            ]
        )
