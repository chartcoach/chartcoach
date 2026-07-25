from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

import click

from chartcoach.catalog.paths import paths
from chartcoach.catalog.releases import CatalogRelease
from chartcoach.catalog.releases.models import safe_sha256

from ..common import CONTEXT_SETTINGS, emit_object, emit_rows, storage_errors

RELEASE_FORMATS = ("table", "json")


@click.group(
    "release",
    context_settings=CONTEXT_SETTINGS,
    help="Validate and publish catalog releases.",
)
def release_command() -> None:
    """Validate and publish catalog releases."""


@click.command("validate", context_settings=CONTEXT_SETTINGS)
@click.argument("release_path", type=click.Path(path_type=Path))
@click.option(
    "--format",
    "output_format",
    type=click.Choice(RELEASE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def release_validate_command(release_path: Path, output_format: str) -> None:
    """Validate a catalog release directory."""

    release = _validate_release_or_fail(release_path)
    _emit_release_result(release.to_record(), output_format=output_format)


@click.command("publish", context_settings=CONTEXT_SETTINGS)
@click.argument("release_path", type=click.Path(path_type=Path))
@click.option(
    "--store",
    "store_url",
    required=True,
    help="File, S3, GCS, or Azure URL that receives the release objects.",
)
@click.option("--dry-run", is_flag=True, help="Print object keys without writing.")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(RELEASE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def release_publish_command(
    release_path: Path,
    store_url: str,
    dry_run: bool,
    output_format: str,
) -> None:
    """Publish an immutable catalog release."""

    _store_scheme(store_url)
    if dry_run:
        release = _validate_release_or_fail(release_path)
        release_paths = paths.release(release.digest)
        targets = [
            *(release_paths.artifact(path) for path in release.artifacts),
            release_paths.json(),
        ]
        emit_rows(
            [{"path": path} for path in targets],
            output_format=output_format,
        )
        return

    try:
        from chartcoach.catalog.curation import publish_release
    except ModuleNotFoundError as exc:
        raise click.ClickException(_curation_dependency_message(exc.name)) from exc
    try:
        with storage_errors("publish", "catalog destination"):
            result = publish_release(release_path, store_url)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc
    _emit_release_result(result.to_record(), output_format=output_format)


@click.command("select", context_settings=CONTEXT_SETTINGS)
@click.argument("digest")
@click.option(
    "--store",
    "store_url",
    required=True,
    help="File, S3, GCS, or Azure URL containing the published release.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Print the selection target without updating catalog.json.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(RELEASE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def release_select_command(
    digest: str,
    store_url: str,
    dry_run: bool,
    output_format: str,
) -> None:
    """Select a published release through catalog.json."""

    _store_scheme(store_url)
    try:
        digest = safe_sha256(digest, label="Catalog release digest")
    except ValueError as exc:
        raise click.BadParameter(str(exc), param_hint="digest") from exc
    if dry_run:
        emit_rows(
            [{"digest": digest, "path": paths.selected()}],
            output_format=output_format,
        )
        return
    try:
        from chartcoach.catalog.curation import select_release
    except ModuleNotFoundError as exc:
        raise click.ClickException(_curation_dependency_message(exc.name)) from exc
    try:
        with storage_errors("select", paths.selected()):
            release = select_release(digest, store_url)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc
    _emit_release_result(
        {"digest": release.digest, "updated": [paths.selected()]},
        output_format=output_format,
    )


def register_release_commands(group: click.Group) -> None:
    release_command.add_command(release_validate_command)
    release_command.add_command(release_publish_command)
    release_command.add_command(release_select_command)
    group.add_command(release_command)


def _store_scheme(value: str) -> str:
    scheme = urlsplit(value).scheme.lower()
    if scheme not in {
        "abfs",
        "abfss",
        "adl",
        "az",
        "azure",
        "file",
        "gcp",
        "gcs",
        "gs",
        "s3",
        "s3a",
    }:
        raise click.BadParameter(
            "must use a file, S3, GCS, or Azure URL",
            param_hint="--store",
        )
    return scheme


def _validate_release_or_fail(release_path: Path) -> CatalogRelease:
    try:
        from chartcoach.catalog.curation import validate_release

        return validate_release(release_path)
    except json.JSONDecodeError as exc:
        raise click.ClickException(
            f"Catalog release file is not valid JSON: {release_path / 'release.json'}"
        ) from exc
    except ModuleNotFoundError as exc:
        raise click.ClickException(_curation_dependency_message(exc.name)) from exc
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc


def _emit_release_result(record: dict[str, object], *, output_format: str) -> None:
    if output_format == "json":
        emit_object(record)
    else:
        emit_rows([record], output_format=output_format)


def _curation_dependency_message(name: str | None) -> str:
    package = name or "curation dependency"
    return f"{package} requires the optional `chartcoach[curation]` dependencies."


__all__ = ["register_release_commands"]
