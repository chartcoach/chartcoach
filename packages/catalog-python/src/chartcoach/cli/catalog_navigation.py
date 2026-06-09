from __future__ import annotations

from collections.abc import Mapping
import json
from typing import cast

import click

from chartcoach.tools import ToolError, format_error

from .catalog_logic import (
    catalog_overview,
    entry_records_to_markdown,
    list_labels,
    list_roles,
    overview_table_rows,
    query_entries,
    retrieve_entry_records,
)
from .catalog_tables import (
    count_values,
    describe_tables,
    list_tables,
    parse_value_field,
)
from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    echo_warn,
    emit_object,
    emit_rows,
    load_catalog,
    source_option,
    source_path,
)

READ_FORMATS = ("markdown", "json", "jsonl")


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
    overview = catalog_overview(catalog, source=source_path(ctx))
    if output_format == "json":
        emit_object(overview, output_format=output_format)
        return
    if output_format == "jsonl":
        click.echo(json.dumps(overview, ensure_ascii=False, default=str))
        return
    if output_format == "csv":
        rows = overview_table_rows(overview)
        emit_rows(rows, output_format=output_format)
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

    try:
        rows = list_labels(
            load_catalog(ctx),
            family=family,
            prefix=prefix,
            contains=contains,
            limit=limit + 1,
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    visible_rows = rows[:limit]
    emit_rows(
        visible_rows, output_format=output_format, empty_message="No labels matched."
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

    rows = list_roles(load_catalog(ctx))
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

    try:
        rows = (
            query_entries(
                load_catalog(ctx),
                labels=label,
                label_prefixes=label_prefix,
                contains=contains,
                limit=limit,
                include_body=False,
            )
            .select("id", "title", "description", "labels")
            .to_dicts()
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(rows, output_format=output_format, empty_message="No entries matched.")


@click.command("query", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--id",
    "entry_ids",
    multiple=True,
    help="Require this exact entry id. Can be passed more than once.",
)
@click.option(
    "--label",
    "labels",
    multiple=True,
    help="Require this exact label. Repeated labels are all-of filters.",
)
@click.option(
    "--any-label",
    "any_labels",
    multiple=True,
    help="Require at least one of these exact labels.",
)
@click.option(
    "--label-prefix",
    "label_prefixes",
    multiple=True,
    help="Require at least one label with this prefix. Repeated prefixes are all-of filters.",
)
@click.option(
    "--contains",
    help="Case-insensitive substring filter over id, title, and description.",
)
@click.option(
    "--body-contains", help="Case-insensitive substring filter over body text."
)
@click.option(
    "--section-contains",
    help="Case-insensitive substring filter over section titles and content.",
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
    default="jsonl",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def query_command(
    ctx: click.Context,
    entry_ids: tuple[str, ...],
    labels: tuple[str, ...],
    any_labels: tuple[str, ...],
    label_prefixes: tuple[str, ...],
    contains: str | None,
    body_contains: str | None,
    section_contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """Filter entries with composable base predicates."""

    try:
        rows = (
            query_entries(
                load_catalog(ctx),
                ids=entry_ids,
                labels=labels,
                any_labels=any_labels,
                label_prefixes=label_prefixes,
                contains=contains,
                body_contains=body_contains,
                section_contains=section_contains,
                limit=limit,
                include_body=False,
            )
            .select("id", "title", "description", "labels")
            .to_dicts()
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(rows, output_format=output_format, empty_message="No entries matched.")


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
    try:
        records = retrieve_entry_records(
            catalog,
            ids=entry_ids,
            roles=sections,
            source_detail=source_detail,
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    if output_format == "json":
        click.echo(json.dumps(records, indent=2, ensure_ascii=False, default=str))
    elif output_format == "jsonl":
        for record in records:
            click.echo(json.dumps(record, ensure_ascii=False, default=str))
    else:
        click.echo(entry_records_to_markdown(records).rstrip())


@click.command("schema", context_settings=CONTEXT_SETTINGS)
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
    table_names: tuple[str, ...],
    list_table_names: bool,
    row_counts: bool,
    output_format: str,
) -> None:
    """Show queryable catalog fields and tables."""

    try:
        if list_table_names:
            rows = list_tables(load_catalog(ctx), include_row_counts=row_counts)
        else:
            rows = describe_tables(tables=table_names)
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(rows, output_format=output_format)


@click.command("values", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("field")
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
    field: str,
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """Count values for a catalog field."""

    catalog = load_catalog(ctx)
    try:
        table, column, explode = parse_value_field(field)
        rows = count_values(
            catalog,
            table,
            column,
            explode=explode,
            contains=contains,
            limit=limit + 1,
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    visible_rows = rows[:limit]
    emit_rows(visible_rows, output_format=output_format)
    if len(rows) > limit:
        echo_warn(
            f"Returned {limit} values.", detail="Increase --limit to inspect more."
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
    """Run one read-only SELECT query over catalog DuckDB tables."""

    try:
        from chartcoach.tools import Tools

        result = Tools(load_catalog(ctx)).sql(query, limit=limit)
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
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
        emit_object(result, output_format=output_format)
        return
    rows = result["rows"]
    if not isinstance(rows, list) or not all(isinstance(row, Mapping) for row in rows):
        raise click.ClickException("SQL result rows were not a list.")
    emit_rows(cast(list[Mapping[str, object]], rows), output_format=output_format)
    if result["truncated"]:
        echo_warn(f"Returned {limit} rows.", detail="Increase --limit to inspect more.")


def register_navigation_commands(group: click.Group) -> None:
    group.add_command(overview_command)
    group.add_command(labels_command)
    group.add_command(roles_command)
    group.add_command(list_command)
    group.add_command(query_command)
    group.add_command(read_command)
    group.add_command(schema_command)
    group.add_command(values_command)
    group.add_command(sql_command)


__all__ = ["register_navigation_commands"]
