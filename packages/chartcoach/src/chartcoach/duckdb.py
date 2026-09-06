from __future__ import annotations

import os
import tempfile
from collections.abc import Mapping
from os import PathLike
from pathlib import Path
from typing import TypeAlias

import duckdb
import polars as pl
from polars.datatypes import DataTypeClass

from .catalog.collection import Catalog
from .catalog.relations import iter_catalog_tables as _iter_catalog_tables

DuckDBConfigValue: TypeAlias = str | bool | int | float | list[str]


def connect_catalog(
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
        _replace_table_from_rows(conn, relation_name, frame)
    return conn


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


def _replace_table_from_rows(
    conn: duckdb.DuckDBPyConnection,
    relation_name: str,
    frame: pl.DataFrame,
) -> None:
    columns = ", ".join(
        f'"{name}" {_duckdb_type(dtype)}' for name, dtype in frame.schema.items()
    )
    conn.execute(f'create or replace table "{relation_name}" ({columns})')
    if frame.is_empty():
        return
    placeholders = ", ".join("?" for _ in frame.columns)
    conn.executemany(
        f'insert into "{relation_name}" values ({placeholders})',
        frame.iter_rows(),
    )


def _duckdb_type(dtype: DataTypeClass | pl.DataType) -> str:
    if dtype == pl.String:
        return "VARCHAR"
    if isinstance(dtype, pl.List):
        return f"{_duckdb_type(dtype.inner)}[]"
    if isinstance(dtype, pl.Struct):
        fields = ", ".join(
            f'"{field.name}" {_duckdb_type(field.dtype)}' for field in dtype.fields
        )
        return f"STRUCT({fields})"
    raise TypeError(f"Unsupported catalog DuckDB type: {dtype}")


__all__ = [
    "DuckDBConfigValue",
    "connect_catalog",
    "register_catalog",
    "write_duckdb",
]
