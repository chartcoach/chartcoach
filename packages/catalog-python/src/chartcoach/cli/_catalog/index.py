from __future__ import annotations

import json
from typing import TYPE_CHECKING, cast

import click

from chartcoach.constants import LANCE_DOCUMENT_TABLE
from chartcoach.search import Mode, index, open as open_index
from chartcoach.search import search as search_guidelines
from chartcoach.tools import ToolError

from ..common import (
    CONTEXT_SETTINGS,
    INDEX_EXTRA_MESSAGE,
    SEARCH_FORMATS,
    emit_rows,
    guideline_search_rows_to_compact_markdown,
    guideline_search_rows_to_markdown,
    load_catalog,
    quiet_runtime_stderr,
    require_index_path,
    required_index_option,
    search_cli_error,
    source_option,
    source_path,
)

if TYPE_CHECKING:
    from lancedb.embeddings import EmbeddingFunction

INDEX_CREATE_FORMATS = ("table", "json", "jsonl")
INDEX_INFO_FORMATS = ("table", "json", "jsonl")


@click.command("find", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_option
@click.argument("query")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=8,
    show_default=True,
    help="Guideline rows to return after document-level deduplication.",
)
@click.option(
    "--candidate-limit",
    type=click.IntRange(min=1),
    help="Maximum indexed documents to inspect before deduplication.",
)
@click.option("--where", help="LanceDB SQL filter over indexed document columns.")
@click.option(
    "--mode",
    type=click.Choice(("auto", "fts", "vector", "hybrid")),
    default="auto",
    show_default=True,
    help="LanceDB query mode for document retrieval.",
)
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to query.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(SEARCH_FORMATS),
    default="compact",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def find_command(
    ctx: click.Context,
    index_path: str | None,
    query: str,
    limit: int,
    candidate_limit: int | None,
    where: str | None,
    mode: str,
    table_name: str,
    output_format: str,
) -> None:
    """Rank entries with an existing LanceDB index."""

    catalog = load_catalog(ctx)
    resolved_index_path = require_index_path(
        index_path,
        source_path=source_path(ctx),
        table_name=table_name,
        use_default=True,
    )
    try:
        table = open_index(resolved_index_path, table_name=table_name)
        with quiet_runtime_stderr():
            result = search_guidelines(
                catalog,
                table,
                query,
                limit=limit,
                candidate_limit=candidate_limit,
                where=where,
                mode=cast(Mode, mode),
            ).to_dict()
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc),
                index_path=resolved_index_path,
                table_name=table_name,
                missing_index_extra=True,
            )
        ) from exc
    except Exception as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc),
                index_path=resolved_index_path,
                table_name=table_name,
            )
        ) from exc

    if output_format == "json":
        click.echo(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        return

    rows = cast(list[dict[str, object]], result["rows"])
    if output_format == "markdown":
        output = guideline_search_rows_to_markdown(rows).rstrip()
        click.echo(output or "No entries matched.")
    elif output_format == "compact":
        output = guideline_search_rows_to_compact_markdown(rows).rstrip()
        click.echo(output or "No entries matched.")
    else:
        emit_rows(
            rows, output_format=output_format, empty_message="No entries matched."
        )


@click.group(
    "index",
    context_settings=CONTEXT_SETTINGS,
    help="Create and inspect LanceDB indexes.",
)
def index_command() -> None:
    """Create and inspect LanceDB indexes."""


@click.command("create", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_option
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to create.",
)
@click.option(
    "--embedding",
    "embedding_name",
    help=(
        "LanceDB embedding function alias from lancedb.embeddings.get_registry(). "
        "When omitted, the table is full-text only."
    ),
)
@click.option(
    "--embedding-option",
    "embedding_options",
    multiple=True,
    metavar="KEY=VALUE",
    help="Option passed to the LanceDB embedding function create() call.",
)
@click.option(
    "--embedding-var",
    "embedding_vars",
    multiple=True,
    metavar="KEY=VALUE",
    help="Set a LanceDB embedding registry variable before create().",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(INDEX_CREATE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def index_create_command(
    ctx: click.Context,
    index_path: str | None,
    table_name: str,
    embedding_name: str | None,
    embedding_options: tuple[str, ...],
    embedding_vars: tuple[str, ...],
    output_format: str,
) -> None:
    """Build a LanceDB index from the catalog."""

    resolved_index_path = require_index_path(index_path)
    catalog = load_catalog(ctx)
    try:
        embedding = _embedding(embedding_name, embedding_options, embedding_vars)
        with quiet_runtime_stderr():
            table = index(
                catalog, resolved_index_path, table_name=table_name, embedding=embedding
            )
        row = {
            "index_path": resolved_index_path,
            "table": table.name,
            "guidelines": len(catalog),
            "documents": table.count_rows(),
            "embedding": embedding_name,
            "catalog_digest": catalog.digest(),
        }
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc),
                index_path=resolved_index_path,
                table_name=table_name,
                missing_index_extra=True,
            )
        ) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc), index_path=resolved_index_path, table_name=table_name
            )
        ) from exc
    emit_rows([row], output_format=output_format)


@click.command("info", context_settings=CONTEXT_SETTINGS)
@required_index_option
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to inspect.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(INDEX_INFO_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def index_info_command(
    index_path: str | None, table_name: str, output_format: str
) -> None:
    """Inspect a LanceDB index."""

    resolved_index_path = require_index_path(
        index_path, table_name=table_name, use_default=True
    )
    try:
        table = open_index(resolved_index_path, table_name=table_name)
        row = {
            "index_path": resolved_index_path,
            "table": table.name,
            "documents": table.count_rows(),
            "embedding_functions": embedding_functions_state(table),
        }
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc),
                index_path=resolved_index_path,
                table_name=table_name,
                missing_index_extra=True,
            )
        ) from exc
    except Exception as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc), index_path=resolved_index_path, table_name=table_name
            )
        ) from exc
    emit_rows([row], output_format=output_format)


def embedding_functions_state(table: object) -> str:
    try:
        functions = getattr(table, "embedding_functions", None)
    except Exception:
        return "unknown"
    return "present" if functions else "absent"


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
        raise ModuleNotFoundError(INDEX_EXTRA_MESSAGE, name=exc.name) from exc

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
            search_cli_error(f"Unknown LanceDB embedding function: {name}")
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


def register_index_commands(group: click.Group) -> None:
    index_command.add_command(index_create_command)
    index_command.add_command(index_info_command)
    group.add_command(find_command)
    group.add_command(index_command)


__all__ = ["register_index_commands"]
