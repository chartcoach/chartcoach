"""Retrieval use-cases (strategy execution, eval artifacts).

This layer is framework-agnostic and should be unit-testable with dependency
injection. CLI and FastAPI live in `chartcoach.retrieval.cli` and
`chartcoach.retrieval.server`.
"""

from __future__ import annotations

from .artifact_store import create_store, default_artifacts_url, normalize_prefix
from .eval_artifacts import EvalArtifactsService
from .retrieval_service import RetrievalService

__all__ = [
    "EvalArtifactsService",
    "RetrievalService",
    "create_store",
    "default_artifacts_url",
    "normalize_prefix",
]
