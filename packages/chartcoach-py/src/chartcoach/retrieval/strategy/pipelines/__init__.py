"""High-quality retrieval pipelines for guideline discovery.

These strategies are intended as *competitive* baselines across families:
- lexical (BM25/FTS) + PRF expansion
- dense (bi-encoder vector search) + MMR diversity
- hybrid (lexical + dense) + rank fusion
- query fusion / multi-query
- HyDE pseudo-document retrieval
- agentic tool-using retrieval
"""

from __future__ import annotations

from .agentic_hybrid import AgenticHybridStrategy
from .bm25 import Bm25PrfStrategy, Bm25PrfStrategyV2, Bm25PrfStrategyV3, Bm25PrfStrategyV4
from .dense import DenseMmrStrategy, DenseMmrStrategyV2, DenseMmrStrategyV3, DenseMmrStrategyV4
from .heuristic_fusion import (
    HeuristicFusionHybridStrategyV2,
    HeuristicFusionHybridStrategyV3,
    HeuristicFusionHybridStrategyV4,
    HeuristicFusionHybridStrategyV5,
)
from .hyde import HydeHybridStrategy, HydeHybridStrategyV2, HydeHybridStrategyV3, HydeHybridStrategyV4
from .hybrid import (
    HybridRrfStrategy,
    HybridRrfStrategyV2,
    HybridRrfStrategyV3,
    HybridRrfStrategyV4,
    HybridRrfStrategyV5,
)
from .query_fusion import (
    QueryFusionHybridStrategy,
    QueryFusionHybridStrategyV2,
    QueryFusionHybridStrategyV3,
    QueryFusionHybridStrategyV4,
)

__all__ = [
    "AgenticHybridStrategy",
    "Bm25PrfStrategy",
    "Bm25PrfStrategyV2",
    "Bm25PrfStrategyV3",
    "Bm25PrfStrategyV4",
    "DenseMmrStrategy",
    "DenseMmrStrategyV2",
    "DenseMmrStrategyV3",
    "DenseMmrStrategyV4",
    "HeuristicFusionHybridStrategyV2",
    "HeuristicFusionHybridStrategyV3",
    "HeuristicFusionHybridStrategyV4",
    "HeuristicFusionHybridStrategyV5",
    "HydeHybridStrategy",
    "HydeHybridStrategyV2",
    "HydeHybridStrategyV3",
    "HydeHybridStrategyV4",
    "HybridRrfStrategy",
    "HybridRrfStrategyV2",
    "HybridRrfStrategyV3",
    "HybridRrfStrategyV4",
    "HybridRrfStrategyV5",
    "QueryFusionHybridStrategy",
    "QueryFusionHybridStrategyV2",
    "QueryFusionHybridStrategyV3",
    "QueryFusionHybridStrategyV4",
]
