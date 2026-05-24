from __future__ import annotations

from pathlib import Path

import click

from chartcoach.catalog import Catalog

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    emit_rows,
    load_catalog,
    source_option,
)


@click.group(
    "catalog",
    context_settings=CONTEXT_SETTINGS,
    help="Build and validate catalog artifacts.",
)
def catalog_command() -> None:
    """Build and validate catalog artifacts."""


@catalog_command.command("build", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--source",
    type=click.Path(file_okay=False, exists=True, path_type=Path),
    required=True,
    help="Guideline folder to read.",
)
@click.option(
    "--out",
    "output_path",
    type=click.Path(dir_okay=False, path_type=Path),
    required=True,
    help="Catalog parquet file to write.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Validate and report what would be written without writing.",
)
@click.option(
    "--overwrite",
    is_flag=True,
    help="Allow replacing an existing output file.",
)
def build_command(
    source: Path,
    output_path: Path,
    dry_run: bool,
    overwrite: bool,
) -> None:
    """Build a parquet catalog from a guideline folder."""

    catalog = Catalog.from_folder(source)
    if len(catalog) == 0:
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected subdirectories with guideline.md files."
        )
    if output_path.exists() and not overwrite and not dry_run:
        raise click.ClickException(f"{output_path} already exists. Pass --overwrite.")
    if dry_run:
        click.echo(f"Would write {len(catalog)} guidelines to {output_path}")
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    catalog.write_parquet(output_path)
    click.echo(f"Wrote {len(catalog)} guidelines to {output_path}")


@catalog_command.command("check", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--source",
    type=click.Path(file_okay=False, exists=True, path_type=Path),
    required=True,
    help="Guideline folder to validate.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def check_command(source: Path, output_format: str) -> None:
    """Validate a guideline folder and report table counts."""

    catalog = Catalog.from_folder(source)
    if len(catalog) == 0:
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected subdirectories with guideline.md files."
        )
    rows = [
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "labels", "rows": catalog.labels().height},
        {"name": "references", "rows": catalog.references().height},
    ]
    emit_rows(rows, output_format=output_format)


@catalog_command.command("duckdb", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--out",
    "output_path",
    type=click.Path(dir_okay=False, path_type=Path),
    required=True,
    help="DuckDB database file to write.",
)
@click.option("--overwrite", is_flag=True, help="Replace an existing DuckDB file.")
@click.pass_context
def duckdb_command(
    ctx: click.Context,
    output_path: Path,
    overwrite: bool,
) -> None:
    """Materialize catalog tables into a DuckDB database."""

    from chartcoach.duckdb import write_duckdb

    catalog = load_catalog(ctx)
    try:
        write_duckdb(catalog, output_path, overwrite=overwrite)
    except FileExistsError as exc:
        raise click.ClickException(f"{output_path} already exists. Pass --overwrite.") from exc
    click.echo(f"Wrote DuckDB catalog to {output_path}")


__all__ = ["catalog_command"]
