from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import sys
from collections.abc import Callable, Mapping, Sequence
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from typing import Iterator, TypeVar, cast
from urllib.parse import urlparse, urlunparse

import click
from tabulate import tabulate

from chartcoach.catalog import Catalog, default_catalog_bundle, default_index_path
from chartcoach.catalog.remote import download_catalog_bundle, release_metadata_url
from chartcoach.constants import (
    DEFAULT_CATALOG_ARTIFACT_BASE_URL,
    INDEX_ENV,
    LANCE_DOCUMENT_TABLE,
    SOURCE_ENV,
)
from chartcoach.tools import Tools, format_error

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
ROW_FORMATS = ("table", "json", "jsonl", "csv")
SEARCH_FORMATS = ("table", "json", "jsonl", "csv", "markdown", "compact")

_Command = TypeVar("_Command", bound=Callable[..., object])


def source_option(command: _Command) -> _Command:
    return click.option(
        "--source",
        "source_path",
        envvar=SOURCE_ENV,
        metavar="PATH_OR_URL",
        callback=_remember_source_path,
        expose_value=False,
        help=(
            "Catalog bundle, entries parquet file, authored folder, or metadata URL. "
            f"Defaults to ${SOURCE_ENV}, then {DEFAULT_CATALOG_ARTIFACT_BASE_URL}."
        ),
    )(command)


def required_index_option(command: _Command) -> _Command:
    return click.option(
        "--index",
        "index_path",
        envvar=INDEX_ENV,
        metavar="PATH_OR_URI",
        help=f"LanceDB database path or URI. Defaults to ${INDEX_ENV} when set.",
    )(command)


def require_index_path(
    index_path: str | None,
    *,
    source_path: object | None = None,
    table_name: str = LANCE_DOCUMENT_TABLE,
    use_default: bool = False,
) -> str:
    if index_path is not None:
        return index_path
    if use_default and source_path is None:
        _require_lancedb_available()
        try:
            return str(
                default_index_path(
                    table_name=table_name,
                    reporter=report_cache_download,
                )
            )
        except Exception as exc:
            raise click.ClickException(
                format_error(
                    "Could not resolve the default LanceDB index.",
                    [
                        str(exc),
                        f"Pass --index PATH_OR_URI or set {INDEX_ENV}.",
                    ],
                )
            ) from exc
    source_part = f" --source {source_path}" if source_path is not None else ""
    raise click.ClickException(
        format_error(
            f"Pass --index PATH_OR_URI or set {INDEX_ENV}.",
            [
                (
                    "Build a full-text index with "
                    f"`chartcoach catalog index create{source_part} --index PATH_OR_URI`."
                ),
                "Then pass the same index path to `chartcoach catalog find`.",
                "Use `--mode fts` for a full-text-only index.",
            ],
        )
    )


def _require_lancedb_available() -> None:
    if importlib.util.find_spec("lancedb") is not None:
        return
    raise click.ClickException(
        format_error(
            "LanceDB indexing requires the optional `chartcoach[index]` dependencies.",
            [
                "Install `chartcoach[index]` to use indexed discovery.",
                f"Or pass --index PATH_OR_URI after installing the extra or set {INDEX_ENV}.",
            ],
        )
    )


def _remember_source_path(
    ctx: click.Context,
    _param: click.Parameter,
    value: str | None,
) -> None:
    if value is not None:
        ctx.ensure_object(dict)["source_path"] = value
    return None


def load_catalog(ctx: click.Context) -> Catalog:
    path = source_path(ctx)
    try:
        if path is None:
            return Catalog.from_bundle(default_catalog_bundle(reporter=report_cache_download))
        if _is_http_url(path):
            return Catalog.from_bundle(
                download_catalog_bundle(
                    release_metadata_url(path),
                    reporter=report_cache_download,
                )
            )
        return Catalog.open(path)
    except FileNotFoundError as exc:
        raise click.ClickException(
            format_error(
                f"Catalog source not found: {path}",
                [
                    "Pass --source PATH to the command.",
                    f"Or export {SOURCE_ENV}=PATH.",
                ],
            )
        ) from exc


