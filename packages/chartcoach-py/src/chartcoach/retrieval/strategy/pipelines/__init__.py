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
from .dense_sparse_rrf import DenseSparseRrfStrategy
from .facet_fusion import FacetFusionHybridStrategy
from .hyde import HydeHybridStrategy
from .hybrid import HybridRrfStrategy
from .hybrid_set_select import (
    HybridRrfFacilitySetSelectStrategy,
    HybridRrfLabelSetSelectStrategy,
)
from .label_first_abstract import LabelFirstAbstractStrategy
from .label_gated_ann import LabelGatedAnnStrategy
from .multirepr_fusion import MultiReprFusionStrategy
from .neighborhood_explorer import NeighborhoodExplorerStrategy
from .query_fusion import QueryFusionHybridStrategy
from .role_aware_sections import RoleAwareSectionsStrategy
from .sparse_splade import SparseSpladeStrategy
from .utility_rerank_hybrid import UtilityRerankHybridStrategy

__all__ = [
    "AnnDenseStrategy",
    "AgenticHybridStrategy",
    "Bm25PrfStrategy",
    "DecomposeParallelStrategy",
    "DenseMmrStrategy",
    "DenseSparseRrfStrategy",
    "FacetFusionHybridStrategy",
    "HydeHybridStrategy",
    "HybridRrfStrategy",
    "HybridRrfFacilitySetSelectStrategy",
    "HybridRrfLabelSetSelectStrategy",
    "LabelFirstAbstractStrategy",
    "LabelGatedAnnStrategy",
    "MultiReprFusionStrategy",
    "NeighborhoodExplorerStrategy",
    "QueryFusionHybridStrategy",
    "RoleAwareSectionsStrategy",
    "SparseSpladeStrategy",
    "UtilityRerankHybridStrategy",
]
