from __future__ import annotations

import os
from collections.abc import Mapping
from ipaddress import IPv6Address
from pathlib import Path
from typing import Literal
from urllib.parse import urlsplit

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    ValidationError,
    ValidationInfo,
    field_validator,
)

from chartcoach._catalog.embedding import read_embedding_variables
from chartcoach._catalog.errors import CatalogError

Transport = Literal["stdio", "sse", "streamable-http"]
Level = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

LOCAL_HOSTS = (
    "127.0.0.1",
    "127.0.0.1:*",
    "localhost",
    "localhost:*",
    "[::1]",
    "[::1]:*",
)
LOCAL_ORIGINS = (
    "http://127.0.0.1",
    "http://127.0.0.1:*",
    "http://localhost",
    "http://localhost:*",
    "http://[::1]",
    "http://[::1]:*",
)

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


class MCPConfig(BaseModel):
    """Validated launch settings. Credentials are excluded from dumps and repr."""

    model_config = ConfigDict(extra="forbid", frozen=True, hide_input_in_errors=True)

    source: str | Path | None = None
    profile: str | None = None
    embedding_vars: Path | None = None
    transport: Transport = "stdio"
    host: str = "127.0.0.1"
    port: int = Field(default=8000, ge=1, le=65535)
    log_level: Level = "INFO"
    public_url: str | None = None
    path: str = "/mcp"
    allowed_hosts: tuple[str, ...] = LOCAL_HOSTS
    allowed_origins: tuple[str, ...] = LOCAL_ORIGINS
    token: SecretStr | None = Field(default=None, repr=False, exclude=True)
    stateless: bool = True
    json_response: bool = True
    sql_timeout: float = Field(default=5.0, gt=0, allow_inf_nan=False)
    embedding_variables: dict[str, str] = Field(
        default_factory=dict, repr=False, exclude=True, validate_default=True
    )
    embedding_environment: dict[str, str] | None = Field(
        default=None, repr=False, exclude=True
    )

    @field_validator("embedding_variables", mode="before")
    @classmethod
    def resolve_variable_file(cls, value: object, info: ValidationInfo) -> object:
        path = info.data.get("embedding_vars")
        if path is not None and isinstance(value, Mapping):
            variables = read_embedding_variables(path)
            variables.update(value)
            return variables
        return value

    @field_validator("host", "profile", "source")
    @classmethod
    def nonempty(cls, value: str | Path | None) -> str | Path | None:
        if isinstance(value, str) and (not value.strip() or value != value.strip()):
            raise ValueError("Use a non-empty value without surrounding whitespace.")
        return value

    @field_validator("transport", mode="before")
    @classmethod
    def normalize_transport(cls, value: object) -> object:
        return value.lower() if isinstance(value, str) else value

    @field_validator("log_level", mode="before")
    @classmethod
    def normalize_level(cls, value: object) -> object:
        return value.upper() if isinstance(value, str) else value

    @field_validator("public_url")
    @classmethod
    def public_origin(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if any(
            character.isspace() or ord(character) < 32 or ord(character) == 127
            for character in value
        ):
            raise ValueError(
                "Use an HTTP origin without whitespace or control characters."
            )
        parsed = urlsplit(value)
        if (
            parsed.scheme not in {"https", "http"}
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path not in {"", "/"}
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError(
                "Use an HTTP or HTTPS origin without credentials or a path."
            )
        port = parsed.port
        host = parsed.hostname.lower()
        if not host.isascii():
            raise ValueError("Use an ASCII or punycode hostname in the public origin.")
        if ":" in host:
            host = f"[{IPv6Address(host).compressed}]"
        if port is not None and port != (443 if parsed.scheme == "https" else 80):
            host = f"{host}:{port}"
        return f"{parsed.scheme}://{host}"

    @field_validator("path")
    @classmethod
    def endpoint_path(cls, value: str) -> str:
        if (
            not value.startswith("/")
            or value.startswith("//")
            or value == "/healthz"
            or any(character in value for character in "?#{}\\")
            or any(character.isspace() for character in value)
        ):
            raise ValueError("Use an absolute HTTP path distinct from /healthz.")
        return value

    @field_validator("allowed_hosts", "allowed_origins")
    @classmethod
    def explicit_allowlist(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        if any(not value or value == "*" or value != value.strip() for value in values):
            raise ValueError(
                "List explicit hosts or origins; a bare wildcard is not supported."
            )
        return values

    @field_validator("token")
    @classmethod
    def bearer_token(cls, value: SecretStr | None) -> SecretStr | None:
        if value is not None:
            token = value.get_secret_value()
            if not token or any(
                ord(character) < 33 or ord(character) > 126 for character in token
            ):
                raise ValueError(
                    "Use one non-empty bearer token without spaces or control characters."
                )
        return value


def load_config(
    *,
    environment: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
) -> MCPConfig:
    """Resolve explicit options over environment values, then schema defaults.

    This function does not read dotenv files or mutate the process environment.
    The CLI loads its dotenv file before calling it.
    """
    env = dict(os.environ if environment is None else environment)
    values: dict[str, object] = {}
    for field, name in ENVIRONMENT_FIELDS.items():
        value = env.get(name)
        if value:
            values[field] = (
                tuple(item.strip() for item in value.split(","))
                if field in {"allowed_hosts", "allowed_origins"}
                else value
            )
    values.update(
        {name: value for name, value in (overrides or {}).items() if value is not None}
    )
    values.setdefault("embedding_environment", env)
    try:
        config = MCPConfig.model_validate(values)
    except ValidationError as exc:
        errors = exc.errors(include_input=False)
        for error in errors:
            cause = error.get("ctx", {}).get("error")
            if isinstance(cause, CatalogError):
                raise cause from None
        names = sorted(
            {
                ENVIRONMENT_FIELDS.get(str(error["loc"][0]), str(error["loc"][0]))
                if error["loc"]
                else "MCPConfig"
                for error in errors
            }
        )
        raise ValueError(
            "Invalid MCP configuration: " + ", ".join(names) + "."
        ) from None
    return config
