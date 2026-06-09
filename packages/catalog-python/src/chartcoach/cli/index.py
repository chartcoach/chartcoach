from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import click

from chartcoach.constants import LANCE_DOCUMENT_TABLE
from chartcoach.search import Mode, index, open as open_index, query as query_table
from chartcoach.tools import search_error

from .common import (
    CONTEXT_SETTINGS,
    emit_object,
    load_catalog,
    quiet_runtime_stderr,
    require_index_path,
    required_index_option,
    search_cli_error,
    source_option,
)

if TYPE_CHECKING:
    from lancedb.embeddings import EmbeddingFunction

INDEX_FORMATS = ("json", "jsonl")


@click.group(
    "index",
    invoke_without_command=True,
    context_settings=CONTEXT_SETTINGS,
    help=(
        "Create and inspect a LanceDB table for catalog document search.\n\n"
        "Running without a subcommand creates or replaces the table. "
        "Use `documents` to query indexed document rows."
    ),
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
@click.option(
    "--embedding",
    "embedding_name",
    help=(
        "LanceDB embedding function alias from "
        "lancedb.embeddings.get_registry(). "
        "When omitted, the table is full-text only."
    ),
)
@click.option(
    "--embedding-option",
    "embedding_options",
    multiple=True,
    metavar="KEY=VALUE",
    help=(
        "Option passed to the LanceDB embedding function create() call. "
        "Values parse as JSON when possible, otherwise as strings. "
        "Can be passed more than once."
    ),
)
@click.option(
    "--embedding-var",
    "embedding_vars",
    multiple=True,
    metavar="KEY=VALUE",
    help=(
        "Set a LanceDB embedding registry variable before create(). "
        "Use this for $var: references in embedding options."
    ),
)
@click.pass_context
def index_command(
    ctx: click.Context,
    index_path: Path | None,
    table_name: str,
    embedding_name: str | None,
    embedding_options: tuple[str, ...],
    embedding_vars: tuple[str, ...],
) -> None:
    """Create or replace a LanceDB table for catalog document search."""

    if ctx.invoked_subcommand is not None:
        ctx.ensure_object(dict)["index_path"] = index_path
        ctx.ensure_object(dict)["table_name"] = table_name
        return

    index_path = require_index_path(index_path)
    catalog = load_catalog(ctx)
    try:
        embedding = _embedding(embedding_name, embedding_options, embedding_vars)
        with quiet_runtime_stderr():
            table = index(catalog, index_path, table_name=table_name, embedding=embedding)
        click.echo(
            f"Wrote LanceDB table for {len(catalog)} guidelines "
            f"({table.count_rows()} documents) "
            f"to {index_path} "
            f"table {table.name!r}"
        )
    except Exception as exc:
        raise click.ClickException(search_error(str(exc))) from exc


def _embedding(
    name: str | None,
    options: tuple[str, ...],
    variables: tuple[str, ...],
) -> "EmbeddingFunction | None":
    if name is None:
        if options or variables:
            raise click.ClickException(
                "Pass --embedding before --embedding-option or --embedding-var."
            )
        return None

    try:
        from lancedb.embeddings import get_registry
    except ModuleNotFoundError as exc:
        raise click.ClickException(search_error(str(exc))) from exc

    registry = get_registry()
    for item in variables:
        key, value = _key_value(item, option="--embedding-var")
        registry.set_var(key, value)
    kwargs = {
        key: _json_or_string(value)
        for key, value in (
            _key_value(item, option="--embedding-option") for item in options
        )
    }
    try:
        return cast("EmbeddingFunction", registry.get(name).create(**kwargs))
    except KeyError as exc:
        raise click.ClickException(
            search_error(f"Unknown LanceDB embedding function: {name}")
        ) from exc


def _key_value(value: str, *, option: str) -> tuple[str, str]:
    if "=" not in value:
        raise click.ClickException(f"{option} expects KEY=VALUE.")
    key, raw = value.split("=", 1)
    key = key.strip()
    if not key:
        raise click.ClickException(f"{option} key cannot be empty.")
    return key, raw


def _json_or_string(value: str) -> object:
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


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

    index_path = require_index_path(
        cast(Path | None, ctx.ensure_object(dict).get("index_path"))
    )
    table_name = cast(str, ctx.ensure_object(dict)["table_name"])
    try:
        table = open_index(index_path, table_name=table_name)
        with quiet_runtime_stderr():
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
        raise click.ClickException(
            search_cli_error(str(exc), index_path=index_path, table_name=table_name)
        ) from exc
    emit_object(result, output_format=output_format)


__all__ = ["index_command"]
