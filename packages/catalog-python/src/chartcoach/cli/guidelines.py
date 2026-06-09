from __future__ import annotations

from collections.abc import Mapping, Sequence
from difflib import SequenceMatcher
import json
from pathlib import Path
from typing import cast

import click
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.constants import LANCE_DOCUMENT_TABLE
from chartcoach.guideline import Guideline
from chartcoach.search import Mode, open as open_index, search
from chartcoach.tools import (
    ToolError,
)

from .common import (
    CONTEXT_SETTINGS,
    RETRIEVE_FORMATS,
    ROW_FORMATS,
    SEARCH_FORMATS,
    SHOW_FORMATS,
    emit_rows,
    evidence_packets_to_markdown,
    guideline_search_rows_to_compact_markdown,
    guideline_search_rows_to_markdown,
    load_catalog,
    quiet_runtime_stderr,
    require_index_path,
    required_index_option,
    search_cli_error,
    source_option,
    source_path,
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
        rows = list_guidelines(
            load_catalog(ctx),
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            limit=limit,
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(
        rows,
        output_format=output_format,
        empty_message="No guidelines matched.",
    )


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
    try:
        entry = get_guideline(catalog, guideline_id)
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc

    if output_format == "json":
        click.echo(json.dumps(entry, indent=2, ensure_ascii=False))
    elif output_format == "jsonl":
        click.echo(json.dumps(entry, ensure_ascii=False))
    else:
        click.echo(Guideline.from_mapping(entry).to_markdown().rstrip())


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
        packets = retrieve_guidelines(
            load_catalog(ctx),
            ids=guideline_ids,
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            roles=sections,
            limit=limit,
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    if not packets and output_format == "markdown":
        click.echo("No guidelines matched.")
        return
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
        emit_rows(
            rows,
            output_format=output_format,
            empty_message="No guidelines matched.",
        )


@guidelines_command.command("search", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_option
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
    help="Maximum indexed documents to inspect before deduplication.",
)
@click.option(
    "--where",
    help="LanceDB SQL filter over indexed document columns.",
)
@click.option(
    "--mode",
    "mode",
    type=click.Choice(("auto", "fts", "vector", "hybrid")),
    default="auto",
    show_default=True,
    help="LanceDB query mode for document retrieval.",
)
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to query.",
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
    index_path: Path | None,
    query: str,
    limit: int,
    candidate_limit: int | None,
    where: str | None,
    mode: str,
    table_name: str,
    output_format: str,
) -> None:
    """Search guidelines using an existing LanceDB index."""

    catalog = load_catalog(ctx)
    try:
        resolved_index_path = require_index_path(
            index_path,
            source_path=source_path(ctx),
        )
        table = open_index(resolved_index_path, table_name=table_name)
        with quiet_runtime_stderr():
            result = search(
                catalog,
                table,
                query,
                limit=limit,
                candidate_limit=candidate_limit,
                where=where,
                mode=cast(Mode, mode),
            ).to_dict()
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc),
                index_path=resolved_index_path,
                table_name=table_name,
            )
        ) from exc

    if output_format == "json":
        click.echo(json.dumps(result, indent=2, ensure_ascii=False))
        return

    rows = cast(list[dict[str, object]], result["rows"])
    if output_format == "markdown":
        output = guideline_search_rows_to_markdown(rows).rstrip()
        click.echo(output or "No guidelines matched.")
    elif output_format == "compact":
        output = guideline_search_rows_to_compact_markdown(rows).rstrip()
        click.echo(output or "No guidelines matched.")
    else:
        emit_rows(
            rows,
            output_format=output_format,
            empty_message="No guidelines matched.",
        )


