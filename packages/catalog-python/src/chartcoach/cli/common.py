from __future__ import annotations

import csv
import io
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, cast

import click

from chartcoach.catalog import Catalog
from chartcoach.constants import INDEX_DIR_ENV, SOURCE_ENV
from chartcoach.paths import default_index_dir
from chartcoach.tools.catalog import CatalogTools, format_tool_error

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
ROW_FORMATS = ("table", "json", "jsonl", "csv")
SEARCH_FORMATS = ("table", "json", "jsonl", "csv", "markdown")
SHOW_FORMATS = ("markdown", "json", "jsonl")
RETRIEVE_FORMATS = ("markdown", "json", "jsonl", "csv", "table")


def source_option(command: Any) -> Any:
    return click.option(
        "--source",
        "source_path",
        envvar=SOURCE_ENV,
        type=click.Path(path_type=Path),
        callback=_remember_source_path,
        expose_value=False,
        help=f"Catalog parquet file or guideline folder. Defaults to ${SOURCE_ENV} when set.",
    )(command)


def index_dir_option(command: Any) -> Any:
    return click.option(
        "--index-dir",
        envvar=INDEX_DIR_ENV,
        type=click.Path(file_okay=False, path_type=Path),
        default=default_index_dir(),
        show_default=True,
        help=(
            "Search index directory. Optional for catalog-only commands. "
            f"defaults to ${INDEX_DIR_ENV}, then a platform cache path."
        ),
    )(command)


def required_index_dir_option(command: Any) -> Any:
    return click.option(
        "--index-dir",
        envvar=INDEX_DIR_ENV,
        type=click.Path(file_okay=False, path_type=Path),
        default=default_index_dir(),
        show_default=True,
        help=f"Search index directory. Defaults to ${INDEX_DIR_ENV}, then a platform cache path.",
    )(command)


def duckdb_option(command: Any) -> Any:
    return click.option(
        "--duckdb",
        "duckdb_path",
        type=click.Path(dir_okay=False, path_type=Path),
        help="DuckDB database file to advertise when listing artifacts.",
    )(command)


def _remember_source_path(
    ctx: click.Context,
    _param: click.Parameter,
    value: Path | None,
) -> None:
    if value is not None:
        ctx.ensure_object(dict)["source_path"] = value
    return None


def load_catalog(ctx: click.Context) -> Catalog:
    path = source_path(ctx)
    try:
        return Catalog.from_source(path)
    except FileNotFoundError as exc:
        raise click.ClickException(
            format_tool_error(
                f"Catalog source not found: {path}",
                [
                    "Pass --source PATH to the command.",
                    f"Or export {SOURCE_ENV}=PATH.",
                ],
            )
        ) from exc


def catalog_tools(ctx: click.Context) -> CatalogTools:
    return CatalogTools(load_catalog(ctx))


def source_path(ctx: click.Context) -> Path:
    path = cast(Mapping[str, object], ctx.obj or {}).get("source_path")
    if path is None:
        raise click.ClickException(
            format_tool_error(
                f"Pass --source PATH or set {SOURCE_ENV}.",
                [
                    "Provide a catalog bundle, catalog parquet file, or authored guideline folder.",
                    f"Or export {SOURCE_ENV}=PATH.",
                ],
            )
        )
    return cast(Path, path)


def emit_rows(rows: Sequence[Mapping[str, object]], *, output_format: str) -> None:
    if output_format == "json":
        click.echo(json.dumps(list(rows), indent=2, ensure_ascii=False, default=str))
    elif output_format == "jsonl":
        for row in rows:
            click.echo(json.dumps(row, ensure_ascii=False, default=str))
    elif output_format == "csv":
        click.echo(rows_to_csv(rows, delimiter=",").rstrip())
    else:
        click.echo(rows_to_csv(rows, delimiter="\t").rstrip())


def emit_object(value: object, *, output_format: str) -> None:
    if output_format == "jsonl":
        click.echo(json.dumps(value, ensure_ascii=False, default=str))
    else:
        click.echo(json.dumps(value, indent=2, ensure_ascii=False, default=str))


def rows_to_csv(rows: Sequence[Mapping[str, object]], *, delimiter: str) -> str:
    if not rows:
        return ""
    output = io.StringIO()
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    for row in rows:
        writer.writerow({key: format_cell(value) for key, value in row.items()})
    return output.getvalue()


def format_cell(value: object) -> object:
    if isinstance(value, list | dict):
        return json.dumps(value, ensure_ascii=False, default=str)
    return value


def evidence_packets_to_markdown(packets: Sequence[Mapping[str, object]]) -> str:
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


def guideline_search_rows_to_markdown(rows: Sequence[Mapping[str, object]]) -> str:
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
        lines.append(f"- matched section: `{row.get('matched_role')}`")
        lines.append(f"- matched document: `{row.get('matched_document_id')}`")
        lines.append(f"- score: `{row.get('score')}`")
        lines.append("")
        lines.append(str(row.get("matched_text") or ""))
        lines.append("")
    return "\n".join(lines)


def truncate(value: object, limit: int) -> str:
    text = "" if value is None else str(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."
