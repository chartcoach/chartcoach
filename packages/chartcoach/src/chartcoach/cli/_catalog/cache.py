from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import Any

import click

from chartcoach.catalog.paths import paths

from ..common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    emit_rows,
    report_cache_download,
    storage_errors,
)


@click.group(
    "cache",
    context_settings=CONTEXT_SETTINGS,
    help="Prefetch published catalog artifacts.",
)
def cache_command() -> None:
    """Prefetch published catalog artifacts."""


@click.command("pull", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--source",
    help="Exact catalog release digest. Omit to pull catalog.json.",
)
@click.option(
    "--profile",
    help="Embedding profile whose LanceDB archive should also be prefetched.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def cache_pull_command(
    source: str | None,
    profile: str | None,
    output_format: str,
) -> None:
    """Download one published catalog release into the local cache."""

    try:
        with storage_errors("cache pull", source or paths.selected()):
            release, catalog_path, index_path = _pull_cache(source, profile=profile)
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc

    emit_rows(
        [
            {
                "digest": release.digest,
                "catalog_path": str(catalog_path),
                "index_path": str(index_path) if index_path is not None else "",
            }
        ],
        output_format=output_format,
    )


def register_cache_commands(group: click.Group) -> None:
    cache_command.add_command(cache_pull_command)
    group.add_command(cache_command)


def _pull_cache(
    source: str | None,
    *,
    profile: str | None,
) -> tuple[Any, Path, Path | None]:
    api = _cache_api()
    root = api.cache_root()
    store = api.cache_store(root)
    release, catalog_path = api.cache_catalog_bundle(
        api.artifact_store(),
        store,
        root,
        reference=source,
        reporter=report_cache_download,
    )
    index_path = (
        api.cache_index_artifact(
            api.artifact_store(),
            store,
            root,
            reference=release.digest,
            profile=profile,
            reporter=report_cache_download,
        )
        if profile is not None
        else None
    )
    return release, catalog_path, index_path


def _cache_api() -> Any:
    try:
        return import_module("chartcoach.catalog.curation.cache")
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            "Published catalog caching requires `chartcoach[curation]`."
        ) from exc


__all__ = ["register_cache_commands"]
