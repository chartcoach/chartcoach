from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import Any

import click

from chartcoach.constants import INDEX_DIR_ENV, SOURCE_ENV
from chartcoach.paths import default_index_dir

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
TRANSPORT_CHOICES = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def _is_missing_optional_dependency(exc: ModuleNotFoundError) -> bool:
    current: BaseException | None = exc
    while current is not None:
        if isinstance(current, ModuleNotFoundError):
            name = current.name
            if name is not None and (name == "mcp" or name.startswith("mcp.")):
                return True
        current = current.__cause__
    return False


def _load_server_module() -> Any:
    try:
        return import_module("chartcoach.mcp.server")
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
        if _is_missing_optional_dependency(exc):
            raise click.ClickException(
                "The `chartcoach mcp serve` command requires the optional MCP dependencies. Install `chartcoach[mcp]` to use it."
            ) from exc
        raise


@click.group(
    "mcp",
    context_settings=CONTEXT_SETTINGS,
    help="Run ChartCoach MCP servers.",
)
def mcp_command() -> None:
    """Run ChartCoach MCP servers."""


@mcp_command.command(
    "serve",
    context_settings=CONTEXT_SETTINGS,
    short_help="Start the ChartCoach MCP server.",
)
@click.option(
    "--source",
    "source_path",
    envvar=SOURCE_ENV,
    type=click.Path(path_type=Path),
    help=f"Catalog parquet file or guideline folder to serve. Defaults to ${SOURCE_ENV}.",
)
@click.option(
    "--index-dir",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    envvar=INDEX_DIR_ENV,
    default=default_index_dir(),
    show_default=True,
    help=(
        "Search index directory for Chroma-backed tools. "
        f"Defaults to ${INDEX_DIR_ENV}, then a platform cache path."
    ),
)
@click.option(
    "--transport",
    type=click.Choice(TRANSPORT_CHOICES, case_sensitive=False),
    help="MCP transport. Defaults to CHARTCOACH_MCP_TRANSPORT or stdio.",
)
@click.option(
    "--host",
    help="Host for sse and streamable-http transports. Defaults to CHARTCOACH_MCP_HOST or 127.0.0.1.",
)
@click.option(
    "--port",
    type=click.IntRange(1, 65535),
    help="Port for sse and streamable-http transports. Defaults to CHARTCOACH_MCP_PORT or 8000.",
)
@click.option(
    "--log-level",
    type=click.Choice(LOG_LEVEL_CHOICES, case_sensitive=False),
    help="Logging level. Defaults to CHARTCOACH_MCP_LOG_LEVEL or INFO.",
)
def serve_command(
    source_path: Path | None,
    index_dir: Path | None,
    transport: str | None,
    host: str | None,
    port: int | None,
    log_level: str | None,
) -> None:
    """Start the ChartCoach MCP server."""

    server = _load_server_module()
    try:
        config = server.resolve_config(
            index_dir=index_dir,
            source=source_path,
            transport=transport.lower() if transport is not None else None,
            host=host,
            port=port,
            log_level=log_level.upper() if log_level is not None else None,
        )
        server.main(
            settings=config.settings,
            runtime=config.runtime,
        )
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
        if _is_missing_optional_dependency(exc):
            raise click.ClickException(
                "The `chartcoach mcp serve` command requires the optional MCP dependencies. Install `chartcoach[mcp]` to use it."
            ) from exc
        raise
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc


__all__ = ["mcp_command", "serve_command"]
