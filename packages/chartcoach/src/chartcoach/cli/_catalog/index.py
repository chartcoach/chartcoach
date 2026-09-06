from __future__ import annotations

from pathlib import Path
from typing import Literal, cast

import click

from chartcoach.catalog.embedding import apply_embedding_variables
from chartcoach.catalog.errors import CatalogError

from ..common import (
    CONTEXT_SETTINGS,
    SEARCH_FORMATS,
    emit_object,
    emit_rows,
    guideline_matches_to_markdown,
    index_profile_option,
    load_catalog,
    source_option,
)


@click.command("search", context_settings=CONTEXT_SETTINGS)
@source_option
@index_profile_option
@click.argument("text")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=10,
    show_default=True,
    help="Maximum indexed documents to consider before guideline deduplication.",
)
@click.option("--where", help="LanceDB SQL filter over indexed document columns.")
@click.option(
    "--mode",
    type=click.Choice(("fts", "vector", "hybrid")),
    default="fts",
    show_default=True,
    help="Index search mode. Vector and hybrid modes embed the text.",
)
@click.option(
    "--embedding-vars",
    type=click.Path(path_type=Path, dir_okay=False),
    help="JSON file mapping LanceDB registry variable names to string values.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(SEARCH_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def search_command(
    ctx: click.Context,
    profile: str,
    text: str,
    limit: int,
    where: str | None,
    mode: str,
    embedding_vars: Path | None,
    output_format: str,
) -> None:
    """Search one index profile for guideline matches."""

    resolved_mode = cast(Literal["fts", "vector", "hybrid"], mode)
    try:
        if resolved_mode != "fts" and embedding_vars is not None:
            apply_embedding_variables(embedding_vars)
        result = load_catalog(ctx).search(
            text,
            profile=profile,
            mode=resolved_mode,
            limit=limit,
            where=where,
        )
    except CatalogError as exc:
        raise click.ClickException(str(exc)) from exc

    if output_format == "json":
        emit_object(result)
        return
    matches = result["matches"]
    if output_format == "markdown":
        click.echo(
            guideline_matches_to_markdown(matches).rstrip()
            or "No guideline entries matched."
        )
        return
    emit_rows(
        matches,
        output_format=output_format,
        empty_message="No guideline entries matched.",
    )


def register_index_commands(group: click.Group) -> None:
    group.add_command(search_command)


__all__ = ["register_index_commands"]
