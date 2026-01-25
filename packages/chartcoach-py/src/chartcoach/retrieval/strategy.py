from __future__ import annotations

from typing import Any, ClassVar

import dspy

from chartcoach.catalog import Catalog
from chartcoach.retrieval.types import RetrievalRequest, RetrievalResponse


class RetrievalStrategy(dspy.Module):
    id: ClassVar[str] = "retrieval@base"

    def __init__(self, catalog: Catalog, /, **_: Any) -> None:
        super().__init__()
        self._catalog = catalog

    @property
    def catalog(self) -> Catalog:
        return self._catalog

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        raise NotImplementedError

    def forward(self, request: RetrievalRequest) -> RetrievalResponse:
        return self._forward(request)
