from __future__ import annotations

import json
from collections.abc import Mapping
from typing import cast

import click

from chartcoach.catalog.errors import CatalogError
from chartcoach.constants import (
    CATALOG_ARTIFACT_BASE_URL,
    CATALOG_ENTRY_PATH,
    DEFAULT_GUIDELINE_URL_TEMPLATE,
)
from chartcoach.tools import ToolError, format_error

from ..common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    catalog_release_digest,
    echo_warn,
    emit_object,
    emit_rows,
    load_catalog,
    source_option,
    source_path,
)
from ..common import (
    tools as catalog_tools,
)
from .rendering import citation_records_to_markdown, entry_records_to_markdown

READ_FORMATS = ("markdown", "json")
CITE_FORMATS = ("markdown", "json")


@click.command("overview", context_settings=CONTEXT_SETTINGS)
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
def overview_command(ctx: click.Context, output_format: str) -> None:
    """Summarize the catalog source, counts, roles, and labels."""

    catalog = load_catalog(ctx)
    from chartcoach.catalog.summary import catalog_overview, overview_table_rows

    overview = catalog_overview(
        catalog,
        source=source_path(ctx)
        or f"{CATALOG_ARTIFACT_BASE_URL.rstrip('/')}/{CATALOG_ENTRY_PATH}",
        release_digest=catalog_release_digest(ctx),
    )
    if output_format == "json":
        emit_object(overview)
        return
    emit_rows(overview_table_rows(overview), output_format=output_format)


