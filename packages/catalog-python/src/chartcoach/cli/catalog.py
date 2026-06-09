from __future__ import annotations

from collections.abc import Mapping, Sequence
from difflib import SequenceMatcher
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import click
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.catalog.relations import (
    TABLE_SPECS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
)
from chartcoach.constants import LANCE_DOCUMENT_TABLE
from chartcoach.guideline.labels import parse_label
from chartcoach.search import Mode, index, open as open_index
from chartcoach.search import search as search_guidelines
from chartcoach.tools import ToolError, format_error

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    SEARCH_FORMATS,
    echo_info,
    echo_success,
    echo_warn,
    emit_object,
    emit_rows,
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

if TYPE_CHECKING:
    from lancedb.embeddings import EmbeddingFunction

READ_FORMATS = ("markdown", "json", "jsonl")
INDEX_CREATE_FORMATS = ("table", "json", "jsonl")
INDEX_INFO_FORMATS = ("table", "json", "jsonl")
VALUE_ALIASES: Mapping[str, tuple[str, str, bool]] = {
    "labels": ("guideline_labels", "label", False),
    "roles": ("sections", "role", False),
    "label": ("guideline_labels", "label", False),
    "label.family": ("guideline_labels", "family", False),
    "label.category": ("guideline_labels", "category", False),
    "label.modifier": ("guideline_labels", "modifier", False),
}


@click.group(
    "catalog",
    context_settings=CONTEXT_SETTINGS,
    help=(
        "Inspect, query, build, and index ChartCoach catalogs.\n\n"
        "\b\n"
        "Progressive Catalog Navigation:\n"
        "  overview          Summarize source, counts, roles, and label families\n"
        "  labels            List label values and counts\n"
        "  roles             List section roles and counts\n"
        "  list              List entries by id, title, description, and labels\n"
        "  query             Filter entries with composable base predicates\n"
        "  read              Read exact entries and selected sections\n"
        "  schema            Show queryable fields and tables\n"
        "  values            Count values for a field\n"
        "  sql               Run one read-only SELECT query\n\n"
        "\b\n"
        "Indexed Discovery, requires chartcoach[index]:\n"
        "  find              Rank entries with an existing LanceDB index\n"
        "  index create      Build a local LanceDB index\n"
        "  index info        Inspect a local LanceDB index\n\n"
        "\b\n"
        "Catalog Lifecycle:\n"
        "  build             Build a catalog bundle from authored entries\n"
        "  validate          Validate a catalog source\n"
        "  manifest          Print the catalog manifest\n"
        "  export duckdb     Materialize catalog tables into DuckDB"
    ),
)
def catalog_command() -> None:
    """Catalog command group."""


@catalog_command.command("overview", context_settings=CONTEXT_SETTINGS)
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


@catalog_command.command("labels", context_settings=CONTEXT_SETTINGS)
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
    emit_rows(visible_rows, output_format=output_format, empty_message="No labels matched.")
    if len(rows) > limit:
        echo_warn(f"Returned {limit} labels.", detail="Increase --limit to inspect more.")


@catalog_command.command("roles", context_settings=CONTEXT_SETTINGS)
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


@catalog_command.command("list", context_settings=CONTEXT_SETTINGS)
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
        rows = query_entries(
            load_catalog(ctx),
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            limit=limit,
            include_body=False,
        ).select("id", "title", "description", "labels").to_dicts()
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(rows, output_format=output_format, empty_message="No entries matched.")


@catalog_command.command("query", context_settings=CONTEXT_SETTINGS)
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
@click.option("--body-contains", help="Case-insensitive substring filter over body text.")
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
        rows = query_entries(
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
        ).select("id", "title", "description", "labels").to_dicts()
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    emit_rows(rows, output_format=output_format, empty_message="No entries matched.")


@catalog_command.command("read", context_settings=CONTEXT_SETTINGS)
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


@catalog_command.command("schema", context_settings=CONTEXT_SETTINGS)
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


@catalog_command.command("values", context_settings=CONTEXT_SETTINGS)
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
        echo_warn(f"Returned {limit} values.", detail="Increase --limit to inspect more.")


