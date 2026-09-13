from __future__ import annotations

from collections.abc import Sequence
from typing import cast

import click

from chartcoach._catalog import SourceDetail
from chartcoach._catalog.errors import CatalogError, format_error
from chartcoach._catalog.identity import catalog_identity
from chartcoach._catalog.sql import catalog_sql
from chartcoach._constants import DEFAULT_GUIDELINE_URL_TEMPLATE

from ..common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    echo_warn,
    emit_guidance,
    emit_object,
    emit_rows,
    load_catalog,
    source_option,
)
from .rendering import citation_records_to_markdown, entry_records_to_markdown

READ_FORMATS = ("json", "markdown")
CITE_FORMATS = ("json", "markdown")


@click.command("describe", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option("--profile", help="Load and report one verified index profile.")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def describe_command(
    ctx: click.Context, profile: str | None, output_format: str
) -> None:
    """Describe catalog identity, tables, vocabulary, and index profiles."""

    try:
        description = load_catalog(ctx).describe(profile=profile)
    except CatalogError as exc:
        raise _command_error(exc) from exc
    if output_format == "json":
        emit_object(description)
        return
    rows: list[dict[str, object]] = [
        {"name": "resolved_location", "value": description["resolved_location"]},
        {"name": "release_digest", "value": description["release_digest"]},
        {"name": "entries_digest", "value": description["entries_digest"]},
        {"name": "manifest_digest", "value": description["manifest_digest"]},
        {"name": "profiles", "value": description["profiles"]},
    ]
    for table in description["tables"]:
        rows.append({"name": f"table.{table['name']}", "value": table["rows"]})
    emit_rows(rows, output_format=output_format)


@click.command("labels", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option("--family", help="Include labels from this family.")
@click.option("--prefix", help="Include labels starting with this prefix.")
@click.option("--contains", help="Case-insensitive substring filter over labels.")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=50,
    show_default=True,
    help="Maximum labels to return.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="json",
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
    """List label values and guideline entry counts."""

    from chartcoach._catalog.summary import list_labels

    try:
        rows = list_labels(
            load_catalog(ctx),
            family=family,
            prefix=prefix,
            contains=contains,
            limit=limit + 1,
        )
    except CatalogError as exc:
        raise _command_error(exc) from exc
    visible = rows[:limit]
    emit_rows(
        visible,
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
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def roles_command(ctx: click.Context, output_format: str) -> None:
    """List manifest section roles and guideline entry counts."""

    from chartcoach._catalog.summary import list_roles

    emit_rows(list_roles(load_catalog(ctx)), output_format=output_format)


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
    help="Maximum guideline entry candidates to return.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="json",
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
    """Return compact guideline entry candidates."""

    catalog = load_catalog(ctx)
    try:
        candidates = catalog.query(
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            limit=limit + 1,
        ).to_dicts()
    except CatalogError as exc:
        raise _command_error(exc) from exc
    rows = candidates[:limit]
    if output_format == "json":
        emit_object(
            {
                "rows": rows,
                "row_count": len(rows),
                "limit": limit,
                "truncated": len(candidates) > limit,
                **catalog_identity(catalog),
            }
        )
        if not rows:
            emit_guidance(
                "No guideline entries matched.",
                _list_empty_hints(label, label_prefix, contains),
            )
        return
    emit_rows(
        rows,
        output_format=output_format,
        empty_message="No guideline entries matched.",
        empty_hints=_list_empty_hints(label, label_prefix, contains),
    )
    if len(candidates) > limit:
        echo_warn(
            f"Returned {limit} guideline entries.",
            detail="Increase --limit to inspect more.",
        )


@click.command("read", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("guideline_ids", nargs=-1, required=True)
@click.option(
    "--role",
    "roles",
    multiple=True,
    help="Include this section role. Repeat for additional roles.",
)
@click.option(
    "--source-detail",
    type=click.Choice(("none", "minimal", "full")),
    default="minimal",
    show_default=True,
    help="Bibliographic source detail included with each guideline entry.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(READ_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def read_command(
    ctx: click.Context,
    guideline_ids: tuple[str, ...],
    roles: tuple[str, ...],
    source_detail: str,
    output_format: str,
) -> None:
    """Read complete guideline entry records by exact guideline entry ID."""

    catalog = load_catalog(ctx)
    try:
        records = catalog.read(
            ids=guideline_ids,
            roles=roles,
            source_detail=cast(SourceDetail, source_detail),
        )
    except CatalogError as exc:
        raise _command_error(exc) from exc
    if output_format == "json":
        emit_object({"records": records, **catalog_identity(catalog)})
        return
    click.echo(entry_records_to_markdown(records).rstrip())


@click.command("cite", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("guideline_ids", nargs=-1, required=True)
@click.option(
    "--url-template",
    default=DEFAULT_GUIDELINE_URL_TEMPLATE,
    show_default=True,
    help="Guideline URL template containing {id}.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CITE_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def cite_command(
    ctx: click.Context,
    guideline_ids: tuple[str, ...],
    url_template: str,
    output_format: str,
) -> None:
    """Return guideline links and formatted source citations."""

    catalog = load_catalog(ctx)
    try:
        records = catalog.cite(ids=guideline_ids, url_template=url_template)
    except CatalogError as exc:
        raise _command_error(exc) from exc
    if output_format == "json":
        emit_object({"records": records, **catalog_identity(catalog)})
        return
    click.echo(citation_records_to_markdown(records).rstrip())


@click.command("schema", context_settings=CONTEXT_SETTINGS)
@click.argument("table_names", nargs=-1, metavar="[TABLE]...")
@source_option
@click.option(
    "--tables",
    "list_table_names",
    is_flag=True,
    help="List catalog tables in place of their columns.",
)
@click.option(
    "--row-counts",
    is_flag=True,
    help="Include row counts with --tables.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="json",
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
    """Return catalog table names or column schemas."""

    from chartcoach._catalog.introspection import describe_tables, list_tables

    try:
        if list_table_names and table_names:
            raise click.ClickException(
                format_error(
                    "`catalog schema --tables` does not accept table names.",
                    ["Use `chartcoach catalog schema TABLE` to inspect its columns."],
                )
            )
        rows = (
            list_tables(load_catalog(ctx), include_row_counts=row_counts)
            if list_table_names
            else describe_tables(tables=table_names)
        )
    except CatalogError as exc:
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
    default="json",
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
    """Run one bounded read-only SELECT over catalog tables."""

    try:
        result = catalog_sql(load_catalog(ctx), query, limit=limit)
    except CatalogError as exc:
        raise _command_error(exc) from exc
    if output_format == "json":
        emit_object(result)
        return
    emit_rows(result["rows"], output_format=output_format)
    if result["truncated"]:
        echo_warn(f"Returned {limit} rows.", detail="Increase --limit to inspect more.")


def _labels_empty_hints(
    *, family: str | None, prefix: str | None, contains: str | None
) -> list[str]:
    hints = []
    if contains:
        hints.append("Try a shorter or broader --contains term.")
    if family:
        hints.append("Run `chartcoach catalog labels` to inspect label families.")
    if prefix:
        hints.append("Try a shorter --prefix or inspect labels by --family.")
    if not hints:
        hints.append("Run `chartcoach catalog describe` to inspect catalog counts.")
    return hints


def _list_empty_hints(
    labels: Sequence[str],
    label_prefixes: Sequence[str],
    contains: str | None,
) -> list[str]:
    hints = []
    if len(labels) > 1:
        hints.append("Repeated --label filters are all-of. Remove one --label.")
    elif labels:
        hints.append("Run `chartcoach catalog labels` to inspect exact labels.")
    if label_prefixes:
        hints.append("Try a shorter --label-prefix.")
    if contains:
        hints.append("Try a broader --contains term.")
    if not hints:
        hints.append("Run `chartcoach catalog describe` to inspect the catalog.")
    return hints


def _command_error(exc: CatalogError) -> click.ClickException:
    return click.ClickException(str(exc))


def register_navigation_commands(group: click.Group) -> None:
    group.add_command(describe_command)
    group.add_command(labels_command)
    group.add_command(roles_command)
    group.add_command(list_command)
    group.add_command(read_command)
    group.add_command(cite_command)
    group.add_command(schema_command)
    group.add_command(sql_command)


__all__ = ["register_navigation_commands"]
