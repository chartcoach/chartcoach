from __future__ import annotations

from pathlib import Path

import click

from chartcoach.catalog import Catalog

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    emit_object,
    emit_rows,
    load_catalog,
    source_path,
    source_option,
)


@click.group(
    "catalog",
    context_settings=CONTEXT_SETTINGS,
    help="Build and validate catalog bundles.",
)
def catalog_command() -> None:
    """Build and validate catalog bundles."""


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
    type=click.Path(file_okay=False, path_type=Path),
    required=True,
    help="Catalog bundle directory to write.",
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
    """Build a catalog bundle from a guideline folder."""

    try:
        catalog = Catalog.from_folder(source)
    except FileNotFoundError as exc:
        raise click.ClickException(str(exc)) from exc
    if len(catalog) == 0:
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected entries/*/guideline.md files."
        )
    manifest_path = output_path / "MANIFEST.md"
    parquet_path = output_path / "entries.parquet"
    metadata_path = output_path / "metadata.json"
    if (
        not overwrite
        and not dry_run
        and (manifest_path.exists() or parquet_path.exists() or metadata_path.exists())
    ):
        raise click.ClickException(
            f"{output_path} already contains a catalog bundle. Pass --overwrite."
        )
    if dry_run:
        click.echo(
            f"Would write {len(catalog)} guidelines to catalog bundle {output_path}"
        )
        return
    catalog.write_bundle(output_path, overwrite=overwrite)
    click.echo(f"Wrote {len(catalog)} guidelines to {output_path}")


@catalog_command.command("check", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def check_command(ctx: click.Context, output_format: str) -> None:
    """Validate a catalog source and report table counts."""

    catalog = load_catalog(ctx)
    if len(catalog) == 0:
        source = source_path(ctx)
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected entries/*/guideline.md files."
        )
    rows = [
        {
            "name": "manifest_section_roles",
            "rows": len(catalog.require_manifest().section_roles),
        },
        {
            "name": "manifest_label_families",
            "rows": len(catalog.require_manifest().label_families),
        },
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "labels", "rows": catalog.labels().height},
        {"name": "references", "rows": catalog.references().height},
    ]
    emit_rows(rows, output_format=output_format)


@catalog_command.command("manifest", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("markdown", "json", "jsonl")),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def manifest_command(ctx: click.Context, output_format: str) -> None:
    """Print the catalog manifest."""

    catalog = load_catalog(ctx)
    try:
        manifest = catalog.require_manifest()
    except ValueError as exc:
        path = source_path(ctx)
        raise click.ClickException(
            "Catalog source has no manifest: "
            f"{path}\n\n"
            "Guidance:\n"
            "  - Use an authored guideline folder with entries/ or a catalog bundle directory.\n"
            "  - Omit --source to use the package-pinned default catalog artifact.\n"
            "  - Use the standalone parquet file for tables, SQL, indexing, and guideline records."
        ) from exc
    if output_format == "markdown":
        click.echo(manifest.markdown.rstrip())
        return
    rows = {
        "section_roles": list(manifest.section_roles),
        "label_families": list(manifest.label_families),
    }
    emit_object(rows, output_format=output_format)


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
        raise click.ClickException(
            f"{output_path} already exists. Pass --overwrite."
        ) from exc
    click.echo(f"Wrote DuckDB catalog to {output_path}")


__all__ = ["catalog_command"]