@catalog_command.command("sql", context_settings=CONTEXT_SETTINGS)
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


@catalog_command.command("find", context_settings=CONTEXT_SETTINGS)
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
@click.option("--where", help="LanceDB SQL filter over indexed document columns.")
@click.option(
    "--mode",
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
    default="compact",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def find_command(
    ctx: click.Context,
    index_path: str | None,
    query: str,
    limit: int,
    candidate_limit: int | None,
    where: str | None,
    mode: str,
    table_name: str,
    output_format: str,
) -> None:
    """Rank entries with an existing LanceDB index."""

    catalog = load_catalog(ctx)
    try:
        resolved_index_path = require_index_path(
            index_path,
            source_path=source_path(ctx),
            table_name=table_name,
            use_default=True,
        )
        table = open_index(resolved_index_path, table_name=table_name)
        with quiet_runtime_stderr():
            result = search_guidelines(
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
        click.echo(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        return

    rows = cast(list[dict[str, object]], result["rows"])
    if output_format == "markdown":
        output = guideline_search_rows_to_markdown(rows).rstrip()
        click.echo(output or "No entries matched.")
    elif output_format == "compact":
        output = guideline_search_rows_to_compact_markdown(rows).rstrip()
        click.echo(output or "No entries matched.")
    else:
        emit_rows(rows, output_format=output_format, empty_message="No entries matched.")


@catalog_command.command("build", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--source",
    type=click.Path(file_okay=False, exists=True, path_type=Path),
    required=True,
    help="Authored catalog folder to read.",
)
@click.option(
    "--out",
    "output_path",
    type=click.Path(file_okay=False, path_type=Path),
    required=True,
    help="Catalog bundle directory to write.",
)
@click.option("--dry-run", is_flag=True, help="Validate without writing.")
@click.option("--overwrite", is_flag=True, help="Allow replacing an existing bundle.")
def build_command(
    source: Path,
    output_path: Path,
    dry_run: bool,
    overwrite: bool,
) -> None:
    """Build a catalog bundle from authored entries."""

    try:
        catalog = Catalog.from_folder(source)
    except FileNotFoundError as exc:
        raise click.ClickException(str(exc)) from exc
    if len(catalog) == 0:
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected entries/*/guideline.md files."
        )
    manifest_path = output_path / "MANIFEST.md"
    parquet_path = output_path / "entries.parquet"
    metadata_path = output_path / "metadata.json"
    if (
        not overwrite
        and not dry_run
        and (manifest_path.exists() or parquet_path.exists() or metadata_path.exists())
    ):
        raise click.ClickException(
            f"{output_path} already contains a catalog bundle. Pass --overwrite."
        )
    if dry_run:
        echo_info(f"Would write {len(catalog)} entries", detail=f"to catalog bundle {output_path}", err=False)
        return
    catalog.write_bundle(output_path, overwrite=overwrite)
    echo_success(f"Wrote {len(catalog)} entries", detail=f"to {output_path}")


@catalog_command.command("validate", context_settings=CONTEXT_SETTINGS)
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
def validate_command(ctx: click.Context, output_format: str) -> None:
    """Validate a catalog source and report table counts."""

    catalog = load_catalog(ctx)
    if len(catalog) == 0:
        source = source_path(ctx)
        raise click.ClickException(
            f"No guideline entries found in {source}. Expected entries/*/guideline.md files."
        )
    rows = validation_rows(catalog)
    emit_rows(rows, output_format=output_format)


@catalog_command.command("manifest", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("markdown", "json", "jsonl")),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def manifest_command(ctx: click.Context, output_format: str) -> None:
    """Print the catalog manifest."""

    catalog = load_catalog(ctx)
    try:
        manifest = catalog.require_manifest()
    except ValueError as exc:
        path = source_path(ctx)
        raise click.ClickException(
            format_error(
                f"Catalog source has no manifest: {path}",
                [
                    "Use an authored folder with entries/ or a catalog bundle directory.",
                    "Omit --source to use the package-pinned default catalog artifact.",
                    "Use standalone parquet files for records, tables, SQL, and indexing.",
                ],
            )
        ) from exc
    if output_format == "markdown":
        click.echo(manifest.markdown.rstrip())
        return
    rows = {
        "section_roles": list(manifest.section_roles),
        "label_families": list(manifest.label_families),
    }
    emit_object(rows, output_format=output_format)


@catalog_command.group("export", context_settings=CONTEXT_SETTINGS, help="Export catalog tables.")
def export_command() -> None:
    """Export catalog tables."""


@export_command.command("duckdb", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--out",
    "output_path",
    type=click.Path(dir_okay=False, path_type=Path),
    required=True,
    help="DuckDB database file to write.",
)
@click.option("--overwrite", is_flag=True, help="Replace an existing DuckDB file.")
@click.pass_context
def export_duckdb_command(
    ctx: click.Context,
    output_path: Path,
    overwrite: bool,
) -> None:
    """Materialize catalog tables into a DuckDB database."""

    catalog = load_catalog(ctx)
    try:
        catalog.write_duckdb(output_path, overwrite=overwrite)
    except FileExistsError as exc:
        raise click.ClickException(f"{output_path} already exists. Pass --overwrite.") from exc
    echo_success("Wrote DuckDB catalog", detail=f"to {output_path}")


@catalog_command.group("index", context_settings=CONTEXT_SETTINGS, help="Create and inspect LanceDB indexes.")
def index_command() -> None:
    """Create and inspect LanceDB indexes."""


@index_command.command("create", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_option
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to create.",
)
@click.option(
    "--embedding",
    "embedding_name",
    help=(
        "LanceDB embedding function alias from lancedb.embeddings.get_registry(). "
        "When omitted, the table is full-text only."
    ),
)
@click.option(
    "--embedding-option",
    "embedding_options",
    multiple=True,
    metavar="KEY=VALUE",
    help="Option passed to the LanceDB embedding function create() call.",
)
@click.option(
    "--embedding-var",
    "embedding_vars",
    multiple=True,
    metavar="KEY=VALUE",
    help="Set a LanceDB embedding registry variable before create().",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(INDEX_CREATE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def index_create_command(
    ctx: click.Context,
    index_path: str | None,
    table_name: str,
    embedding_name: str | None,
    embedding_options: tuple[str, ...],
    embedding_vars: tuple[str, ...],
    output_format: str,
) -> None:
    """Build a LanceDB index from the catalog."""

    resolved_index_path = require_index_path(index_path)
    catalog = load_catalog(ctx)
    try:
        embedding = _embedding(embedding_name, embedding_options, embedding_vars)
        with quiet_runtime_stderr():
            table = index(catalog, resolved_index_path, table_name=table_name, embedding=embedding)
        row = {
            "index_path": resolved_index_path,
            "table": table.name,
            "guidelines": len(catalog),
            "documents": table.count_rows(),
            "embedding": embedding_name,
            "catalog_digest": catalog.digest(),
        }
    except Exception as exc:
        raise click.ClickException(search_cli_error(str(exc), index_path=resolved_index_path, table_name=table_name)) from exc
    emit_rows([row], output_format=output_format)


@index_command.command("info", context_settings=CONTEXT_SETTINGS)
@required_index_option
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name to inspect.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(INDEX_INFO_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def index_info_command(index_path: str | None, table_name: str, output_format: str) -> None:
    """Inspect a LanceDB index."""

    resolved_index_path = require_index_path(index_path, table_name=table_name, use_default=True)
    try:
        table = open_index(resolved_index_path, table_name=table_name)
        row = {
            "index_path": resolved_index_path,
            "table": table.name,
            "documents": table.count_rows(),
            "embedding_functions": embedding_functions_state(table),
        }
    except Exception as exc:
        raise click.ClickException(search_cli_error(str(exc), index_path=resolved_index_path, table_name=table_name)) from exc
    emit_rows([row], output_format=output_format)


def embedding_functions_state(table: object) -> str:
    try:
        functions = getattr(table, "embedding_functions", None)
    except Exception:
        return "unknown"
    return "present" if functions else "absent"


def catalog_overview(catalog: Catalog, *, source: str | None) -> dict[str, object]:
    manifest = catalog.manifest
    return {
        "source": source,
        "catalog_digest": catalog.digest(),
        "tables": overview_table_count_rows(catalog),
        "section_roles": list(manifest.section_roles) if manifest is not None else sorted(distinct_strings(catalog, table="sections", column="role")),
        "label_families": list(manifest.label_families) if manifest is not None else sorted(distinct_strings(catalog, table="guideline_labels", column="family")),
    }


def overview_table_count_rows(catalog: Catalog) -> list[dict[str, object]]:
    return [
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "labels", "rows": catalog.labels().height},
        {"name": "guideline_labels", "rows": catalog.guideline_labels().height},
    ]


def overview_table_rows(overview: Mapping[str, object]) -> list[dict[str, object]]:
    table_counts = {
        str(row["name"]): row["rows"]
        for row in cast(Sequence[Mapping[str, object]], overview["tables"])
    }
    return [
        {"name": "source", "value": overview.get("source") or "default"},
        {"name": "catalog_digest", "value": overview["catalog_digest"]},
        *[
            {"name": f"table.{name}", "value": rows}
            for name, rows in table_counts.items()
        ],
        {"name": "section_roles", "value": overview["section_roles"]},
        {"name": "label_families", "value": overview["label_families"]},
    ]


def validation_rows(catalog: Catalog) -> list[dict[str, object]]:
    manifest = catalog.manifest
    rows: list[dict[str, object]] = [
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "labels", "rows": catalog.labels().height},
        {"name": "references", "rows": catalog.references().height},
    ]
    if manifest is not None:
        rows.insert(0, {"name": "manifest_section_roles", "rows": len(manifest.section_roles)})
        rows.insert(1, {"name": "manifest_label_families", "rows": len(manifest.label_families)})
    return rows


def list_labels(
    catalog: Catalog,
    *,
    family: str | None = None,
    prefix: str | None = None,
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
    available_families = distinct_strings(catalog, table="guideline_labels", column="family")
    if family is not None and family not in available_families:
        raise unknown_label_family_error(catalog, family)

    frame = catalog.guideline_labels()
    if family is not None:
        frame = frame.filter(pl.col("family") == family)
    if prefix is not None:
        frame = frame.filter(pl.col("label").str.starts_with(prefix))
    if contains is not None:
        needle = contains.lower()
        frame = frame.filter(pl.col("label").str.to_lowercase().str.contains(needle, literal=True))
    return (
        frame.group_by("label", "family", "category", "modifier")
        .len("entries")
        .sort(["entries", "label"], descending=[True, False])
        .head(limit)
        .to_dicts()
    )


def list_roles(catalog: Catalog) -> list[dict[str, object]]:
    count_rows = (
        catalog.sections()
        .group_by("role")
        .len("entries")
        .sort("role")
        .to_dicts()
    )
    counts = {str(row["role"]): row["entries"] for row in count_rows}
    manifest = catalog.manifest
    definitions = manifest.section_roles if manifest is not None else {}
    role_names = list(definitions) if definitions else sorted(counts)
    return [
        {
            "role": role,
            "entries": counts.get(role, 0),
            "use": _first_sentence(definitions[role].description)
            if role in definitions
            else "",
        }
        for role in role_names
    ]


def query_entries(
    catalog: Catalog,
    *,
    ids: Sequence[str] = (),
    labels: Sequence[str] = (),
    any_labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
    contains: str | None = None,
    body_contains: str | None = None,
    section_contains: str | None = None,
    limit: int = 50,
    include_body: bool = True,
) -> pl.DataFrame:
    validate_filters(catalog, labels=labels, any_labels=any_labels, label_prefixes=label_prefixes)
    validate_ids(catalog, ids)
    df = catalog.guidelines()
    if ids:
        order = pl.DataFrame({"id": list(ids), "_catalog_order": range(len(ids))})
        df = order.join(df, on="id", how="inner").sort("_catalog_order")
    for label in labels:
        df = df.filter(pl.col("labels").list.contains(label))
    if any_labels:
        df = df.filter(
            pl.any_horizontal(*(pl.col("labels").list.contains(label) for label in any_labels))
        )
    for prefix in label_prefixes:
        df = df.filter(
            pl.col("labels").list.eval(pl.element().str.starts_with(prefix)).list.any()
        )
    if contains:
        needle = contains.lower()
        df = df.filter(
            pl.any_horizontal(
                pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("title").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("description").str.to_lowercase().str.contains(needle, literal=True),
            )
        )
    if body_contains:
        needle = body_contains.lower()
        df = df.filter(pl.col("body").str.to_lowercase().str.contains(needle, literal=True))
    if section_contains:
        matching_ids = _section_matching_ids(catalog, section_contains)
        df = df.filter(pl.col("id").is_in(matching_ids))
    references = catalog.to_frame().select("id", "references")
    selected = df.head(limit).join(references, on="id", how="left").drop("_catalog_order", strict=False)
    if not include_body:
        selected = selected.drop("body", "sections", "references", strict=False)
    return selected


def _section_matching_ids(catalog: Catalog, contains: str) -> list[str]:
    needle = contains.lower()
    return (
        catalog.sections()
        .filter(
            pl.any_horizontal(
                pl.col("title").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("content").str.to_lowercase().str.contains(needle, literal=True),
            )
        )
        .get_column("guideline_id")
        .unique()
        .to_list()
    )


def retrieve_entry_records(
    catalog: Catalog,
    *,
    ids: Sequence[str],
    roles: Sequence[str] = (),
    source_detail: str = "minimal",
) -> list[dict[str, object]]:
    validate_section_roles(catalog, roles)
    frame = query_entries(catalog, ids=ids, limit=len(ids), include_body=True)
    role_set = set(roles) if roles else None
    return [
        entry_record_from_row(
            row,
            roles=role_set,
            source_detail=source_detail,
            sources=source_rows(catalog, cast(str, row["id"]), detail=source_detail),
        )
        for row in frame.to_dicts()
    ]


def entry_record_from_row(
    row: Mapping[str, object],
    *,
    roles: set[str] | None,
    source_detail: str,
    sources: list[dict[str, object]],
) -> dict[str, object]:
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
    record = {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "labels": list(cast(Sequence[str], row.get("labels") or ())),
        "sections": sections,
        "sources": sources,
    }
    if source_detail == "full":
        record["references"] = list(cast(Sequence[str], row.get("references") or ()))
    return record


def source_rows(catalog: Catalog, guideline_id: str, *, detail: str) -> list[dict[str, object]]:
    if detail == "none":
        return []
    frame = catalog.guideline_sources().filter(pl.col("guideline_id") == guideline_id)
    if frame.is_empty():
        return []
    columns = ["reference_id", "authors_text", "year", "source_title", "doi", "url"]
    if detail == "full":
        columns = frame.columns
    return frame.select([column for column in columns if column in frame.columns]).to_dicts()


def entry_records_to_markdown(records: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for record in records:
        lines.append(f"## {record['id']}")
        lines.append("")
        lines.append(f"**{record['title']}**")
        lines.append("")
        lines.append(str(record["description"]))
        lines.append("")
        labels = cast(Sequence[str], record.get("labels") or ())
        if labels:
            lines.append("Labels: " + ", ".join(f"`{label}`" for label in labels))
            lines.append("")
        for section in cast(Sequence[Mapping[str, str]], record.get("sections") or ()):
            lines.append(f"### {section['role']}: {section['title']}")
            lines.append("")
            lines.append(section["content"].strip())
            lines.append("")
        sources = cast(Sequence[Mapping[str, object]], record.get("sources") or ())
        if sources:
            lines.append("### Sources")
            lines.append("")
            for source in sources:
                lines.append(f"- {source_label(source)}")
            lines.append("")
    return "\n".join(lines)


def source_label(source: Mapping[str, object]) -> str:
    authors = str(source.get("authors_text") or "").strip()
    year = str(source.get("year") or "").strip()
    title = str(source.get("source_title") or "").strip()
    doi = str(source.get("doi") or "").strip()
    url = str(source.get("url") or "").strip()
    parts = [part for part in (authors, year, title) if part]
    label = ", ".join(parts) if parts else str(source.get("reference_id") or "source")
    links = [value for value in (doi, url) if value]
    if links:
        return f"{label} ({', '.join(links)})"
    return label


def validate_filters(
    catalog: Catalog,
    *,
    labels: Sequence[str] = (),
    any_labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
) -> None:
    validate_labels(catalog, (*labels, *any_labels))
    validate_label_prefixes(catalog, label_prefixes)


def validate_ids(catalog: Catalog, ids: Sequence[str]) -> None:
    if not ids:
        return
    available = set(catalog.guidelines().get_column("id").to_list())
    for guideline_id in ids:
        if guideline_id not in available:
            raise unknown_id_error(catalog, guideline_id)


def validate_labels(catalog: Catalog, labels: Sequence[str]) -> None:
    if not labels:
        return
    available = distinct_strings(catalog, table="guideline_labels", column="label")
    missing = sorted(set(labels) - available)
    if missing:
        raise unknown_label_error(catalog, missing)


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
                "Run `chartcoach catalog labels` to inspect valid labels.",
                "Run `chartcoach catalog labels --family FAMILY` after choosing a family.",
            ],
        )


def validate_section_roles(catalog: Catalog, roles: Sequence[str]) -> None:
    if not roles:
        return
    available = (
        set(catalog.manifest.section_roles)
        if catalog.manifest is not None
        else distinct_strings(catalog, table="sections", column="role")
    )
    missing = sorted(set(roles) - available)
    if missing:
        raise ToolError(
            f"Unknown section role(s): {', '.join(missing)}",
            hints=[
                "Valid roles: " + ", ".join(sorted(available)),
                "Run `chartcoach catalog roles` to inspect section roles.",
            ],
        )


def distinct_strings(catalog: Catalog, *, table: str, column: str) -> set[str]:
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
    suggestions = nearest_values(
        guideline_id,
        [str(value) for value in catalog.guidelines().get_column("id").to_list()],
    )
    hints = []
    if suggestions:
        hints.append("Nearest entry ids: " + ", ".join(suggestions))
    hints.extend(
        [
            "Copy ids exactly from `chartcoach catalog list` or `chartcoach catalog query`.",
            "Run `chartcoach catalog read ID` with exact ids.",
        ]
    )
    return ToolError(f"Unknown entry id: {guideline_id}", hints=hints)


def unknown_label_error(catalog: Catalog, labels: Sequence[str]) -> ToolError:
    available = sorted(distinct_strings(catalog, table="guideline_labels", column="label"))
    hints: list[str] = []
    for label in labels:
        suggestions = nearest_values(label, available)
        if suggestions:
            hints.append(f"Nearest labels for {label}: " + ", ".join(suggestions))
        try:
            family = parse_label(label, context=f"label {label!r}").family
        except (TypeError, ValueError):
            family = None
        if family:
            hints.append(f"Run `chartcoach catalog labels --family {family}` to inspect that family.")
    hints.append("Run `chartcoach catalog labels` to inspect valid labels.")
    return ToolError(f"Unknown label(s): {', '.join(labels)}", hints=hints)


def unknown_label_family_error(catalog: Catalog, family: str) -> ToolError:
    available = sorted(distinct_strings(catalog, table="guideline_labels", column="family"))
    suggestions = nearest_values(family, available)
    hints = ["Available label families: " + ", ".join(available)]
    if suggestions:
        hints.append("Nearest label families: " + ", ".join(suggestions))
    return ToolError(f"Unknown label family: {family}", hints=hints)


def nearest_values(value: str, candidates: Sequence[str], *, limit: int = 3) -> list[str]:
    scored = [(SequenceMatcher(a=value, b=candidate).ratio(), candidate) for candidate in candidates]
    return [
        candidate
        for score, candidate in sorted(scored, key=lambda item: (-item[0], item[1]))
        if score > 0
    ][:limit]


def list_tables(catalog: Catalog, *, include_row_counts: bool = False) -> list[dict[str, object]]:
    if include_row_counts:
        return catalog_table_rows(catalog)
    return [
        {"name": spec.name, "columns": len(spec.schema), "rows": None}
        for spec in TABLE_SPECS.values()
    ]


def describe_tables(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    try:
        return catalog_table_schema(tables)
    except KeyError as exc:
        raise unknown_table_error([str(exc).strip("'")]) from exc


def parse_value_field(field: str) -> tuple[str, str, bool]:
    if field in VALUE_ALIASES:
        return VALUE_ALIASES[field]
    if "." not in field:
        raise ToolError(
            f"Unknown catalog value field: {field}",
            hints=[
                "Use aliases such as labels, roles, label.family, label.category, or label.modifier.",
                "Use raw table fields as TABLE.COLUMN after inspecting `chartcoach catalog schema`.",
            ],
        )
    table, column = field.split(".", 1)
    if not table or not column:
        raise ToolError("Value fields must be aliases or TABLE.COLUMN.")
    return table, column, False


def count_values(
    catalog: Catalog,
    table: str,
    column: str,
    *,
    explode: bool = False,
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
    frame = require_table(catalog, table)
    require_column(table, frame, column)
    dtype = frame.schema[column]
    value_expr = pl.col(column).explode() if explode or _is_list_dtype(dtype) else pl.col(column)
    values = frame.select(value_expr.alias("value")).filter(pl.col("value").is_not_null())
    values = values.with_columns(pl.col("value").cast(pl.String).alias("value"))
    if contains:
        needle = contains.lower()
        values = values.filter(pl.col("value").str.to_lowercase().str.contains(needle, literal=True))
    return (
        values.group_by("value")
        .len("rows")
        .sort(["rows", "value"], descending=[True, False])
        .head(limit)
        .with_columns(pl.lit(table).alias("table"), pl.lit(column).alias("column"))
        .select("table", "column", "value", "rows")
        .to_dicts()
    )


def require_table(catalog: Catalog, table: str) -> pl.DataFrame:
    if table not in catalog_table_names():
        raise unknown_table_error([table])
    return catalog.table(table)


def require_column(table: str, frame: pl.DataFrame, column: str) -> None:
    if column not in frame.columns:
        columns = ", ".join(frame.columns)
        raise ToolError(
            f"Unknown column for table {table}: {column}",
            hints=[
                f"Available columns on {table}: {columns}",
                "Run `chartcoach catalog schema` to inspect fields.",
            ],
        )


def unknown_table_error(tables: Sequence[str]) -> ToolError:
    available = ", ".join(catalog_table_names())
    return ToolError(
        f"Unknown table(s): {', '.join(tables)}",
        hints=[
            f"Available tables: {available}",
            "Run `chartcoach catalog schema --tables` to inspect tables.",
        ],
    )


def _is_list_dtype(dtype: object) -> bool:
    return isinstance(dtype, pl.DataType) and dtype.base_type() == pl.List


def _first_sentence(text: str) -> str:
    stripped = " ".join(text.split())
    if "." not in stripped:
        return stripped
    return stripped.split(".", 1)[0] + "."


def _embedding(
    name: str | None,
    options: tuple[str, ...],
    variables: tuple[str, ...],
) -> "EmbeddingFunction | None":
    if name is None:
        if options or variables:
            raise click.ClickException("Pass --embedding before --embedding-option or --embedding-var.")
        return None

    try:
        from lancedb.embeddings import get_registry
    except ModuleNotFoundError as exc:
        raise click.ClickException(search_cli_error(str(exc))) from exc

    registry = get_registry()
    for item in variables:
        key, value = _key_value(item, option="--embedding-var")
        registry.set_var(key, value)
    kwargs = {
        key: _json_or_string(value)
        for key, value in (_key_value(item, option="--embedding-option") for item in options)
    }
    try:
        return cast("EmbeddingFunction", registry.get(name).create(**kwargs))
    except KeyError as exc:
        raise click.ClickException(search_cli_error(f"Unknown LanceDB embedding function: {name}")) from exc


def _key_value(value: str, *, option: str) -> tuple[str, str]:
    if "=" not in value:
        raise click.ClickException(f"{option} expects KEY=VALUE.")
    key, raw = value.split("=", 1)
    key = key.strip()
    if not key:
        raise click.ClickException(f"{option} key cannot be empty.")
    return key, raw


def _json_or_string(value: str) -> object:
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


__all__ = ["catalog_command"]
