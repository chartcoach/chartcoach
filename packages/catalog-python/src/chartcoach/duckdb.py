from __future__ import annotations

import os
from os import PathLike
from pathlib import Path
import tempfile
from typing import Any

import polars as pl

from .catalog.collection import Catalog
from .catalog.relations import (
    FORMATTED_REFERENCES_RELATION,
    GUIDELINES_RELATION,
    GUIDELINE_LABELS_RELATION,
    GUIDELINE_REFERENCES_RELATION,
    LABELS_RELATION,
    REFERENCES_RELATION,
    SECTIONS_RELATION,
    iter_catalog_tables,
)


def register_catalog(conn: Any, catalog: Catalog) -> None:
    """Create or replace catalog tables in a caller-owned DuckDB connection."""

    for relation_name, frame in iter_catalog_tables(catalog):
        _replace_table(conn, relation_name, frame)


def write_duckdb(
    catalog: Catalog,
    output_path: str | PathLike[str],
    *,
    overwrite: bool = False,
) -> Path:
    """Write catalog tables into a DuckDB database file."""

    path = Path(output_path)
    if path.exists():
        if not overwrite:
            raise FileExistsError(f"{path} already exists. Pass overwrite=True.")
    path.parent.mkdir(parents=True, exist_ok=True)

    duckdb = _load_duckdb()
    fd, raw_temp_path = tempfile.mkstemp(
        prefix=f".{path.name}-",
        suffix=".duckdb",
        dir=path.parent,
    )
    os.close(fd)
    temp_path = Path(raw_temp_path)
    temp_path.unlink()

    try:
        conn = duckdb.connect(temp_path)
        try:
            register_catalog(conn, catalog)
        finally:
            conn.close()
        temp_path.replace(path)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise
    return path


def _load_duckdb() -> Any:
    try:
        import duckdb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "DuckDB catalog artifacts require the optional `chartcoach[duckdb]` dependencies."
        ) from exc
    return duckdb


def _replace_table(conn: Any, relation_name: str, frame: pl.DataFrame) -> None:
    source_relation = f"{relation_name}_source"
    conn.register(source_relation, frame)
    try:
        conn.execute(
            f'create or replace table "{relation_name}" as '
            f'(select * from "{source_relation}")'
        )
    finally:
        conn.unregister(source_relation)


__all__ = [
    "FORMATTED_REFERENCES_RELATION",
    "GUIDELINES_RELATION",
    "GUIDELINE_LABELS_RELATION",
    "GUIDELINE_REFERENCES_RELATION",
    "LABELS_RELATION",
    "REFERENCES_RELATION",
    "SECTIONS_RELATION",
    "iter_catalog_tables",
    "register_catalog",
    "write_duckdb",
]