@click.command("labels", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option("--family", help="Only include labels from this family.")
@click.option("--prefix", help="Only include labels starting with this prefix.")
@click.option("--contains", help="Case-insensitive substring filter over labels.")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=50,
    show_default=True,
    help="Maximum labels to print.",
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
def labels_command(
    ctx: click.Context,
    family: str | None,
    prefix: str | None,
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """List label values and counts."""

    catalog = load_catalog(ctx)
    from chartcoach.catalog.summary import list_labels

    try:
        rows = list_labels(
            catalog,
            family=family,
            prefix=prefix,
            contains=contains,
            limit=limit + 1,
        )
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    visible_rows = rows[:limit]
    emit_rows(
        visible_rows,
        output_format=output_format,
        empty_message="No labels matched.",
        empty_hints=_labels_empty_hints(
            family=family,
            prefix=prefix,
            contains=contains,
        ),
    )
    if len(rows) > limit:
        echo_warn(
            f"Returned {limit} labels.", detail="Increase --limit to inspect more."
        )


@click.command("roles", context_settings=CONTEXT_SETTINGS)
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
def roles_command(ctx: click.Context, output_format: str) -> None:
    """List section roles and counts."""

    catalog = load_catalog(ctx)
    from chartcoach.catalog.summary import list_roles

    rows = list_roles(catalog)
    emit_rows(rows, output_format=output_format)


@click.command("list", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option("--label", multiple=True, help="Require this exact label.")
@click.option(
    "--label-prefix",
    multiple=True,
    help="Require at least one label with this prefix.",
)
@click.option(
    "--contains",
    help="Case-insensitive substring filter over id, title, and description.",
)
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=50,
    show_default=True,
    help="Maximum rows to print.",
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
def list_command(
    ctx: click.Context,
    label: tuple[str, ...],
    label_prefix: tuple[str, ...],
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """List entry ids and summaries."""

    catalog = load_catalog(ctx)
    from chartcoach.catalog.query import query_entries

    try:
        rows = (
            query_entries(
                catalog,
                labels=label,
                label_prefixes=label_prefix,
                contains=contains,
                limit=limit,
                include_body=False,
            )
            .select("id", "title", "description", "labels")
            .to_dicts()
        )
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    emit_rows(
        rows,
        output_format=output_format,
        empty_message="No entries matched.",
        empty_hints=_list_empty_hints(
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
        ),
    )


def _labels_empty_hints(
    *,
    family: str | None,
    prefix: str | None,
    contains: str | None,
) -> list[str]:
    hints = []
    if contains:
        hints.append("Try a shorter or broader --contains term.")
    if family:
        hints.append(
            "Run `chartcoach catalog labels --format json` to inspect all labels."
        )
    if prefix:
        hints.append("Try a shorter --prefix or inspect labels by --family.")
    if not hints:
        hints.append(
            "Run `chartcoach catalog overview --format json` to inspect catalog counts."
        )
    return hints


def _list_empty_hints(
    *,
    labels: tuple[str, ...],
    label_prefixes: tuple[str, ...],
    contains: str | None,
) -> list[str]:
    hints = []
    if len(labels) > 1:
        hints.append("Repeated --label filters are all-of. Remove one --label.")
    elif labels:
        hints.append(
            "Try `chartcoach catalog labels --contains TEXT --format json` to find related labels."
        )
    if label_prefixes:
        hints.append(
            "Try a shorter --label-prefix or inspect labels with `chartcoach catalog labels --format json`."
        )
    if contains:
        hints.append("Try a broader --contains term.")
    if not hints:
        hints.append(
            "Run `chartcoach catalog overview --format json` to confirm the catalog has entries."
        )
    return hints


@click.command("read", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("entry_ids", nargs=-1, required=True)
@click.option(
    "--section",
    "sections",
    multiple=True,
    help="Include only these section roles. Can be passed more than once.",
)
@click.option(
    "--source-detail",
    type=click.Choice(("none", "minimal", "full")),
    default="minimal",
    show_default=True,
    help="Amount of source metadata to include.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(READ_FORMATS),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def read_command(
    ctx: click.Context,
    entry_ids: tuple[str, ...],
    sections: tuple[str, ...],
    source_detail: str,
    output_format: str,
) -> None:
    """Read exact entries and selected sections."""

    catalog = load_catalog(ctx)
    from chartcoach.catalog.read import retrieve_entry_records

    try:
        records = retrieve_entry_records(
            catalog,
            ids=entry_ids,
            roles=sections,
            source_detail=source_detail,
        )
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    if output_format == "json":
        click.echo(json.dumps(records, indent=2, ensure_ascii=False, default=str))
    else:
        click.echo(entry_records_to_markdown(records).rstrip())


@click.command("cite", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("entry_ids", nargs=-1, required=True)
@click.option(
    "--url-template",
    default=DEFAULT_GUIDELINE_URL_TEMPLATE,
    show_default=True,
    help="Guideline URL template. Must contain {id}.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CITE_FORMATS),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def cite_command(
    ctx: click.Context,
    entry_ids: tuple[str, ...],
    url_template: str,
    output_format: str,
) -> None:
    """Print guideline URLs and formatted source citations."""

    catalog = load_catalog(ctx)
    from chartcoach.catalog.references import citation_records

    try:
        records = citation_records(
            catalog,
            ids=entry_ids,
            url_template=url_template,
        )
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    if output_format == "json":
        click.echo(json.dumps(records, indent=2, ensure_ascii=False, default=str))
    else:
        click.echo(citation_records_to_markdown(records).rstrip())


@click.command("schema", context_settings=CONTEXT_SETTINGS)
@click.argument("argument_table_names", nargs=-1, metavar="[TABLE]...")
@source_option
@click.option(
    "--table",
    "table_names",
    multiple=True,
    help="Only include this table. Can be passed more than once.",
)
@click.option(
    "--tables",
    "list_table_names",
    is_flag=True,
    help="List tables instead of columns.",
)
@click.option(
    "--row-counts",
    is_flag=True,
    help="Include row counts when listing tables.",
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
    argument_table_names: tuple[str, ...],
    table_names: tuple[str, ...],
    list_table_names: bool,
    row_counts: bool,
    output_format: str,
) -> None:
    """Show queryable catalog fields and tables."""

    from chartcoach.catalog.introspection import describe_tables, list_tables

    try:
        selected_tables = (*table_names, *argument_table_names)
        if list_table_names and selected_tables:
            raise click.ClickException(
                format_error(
                    "`catalog schema --tables` lists table names and does not accept table filters.",
                    [
                        "Use `chartcoach catalog schema TABLE` to inspect one table's columns.",
                        "Use `chartcoach catalog schema --table TABLE` to inspect one table's columns.",
                    ],
                )
            )
        if list_table_names:
            rows = list_tables(load_catalog(ctx), include_row_counts=row_counts)
        else:
            rows = describe_tables(tables=selected_tables)
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    emit_rows(rows, output_format=output_format)


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
    """Run one read-only SELECT query over catalog DuckDB tables."""

    try:
        result = catalog_tools(ctx).sql(query, limit=limit)
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    except Exception as exc:
        raise click.ClickException(
            format_error(
                str(exc),
                [
                    "Run `chartcoach catalog schema --tables` to inspect table names.",
                    "Run `chartcoach catalog schema` to inspect column names.",
                ],
            )
        ) from exc
    if output_format == "json":
        emit_object(result)
        return
    rows = result["rows"]
    if not isinstance(rows, list) or not all(isinstance(row, Mapping) for row in rows):
        raise click.ClickException("SQL result rows were not a list.")
    emit_rows(cast(list[Mapping[str, object]], rows), output_format=output_format)
    if result["truncated"]:
        echo_warn(f"Returned {limit} rows.", detail="Increase --limit to inspect more.")


def _command_error(exc: CatalogError | ToolError) -> click.ClickException:
    message = getattr(exc, "message", str(exc))
    hints = getattr(exc, "hints", ())
    return click.ClickException(format_error(message, hints))


def register_navigation_commands(group: click.Group) -> None:
    group.add_command(overview_command)
    group.add_command(labels_command)
    group.add_command(roles_command)
    group.add_command(list_command)
    group.add_command(read_command)
    group.add_command(cite_command)
    group.add_command(schema_command)
    group.add_command(sql_command)


__all__ = ["register_navigation_commands"]
