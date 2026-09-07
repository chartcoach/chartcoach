from __future__ import annotations

import os
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from typing import TypeAlias
from uuid import uuid4

import duckdb
import polars as pl

from ._catalog.model import Catalog
from ._catalog.relations import iter_catalog_tables as _iter_catalog_tables

DuckDBConfigValue: TypeAlias = str | bool | int | float | list[str]


def _connect_catalog(
    catalog: Catalog,
    *,
    config: Mapping[str, DuckDBConfigValue] | None = None,
) -> duckdb.DuckDBPyConnection:
    """Return an in-memory DuckDB connection with catalog tables registered."""

    conn = duckdb.connect(":memory:", config=dict(config or {}))
    try:
        register_catalog(conn, catalog)
    except Exception:
        conn.close()
        raise
    return conn


def register_catalog(
    conn: duckdb.DuckDBPyConnection,
    catalog: Catalog,
) -> duckdb.DuckDBPyConnection:
    """Create or replace catalog tables in a caller-owned DuckDB connection."""

    for relation_name, frame in _iter_catalog_tables(catalog):
        _replace_table(conn, relation_name, frame)
    return conn


def write_duckdb(
    catalog: Catalog,
    output_path: str | PathLike[str],
    *,
    overwrite: bool = False,
) -> Path:
    """Write catalog tables into a DuckDB database file."""

    path = Path(output_path)
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists. Pass overwrite=True.")
    path.parent.mkdir(parents=True, exist_ok=True)

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


@dataclass(frozen=True, slots=True)
class _ArrowStream:
    # Expose the Arrow protocol directly so DuckDB does not route Polars
    # objects through its optional PyArrow integration.
    frame: pl.DataFrame

    def __arrow_c_stream__(self, requested_schema: object | None = None) -> object:
        return self.frame.__arrow_c_stream__(requested_schema)


def _replace_table(
    conn: duckdb.DuckDBPyConnection,
    relation_name: str,
    frame: pl.DataFrame,
) -> None:
    source = f"_chartcoach_{uuid4().hex}"
    conn.register(source, _ArrowStream(frame))
    try:
        conn.execute(
            f'create or replace table "{relation_name}" as select * from "{source}"'
        )
    finally:
        conn.unregister(source)


__all__ = [
    "DuckDBConfigValue",
    "register_catalog",
    "write_duckdb",
]
