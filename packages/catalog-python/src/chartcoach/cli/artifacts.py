from __future__ import annotations

from pathlib import Path

import click

from chartcoach.artifacts import catalog_artifact_rows

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    duckdb_option,
    emit_rows,
    index_dir_option,
    load_catalog,
    source_option,
    source_path,
)


@click.command("artifacts", context_settings=CONTEXT_SETTINGS)
@source_option
@index_dir_option
@duckdb_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def artifacts_command(
    ctx: click.Context,
    index_dir: Path | None,
    duckdb_path: Path | None,
    output_format: str,
) -> None:
    """List catalog, DuckDB, and LanceDB artifact paths."""

    catalog = load_catalog(ctx)
    rows = catalog_artifact_rows(
        catalog,
        source_path=source_path(ctx),
        index_dir=index_dir,
        duckdb_path=duckdb_path,
    )
    emit_rows(rows, output_format=output_format)


__all__ = ["artifacts_command"]
