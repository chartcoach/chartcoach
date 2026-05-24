from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from typing import cast

import click

from chartcoach.search import ChromaIndex, search_guidelines
from chartcoach.tools.catalog import (
    CatalogToolError,
    CatalogTools,
    search_error_message,
)

from .common import (
    CONTEXT_SETTINGS,
    RETRIEVE_FORMATS,
    ROW_FORMATS,
    SEARCH_FORMATS,
    SHOW_FORMATS,
    source_option,
    catalog_tools,
    emit_rows,
    evidence_packets_to_markdown,
    guideline_search_rows_to_markdown,
    load_catalog,
    parse_json_object,
    required_index_dir_option,
)


@click.group(
    "guidelines",
    context_settings=CONTEXT_SETTINGS,
    help="List, read, retrieve, and search guidelines.",
)
def guidelines_command() -> None:
    """List, read, retrieve, and search guidelines."""


@guidelines_command.command("list", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option("--label", multiple=True, help="Only include guidelines with this label.")
@click.option(
    "--label-prefix",
    multiple=True,
    help="Only include guidelines with a label starting with this prefix.",
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
    """List guideline ids and summaries."""

    try:
        rows = catalog_tools(ctx).list_guidelines(
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            limit=limit,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(rows, output_format=output_format)


@guidelines_command.command("show", context_settings=CONTEXT_SETTINGS)
@source_option
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

    catalog = load_catalog(ctx)
    tools = CatalogTools(catalog)
    try:
        entry = tools.get_guideline(guideline_id)
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc

    if output_format == "json":
        click.echo(json.dumps(entry, indent=2, ensure_ascii=False))
    elif output_format == "jsonl":
        click.echo(json.dumps(entry, ensure_ascii=False))
    else:
        click.echo(catalog.entry(guideline_id).guideline.to_markdown().rstrip())


@guidelines_command.command("retrieve", context_settings=CONTEXT_SETTINGS)
@source_option
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
    "--section",
    "sections",
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
    sections: tuple[str, ...],
    limit: int,
    output_format: str,
) -> None:
    """Retrieve guideline records with optional section filtering."""

    try:
        packets = catalog_tools(ctx).retrieve_guidelines(
            ids=guideline_ids,
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            roles=sections,
            limit=limit,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    if output_format == "markdown":
        click.echo(evidence_packets_to_markdown(packets).rstrip())
    elif output_format == "json":
        click.echo(json.dumps(packets, indent=2, ensure_ascii=False))
    elif output_format == "jsonl":
        for packet in packets:
            click.echo(json.dumps(packet, ensure_ascii=False))
    else:
        rows: list[dict[str, object]] = []
        for packet in packets:
            section_rows = cast(
                Sequence[Mapping[str, object]], packet.get("sections") or ()
            )
            rows.append(
                {
                    "id": packet["id"],
                    "title": packet["title"],
                    "description": packet["description"],
                    "labels": packet["labels"],
                    "sections": [section.get("role") for section in section_rows],
                }
            )
        emit_rows(rows, output_format=output_format)


@guidelines_command.command("search", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
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
    help="Maximum Chroma document candidates to inspect before deduplication.",
)
@click.option(
    "--where",
    help="Native Chroma metadata filter JSON.",
)
@click.option(
    "--where-document",
    help="Native Chroma document filter JSON.",
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
    index_dir: str | None,
    query: str,
    limit: int,
    candidate_limit: int | None,
    where: str | None,
    where_document: str | None,
    output_format: str,
) -> None:
    """Search guidelines using an existing Chroma index."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    where_filter = parse_json_object(where, option_name="--where")
    where_document_filter = parse_json_object(
        where_document,
        option_name="--where-document",
    )
    try:
        index = ChromaIndex.from_cache(
            catalog,
            cache_dir=index_dir,
            cache_mode="reuse_only",
        )
        result = search_guidelines(
            index,
            query,
            limit=limit,
            candidate_limit=candidate_limit,
            where=where_filter,
            where_document=where_document_filter,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc

    if output_format == "json":
        click.echo(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        return

    rows = cast(list[dict[str, object]], result.to_dict()["rows"])
    if output_format == "markdown":
        click.echo(guideline_search_rows_to_markdown(rows).rstrip())
    else:
        emit_rows(rows, output_format=output_format)


__all__ = ["guidelines_command"]
