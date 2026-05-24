from __future__ import annotations

import click

from chartcoach.tools.catalog import search_error_message

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    emit_object,
    emit_rows,
    load_catalog,
    parse_json_object,
    required_index_dir_option,
    source_option,
)

CHROMA_FORMATS = ("json", "jsonl")


@click.group(
    "index",
    context_settings=CONTEXT_SETTINGS,
    help="Build and inspect the Chroma search artifact.",
)
def index_command() -> None:
    """Build and inspect the Chroma search artifact."""


@index_command.command("status", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def status_command(
    ctx: click.Context,
    index_dir: str | None,
    output_format: str,
) -> None:
    """Report the native Chroma artifact path for this catalog."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    row: dict[str, object] = {
        "catalog_digest": catalog.digest(),
        "documents_version": None,
        "index_root": None,
        "cache_path": None,
        "chroma_path": None,
        "collection_name": None,
        "embedding_name": None,
        "ready": True,
        "documents": None,
        "error": None,
    }
    try:
        from chartcoach.search.chroma import ChromaIndex

        paths = ChromaIndex.cache_paths(catalog, cache_dir=index_dir)
        row.update(
            {
                "documents_version": paths.documents_version,
                "index_root": str(paths.index_root),
                "cache_path": str(paths.cache_path),
                "chroma_path": str(paths.chroma_path),
                "collection_name": paths.collection_name,
                "embedding_name": paths.embedding_name,
            }
        )
        index = ChromaIndex.from_cache(
            catalog,
            cache_dir=index_dir,
            cache_mode="reuse_only",
        )
        row["documents"] = index.collection.count()
    except Exception as exc:
        row["ready"] = False
        row["error"] = str(exc)
    emit_rows([row], output_format=output_format)


@index_command.command("build", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.pass_context
def build_command(ctx: click.Context, index_dir: str | None) -> None:
    """Create the Chroma artifact if it is missing."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    try:
        from chartcoach.search.chroma import ChromaIndex

        index = ChromaIndex.from_cache(
            catalog,
            cache_dir=index_dir,
            cache_mode="reuse_or_create",
        )
        click.echo(
            f"Index ready for {len(catalog)} guidelines "
            f"({index.collection.count()} documents) "
            f"at {index.chroma_path} "
            f"collection {index.collection_name!r}"
        )
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc


@index_command.command("rebuild", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.option(
    "--yes",
    is_flag=True,
    help="Confirm rebuilding the content-addressed index cache path.",
)
@click.pass_context
def rebuild_command(ctx: click.Context, index_dir: str | None, yes: bool) -> None:
    """Rebuild the Chroma artifact for the catalog."""

    if not yes:
        raise click.ClickException("Pass --yes to rebuild the search index.")
    catalog = load_catalog(ctx)
    assert index_dir is not None
    try:
        from chartcoach.search.chroma import ChromaIndex

        index = ChromaIndex.from_cache(
            catalog,
            cache_dir=index_dir,
            cache_mode="force_rebuild",
        )
        click.echo(
            f"Rebuilt index for {len(catalog)} guidelines "
            f"({index.collection.count()} documents) "
            f"at {index.chroma_path} "
            f"collection {index.collection_name!r}"
        )
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc


@index_command.command("query", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.argument("params_json")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CHROMA_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def query_command(
    ctx: click.Context,
    index_dir: str | None,
    params_json: str,
    output_format: str,
) -> None:
    """Run collection.query(**PARAMS_JSON) against the Chroma collection."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    params = parse_json_object(params_json, option_name="PARAMS_JSON")
    assert params is not None
    try:
        from chartcoach.search.chroma import ChromaIndex

        index = ChromaIndex.from_cache(
            catalog,
            cache_dir=index_dir,
            cache_mode="reuse_only",
        )
        result = index.collection.query(**params)
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc
    emit_object(result, output_format=output_format)


@index_command.command("get", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_dir_option
@click.argument("params_json", required=False, default="{}")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CHROMA_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def get_command(
    ctx: click.Context,
    index_dir: str | None,
    params_json: str,
    output_format: str,
) -> None:
    """Run collection.get(**PARAMS_JSON) against the Chroma collection."""

    catalog = load_catalog(ctx)
    assert index_dir is not None
    params = parse_json_object(params_json, option_name="PARAMS_JSON")
    assert params is not None
    try:
        from chartcoach.search.chroma import ChromaIndex

        index = ChromaIndex.from_cache(
            catalog,
            cache_dir=index_dir,
            cache_mode="reuse_only",
        )
        result = index.collection.get(**params)
    except Exception as exc:
        raise click.ClickException(search_error_message(str(exc))) from exc
    emit_object(result, output_format=output_format)


__all__ = ["index_command"]
