from __future__ import annotations

import logging
import pathlib

import chromadb
import duckdb
from chromadb.api import ClientAPI

logger = logging.getLogger(__name__)


def create_chroma_client(
    path: str | pathlib.Path,
) -> ClientAPI:
    """Create a persistent Chroma client at the given path."""
    chroma_path = pathlib.Path(path)
    logger.debug("Opening Chroma persistent client at %s", chroma_path)
    return chromadb.PersistentClient(chroma_path)


def create_duckdb_conn(
    path: str | pathlib.Path,
    *,
    read_only: bool = False,
) -> duckdb.DuckDBPyConnection:
    """Create a DuckDB connection at the given path."""
    duckdb_path = pathlib.Path(path)
    logger.debug(
        "Opening DuckDB connection at %s (read_only=%s)",
        duckdb_path,
        read_only,
    )
    return duckdb.connect(duckdb_path, read_only=read_only)


__all__ = ["create_chroma_client", "create_duckdb_conn"]
