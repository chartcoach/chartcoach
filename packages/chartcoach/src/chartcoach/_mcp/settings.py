"""Shared MCP settings metadata; safe to import without optional capabilities."""

from typing import Literal

Transport = Literal["stdio", "sse", "streamable-http"]
Level = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

DEFAULT_TRANSPORT: Transport = "stdio"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_LOG_LEVEL: Level = "INFO"
DEFAULT_PATH = "/mcp"
DEFAULT_STATELESS = True
DEFAULT_JSON_RESPONSE = True
DEFAULT_SQL_TIMEOUT = 5.0

# CLI, environment loading, and Python composition use this one schema.
ENVIRONMENT_FIELDS = {
    "source": "CHARTCOACH_SOURCE",
    "profile": "CHARTCOACH_INDEX_PROFILE",
    "embedding_vars": "CHARTCOACH_EMBEDDING_VARS",
    "transport": "CHARTCOACH_MCP_TRANSPORT",
    "host": "CHARTCOACH_MCP_HOST",
    "port": "CHARTCOACH_MCP_PORT",
    "log_level": "CHARTCOACH_MCP_LOG_LEVEL",
    "public_url": "CHARTCOACH_MCP_PUBLIC_URL",
    "path": "CHARTCOACH_MCP_PATH",
    "allowed_hosts": "CHARTCOACH_MCP_ALLOWED_HOSTS",
    "allowed_origins": "CHARTCOACH_MCP_ALLOWED_ORIGINS",
    "token": "CHARTCOACH_MCP_TOKEN",
    "stateless": "CHARTCOACH_MCP_STATELESS",
    "json_response": "CHARTCOACH_MCP_JSON_RESPONSE",
    "sql_timeout": "CHARTCOACH_MCP_SQL_TIMEOUT",
}
