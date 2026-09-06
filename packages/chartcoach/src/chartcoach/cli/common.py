from __future__ import annotations

import json
from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, TypeVar, cast

import click
from tabulate import tabulate

from chartcoach.catalog import open_catalog
from chartcoach.catalog.errors import CatalogError
from chartcoach.constants import (
    CATALOG_SOURCE_ENV,
    INDEX_PROFILE_ENV,
)

if TYPE_CHECKING:
    from chartcoach.catalog.model import Catalog

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
ROW_FORMATS = ("table", "json")
SEARCH_FORMATS = ("table", "json", "markdown")
HUMAN_TABLE_FORMAT = "rounded_outline"
HUMAN_TABLE_COLUMN_WIDTHS = {
    "id": 32,
    "name": 28,
    "value": 72,
    "title": 36,
    "description": 48,
    "labels": 38,
    "matches": 52,
    "matched_excerpt": 52,
    "content": 52,
    "text": 52,
    "source": 40,
    "url": 44,
}
HEADER_INITIALISMS = {
    "api",
    "doi",
    "id",
    "json",
    "mcp",
    "sql",
    "url",
}
_Command = TypeVar("_Command", bound=Callable[..., object])


def source_option(command: _Command) -> _Command:
    return click.option(
        "--source",
        "source_path",
        envvar=CATALOG_SOURCE_ENV,
        metavar="PATH_OR_URI",
        callback=_remember_source_path,
        expose_value=False,
        help=(
            "Catalog source: authored folder, bundle, deployed root, catalog.json, or "
            "release.json path or URI. "
            f"Defaults to ${CATALOG_SOURCE_ENV}, then the official catalog."
        ),
    )(command)


def index_profile_option(command: _Command) -> _Command:
    return click.option(
        "--profile",
        envvar=INDEX_PROFILE_ENV,
        required=True,
        help=(
            "Index profile in the catalog release. "
            f"Defaults to ${INDEX_PROFILE_ENV} when set."
        ),
    )(command)


def _remember_source_path(
    ctx: click.Context,
    _param: click.Parameter,
    value: str | None,
) -> None:
    if value is not None:
        ctx.ensure_object(dict)["source_path"] = value


def load_catalog(
    ctx: click.Context,
    *,
    source: str | None = None,
) -> Catalog:
    source = source_path(ctx) if source is None else source
    try:
        return open_catalog(source)
    except ModuleNotFoundError as exc:
        raise click.ClickException(str(exc)) from exc
    except (CatalogError, OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc


@contextmanager
def storage_errors(operation: str, target: str) -> Iterator[None]:
    """Render installed object-store backend failures as CLI errors."""

    try:
        from obspec.exceptions import BaseError as ObspecError
        from obspec.exceptions import map_exception
        from obstore.exceptions import BaseError as ObstoreError
    except ModuleNotFoundError:
        yield
        return
    try:
        yield
    except Exception as exc:
        mapped = map_exception(exc)
        if not isinstance(mapped, ObspecError | ObstoreError):
            raise
        raise click.ClickException(
            f"Object-store {operation} failed for {target}: {mapped}"
        ) from exc


def source_path(ctx: click.Context) -> str | None:
    path = cast(Mapping[str, object], ctx.obj or {}).get("source_path")
    return cast(str | None, path)


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
    empty_hints: Sequence[str] = (),
) -> None:
    if output_format == "json":
        click.echo(json.dumps(list(rows), indent=2, ensure_ascii=False, default=str))
    elif not rows:
        click.echo(empty_message)
    else:
        click.echo(rows_to_table(rows).rstrip())
    if not rows and empty_hints:
        emit_guidance(
            empty_message,
            empty_hints,
            include_message=output_format == "json",
        )


def emit_guidance(
    message: str,
    hints: Sequence[str],
    *,
    include_message: bool = True,
) -> None:
    if include_message:
        click.echo(f"{message}\n\nGuidance:", err=True)
    else:
        click.echo("Guidance:", err=True)
    for hint in hints:
        click.echo(f"  - {hint}", err=True)


def rows_to_table(rows: Sequence[Mapping[str, object]]) -> str:
    if not rows:
        return ""
    keys = _table_keys(rows)
    normalized = [
        [format_cell(row.get(key), human=True) for key in keys] for row in rows
    ]
    table = cast(Any, tabulate)(
        normalized,
        headers=[human_table_header(key) for key in keys],
        tablefmt=HUMAN_TABLE_FORMAT,
        colalign=("left",) * len(keys),
        disable_numparse=True,
        maxcolwidths=[HUMAN_TABLE_COLUMN_WIDTHS.get(key, 24) for key in keys],
        break_long_words=False,
    )
    return cast(str, table)


def _table_keys(rows: Sequence[Mapping[str, object]]) -> list[str]:
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    return keys


def human_table_header(key: str) -> str:
    return " ".join(_human_table_header_part(part) for part in key.split("_"))


def _human_table_header_part(part: str) -> str:
    if part.lower() in HEADER_INITIALISMS:
        return part.upper()
    return part.capitalize()


def emit_object(value: object) -> None:
    click.echo(json.dumps(value, indent=2, ensure_ascii=False, default=str))


def format_cell(value: object, *, human: bool = False) -> object:
    if human and isinstance(value, list):
        return ", ".join(str(item) for item in value)
    if human and isinstance(value, dict):
        return ", ".join(f"{key}={item}" for key, item in value.items())
    if isinstance(value, list | dict):
        return json.dumps(value, ensure_ascii=False, default=str)
    return value


def guideline_matches_to_markdown(matches: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for match in matches:
        lines.append(f"### {match['rank']}. {match['id']}")
        lines.append("")
        lines.append(f"**{match.get('title')}**")
        lines.append("")
        lines.append(str(match.get("description") or ""))
        lines.append("")
        labels = match.get("labels")
        if labels:
            lines.append(
                "Labels: "
                + ", ".join(f"`{label}`" for label in cast(list[str], labels))
            )
            lines.append("")
        lines.append(f"- matched document role: `{match.get('matched_role')}`")
        lines.append(f"- retrieval hint: {retrieval_hint(match.get('matched_role'))}")
        lines.append(f"- matched document: `{match.get('matched_document_id')}`")
        lines.append(f"- score: `{match.get('score')}`")
        lines.append("")
        lines.append(str(match.get("matched_excerpt") or ""))
        lines.append("")
    return "\n".join(lines)


def retrieval_hint(role: object) -> str:
    if not isinstance(role, str) or not role:
        return "retrieve by guideline entry ID or a manifest section role"
    prefix = "section."
    if role.startswith(prefix):
        return f"retrieve section `{role.removeprefix(prefix)}`"
    return "retrieve by guideline entry ID or a manifest section role"