def tools(ctx: click.Context) -> Tools:
    return Tools(load_catalog(ctx))


def source_path(ctx: click.Context) -> str | None:
    path = cast(Mapping[str, object], ctx.obj or {}).get("source_path")
    if path is None:
        return None
    return cast(str, path)


def report_cache_download(kind: str, source: str, target: Path) -> None:
    name = "catalog" if kind == "catalog" else "LanceDB index"
    echo_info(
        f"Downloading ChartCoach {name}",
        detail=f"from {_display_source(source)}",
        err=True,
    )
    echo_info("Cache", detail=str(target), err=True)


def echo_info(message: str, *, detail: str | None = None, err: bool = True) -> None:
    _echo_status(message, detail=detail, fg="cyan", err=err)


def echo_success(message: str, *, detail: str | None = None, err: bool = False) -> None:
    _echo_status(message, detail=detail, fg="green", err=err)


def echo_warn(message: str, *, detail: str | None = None, err: bool = True) -> None:
    _echo_status(message, detail=detail, fg="yellow", err=err)


def _echo_status(
    message: str,
    *,
    detail: str | None,
    fg: str,
    err: bool,
) -> None:
    text = click.style(message, fg=fg)
    if detail is not None:
        text += f" {detail}"
    click.echo(text, err=err)


def emit_rows(
    rows: Sequence[Mapping[str, object]],
    *,
    output_format: str,
    empty_message: str = "0 rows",
) -> None:
    if output_format == "json":
        click.echo(json.dumps(list(rows), indent=2, ensure_ascii=False, default=str))
    elif output_format == "jsonl":
        for row in rows:
            click.echo(json.dumps(row, ensure_ascii=False, default=str))
    elif output_format == "csv":
        click.echo(rows_to_csv(rows, delimiter=",").rstrip())
    elif not rows:
        click.echo(empty_message)
    else:
        click.echo(rows_to_table(rows).rstrip())


def rows_to_table(rows: Sequence[Mapping[str, object]]) -> str:
    if not rows:
        return ""
    normalized = [
        {key: format_cell(value, human=True) for key, value in row.items()}
        for row in rows
    ]
    return tabulate(
        normalized,
        headers="keys",
        tablefmt="plain",
        disable_numparse=True,
    )


def emit_object(value: object, *, output_format: str) -> None:
    if output_format == "jsonl":
        click.echo(json.dumps(value, ensure_ascii=False, default=str))
    else:
        click.echo(json.dumps(value, indent=2, ensure_ascii=False, default=str))


def rows_to_csv(
    rows: Sequence[Mapping[str, object]],
    *,
    delimiter: str,
    human: bool = False,
) -> str:
    if not rows:
        return ""
    output = io.StringIO()
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    for row in rows:
        writer.writerow(
            {key: format_cell(value, human=human) for key, value in row.items()}
        )
    return output.getvalue()


def format_cell(value: object, *, human: bool = False) -> object:
    if human and isinstance(value, list):
        return ", ".join(str(item) for item in value)
    if human and isinstance(value, dict):
        return ", ".join(f"{key}={item}" for key, item in value.items())
    if isinstance(value, list | dict):
        return json.dumps(value, ensure_ascii=False, default=str)
    return value


def _is_http_url(value: str) -> bool:
    return urlparse(value).scheme in {"http", "https"}


