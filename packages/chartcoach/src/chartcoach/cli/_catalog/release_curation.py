from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

import click

from chartcoach._catalog._object_store import CATALOG_STORE_SCHEMES
from chartcoach._catalog.paths import paths
from chartcoach._catalog.releases import CatalogRelease
from chartcoach._catalog.releases.models import safe_sha256

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
@click.argument("release_path", type=click.Path(path_type=Path), required=False)
@click.option(
    "--store",
    "store_url",
    help="File, S3, GCS, or Azure URL containing the published catalog.",
)
@click.option(
    "--digest", help="Validate this published release instead of catalog.json."
)
@click.option(
    "--expect-digest", help="Require the selected catalog to have this release digest."
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(RELEASE_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
def release_validate_command(
    release_path: Path | None,
    store_url: str | None,
    digest: str | None,
    expect_digest: str | None,
    output_format: str,
) -> None:
    """Validate local release files or fresh published catalog bytes."""

    if (release_path is None) == (store_url is None):
        raise click.UsageError("Pass either RELEASE_PATH or --store.")
    if digest is not None:
        if store_url is None:
            raise click.UsageError("--digest requires --store.")
        digest = _digest_or_fail(digest, "--digest")
    if expect_digest is not None:
        if store_url is None or digest is not None:
            raise click.UsageError(
                "--expect-digest requires --store and a selected catalog, with --digest omitted."
            )
        expect_digest = _digest_or_fail(expect_digest, "--expect-digest")
    if release_path is not None:
        release = _validate_release_or_fail(release_path)
    else:
        assert store_url is not None
        _store_scheme(store_url)
        release = _validate_published_release_or_fail(store_url, digest)
        if expect_digest is not None and release.digest != expect_digest:
            raise click.ClickException(
                f"Selected release digest is {release.digest}, expected {expect_digest}."
            )
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
        from chartcoach.curation import publish_release
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
    digest = _digest_or_fail(digest, "digest")
    if dry_run:
        _validate_published_release_or_fail(store_url, digest)
        emit_rows(
            [{"digest": digest, "path": paths.selected()}],
            output_format=output_format,
        )
        return
    try:
        from chartcoach.curation import select_release
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
    if scheme not in CATALOG_STORE_SCHEMES:
        raise click.BadParameter(
            "must use a file, S3, GCS, or Azure URL",
            param_hint="--store",
        )
    return scheme


def _validate_release_or_fail(release_path: Path) -> CatalogRelease:
    try:
        from chartcoach.curation import validate_release

        return validate_release(release_path)
    except json.JSONDecodeError as exc:
        raise click.ClickException(
            f"Catalog release file is not valid JSON: {release_path / 'release.json'}"
        ) from exc
    except ModuleNotFoundError as exc:
        raise click.ClickException(_curation_dependency_message(exc.name)) from exc
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc


def _validate_published_release_or_fail(
    destination: str, digest: str | None
) -> CatalogRelease:
    try:
        from chartcoach.curation import validate_published_release

        with storage_errors("validate", "published catalog"):
            return validate_published_release(destination, digest=digest)
    except ModuleNotFoundError as exc:
        raise click.ClickException(_curation_dependency_message(exc.name)) from exc
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc


def _digest_or_fail(value: str, param_hint: str) -> str:
    try:
        return safe_sha256(value, label="Catalog release digest")
    except ValueError as exc:
        raise click.BadParameter(str(exc), param_hint=param_hint) from exc


def _emit_release_result(record: dict[str, object], *, output_format: str) -> None:
    if output_format == "json":
        emit_object(record)
    else:
        emit_rows([record], output_format=output_format)


def _curation_dependency_message(name: str | None) -> str:
    package = name or "curation dependency"
    return f"{package} requires the optional `chartcoach[curation]` dependencies."


__all__ = ["register_release_commands"]