def list_guidelines(
    catalog: Catalog,
    *,
    labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
    """List guideline ids and summaries with deterministic filters."""

    validate_labels(catalog, labels)
    validate_label_prefixes(catalog, label_prefixes)
    df = catalog.guidelines().select("id", "title", "description", "labels")
    for label_value in labels:
        df = df.filter(pl.col("labels").list.contains(label_value))
    for prefix in label_prefixes:
        df = df.filter(
            pl.col("labels")
            .list.eval(pl.element().str.starts_with(prefix))
            .list.any()
        )
    if contains:
        needle = contains.lower()
        df = df.filter(
            pl.any_horizontal(
                pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("title").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("description")
                .str.to_lowercase()
                .str.contains(needle, literal=True),
            )
        )
    return df.head(limit).to_dicts()


def get_guideline(catalog: Catalog, guideline_id: str) -> dict[str, object]:
    """Return one complete guideline record by id."""

    try:
        return catalog.entry(guideline_id)
    except KeyError as exc:
        raise unknown_id_error(catalog, guideline_id) from exc


def retrieve_guidelines(
    catalog: Catalog,
    *,
    ids: Sequence[str] = (),
    labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
    contains: str | None = None,
    roles: Sequence[str] = (),
    limit: int = 12,
) -> list[dict[str, object]]:
    """Return guideline records with optional section filtering."""

    validate_filters(
        catalog,
        labels=labels,
        label_prefixes=label_prefixes,
        roles=roles,
    )
    frame = query_guidelines(
        catalog,
        ids=ids,
        labels=labels,
        label_prefixes=label_prefixes,
        contains=contains,
        limit=limit,
    )
    role_set = set(roles) if roles else None
    return [guideline_record_from_row(row, roles=role_set) for row in frame.to_dicts()]


def validate_filters(
    catalog: Catalog,
    *,
    labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
    roles: Sequence[str] = (),
) -> None:
    validate_labels(catalog, labels)
    validate_label_prefixes(catalog, label_prefixes)
    validate_section_roles(catalog, roles)


def query_guidelines(
    catalog: Catalog,
    *,
    ids: Sequence[str],
    labels: Sequence[str],
    label_prefixes: Sequence[str],
    contains: str | None,
    limit: int,
) -> pl.DataFrame:
    df = catalog.guidelines()
    if ids:
        available = set(df.get_column("id").to_list())
        missing = [guideline_id for guideline_id in ids if guideline_id not in available]
        if missing:
            raise unknown_id_error(catalog, missing[0])
        order = pl.DataFrame({"id": list(ids), "_catalog_order": range(len(ids))})
        df = order.join(df, on="id", how="inner").sort("_catalog_order")

    for label in labels:
        df = df.filter(pl.col("labels").list.contains(label))
    for prefix in label_prefixes:
        df = df.filter(
            pl.col("labels")
            .list.eval(pl.element().str.starts_with(prefix))
            .list.any()
        )
    if contains:
        needle = contains.lower()
        df = df.filter(
            pl.any_horizontal(
                pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("title").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("description")
                .str.to_lowercase()
                .str.contains(needle, literal=True),
                pl.col("body").str.to_lowercase().str.contains(needle, literal=True),
            )
        )

    references = catalog.to_frame().select("id", "references")
    return (
        df.head(limit)
        .join(references, on="id", how="left")
        .drop("_catalog_order", strict=False)
    )


def guideline_record_from_row(
    row: Mapping[str, object],
    *,
    roles: set[str] | None,
) -> dict[str, object]:
    """Return one CLI evidence record."""

    raw_sections = cast(Sequence[Mapping[str, object]], row.get("sections") or ())
    sections = [
        {
            "role": str(section["role"]),
            "title": str(section["title"]),
            "content": str(section["content"]),
        }
        for section in raw_sections
        if roles is None or section.get("role") in roles
    ]
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "labels": list(cast(Sequence[str], row.get("labels") or ())),
        "references": list(cast(Sequence[str], row.get("references") or ())),
        "sections": sections,
    }


def validate_labels(catalog: Catalog, labels: Sequence[str]) -> None:
    if not labels:
        return
    available = distinct_strings(catalog, table="guideline_labels", column="label")
    missing = sorted(set(labels) - available)
    if missing:
        raise ToolError(
            f"Unknown label(s): {', '.join(missing)}",
            hints=["Inspect the guideline_labels table before filtering by label."],
        )


def validate_label_prefixes(catalog: Catalog, prefixes: Sequence[str]) -> None:
    if not prefixes:
        return
    available = distinct_strings(catalog, table="guideline_labels", column="label")
    missing = [
        prefix
        for prefix in sorted(set(prefixes))
        if not any(label.startswith(prefix) for label in available)
    ]
    if missing:
        raise ToolError(
            f"No labels match prefix(es): {', '.join(missing)}",
            hints=[
                "Inspect the guideline_labels table before filtering by label prefix.",
            ],
        )


def validate_section_roles(catalog: Catalog, roles: Sequence[str]) -> None:
    if not roles:
        return
    available = distinct_strings(catalog, table="sections", column="role")
    missing = sorted(set(roles) - available)
    if missing:
        raise ToolError(
            f"Unknown section role(s): {', '.join(missing)}",
            hints=[
                "Valid roles: " + ", ".join(sorted(available)),
                "Run `chartcoach catalog manifest --source PATH` for the catalog contract.",
            ],
        )


def distinct_strings(
    catalog: Catalog,
    *,
    table: str,
    column: str,
) -> set[str]:
    frame = catalog.table(table)
    value_expr = pl.col(column)
    if frame.schema[column].base_type() == pl.List:
        value_expr = value_expr.explode()
    values = (
        frame.select(value_expr.alias("value"))
        .filter(pl.col("value").is_not_null())
        .with_columns(pl.col("value").cast(pl.String).alias("value"))
        .get_column("value")
        .to_list()
    )
    return {value for value in values if isinstance(value, str)}


def unknown_id_error(catalog: Catalog, guideline_id: str) -> ToolError:
    suggestions = nearest_guideline_ids(catalog, guideline_id)
    hints = []
    if suggestions:
        hints.append("Nearest guideline ids: " + ", ".join(suggestions))
    hints.extend(
        [
            "Copy ids exactly from `chartcoach guidelines search --format compact QUERY`.",
            "Run `chartcoach guidelines show ID` or `chartcoach guidelines retrieve --id ID` with one exact id.",
            "Run `chartcoach guidelines list --contains TEXT` to inspect candidate ids.",
        ]
    )
    return ToolError(
        f"Unknown guideline id: {guideline_id}",
        hints=hints,
    )


def nearest_guideline_ids(
    catalog: Catalog,
    guideline_id: str,
    *,
    limit: int = 3,
) -> list[str]:
    ids = [str(value) for value in catalog.guidelines().get_column("id").to_list()]
    scored = [
        (
            SequenceMatcher(a=guideline_id, b=candidate).ratio(),
            candidate,
        )
        for candidate in ids
    ]
    return [
        candidate
        for score, candidate in sorted(scored, key=lambda item: (-item[0], item[1]))
        if score > 0
    ][:limit]


__all__ = ["guidelines_command"]