def _display_source(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme not in {"http", "https"} or parsed.hostname is None:
        return source
    netloc = parsed.hostname
    if parsed.port is not None:
        netloc = f"{netloc}:{parsed.port}"
    name = PurePosixPath(parsed.path).name
    path = f"/.../{name}" if name else ""
    return urlunparse((parsed.scheme, netloc, path, "", "", ""))


def search_cli_error(
    message: str,
    *,
    index_path: str | None = None,
    table_name: str = LANCE_DOCUMENT_TABLE,
) -> str:
    """Return a CLI search error with local index-path recovery hints."""

    return format_error(
        message,
        [
            *_index_path_hints(index_path, table_name=table_name),
            (
                "Build a full-text LanceDB table with "
                "`chartcoach catalog index create --source PATH --index PATH`."
            ),
            "Pass the same index path to `chartcoach catalog find --mode fts`.",
            (
                "Use `chartcoach catalog index create --embedding ...` when vector "
                "or hybrid search is required."
            ),
        ],
    )


def _index_path_hints(index_path: str | None, *, table_name: str) -> list[str]:
    local_path = _local_index_path(index_path)
    if local_path is None or not local_path.is_dir():
        return []

    table_dir = f"{table_name}.lance"
    child_indexes = [
        child
        for child in sorted(local_path.iterdir(), key=str)
        if child.is_dir() and (child / table_dir).is_dir()
    ]
    if not child_indexes:
        return []

    if len(child_indexes) == 1:
        return [
            (
                f"Found table {table_name!r} under {child_indexes[0]}. "
                f"Pass `--index {child_indexes[0]}`."
            )
        ]
    formatted = ", ".join(str(path) for path in child_indexes)
    return [
        (
            f"Found table {table_name!r} under child index directories: {formatted}. "
            "Pass one of those paths with `--index`."
        )
    ]


def _local_index_path(index_path: str | None) -> Path | None:
    if index_path is None:
        return None
    parsed = urlparse(index_path)
    if parsed.scheme:
        return None
    return Path(index_path)


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
        lines.append(f"- matched document role: `{row.get('matched_role')}`")
        lines.append(f"- retrieval hint: {retrieval_hint(row.get('matched_role'))}")
        lines.append(f"- matched document: `{row.get('matched_document_id')}`")
        lines.append(f"- score: `{row.get('score')}`")
        lines.append("")
        lines.append(str(row.get("matched_text") or ""))
        lines.append("")
    return "\n".join(lines)


def guideline_search_rows_to_compact_markdown(
    rows: Sequence[Mapping[str, object]],
    *,
    text_limit: int = 360,
) -> str:
    lines: list[str] = []
    for row in rows:
        lines.append(f"{row['rank']}. `{row['id']}` - {row.get('title')}")
        description = str(row.get("description") or "")
        if description:
            lines.append(f"   {description}")
        labels = row.get("labels")
        if labels:
            lines.append(
                "   labels: "
                + ", ".join(f"`{label}`" for label in cast(list[str], labels))
            )
        lines.append(
            "   match: "
            f"document role `{row.get('matched_role')}` "
            f"({retrieval_hint(row.get('matched_role'))}), "
            f"from `{row.get('matched_document_id')}`, "
            f"score `{row.get('score')}`"
        )
        matched = " ".join(truncate(row.get("matched_text") or "", text_limit).split())
        if matched:
            lines.append(f"   text: {matched}")
        lines.append("")
    return "\n".join(lines)


@contextmanager
def quiet_runtime_stderr() -> Iterator[None]:
    """Suppress noisy native stderr output during successful CLI operations."""

    sys.stderr.flush()
    old_fd = os.dup(2)
    try:
        with open(os.devnull, "w", encoding="utf-8") as devnull:
            os.dup2(devnull.fileno(), 2)
            yield
    finally:
        sys.stderr.flush()
        os.dup2(old_fd, 2)
        os.close(old_fd)


def truncate(value: object, limit: int) -> str:
    text = "" if value is None else str(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def retrieval_hint(role: object) -> str:
    if not isinstance(role, str) or not role:
        return "retrieve by guideline id or a manifest section role"
    prefix = "section."
    if role.startswith(prefix):
        return f"retrieve section `{role.removeprefix(prefix)}`"
    return "retrieve by guideline id or a manifest section role"
