import pathlib
from functools import cached_property
from os import PathLike

import polars as pl

from .paths import VISGROUND_DATA_ROOT

VISJUDGEBENCH_DATASET_ROOT = VISGROUND_DATA_ROOT / "vis-judge-bench" / "VisJudgeBench"


class VisJudgeBenchDataset:
    def __init__(
        self,
        dataset_root: str | PathLike[str] = VISJUDGEBENCH_DATASET_ROOT,
    ):
        self._root = pathlib.Path(dataset_root)

    @cached_property
    def df(self) -> pl.DataFrame:
        return pl.read_ndjson(self._root / "VisJudgeBench.json").with_columns(
            chart_description=pl.col("prompt")
            .str.split(
                "Chart description: ",
                literal=True,
            )
            .list.get(-1)
            .str.split("\n")
            .list.get(0),
        )
