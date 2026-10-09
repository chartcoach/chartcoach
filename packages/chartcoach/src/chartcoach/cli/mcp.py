from __future__ import annotations

from pathlib import Path
from typing import get_args

import click

from chartcoach._constants import CATALOG_ARTIFACT_BASE_URL, CATALOG_SELECTION_PATH
from chartcoach._mcp import settings

from .common import storage_errors
from .environment import load_env_file


@click.command(
    "mcp",
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Start the chartcoach MCP server. Options override environment variables and .env.",
)
@click.option(
    "--env-file",
    type=click.Path(path_type=Path, dir_okay=False),
    envvar="CHARTCOACH_ENV_FILE",
    is_eager=True,
    expose_value=False,
    callback=load_env_file,
    help="Load this UTF-8 dotenv file. Defaults to .env in the working directory. Existing environment values win.",
)
@click.option(
    "--source",
    metavar="PATH_OR_URI",
    help=f"Catalog location ({settings.ENVIRONMENT_FIELDS['source']}). Defaults to the official catalog.",
)
@click.option(
    "--profile",
    help=f"Release-owned index profile ({settings.ENVIRONMENT_FIELDS['profile']}).",
)
@click.option(
    "--embedding-vars",
    type=click.Path(path_type=Path, dir_okay=False),
    help=f"JSON registry variable file ({settings.ENVIRONMENT_FIELDS['embedding_vars']}). Values override the environment.",
)
@click.option(
    "--transport",
    type=click.Choice(get_args(settings.Transport), case_sensitive=False),
    help=f"Transport ({settings.ENVIRONMENT_FIELDS['transport']}). Default: {settings.DEFAULT_TRANSPORT}.",
)
@click.option(
    "--host",
    help=f"HTTP listener ({settings.ENVIRONMENT_FIELDS['host']}). Default: {settings.DEFAULT_HOST}.",
)
@click.option(
    "--port",
    type=click.IntRange(1, 65535),
    help=f"HTTP port ({settings.ENVIRONMENT_FIELDS['port']}). Default: {settings.DEFAULT_PORT}.",
)
@click.option(
    "--log-level",
    type=click.Choice(get_args(settings.Level), case_sensitive=False),
    help=f"Log level ({settings.ENVIRONMENT_FIELDS['log_level']}). Default: {settings.DEFAULT_LOG_LEVEL}.",
)
@click.option(
    "--public-url",
    help=f"Public HTTP origin ({settings.ENVIRONMENT_FIELDS['public_url']}); adds its host and origin to the allowlists.",
)
@click.option(
    "--path",
    help=f"Streamable HTTP endpoint ({settings.ENVIRONMENT_FIELDS['path']}). Default: {settings.DEFAULT_PATH}.",
)
@click.option(
    "--allowed-host",
    "allowed_hosts",
    multiple=True,
    help=f"Additional allowed Host value; overrides {settings.ENVIRONMENT_FIELDS['allowed_hosts']} when supplied.",
)
@click.option(
    "--allowed-origin",
    "allowed_origins",
    multiple=True,
    help=f"Additional browser origin; overrides {settings.ENVIRONMENT_FIELDS['allowed_origins']} when supplied.",
)
@click.option(
    "--stateless/--stateful",
    default=None,
    help=f"HTTP session policy ({settings.ENVIRONMENT_FIELDS['stateless']}). Default: {'stateless' if settings.DEFAULT_STATELESS else 'stateful'}.",
)
@click.option(
    "--json-response/--stream-response",
    default=None,
    help=f"HTTP response format ({settings.ENVIRONMENT_FIELDS['json_response']}). Default: {'JSON' if settings.DEFAULT_JSON_RESPONSE else 'stream'}.",
)
@click.option(
    "--sql-timeout",
    type=click.FloatRange(min=0, min_open=True),
    help=f"SQL execution deadline in seconds ({settings.ENVIRONMENT_FIELDS['sql_timeout']}). Default: {settings.DEFAULT_SQL_TIMEOUT:g}.",
)
def mcp_command(**options: object) -> None:
    from chartcoach._catalog.errors import CatalogError

    try:
        from chartcoach.mcp import load_config, run
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            "chartcoach MCP server requires optional dependencies. Install chartcoach[mcp]."
        ) from exc
    try:
        for name in ("allowed_hosts", "allowed_origins"):
            options[name] = options[name] or None
        config = load_config(overrides=options)
        target = (
            str(config.source)
            if config.source is not None
            else f"{CATALOG_ARTIFACT_BASE_URL}/{CATALOG_SELECTION_PATH}"
        )
        with storage_errors("read", target):
            run(config)
    except (CatalogError, OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc


__all__ = ["mcp_command"]
