from __future__ import annotations

import click

from chartcoach.tools.catalog import (
    CatalogToolError,
    CatalogTools,
    search_error_message,
)

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    emit_object,
    emit_rows,
    load_catalog,
    required_index_dir_option,
    source_option,
)

INDEX_FORMATS = ("json", "jsonl")


@click.group(
    "index",
    context_settings=CONTEXT_SETTINGS,
    help="Build and inspect the LanceDB search index.",
)
def index_command() -> None:
    """Build and inspect the LanceDB search index."""


@index_command.command("status", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def status_command(
    ctx: click.Context,
    index_dir: str | None,
    output_format: str,
) -> None:
    """Report the LanceDB index path for this catalog."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    row = CatalogTools(catalog, index_dir=index_dir).index_status()
    emit_rows([row], output_format=output_format)


@index_command.command("build", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.pass_context
def build_command(ctx: click.Context, index_dir: str | None) -> None:
    """Create the LanceDB index if it is missing."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    try:
        summary = CatalogTools(catalog, index_dir=index_dir).build_index(
            cache_mode="reuse_or_create"
        )
        click.echo(
            f"Index ready for {summary['guidelines']} guidelines "
            f"({summary['documents']} documents) "
            f"at {summary['index_root']} "
            f"table {summary['table_name']!r}"
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc


@index_command.command("rebuild", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.option(
    "--yes",
    is_flag=True,
    help="Confirm rebuilding the content-addressed index cache path.",
)
@click.pass_context
def rebuild_command(ctx: click.Context, index_dir: str | None, yes: bool) -> None:
    """Rebuild the LanceDB index for the catalog."""

    if not yes:
        raise click.ClickException("Pass --yes to rebuild the search index.")
    catalog = load_catalog(ctx)
    assert index_dir is not None
    try:
        summary = CatalogTools(catalog, index_dir=index_dir).build_index(
            cache_mode="force_rebuild"
        )
        click.echo(
            f"Rebuilt index for {summary['guidelines']} guidelines "
            f"({summary['documents']} documents) "
            f"at {summary['index_root']} "
            f"table {summary['table_name']!r}"
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc


@index_command.command("query", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
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
    "--format",
    "output_format",
    type=click.Choice(INDEX_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def query_command(
    ctx: click.Context,
    index_dir: str | None,
    query: str,
    limit: int,
    where: str | None,
    output_format: str,
) -> None:
    """Run a LanceDB full-text query."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    try:
        result = CatalogTools(catalog, index_dir=index_dir).query_documents(
            query,
            limit=limit,
            where=where,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc
    emit_object(result, output_format=output_format)


__all__ = ["index_command"]
