from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import Any

import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
TRANSPORT_CHOICES = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
MCP_HELP = """Start the ChartCoach MCP server.

ChartCoach creates a ready coach at startup, then exposes its tools over MCP.
CLI options override environment variables. When an option is omitted, the command falls
back to the matching env var and then the built-in default.
"""


def _load_server_module() -> Any:
    try:
        return import_module("chartcoach.mcp.server")
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
        if exc.name == "mcp" or (exc.name is not None and exc.name.startswith("mcp.")):
            raise click.ClickException(
                "The `chartcoach mcp` command requires the optional MCP dependencies. Install `chartcoach[mcp]` to use it."
            ) from exc
        raise


@click.command(
    "mcp",
    context_settings=CONTEXT_SETTINGS,
    short_help="Start the ChartCoach MCP server.",
    help=MCP_HELP,
)
@click.option(
    "--catalog-path",
    metavar="PATH_OR_URL",
    help=(
        "Catalog source to load before building or reusing cached search data. "
        "Overrides CHARTCOACH_CATALOG_PATH."
    ),
)
@click.option(
    "--cache-dir",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    help="Directory root for cached catalog, Chroma, and DuckDB artifacts. Overrides CHARTCOACH_CACHE_DIR.",
)
@click.option(
    "--transport",
    type=click.Choice(TRANSPORT_CHOICES, case_sensitive=False),
    help="MCP transport to run. Overrides MCP_TRANSPORT. Allowed values: stdio, sse, streamable-http.",
)
@click.option(
    "--host",
    help="Host to bind for sse and streamable-http transports. Overrides MCP_HOST.",
)
@click.option(
    "--port",
    type=click.IntRange(1, 65535),
    help="Port to bind for sse and streamable-http transports. Overrides MCP_PORT.",
)
@click.option(
    "--log-level",
    type=click.Choice(LOG_LEVEL_CHOICES, case_sensitive=False),
    help="Logging level. Overrides MCP_LOG_LEVEL. Allowed values: DEBUG, INFO, WARNING, ERROR, CRITICAL.",
)
def mcp_command(
    catalog_path: str | None,
    cache_dir: Path | None,
    transport: str | None,
    host: str | None,
    port: int | None,
    log_level: str | None,
) -> None:
    """Start the ChartCoach MCP server."""

    server = _load_server_module()
    resolved_settings = server._resolve_settings(
        cache_dir=cache_dir,
        catalog=catalog_path,
    )
    resolved_runtime = server._resolve_runtime(
        transport=transport.lower() if transport is not None else None,
        host=host,
        port=port,
        log_level=log_level.upper() if log_level is not None else None,
    )
    server.main(
        settings=resolved_settings,
        runtime=resolved_runtime,
    )


__all__ = ["mcp_command"]
