import json
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

import dspy
import PIL.Image

from visground.datasets.viseval import VisEvalDataset
from visground.generation.models import VisualizationRequestRecord
from visground.generation.utils import (
    describe_dataframe,
    normalize_df,
    pyexecute,
)
from visground.utils import unfence

T = TypeVar("T")


class VisualizationBackend(ABC, Generic[T]):
    """Backend contract for DSPy example building and visualization materialization."""

    dataset: VisEvalDataset

    def __init__(self, dataset: VisEvalDataset) -> None:
        self.dataset = dataset

    @abstractmethod
    def build_requirements(self, req: VisualizationRequestRecord) -> list[str]:
        raise NotImplementedError()

    def build_example(
        self,
        req: VisualizationRequestRecord,
    ) -> dspy.Example:
        rel = self.dataset.vis_relation(req["id"])
        df = normalize_df(rel.pl())
        tablespec_dict = describe_dataframe(df)
        requirements = [
            *self.build_requirements(req),
        ]
        if req["requirements"]:
            requirements.extend(
                [
                    "**Design Guidance**",
                    *req["requirements"],
                ]
            )

        return dspy.Example(
            id=req["id"],
            query=req["query"],
            tablespec=json.dumps(
                tablespec_dict,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            ),
            requirements=requirements,
        ).with_inputs(
            "id",
            "query",
            "tablespec",
            "requirements",
        )

    def materialize_visualization(self, id: str, code: str) -> T:
        code = unfence(code)[0]
        rel = self.dataset.vis_relation(id)

        # This fixes altair render errors when column would be called `sum(x)` or similar
        df = normalize_df(rel.pl()).to_pandas()
        result = pyexecute(
            code,
            context={
                "df": df,
                "plot_df": df,
            },
            result_name="chart",
        )

        return cast(T, result)

    @abstractmethod
    def rasterize(self, chart: T) -> PIL.Image.Image:
        raise NotImplementedError()
