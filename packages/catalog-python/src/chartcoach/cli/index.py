from __future__ import annotations

from pathlib import Path
from typing import cast

import click

from chartcoach.constants import LANCE_DOCUMENT_TABLE
from chartcoach.search import Mode, index, open as open_index, query as query_table
from chartcoach.tools import search_error

from .common import (
    CONTEXT_SETTINGS,
    emit_object,
    load_catalog,
    required_index_option,
    source_option,
)

INDEX_FORMATS = ("json", "jsonl")


@click.group(
    "index",
    invoke_without_command=True,
    context_settings=CONTEXT_SETTINGS,
    help="Create a LanceDB table for catalog document search.",
)
@source_option
@required_index_option
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to create or query.",
)
@click.pass_context
def index_command(
    ctx: click.Context,
    index_path: Path,
    table_name: str,
) -> None:
    """Create or replace a LanceDB table for catalog document search."""

    if ctx.invoked_subcommand is not None:
        ctx.ensure_object(dict)["index_path"] = index_path
        ctx.ensure_object(dict)["table_name"] = table_name
        return

    catalog = load_catalog(ctx)
    try:
        table = index(catalog, index_path, table_name=table_name)
        click.echo(
            f"Wrote LanceDB table for {len(catalog)} guidelines "
            f"({table.count_rows()} documents) "
            f"to {index_path} "
            f"table {table.name!r}"
        )
    except Exception as exc:
        raise click.ClickException(search_error(str(exc))) from exc


@index_command.command("documents", context_settings=CONTEXT_SETTINGS)
@click.argument("query")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=10,
    show_default=True,
    help="Maximum indexed document rows to return.",
)
@click.option(
    "--where",
    help="LanceDB SQL filter over indexed document columns.",
)
@click.option(
    "--mode",
    type=click.Choice(("auto", "fts", "vector", "hybrid")),
    default="auto",
    show_default=True,
    help="LanceDB query mode.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(INDEX_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def documents_command(
    ctx: click.Context,
    query: str,
    limit: int,
    where: str | None,
    mode: str,
    output_format: str,
) -> None:
    """Run LanceDB search over indexed document rows."""

    index_path = cast(Path, ctx.ensure_object(dict)["index_path"])
    table_name = cast(str, ctx.ensure_object(dict)["table_name"])
    try:
        table = open_index(index_path, table_name=table_name)
        rows = query_table(
            table,
            query,
            limit=limit,
            where=where,
            mode=cast(Mode, mode),
        )
        result = {
            "query": query,
            "mode": mode,
            "rows": rows,
            "row_count": len(rows),
            "limit": limit,
            "where": where,
            "index_path": str(index_path),
            "table_name": table.name,
        }
    except Exception as exc:
        raise click.ClickException(search_error(str(exc))) from exc
    emit_object(result, output_format=output_format)


__all__ = ["index_command"]
