from __future__ import annotations

from collections.abc import Mapping
from typing import cast

import click

from chartcoach.tools.catalog import CatalogToolError, format_tool_error

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    catalog_tools,
    emit_object,
    emit_rows,
    source_option,
)


@click.command("sql", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("query")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=100,
    show_default=True,
    help="Maximum result rows to return.",
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
def sql_command(
    ctx: click.Context,
    query: str,
    limit: int,
    output_format: str,
) -> None:
    """Run one SELECT query over catalog DuckDB tables."""

    try:
        result = catalog_tools(ctx).sql_query(query, limit=limit)
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            format_tool_error(
                str(exc),
                [
                    "Inspect table names before running the query.",
                    "Inspect column schemas before selecting fields.",
                ],
            )
        ) from exc

    if output_format == "json":
        emit_object(result, output_format=output_format)
        return

    rows = result["rows"]
    if not isinstance(rows, list) or not all(isinstance(row, Mapping) for row in rows):
        raise click.ClickException("SQL result rows were not a list.")
    emit_rows(cast(list[Mapping[str, object]], rows), output_format=output_format)
    if result["truncated"]:
        click.echo(
            f"Returned {limit} rows. Increase --limit to inspect more.",
            err=True,
        )


__all__ = ["sql_command"]
