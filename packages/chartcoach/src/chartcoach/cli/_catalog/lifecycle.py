from __future__ import annotations

from pathlib import Path

import click

from ..common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    echo_info,
    echo_success,
    emit_object,
    emit_rows,
    load_catalog,
    source_option,
    source_path,
)


@click.command("build", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--source",
    type=click.Path(file_okay=False, exists=True, path_type=Path),
    required=True,
    help="Authored catalog folder to read.",
)
@click.option(
    "--out",
    "output_path",
    type=click.Path(file_okay=False, path_type=Path),
    required=True,
    help="Catalog bundle directory to create.",
)
@click.option("--dry-run", is_flag=True, help="Validate without creating the bundle.")
def build_command(
    source: Path,
    output_path: Path,
    dry_run: bool,
) -> None:
    """Build a catalog bundle from authored guideline entries."""

    from chartcoach import open_catalog

    try:
        catalog = open_catalog(source)
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc
    if len(catalog) == 0:
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected entries/*/guideline.md files."
        )
    if dry_run:
        echo_info(
            f"Would write {len(catalog)} entries",
            detail=f"to catalog bundle {output_path}",
            err=False,
        )
        return
    try:
        from chartcoach.curation import write_bundle

        write_bundle(catalog, output_path)
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            "Catalog bundle builds require chartcoach[curation]."
        ) from exc
    except FileExistsError as exc:
        raise click.ClickException(f"{output_path} already exists.") from exc
    echo_success(f"Wrote {len(catalog)} entries", detail=f"to {output_path}")


@click.command("validate", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def validate_command(ctx: click.Context, output_format: str) -> None:
    """Validate a catalog source and report table counts."""

    catalog = load_catalog(ctx)
    from chartcoach._catalog.summary import validation_rows

    if len(catalog) == 0:
        source = source_path(ctx)
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected entries/*/guideline.md files."
        )
    rows = validation_rows(catalog)
    emit_rows(rows, output_format=output_format)


@click.command("manifest", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("markdown", "json")),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def manifest_command(ctx: click.Context, output_format: str) -> None:
    """Print the catalog manifest."""

    catalog = load_catalog(ctx)
    manifest = catalog.manifest
    if output_format == "markdown":
        click.echo(manifest.markdown.rstrip())
        return
    rows = {
        "section_roles": list(manifest.section_roles),
        "label_families": list(manifest.label_families),
    }
    emit_object(rows)


@click.group("export", context_settings=CONTEXT_SETTINGS, help="Export catalog tables.")
def export_command() -> None:
    """Export catalog tables."""


@click.command("duckdb", context_settings=CONTEXT_SETTINGS)
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
def export_duckdb_command(
    ctx: click.Context,
    output_path: Path,
    overwrite: bool,
) -> None:
    """Materialize catalog tables into a DuckDB database."""

    catalog = load_catalog(ctx)
    try:
        from chartcoach.duckdb import write_duckdb

        write_duckdb(catalog, output_path, overwrite=overwrite)
    except FileExistsError as exc:
        raise click.ClickException(
            f"{output_path} already exists. Pass --overwrite."
        ) from exc
    echo_success("Wrote DuckDB catalog", detail=f"to {output_path}")


def register_lifecycle_commands(group: click.Group) -> None:
    export_command.add_command(export_duckdb_command)
    group.add_command(build_command)
    group.add_command(validate_command)
    group.add_command(manifest_command)
    group.add_command(export_command)


__all__ = ["register_lifecycle_commands"]
