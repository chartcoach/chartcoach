from __future__ import annotations

from collections.abc import Mapping
import json
from typing import cast

import click

from chartcoach.catalog.errors import CatalogError
from chartcoach.catalog.references import (
    DEFAULT_GUIDELINE_URL_TEMPLATE,
    citation_records,
)
from chartcoach.catalog.introspection import (
    count_values,
    describe_tables,
    list_tables,
    parse_value_field,
)
from chartcoach.catalog.query import (
    query_entries,
    text_matches_for_entry,
)
from chartcoach.catalog.read import retrieve_entry_records
from chartcoach.catalog.summary import (
    catalog_overview,
    list_labels,
    list_roles,
    overview_table_rows,
)
from chartcoach.tools import ToolError, format_error

from ..common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    echo_warn,
    emit_object,
    emit_rows,
    load_catalog,
    source_option,
    source_path,
)
from .rendering import citation_records_to_markdown, entry_records_to_markdown

READ_FORMATS = ("markdown", "json", "jsonl")
CITE_FORMATS = ("markdown", "json", "jsonl")


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
@click.option(
    "--show-matches",
    is_flag=True,
    help="Include text-filter match evidence in query results.",
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
    show_matches: bool,
) -> None:
    """Filter entries with composable base predicates."""

    try:
        frame = query_entries(
            load_catalog(ctx),
            ids=entry_ids,
            labels=labels,
            any_labels=any_labels,
            label_prefixes=label_prefixes,
            contains=contains,
            body_contains=body_contains,
            section_contains=section_contains,
            limit=limit,
            include_body=show_matches,
        )
        if show_matches:
            rows = [
                _query_row_with_matches(
                    row,
                    output_format=output_format,
                    contains=contains,
                    body_contains=body_contains,
                    section_contains=section_contains,
                )
                for row in frame.to_dicts()
            ]
        else:
            rows = frame.select("id", "title", "description", "labels").to_dicts()
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    emit_rows(
        rows,
        output_format=output_format,
        empty_message="No entries matched.",
        empty_hints=_query_empty_hints(
            labels=labels,
            any_labels=any_labels,
            label_prefixes=label_prefixes,
            contains=contains,
            body_contains=body_contains,
            section_contains=section_contains,
        ),
    )


def _query_row_with_matches(
    row: Mapping[str, object],
    *,
    output_format: str,
    contains: str | None,
    body_contains: str | None,
    section_contains: str | None,
) -> dict[str, object]:
    matches = text_matches_for_entry(
        row,
        contains=contains,
        body_contains=body_contains,
        section_contains=section_contains,
    )
    output: dict[str, object] = {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "labels": row["labels"],
    }
    output["matches"] = _match_summary(matches) if output_format == "table" else matches
    return output


def _match_summary(matches: list[dict[str, object]]) -> str:
    parts = []
    for match in matches[:3]:
        field = str(match.get("field") or "")
        if field.startswith("section."):
            role = str(match.get("role") or "section")
            field = f"{role}.{field.removeprefix('section.')}"
        parts.append(f"{field}: {match.get('snippet')}")
    if len(matches) > 3:
        parts.append(f"+{len(matches) - 3} more")
    return " | ".join(parts)


def _labels_empty_hints(
    *,
    family: str | None,
    prefix: str | None,
    contains: str | None,
) -> list[str]:
    hints = []
    if contains:
        hints.append("Try a shorter or broader --contains term.")
        hints.append(
            "Run `chartcoach catalog query --section-contains TEXT --format jsonl` when the concept may appear in guideline sections."
        )
    if family:
        hints.append(
            "Run `chartcoach catalog labels --format jsonl` to inspect all label families."
        )
    if prefix:
        hints.append("Try a shorter --prefix or inspect labels by --family.")
    if not hints:
        hints.append("Run `chartcoach catalog overview --format json` to inspect catalog counts.")
    return hints


def _list_empty_hints(
    *,
    labels: tuple[str, ...],
    label_prefixes: tuple[str, ...],
    contains: str | None,
) -> list[str]:
    hints = []
    if len(labels) > 1:
        hints.append(
            "Repeated --label filters are all-of. Remove one --label or use `chartcoach catalog query --any-label LABEL --any-label OTHER`."
        )
    elif labels:
        hints.append("Try `chartcoach catalog labels --contains TEXT --format jsonl` to find related labels.")
    if label_prefixes:
        hints.append("Try a shorter --label-prefix or inspect labels with `chartcoach catalog labels --format jsonl`.")
    if contains:
        hints.append(
            "Try a broader --contains term, or use `chartcoach catalog query --body-contains TEXT --format jsonl` for full body text."
        )
    if not hints:
        hints.append("Run `chartcoach catalog overview --format json` to confirm the catalog has entries.")
    return hints


def _query_empty_hints(
    *,
    labels: tuple[str, ...],
    any_labels: tuple[str, ...],
    label_prefixes: tuple[str, ...],
    contains: str | None,
    body_contains: str | None,
    section_contains: str | None,
) -> list[str]:
    hints = []
    if len(labels) > 1:
        hints.append(
            "Repeated --label filters are all-of. Relax one --label or use repeated --any-label for alternatives."
        )
    elif labels:
        hints.append("Try `chartcoach catalog labels --contains TEXT --format jsonl` to find broader labels.")
    if any_labels:
        hints.append("Remove one --any-label or inspect label families with `chartcoach catalog labels --format jsonl`.")
    if label_prefixes:
        hints.append("Try a shorter --label-prefix or inspect current labels with `chartcoach catalog labels --format jsonl`.")
    if contains or body_contains or section_contains:
        hints.append(
            "Relax one text predicate or try broader --contains, --body-contains, or --section-contains text."
        )
    if not hints:
        hints.append("Run `chartcoach catalog list --format jsonl` to inspect available entries.")
    return hints


def _values_empty_hints(*, field: str, contains: str | None) -> list[str]:
    hints = []
    if contains:
        hints.append("Try a shorter or broader --contains value.")
    hints.append(
        "Use aliases such as labels, roles, label.family, label.category, or label.modifier."
    )
    hints.append(
        "Run `chartcoach catalog schema` before querying a raw TABLE.COLUMN field."
    )
    if "." in field:
        hints.append("Try `chartcoach catalog values labels --contains TEXT` when looking for label values.")
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
    elif output_format == "jsonl":
        for record in records:
            click.echo(json.dumps(record, ensure_ascii=False, default=str))
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
    elif output_format == "jsonl":
        for record in records:
            click.echo(json.dumps(record, ensure_ascii=False, default=str))
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
    """Count values for a field alias or TABLE.COLUMN."""

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
    except (CatalogError, ToolError) as exc:
        raise _command_error(exc) from exc
    visible_rows = rows[:limit]
    emit_rows(
        visible_rows,
        output_format=output_format,
        empty_hints=_values_empty_hints(field=field, contains=contains),
    )
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
        emit_object(result, output_format=output_format)
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
    group.add_command(query_command)
    group.add_command(read_command)
    group.add_command(cite_command)
    group.add_command(schema_command)
    group.add_command(values_command)
    group.add_command(sql_command)


__all__ = ["register_navigation_commands"]
