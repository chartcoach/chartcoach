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
from .bm25 import Bm25PrfStrategy
from .dense import DenseMmrStrategy
from .hyde import HydeHybridStrategy
from .hybrid import HybridRrfStrategy
from .query_fusion import QueryFusionHybridStrategy

__all__ = [
    "AgenticHybridStrategy",
    "Bm25PrfStrategy",
    "DenseMmrStrategy",
    "HydeHybridStrategy",
    "HybridRrfStrategy",
    "QueryFusionHybridStrategy",
]
