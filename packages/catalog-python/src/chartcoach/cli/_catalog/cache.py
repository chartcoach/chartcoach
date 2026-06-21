from __future__ import annotations

import shutil
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import click

from chartcoach.catalog.remote import (
    CatalogArtifactRelease,
    artifact_cache_root,
    default_artifact_index_url,
    download_catalog_bundle,
    download_index_artifact,
    read_artifact_index,
    release_metadata_url_from_index,
)
from chartcoach.constants import (
    DEFAULT_CATALOG_VERSION,
    LANCE_DOCUMENT_TABLE,
)
from chartcoach.tools import format_error

from ..common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    echo_info,
    echo_success,
    emit_rows,
    report_cache_download,
)

CACHE_FORMATS = ROW_FORMATS


@click.group(
    "cache",
    context_settings=CONTEXT_SETTINGS,
    help="Inspect, clear, and prefetch chartcoach artifact cache entries.",
)
def cache_command() -> None:
    """Inspect, clear, and prefetch chartcoach artifact cache entries."""


@click.command("path", context_settings=CONTEXT_SETTINGS)
def cache_path_command() -> None:
    """Print the chartcoach artifact cache root."""

    click.echo(artifact_cache_root())


@click.command("list", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CACHE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def cache_list_command(output_format: str) -> None:
    """List locally cached catalog releases."""

    rows = _cached_release_rows()
    emit_rows(rows, output_format=output_format, empty_message="No cached releases.")


@click.command("versions", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--index-url",
    default=None,
    help="Artifact index URL. Defaults to the configured chartcoach artifact host.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CACHE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def cache_versions_command(index_url: str | None, output_format: str) -> None:
    """List catalog releases from the root artifact index."""

    index = read_artifact_index(index_url)
    rows = [_release_row(release) for release in index.catalogs]
    emit_rows(rows, output_format=output_format, empty_message="No catalog releases.")


@click.command("clear", context_settings=CONTEXT_SETTINGS)
@click.option("--all", "clear_all", is_flag=True, help="Remove every cached release.")
@click.option("--version", help="Catalog version to remove from the cache.")
@click.option("--digest", help="Catalog digest to remove from the cache.")
@click.option("--yes", is_flag=True, help="Accepted for non-interactive scripts.")
def cache_clear_command(
    clear_all: bool,
    version: str | None,
    digest: str | None,
    yes: bool,
) -> None:
    """Delete cached catalog artifacts."""

    del yes
    targets = _clear_targets(clear_all=clear_all, version=version, digest=digest)
    removed: list[Path] = []
    for target in targets:
        if target.exists():
            shutil.rmtree(target)
            removed.append(target)
    if removed:
        for target in removed:
            echo_success("Deleted cached artifacts", detail=str(target))
        return
    echo_info("No cached artifacts matched", detail=str(artifact_cache_root()))


@click.command("pull", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--version",
    help="Catalog version to pull. Defaults to the newest release in the artifact index.",
)
@click.option("--digest", help="Catalog digest to pull.")
@click.option(
    "--catalog-only",
    is_flag=True,
    help="Download only metadata, MANIFEST.md, and entries.parquet.",
)
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name for the default index artifact.",
)
@click.option(
    "--index-url",
    default=None,
    help="Artifact index URL. Defaults to the configured chartcoach artifact host.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(CACHE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def cache_pull_command(
    version: str | None,
    digest: str | None,
    catalog_only: bool,
    table_name: str,
    index_url: str | None,
    output_format: str,
) -> None:
    """Download a release into the chartcoach artifact cache."""

    release = _resolve_release(index_url=index_url, version=version, digest=digest)
    metadata_url = release_metadata_url_from_index(
        release,
        base_url=_artifact_base_url(index_url),
    )
    catalog_path = download_catalog_bundle(metadata_url, reporter=report_cache_download)

    index_path: Path | None = None
    if not catalog_only:
        index_path = download_index_artifact(
            metadata_url,
            table_name=table_name,
            reporter=report_cache_download,
        )

    rows = [
        {
            "version": release.version,
            "digest": release.digest,
            "catalog_path": str(catalog_path),
            "index_path": str(index_path) if index_path is not None else "",
        }
    ]
    emit_rows(rows, output_format=output_format)


def register_cache_commands(group: click.Group) -> None:
    cache_command.add_command(cache_path_command)
    cache_command.add_command(cache_list_command)
    cache_command.add_command(cache_versions_command)
    cache_command.add_command(cache_clear_command)
    cache_command.add_command(cache_pull_command)
    group.add_command(cache_command)


def _resolve_release(
    *,
    index_url: str | None,
    version: str | None,
    digest: str | None,
) -> CatalogArtifactRelease:
    index = read_artifact_index(index_url)
    try:
        return index.catalog(version=version, digest=digest)
    except KeyError as exc:
        label = version or digest or "latest release"
        raise click.ClickException(
            format_error(
                f"Catalog release not found: {label}",
                [
                    "Run `chartcoach catalog cache versions` to inspect releases.",
                    f"Artifact index: {index_url or default_artifact_index_url()}",
                ],
            )
        ) from exc


def _artifact_base_url(index_url: str | None) -> str | None:
    if index_url is None:
        return None
    parsed = urlparse(index_url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc == "":
        return None
    return urlunparse((parsed.scheme, parsed.netloc, "", "", "", ""))


def _release_row(release: CatalogArtifactRelease) -> dict[str, object]:
    return {
        "name": release.name,
        "version": release.version,
        "digest": release.digest,
        "metadata": release.metadata,
        "artifacts": len(release.artifacts),
    }


def _cached_release_rows() -> list[dict[str, object]]:
    root = artifact_cache_root() / "catalog" / "releases"
    if not root.is_dir():
        return []
    rows: list[dict[str, object]] = []
    for version_path in sorted(root.iterdir(), key=lambda path: path.name):
        if not version_path.is_dir():
            continue
        for digest_path in sorted(version_path.iterdir(), key=lambda path: path.name):
            if not digest_path.is_dir():
                continue
            rows.append(
                {
                    "version": version_path.name,
                    "digest": digest_path.name,
                    "path": str(digest_path),
                    "metadata": (digest_path / "metadata.json").is_file(),
                    "catalog": _catalog_files_present(digest_path),
                    "indexes": _index_count(digest_path),
                }
            )
    return rows


def _catalog_files_present(path: Path) -> bool:
    return (path / "MANIFEST.md").is_file() and (path / "entries.parquet").is_file()


def _index_count(path: Path) -> int:
    indexes_root = path / "indexes" / "lancedb"
    if not indexes_root.is_dir():
        return 0
    return sum(1 for child in indexes_root.glob("*/*/db") if child.is_dir())


def _clear_targets(
    *,
    clear_all: bool,
    version: str | None,
    digest: str | None,
) -> list[Path]:
    releases_root = artifact_cache_root() / "catalog" / "releases"
    if clear_all:
        return [artifact_cache_root() / "catalog"]
    if version is None:
        version = DEFAULT_CATALOG_VERSION
    if digest is not None:
        return [releases_root / version / digest]
    version_root = releases_root / version
    if not version_root.is_dir():
        return [version_root]
    return [path for path in version_root.iterdir() if path.is_dir()]


__all__ = ["register_cache_commands"]
