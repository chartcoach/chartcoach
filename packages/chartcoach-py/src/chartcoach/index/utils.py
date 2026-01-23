from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np
import polars as pl

from chartcoach.embedding.vectors import vector_matrix


def cache_root() -> Path:
    """Return the cache root used by chartcoach.

    This is intentionally independent of any embedding backend. Tests can override
    via `CHARTCOACH_CACHE_DIR`.
    """

    override = os.getenv("CHARTCOACH_CACHE_DIR")
    if override:
        return Path(override)

    home = Path.home()
    if sys.platform == "darwin":
        return home / "Library" / "Caches" / "chartcoach"

    xdg = os.getenv("XDG_CACHE_HOME")
    if xdg:
        return Path(xdg) / "chartcoach"

    if os.name == "nt":
        local = os.getenv("LOCALAPPDATA")
        if local:
            return Path(local) / "chartcoach" / "Cache"
        return home / "AppData" / "Local" / "chartcoach" / "Cache"

    return home / ".cache" / "chartcoach"


def cache_path(name: str) -> Path:
    return cache_root() / name


def default_indices_root() -> Path:
    return cache_path("indices")


def _hash_bytes(*chunks: bytes) -> str:
    h = hashlib.sha256()
    for chunk in chunks:
        h.update(chunk)
    return h.hexdigest()


def hash_vectors_for_index(
    embedded_text_df: pl.DataFrame,
    *,
    embedding_column: str,
    version: int,
    extra: dict[str, object] | None = None,
) -> tuple[str, np.ndarray]:
    vectors = vector_matrix(embedded_text_df.get_column(embedding_column))
    vectors_digest = _hash_bytes(
        str(vectors.shape).encode(),
        str(vectors.dtype).encode(),
        vectors.tobytes(order="C"),
    )
    payload = {
        "version": version,
        "vectors": {
            "shape": vectors.shape,
            "dtype": str(vectors.dtype),
            "sha256": vectors_digest,
        },
        "extra": {} if extra is None else extra,
    }
    digest = _hash_bytes(json.dumps(payload, sort_keys=True, default=str).encode())
    return digest, vectors

