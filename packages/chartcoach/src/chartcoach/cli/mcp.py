from __future__ import annotations

import click

from chartcoach.constants import (
    CATALOG_ARTIFACT_BASE_URL,
    CATALOG_ENTRY_PATH,
    INDEX_PROFILE_ENV,
    SOURCE_ENV,
)
from chartcoach.tools import format_error

from .common import storage_errors

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
TRANSPORT_CHOICES = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
MCP_TRANSPORT_ENV = "CHARTCOACH_MCP_TRANSPORT"
MCP_HOST_ENV = "CHARTCOACH_MCP_HOST"
MCP_PORT_ENV = "CHARTCOACH_MCP_PORT"
MCP_LOG_LEVEL_ENV = "CHARTCOACH_MCP_LOG_LEVEL"
MCP_INDEX_EXTRA_HINTS = (
    "For one-off runs, use `uvx --from 'chartcoach[mcp,index]@latest' chartcoach ...`.",
    "From a checkout, use `uv run --package chartcoach --extra mcp --extra index chartcoach ...`.",
)


def _is_missing_optional_dependency(exc: ModuleNotFoundError) -> bool:
    return _has_missing_module(exc, ("mcp",))


def _is_missing_search_dependency(exc: ModuleNotFoundError) -> bool:
    return _has_missing_module(exc, ("lancedb",))


def _has_missing_module(
    exc: ModuleNotFoundError,
    module_names: tuple[str, ...],
) -> bool:
    current: BaseException | None = exc
    while current is not None:
        if isinstance(current, ModuleNotFoundError):
            name = current.name
            if name is not None and any(
                name == module or name.startswith(f"{module}.")
                for module in module_names
            ):
                return True
        current = current.__cause__
    return False


@click.command(
    "mcp",
    context_settings=CONTEXT_SETTINGS,
    help="Start the chartcoach MCP server.",
)
@click.option(
    "--source",
    "source_path",
    envvar=SOURCE_ENV,
    metavar="PATH_OR_URI",
    help=(
        "Catalog folder, bundle, catalog.json, or release.json path or URI. "
        f"Defaults to ${SOURCE_ENV}, then the official catalog."
    ),
)
@click.option(
    "--profile",
    envvar=INDEX_PROFILE_ENV,
    help="Embedding profile in the catalog release.",
)
@click.option(
    "--transport",
    type=click.Choice(TRANSPORT_CHOICES, case_sensitive=False),
    envvar=MCP_TRANSPORT_ENV,
    default="stdio",
    show_default=True,
    help="MCP transport.",
)
@click.option(
    "--host",
    envvar=MCP_HOST_ENV,
    default="127.0.0.1",
    show_default=True,
    help="Host for sse and streamable-http transports.",
)
@click.option(
    "--port",
    type=click.IntRange(1, 65535),
    envvar=MCP_PORT_ENV,
    default=8000,
    show_default=True,
    help="Port for sse and streamable-http transports.",
)
@click.option(
    "--log-level",
    type=click.Choice(LOG_LEVEL_CHOICES, case_sensitive=False),
    envvar=MCP_LOG_LEVEL_ENV,
    default="INFO",
    show_default=True,
    help="Logging level.",
)
def mcp_command(
    source_path: str | None,
    profile: str | None,
    transport: str,
    host: str,
    port: int,
    log_level: str,
) -> None:
    """Start the chartcoach MCP server."""

    try:
        _run_server(
            profile=profile,
            source_path=source_path,
            transport=transport,
            host=host,
            port=port,
            log_level=log_level,
        )
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
        if _is_missing_optional_dependency(exc):
            raise click.ClickException(
                "The `chartcoach mcp` command requires the optional MCP dependencies. Install `chartcoach[mcp]` to use it."
            ) from exc
        if _is_missing_search_dependency(exc):
            raise click.ClickException(
                format_error(
                    "Indexed MCP search requires the optional LanceDB dependencies.",
                    MCP_INDEX_EXTRA_HINTS,
                )
            ) from exc
        raise
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc


def _run_server(
    *,
    profile: str | None,
    source_path: str | None,
    transport: str,
    host: str,
    port: int,
    log_level: str,
) -> None:
    from chartcoach import mcp

    default_source = f"{CATALOG_ARTIFACT_BASE_URL.rstrip('/')}/{CATALOG_ENTRY_PATH}"
    with storage_errors("MCP startup", source_path or default_source):
        mcp.main(
            profile=profile,
            source=source_path,
            transport=transport.lower(),
            host=host,
            port=port,
            log_level=log_level.upper(),
        )


__all__ = ["mcp_command"]
