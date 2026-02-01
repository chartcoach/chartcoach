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
from .bm25 import Bm25PrfStrategy, Bm25PrfStrategyV2
from .dense import DenseMmrStrategy, DenseMmrStrategyV2
from .heuristic_fusion import HeuristicFusionHybridStrategyV2
from .hyde import HydeHybridStrategy, HydeHybridStrategyV2
from .hybrid import HybridRrfStrategy, HybridRrfStrategyV2
from .query_fusion import QueryFusionHybridStrategy, QueryFusionHybridStrategyV2

__all__ = [
    "AgenticHybridStrategy",
    "Bm25PrfStrategy",
    "Bm25PrfStrategyV2",
    "DenseMmrStrategy",
    "DenseMmrStrategyV2",
    "HeuristicFusionHybridStrategyV2",
    "HydeHybridStrategy",
    "HydeHybridStrategyV2",
    "HybridRrfStrategy",
    "HybridRrfStrategyV2",
    "QueryFusionHybridStrategy",
    "QueryFusionHybridStrategyV2",
]
