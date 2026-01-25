from __future__ import annotations

import inspect
from typing import Any, ClassVar

import dspy
from pydantic import BaseModel, ConfigDict

from chartcoach.catalog import Catalog
from chartcoach.retrieval.types import RetrievalRequest, RetrievalResponse


class StrategyInfo(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    name: str
    description: str


class RetrievalStrategy(dspy.Module):
    id: ClassVar[str] = "retrieval@base"

    def __init__(self, catalog: Catalog, /, **_: Any) -> None:
        super().__init__()
        self._catalog = catalog

    @classmethod
    def info(cls) -> StrategyInfo:
        doc = inspect.getdoc(cls) or ""
        return StrategyInfo(
            id=cls.id,
            name=cls.__name__,
            description=doc.splitlines()[0] if doc else "",
        )

    @property
    def catalog(self) -> Catalog:
        return self._catalog

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        raise NotImplementedError

    def forward(self, request: RetrievalRequest) -> RetrievalResponse:
        return self._forward(request)
