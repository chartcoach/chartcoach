from __future__ import annotations

import click

from chartcoach.tools.catalog import CatalogToolError, format_tool_error

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    source_option,
    catalog_tools,
    emit_rows,
)


@click.group(
    "tables",
    context_settings=CONTEXT_SETTINGS,
    help="Inspect structured catalog tables.",
)
def tables_command() -> None:
    """Inspect structured catalog tables."""


@tables_command.command("list", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--row-counts",
    is_flag=True,
    help="Materialize each table enough to include row counts.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def list_command(ctx: click.Context, row_counts: bool, output_format: str) -> None:
    """List queryable catalog tables."""

    emit_rows(
        catalog_tools(ctx).list_tables(include_row_counts=row_counts),
        output_format=output_format,
    )


@tables_command.command("schema", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--table",
    "table_names",
    multiple=True,
    help="Only include this table. Can be passed more than once.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def schema_command(
    ctx: click.Context,
    table_names: tuple[str, ...],
    output_format: str,
) -> None:
    """List columns for SQL-visible catalog tables."""

    tools = catalog_tools(ctx)
    try:
        rows = tools.describe_tables(tables=table_names)
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            format_tool_error(
                str(exc),
                ["Run tables list first to inspect available table names."],
            )
        ) from exc
    emit_rows(rows, output_format=output_format)


@tables_command.command("values", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("table")
@click.argument("column")
@click.option(
    "--explode",
    is_flag=True,
    help="Count each item in a list-valued column separately.",
)
@click.option("--contains", help="Case-insensitive substring filter over values.")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=50,
    show_default=True,
    help="Maximum values to print.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def values_command(
    ctx: click.Context,
    table: str,
    column: str,
    explode: bool,
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """Count distinct values in a catalog table column."""

    tools = catalog_tools(ctx)
    try:
        rows = tools.count_values(
            table,
            column,
            explode=explode,
            contains=contains,
            limit=limit,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            format_tool_error(
                str(exc),
                ["Run tables schema first to inspect available columns."],
            )
        ) from exc
    emit_rows(rows, output_format=output_format)


__all__ = ["tables_command"]
