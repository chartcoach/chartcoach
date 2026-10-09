from __future__ import annotations

from pathlib import Path

import click

from chartcoach._constants import CATALOG_ARTIFACT_BASE_URL, CATALOG_SELECTION_PATH

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
    help="Catalog location (CHARTCOACH_SOURCE). Defaults to the official catalog.",
)
@click.option(
    "--profile", help="Release-owned index profile (CHARTCOACH_INDEX_PROFILE)."
)
@click.option(
    "--embedding-vars",
    type=click.Path(path_type=Path, dir_okay=False),
    help="JSON registry variable file (CHARTCOACH_EMBEDDING_VARS). Values override the environment.",
)
@click.option(
    "--transport",
    type=click.Choice(["stdio", "sse", "streamable-http"], case_sensitive=False),
    help="Transport (CHARTCOACH_MCP_TRANSPORT). Default: stdio.",
)
@click.option("--host", help="HTTP listener (CHARTCOACH_MCP_HOST). Default: 127.0.0.1.")
@click.option(
    "--port",
    type=click.IntRange(1, 65535),
    help="HTTP port (CHARTCOACH_MCP_PORT). Default: 8000.",
)
@click.option(
    "--log-level",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False
    ),
    help="Log level (CHARTCOACH_MCP_LOG_LEVEL). Default: INFO.",
)
@click.option(
    "--public-url",
    help="Public HTTP origin (CHARTCOACH_MCP_PUBLIC_URL); adds its host and origin to the allowlists.",
)
@click.option(
    "--path", help="Streamable HTTP endpoint (CHARTCOACH_MCP_PATH). Default: /mcp."
)
@click.option(
    "--allowed-host",
    "allowed_hosts",
    multiple=True,
    help="Additional allowed Host value; overrides CHARTCOACH_MCP_ALLOWED_HOSTS when supplied.",
)
@click.option(
    "--allowed-origin",
    "allowed_origins",
    multiple=True,
    help="Additional browser origin; overrides CHARTCOACH_MCP_ALLOWED_ORIGINS when supplied.",
)
@click.option(
    "--stateless/--stateful",
    default=None,
    help="Legacy HTTP session policy (CHARTCOACH_MCP_STATELESS). Default: stateless.",
)
@click.option(
    "--json-response/--stream-response",
    default=None,
    help="HTTP response format (CHARTCOACH_MCP_JSON_RESPONSE). Default: JSON.",
)
@click.option(
    "--sql-timeout",
    type=click.FloatRange(min=0, min_open=True),
    help="SQL execution deadline in seconds (CHARTCOACH_MCP_SQL_TIMEOUT). Default: 5.",
)
def mcp_command(
    source: str | None,
    profile: str | None,
    embedding_vars: Path | None,
    transport: str | None,
    host: str | None,
    port: int | None,
    log_level: str | None,
    public_url: str | None,
    path: str | None,
    allowed_hosts: tuple[str, ...],
    allowed_origins: tuple[str, ...],
    stateless: bool | None,
    json_response: bool | None,
    sql_timeout: float | None,
) -> None:
    from chartcoach._catalog.errors import CatalogError

    try:
        from chartcoach.mcp import load_config, run
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            "chartcoach MCP server requires optional dependencies. Install chartcoach[mcp]."
        ) from exc
    try:
        config = load_config(
            overrides={
                "source": source,
                "profile": profile,
                "embedding_vars": embedding_vars,
                "transport": transport,
                "host": host,
                "port": port,
                "log_level": log_level,
                "public_url": public_url,
                "path": path,
                "allowed_hosts": allowed_hosts or None,
                "allowed_origins": allowed_origins or None,
                "stateless": stateless,
                "json_response": json_response,
                "sql_timeout": sql_timeout,
            }
        )
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
