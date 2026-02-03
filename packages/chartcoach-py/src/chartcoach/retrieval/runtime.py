from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from chartcoach.catalog import Catalog
from chartcoach.index import LanceVectorIndexBackend
from chartcoach.retrieval.strategy.dspy_models import create_lm
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.pipelines.guideline_status import (
    StatusScorer,
    create_status_scorer,
)
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.pipelines.vision import ChartVisionModule
from chartcoach.retrieval.strategy.vector_index import CatalogVectorIndex

if TYPE_CHECKING:
    import dspy
    from chartcoach.index.sparse import CatalogSparseIndex
    from chartcoach.retrieval.config import RetrievalRunConfig
else:
    dspy = require_dspy()


@dataclass(slots=True)
class StrategyRuntime:
    """Run-scoped caches and shared dependencies for retrieval strategies.

    A runtime exists to:
    - eliminate module-level caches (which leak across runs), and
    - share expensive artifacts (indices) across many strategies within a run.
    """

    catalog: Catalog
    run_config: RetrievalRunConfig

    _vector_index: CatalogVectorIndex | None = None
    _abstract_index: CatalogVectorIndex | None = None
    _sparse_index: CatalogSparseIndex | None = None
    _searcher: GuidelineSearcher | None = None
    _abstract_searcher: GuidelineSearcher | None = None

    _vlm: dspy.LM | None = None
    _status_lm: dspy.LM | None = None
    _vision: ChartVisionModule | None = None
    _status_scorer: StatusScorer | None = None

    def new_strategy_lm(self) -> dspy.LM:
        cfg = self.run_config.lms.strategy
        return create_lm(
            model=cfg.model,
            timeout_seconds=cfg.timeout_seconds,
            num_retries=cfg.num_retries,
            temperature=cfg.temperature,
            max_tokens=cfg.max_tokens,
        )

    def _require_vlm(self) -> dspy.LM:
        if self._vlm is not None:
            return self._vlm
        cfg = self.run_config.lms.vlm
        self._vlm = create_lm(
            model=cfg.model,
            timeout_seconds=cfg.timeout_seconds,
            num_retries=cfg.num_retries,
            temperature=cfg.temperature,
            max_tokens=cfg.max_tokens,
        )
        return self._vlm

    def _require_status_lm(self) -> dspy.LM:
        if self._status_lm is not None:
            return self._status_lm
        cfg = self.run_config.lms.guideline_status
        self._status_lm = create_lm(
            model=cfg.model,
            timeout_seconds=cfg.timeout_seconds,
            num_retries=cfg.num_retries,
            temperature=cfg.temperature,
            max_tokens=cfg.max_tokens,
        )
        return self._status_lm

    def vision(self) -> ChartVisionModule | None:
        if not self.run_config.chart_vision.enabled:
            return None
        if self._vision is None:
            self._vision = ChartVisionModule(
                vlm=self._require_vlm(), config=self.run_config.chart_vision
            )
        return self._vision

    def maybe_status_scorer(self) -> StatusScorer | None:
        if not self.run_config.focus.use_status_filter:
            return None
        return self.status_scorer()

    def status_scorer(self) -> StatusScorer:
        if self._status_scorer is None:
            self._status_scorer = create_status_scorer(
                lm=self._require_status_lm(),
                config=self.run_config.status_scorer,
            )
        return self._status_scorer

    def vector_index(self) -> CatalogVectorIndex:
        if self._vector_index is not None:
            return self._vector_index

        from chartcoach.embedding import (
            GuidelineFieldTextSource,
            GuidelineLabelsTextSource,
            SectionsWithTitleTextSource,
        )

        sources = [
            SectionsWithTitleTextSource(),
            GuidelineFieldTextSource("title"),
            GuidelineFieldTextSource("description"),
            GuidelineLabelsTextSource(),
        ]
        self._vector_index = CatalogVectorIndex.from_catalog(
            self.catalog,
            sources=sources,
            config=self.run_config.embedding,
            index_backend=LanceVectorIndexBackend(),
        )
        return self._vector_index

    def abstract_index(self) -> CatalogVectorIndex:
        if self._abstract_index is not None:
            return self._abstract_index

        from chartcoach.embedding import GuidelineAbstractTextSource

        self._abstract_index = CatalogVectorIndex.from_catalog(
            self.catalog,
            sources=[GuidelineAbstractTextSource()],
            config=self.run_config.embedding,
            index_backend=LanceVectorIndexBackend(),
        )
        return self._abstract_index

    def sparse_index(self) -> CatalogSparseIndex:
        if self._sparse_index is not None:
            return self._sparse_index

        from chartcoach.embedding import GuidelineAbstractTextSource
        from chartcoach.index.sparse import CatalogSparseIndex

        self._sparse_index = CatalogSparseIndex.from_catalog(
            self.catalog,
            sources=[GuidelineAbstractTextSource()],
            config=self.run_config.sparse_embedding,
        )
        return self._sparse_index

    def searcher(self) -> GuidelineSearcher:
        if self._searcher is None:
            self._searcher = GuidelineSearcher(
                catalog=self.catalog,
                vector_index=self.vector_index(),
            )
        return self._searcher

    def abstract_searcher(self) -> GuidelineSearcher:
        if self._abstract_searcher is None:
            self._abstract_searcher = GuidelineSearcher(
                catalog=self.catalog,
                vector_index=self.abstract_index(),
            )
        return self._abstract_searcher
