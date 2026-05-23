from __future__ import annotations

import csv
import io
import json
from collections.abc import Mapping, Sequence
from os import PathLike
from pathlib import Path
from typing import Any, Literal, TypeAlias, cast

import click

from chartcoach.catalog import Catalog
from chartcoach.tools.catalog import (
    CatalogToolError,
    CatalogTools,
    format_tool_error,
    search_error_message,
    sql_error_message,
)
from chartcoach.search.results import flatten_search_result
from chartcoach.search.sql_tools import SqlTools

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
CATALOG_PATH_ENV = "CHARTCOACH_CATALOG_PATH"
ROW_FORMATS = ("table", "json", "jsonl", "csv")
SEARCH_FORMATS = ("table", "json", "jsonl", "csv", "markdown")
SHOW_FORMATS = ("markdown", "json", "jsonl")
RETRIEVE_FORMATS = ("markdown", "json", "jsonl", "csv", "table")
CacheMode: TypeAlias = Literal["reuse_or_create", "reuse_only", "force_rebuild"]


@click.group(
    "catalog",
    context_settings=CONTEXT_SETTINGS,
    help=(
        "Inspect and query a ChartCoach catalog parquet file.\n\n"
        "Pass --catalog once, or set CHARTCOACH_CATALOG_PATH. SQL commands use "
        "only the catalog tables unless --with-search is requested. Semantic "
        "search builds or reuses a separate Chroma cache."
    ),
)
@click.option(
    "--catalog",
    "catalog_path",
    envvar=CATALOG_PATH_ENV,
    type=click.Path(dir_okay=False, path_type=Path),
    help=f"Catalog parquet file. Defaults to ${CATALOG_PATH_ENV}.",
)
@click.pass_context
def catalog_command(ctx: click.Context, catalog_path: Path | None) -> None:
    ctx.obj = {"catalog_path": catalog_path}


