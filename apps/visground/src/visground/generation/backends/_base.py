import json
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

import dspy
import PIL.Image

from visground.datasets.viseval import VisEvalDataset
from visground.generation.models import VisualizationRequestRecord
from visground.generation.utils import describe_dataframe, pyexecute
from visground.utils import unfence

T = TypeVar("T")


class VisualizationBackend(ABC, Generic[T]):
    """Backend contract for DSPy example building and visualization materialization."""

    dataset: VisEvalDataset

    def __init__(self, dataset: VisEvalDataset) -> None:
        self.dataset = dataset

    @abstractmethod
    def build_requirements(self, req: VisualizationRequestRecord) -> list[str]:
        """List of requirements the generator LLM should follow"""
        raise NotImplementedError()

    def build_example(
        self,
        req: VisualizationRequestRecord,
    ) -> dspy.Example:
        """Convert a structured request into a backend-specific DSPy example."""
        rel = self.dataset.vis_relation(req["id"])
        df = rel.pl()
        tablespec_dict = describe_dataframe(df)
        return dspy.Example(
            id=req["id"],
            query=req["query"],
            tablespec=json.dumps(
                tablespec_dict,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            ),
            requirements=self.build_requirements(req),
        ).with_inputs(
            "id",
            "query",
            "tablespec",
            "requirements",
        )

    def materialize_visualization(self, id: str, code: str) -> T:
        """Execute generated code and return the backend-specific visualization object."""
        code = unfence(code)[0]
        rel = self.dataset.vis_relation(id)
        df = rel.to_df()
        result = pyexecute(
            code,
            context={"df": df},
            result_name="chart",
        )

        return cast(T, result)

    @abstractmethod
    def rasterize(self, chart: T) -> PIL.Image.Image:
        """Convert the backend-specific visualization object into a raster image."""
        raise NotImplementedError()
