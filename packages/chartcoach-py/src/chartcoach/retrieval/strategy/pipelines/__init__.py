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

from .ann_dense import AnnDenseStrategy
from .agentic_hybrid import AgenticHybridStrategy
from .bm25 import Bm25PrfStrategy
from .decompose_parallel import DecomposeParallelStrategy
from .dense import DenseMmrStrategy
from .facet_fusion import FacetFusionHybridStrategy
from .hyde import HydeHybridStrategy
from .hybrid import HybridRrfStrategy
from .label_first_abstract import LabelFirstAbstractStrategy
from .label_gated_ann import LabelGatedAnnStrategy
from .neighborhood_explorer import NeighborhoodExplorerStrategy
from .query_fusion import QueryFusionHybridStrategy
from .role_aware_sections import RoleAwareSectionsStrategy

__all__ = [
    "AnnDenseStrategy",
    "AgenticHybridStrategy",
    "Bm25PrfStrategy",
    "DecomposeParallelStrategy",
    "DenseMmrStrategy",
    "FacetFusionHybridStrategy",
    "HydeHybridStrategy",
    "HybridRrfStrategy",
    "LabelFirstAbstractStrategy",
    "LabelGatedAnnStrategy",
    "NeighborhoodExplorerStrategy",
    "QueryFusionHybridStrategy",
    "RoleAwareSectionsStrategy",
]