@catalog_command.command("info", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def info_command(ctx: click.Context, output_format: str) -> None:
    """Show catalog table counts."""

    _emit_rows(_catalog_tools(ctx).relations(), output_format=output_format)


@catalog_command.command("relations", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def relations_command(ctx: click.Context, output_format: str) -> None:
    """List queryable catalog relations and row counts."""

    _emit_rows(_catalog_tools(ctx).relations(), output_format=output_format)


@catalog_command.command("list", context_settings=CONTEXT_SETTINGS)
@click.option("--label", multiple=True, help="Only include guidelines with this label.")
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
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """List guideline ids and summaries."""

    rows = _catalog_tools(ctx).list_guidelines(
        labels=label,
        contains=contains,
        limit=limit,
    )
    _emit_rows(rows, output_format=output_format)


@catalog_command.command("schema", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--relation",
    multiple=True,
    help="Only include this relation. Can be passed more than once.",
)
@click.option(
    "--with-search",
    is_flag=True,
    help="Also include the Chroma embeddings relation.",
)
@click.option(
    "--cache-dir",
    type=click.Path(file_okay=False, path_type=Path),
    help="Chroma cache root used with --with-search.",
)
@click.option(
    "--cache-mode",
    type=click.Choice(("reuse_or_create", "reuse_only", "force_rebuild")),
    default="reuse_or_create",
    show_default=True,
    help="Chroma cache behavior used with --with-search.",
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
    relation: tuple[str, ...],
    with_search: bool,
    cache_dir: Path | None,
    cache_mode: CacheMode,
    output_format: str,
) -> None:
    """List SQL relation columns without guessing table names."""

    tools = _catalog_tools(ctx)
    try:
        if with_search:
            with _open_search_session(
                tools.catalog,
                cache_dir=cache_dir,
                cache_mode=cache_mode,
            ) as session:
                rows = session.sql_tools.schema(relations=relation)
        else:
            from chartcoach.search.sql import connect_catalog

            conn = connect_catalog(tools.catalog)
            try:
                rows = SqlTools(conn).schema(relations=relation)
            finally:
                conn.close()
    except Exception as exc:
        hints = [
            "Run relations first to inspect structured catalog relations.",
            "Use --with-search only when you also need the embeddings relation.",
        ]
        if with_search:
            hints.append(
                "Use --cache-mode reuse_or_create to build the Chroma cache if it is missing."
            )
        raise click.ClickException(
            format_tool_error(
                str(exc),
                hints,
            )
        ) from exc
    _emit_rows(rows, output_format=output_format)


@catalog_command.command("values", context_settings=CONTEXT_SETTINGS)
@click.argument("relation")
@click.argument("column")
@click.option(
    "--explode",
    is_flag=True,
    help="Explode list-valued cells before counting distinct values.",
)
@click.option(
    "--contains",
    help="Case-insensitive substring filter over the rendered value.",
)
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
    relation: str,
    column: str,
    explode: bool,
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """Count distinct values in any structured catalog relation column."""

    try:
        rows = _catalog_tools(ctx).values(
            relation=relation,
            column=column,
            explode=explode,
            contains=contains,
            limit=limit,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    _emit_rows(rows, output_format=output_format)


@catalog_command.command("show", context_settings=CONTEXT_SETTINGS)
@click.argument("guideline_id")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(SHOW_FORMATS),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def show_command(
    ctx: click.Context,
    guideline_id: str,
    output_format: str,
) -> None:
    """Print one guideline by id."""

    try:
        entry = _catalog_tools(ctx).get_guideline(guideline_id)
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc

    if output_format == "json":
        click.echo(json.dumps(entry, indent=2, ensure_ascii=False))
    elif output_format == "jsonl":
        click.echo(json.dumps(entry, ensure_ascii=False))
    else:
        click.echo(
            _load_catalog(ctx).get(guideline_id).guideline.to_markdown().rstrip()
        )


@catalog_command.command("retrieve", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--id",
    "guideline_ids",
    multiple=True,
    help="Include this guideline id. Can be passed more than once.",
)
@click.option(
    "--label",
    multiple=True,
    help="Require this exact label. Can be passed more than once.",
)
@click.option(
    "--label-prefix",
    multiple=True,
    help="Require at least one label with this prefix. Can be passed more than once.",
)
@click.option(
    "--contains",
    help="Case-insensitive substring filter over id, title, description, and body.",
)
@click.option(
    "--role",
    multiple=True,
    help="Include only these section roles. Can be passed more than once.",
)
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=12,
    show_default=True,
    help="Maximum guidelines to print.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(RETRIEVE_FORMATS),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def retrieve_command(
    ctx: click.Context,
    guideline_ids: tuple[str, ...],
    label: tuple[str, ...],
    label_prefix: tuple[str, ...],
    contains: str | None,
    role: tuple[str, ...],
    limit: int,
    output_format: str,
) -> None:
    """Retrieve guideline records with optional section filtering."""

    try:
        packets = _catalog_tools(ctx).retrieve_guidelines(
            ids=guideline_ids,
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            roles=role,
            limit=limit,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    if output_format == "markdown":
        click.echo(_evidence_packets_to_markdown(packets).rstrip())
    elif output_format == "json":
        click.echo(json.dumps(packets, indent=2, ensure_ascii=False))
    elif output_format == "jsonl":
        for packet in packets:
            click.echo(json.dumps(packet, ensure_ascii=False))
    else:
        rows: list[dict[str, object]] = []
        for packet in packets:
            sections = cast(
                Sequence[Mapping[str, object]], packet.get("sections") or ()
            )
            rows.append(
                {
                    "id": packet["id"],
                    "title": packet["title"],
                    "description": packet["description"],
                    "labels": packet["labels"],
                    "sections": [section.get("role") for section in sections],
                }
            )
        _emit_rows(rows, output_format=output_format)


@catalog_command.command("sql", context_settings=CONTEXT_SETTINGS)
@click.argument("sql")
@click.option(
    "--with-search",
    is_flag=True,
    help="Also register the Chroma embeddings table before running SQL.",
)
@click.option(
    "--cache-dir",
    type=click.Path(file_okay=False, path_type=Path),
    help="Chroma cache root used with --with-search.",
)
@click.option(
    "--cache-mode",
    type=click.Choice(("reuse_or_create", "reuse_only", "force_rebuild")),
    default="reuse_or_create",
    show_default=True,
    help="Chroma cache behavior used with --with-search.",
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
def sql_command(
    ctx: click.Context,
    sql: str,
    with_search: bool,
    cache_dir: Path | None,
    cache_mode: CacheMode,
    limit: int,
    output_format: str,
) -> None:
    """Run DuckDB SQL over catalog tables."""

    catalog = _load_catalog(ctx)
    session = None
    try:
        if with_search:
            session = _open_search_session(
                catalog,
                cache_dir=cache_dir,
                cache_mode=cache_mode,
            )
            result = session.tools.sql(sql, row_limit=limit)
        else:
            from chartcoach.search.sql import connect_catalog

            conn = connect_catalog(catalog)
            try:
                result = SqlTools(conn).sql(sql, row_limit=limit)
            finally:
                conn.close()
    except Exception as exc:
        raise click.ClickException(sql_error_message(str(exc))) from exc
    finally:
        if session is not None:
            session.close()

    if output_format == "json":
        click.echo(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        _emit_rows(
            cast(list[dict[str, object]], result["rows"]), output_format=output_format
        )


@catalog_command.command("search", context_settings=CONTEXT_SETTINGS)
@click.argument("query")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=8,
    show_default=True,
    help="Maximum semantic matches to print.",
)
@click.option(
    "--where",
    help="Chroma metadata filter JSON.",
)
@click.option(
    "--where-document",
    help="Chroma document filter JSON.",
)
@click.option(
    "--level",
    type=click.Choice(("guideline", "document")),
    default="guideline",
    show_default=True,
    help="Return deduplicated guidelines or raw indexed documents.",
)
@click.option(
    "--role",
    multiple=True,
    help="Guideline-level search only: keep matches from these roles.",
)
@click.option(
    "--label",
    multiple=True,
    help="Guideline-level search only: require this exact label.",
)
@click.option(
    "--label-prefix",
    multiple=True,
    help="Guideline-level search only: require at least one label with this prefix.",
)
@click.option(
    "--cache-dir",
    type=click.Path(file_okay=False, path_type=Path),
    help="Chroma cache root.",
)
@click.option(
    "--cache-mode",
    type=click.Choice(("reuse_or_create", "reuse_only", "force_rebuild")),
    default="reuse_or_create",
    show_default=True,
    help="Chroma cache behavior.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(SEARCH_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def search_command(
    ctx: click.Context,
    query: str,
    limit: int,
    where: str | None,
    where_document: str | None,
    level: str,
    role: tuple[str, ...],
    label: tuple[str, ...],
    label_prefix: tuple[str, ...],
    cache_dir: Path | None,
    cache_mode: CacheMode,
    output_format: str,
) -> None:
    """Semantically search indexed guideline documents."""

    catalog = _load_catalog(ctx)
    if level == "guideline":
        try:
            CatalogTools(catalog).validate_guideline_filters(
                labels=label,
                label_prefixes=label_prefix,
            )
        except CatalogToolError as exc:
            raise click.ClickException(str(exc)) from exc
        if where is not None or where_document is not None:
            raise click.ClickException(
                format_tool_error(
                    "--where and --where-document are only available with --level document.",
                    [
                        "Use --level document when you need raw Chroma metadata filters.",
                        "Use --label, --label-prefix, or --role for guideline-level filtering.",
                    ],
                )
            )
    else:
        role = ()
    try:
        with _open_search_session(
            catalog,
            cache_dir=cache_dir,
            cache_mode=cache_mode,
        ) as session:
            if level == "guideline":
                result = session.tools.search_guidelines(
                    query,
                    limit=limit,
                    roles=role or None,
                    labels=label or None,
                    label_prefixes=label_prefix or None,
                )
            else:
                result = session.tools.search(
                    query,
                    limit=limit,
                    where=_parse_json_object(where, "--where"),
                    where_document=_parse_json_object(
                        where_document, "--where-document"
                    ),
                )
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc

    if output_format == "json":
        click.echo(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if level == "guideline":
        rows = cast(list[dict[str, object]], result["rows"])
        if output_format == "markdown":
            click.echo(_guideline_search_rows_to_markdown(rows).rstrip())
        else:
            _emit_rows(rows, output_format=output_format)
        return

    rows = _flatten_search_result(result)
    if output_format == "markdown":
        click.echo(_search_rows_to_markdown(rows).rstrip())
    else:
        _emit_rows(rows, output_format=output_format)


def _open_search_session(
    catalog: Catalog,
    *,
    cache_dir: str | PathLike[str] | None,
    cache_mode: CacheMode,
) -> Any:
    from chartcoach.search.session import open_search_session

    return open_search_session(
        catalog,
        cache_dir=cache_dir,
        cache_mode=cache_mode,
    )


def _load_catalog(ctx: click.Context) -> Catalog:
    path = _catalog_path(ctx)
    try:
        return Catalog.from_parquet(path)
    except FileNotFoundError as exc:
        raise click.ClickException(
            format_tool_error(
                f"Catalog not found: {path}",
                [
                    "Pass a valid catalog parquet with --catalog PATH.",
                    f"Or export {CATALOG_PATH_ENV}=guidelines/catalog.parquet.",
                ],
            )
        ) from exc


def _catalog_tools(ctx: click.Context) -> CatalogTools:
    return CatalogTools(_load_catalog(ctx))


def _catalog_path(ctx: click.Context) -> Path:
    path = cast(Mapping[str, object], ctx.obj or {}).get("catalog_path")
    if path is None:
        raise click.ClickException(
            format_tool_error(
                f"Pass --catalog PATH or set {CATALOG_PATH_ENV}.",
                [
                    "Example: chartcoach catalog --catalog guidelines/catalog.parquet relations",
                    f"Or export {CATALOG_PATH_ENV}=guidelines/catalog.parquet.",
                ],
            )
        )
    return cast(Path, path)


def _parse_json_object(value: str | None, option_name: str) -> dict[str, Any] | None:
    if value is None:
        return None
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise click.BadParameter(str(exc), param_hint=option_name) from exc
    if not isinstance(parsed, dict):
        raise click.BadParameter("must be a JSON object", param_hint=option_name)
    return cast(dict[str, Any], parsed)


def _evidence_packets_to_markdown(packets: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for packet in packets:
        lines.append(f"## {packet['id']}")
        lines.append("")
        lines.append(f"**{packet['title']}**")
        lines.append("")
        lines.append(str(packet["description"]))
        lines.append("")
        labels = packet.get("labels")
        if labels:
            lines.append(
                "Labels: "
                + ", ".join(f"`{label}`" for label in cast(list[str], labels))
            )
            lines.append("")
        for section in cast(list[Mapping[str, str]], packet.get("sections") or []):
            lines.append(f"### {section['role']}: {section['title']}")
            lines.append("")
            lines.append(section["content"].strip())
            lines.append("")
    return "\n".join(lines)


def _emit_rows(rows: Sequence[Mapping[str, object]], *, output_format: str) -> None:
    if output_format == "json":
        click.echo(json.dumps(list(rows), indent=2, ensure_ascii=False))
    elif output_format == "jsonl":
        for row in rows:
            click.echo(json.dumps(row, ensure_ascii=False))
    elif output_format == "csv":
        click.echo(_rows_to_csv(rows, delimiter=",").rstrip())
    else:
        click.echo(_rows_to_csv(rows, delimiter="\t").rstrip())


def _rows_to_csv(rows: Sequence[Mapping[str, object]], *, delimiter: str) -> str:
    if not rows:
        return ""
    output = io.StringIO()
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    for row in rows:
        writer.writerow({key: _format_cell(value) for key, value in row.items()})
    return output.getvalue()


def _format_cell(value: object) -> object:
    if isinstance(value, list | dict):
        return json.dumps(value, ensure_ascii=False)
    return value


def _flatten_search_result(result: Mapping[str, Any]) -> list[dict[str, object]]:
    return [
        {
            "query": row.query_index,
            "rank": row.rank,
            "id": row.document_id,
            "guideline_id": row.guideline_id,
            "role": row.role,
            "distance": row.distance,
            "labels": row.labels,
            "document": _truncate(row.document, 240),
        }
        for row in flatten_search_result(result)
    ]


def _search_rows_to_markdown(rows: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for row in rows:
        lines.append(f"### {row['rank']}. {row.get('guideline_id') or row['id']}")
        lines.append("")
        lines.append(f"- document: `{row['id']}`")
        lines.append(f"- role: `{row.get('role')}`")
        lines.append(f"- distance: `{row.get('distance')}`")
        labels = row.get("labels")
        if labels:
            lines.append(f"- labels: {labels}")
        lines.append("")
        lines.append(str(row.get("document") or ""))
        lines.append("")
    return "\n".join(lines)


def _guideline_search_rows_to_markdown(rows: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for row in rows:
        lines.append(f"### {row['rank']}. {row['id']}")
        lines.append("")
        lines.append(f"**{row.get('title')}**")
        lines.append("")
        lines.append(str(row.get("description") or ""))
        lines.append("")
        labels = row.get("labels")
        if labels:
            lines.append(
                "Labels: "
                + ", ".join(f"`{label}`" for label in cast(list[str], labels))
            )
            lines.append("")
        lines.append(f"- matched role: `{row.get('matched_role')}`")
        lines.append(f"- matched document: `{row.get('matched_document_id')}`")
        lines.append(f"- distance: `{row.get('distance')}`")
        lines.append("")
        lines.append(str(row.get("matched_text") or ""))
        lines.append("")
    return "\n".join(lines)


def _truncate(value: object, limit: int) -> str:
    text = "" if value is None else str(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


__all__ = ["catalog_command"]
