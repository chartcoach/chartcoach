from __future__ import annotations

import os
from pathlib import Path

import pytest
from chartcoach.cli.main import main
from chartcoach.mcp import MCPConfig, load_config
from click.testing import CliRunner
from pydantic import BaseModel, ValidationError

pytestmark = pytest.mark.mcp


def test_environment_overrides_and_configuration_redaction(tmp_path: Path) -> None:
    before = dict(os.environ)
    variables = tmp_path / "variables.json"
    variables.write_text('{"provider-key": "file-secret"}')
    config = load_config(
        environment={
            "CHARTCOACH_MCP_TRANSPORT": "STREAMABLE-HTTP",
            "CHARTCOACH_MCP_HOST": "0.0.0.0",
            "CHARTCOACH_MCP_PORT": "9000",
            "CHARTCOACH_MCP_PUBLIC_URL": "https://mcp.chartcoach.dev/",
            "CHARTCOACH_MCP_ALLOWED_HOSTS": "mcp.internal, mcp.example.test",
            "CHARTCOACH_MCP_TOKEN": "access-secret",
            "CHARTCOACH_MCP_STATELESS": "false",
            "CHARTCOACH_MCP_SQL_TIMEOUT": "2.5",
            "CHARTCOACH_EMBEDDING_VARS": str(variables),
            "OPENROUTER_API_KEY": "provider-secret",
        },
        overrides={"port": 8001},
    )
    assert config.transport == "streamable-http"
    assert config.port == 8001
    assert config.allowed_hosts == ("mcp.internal", "mcp.example.test")
    assert config.public_url == "https://mcp.chartcoach.dev"
    assert config.stateless is False
    assert config.sql_timeout == 2.5
    assert config.embedding_variables == {"provider-key": "file-secret"}
    assert config.embedding_environment is not None
    assert config.embedding_environment["OPENROUTER_API_KEY"] == "provider-secret"
    assert config.token is not None
    for rendered in (repr(config), config.model_dump_json()):
        assert "secret" not in rendered
    assert dict(os.environ) == before


@pytest.mark.parametrize(
    "name,value",
    [
        ("CHARTCOACH_MCP_PORT", "private-invalid-value"),
        ("CHARTCOACH_MCP_TRANSPORT", "private-invalid-value"),
        ("CHARTCOACH_MCP_TOKEN", "private invalid value"),
        (
            "CHARTCOACH_MCP_PUBLIC_URL",
            "https://user:private-invalid-value@example.test",
        ),
        ("CHARTCOACH_MCP_PUBLIC_URL", "https://mcp.example.test\n"),
    ],
)
def test_configuration_errors_name_settings_without_values(
    name: str, value: str
) -> None:
    with pytest.raises(ValueError) as caught:
        load_config(environment={name: value})
    assert name in str(caught.value)
    assert value not in str(caught.value)


def test_python_validation_errors_hide_credentials() -> None:
    secret = "private invalid credential"
    with pytest.raises(ValidationError) as caught:
        MCPConfig(token=secret)
    assert secret not in str(caught.value)
    assert "bearer token" in str(caught.value)


@pytest.mark.parametrize(
    "contents", ["[" * 32000 + "0" + "]" * 32000, '{"key": ' + "1" * 5000 + "}"]
)
def test_nested_variable_json_returns_a_cli_diagnostic(
    tmp_path: Path, contents: str
) -> None:
    file = tmp_path / "variables.json"
    file.write_text(contents)
    result = CliRunner().invoke(main, ["mcp", "--embedding-vars", str(file)])
    assert result.exit_code == 1
    assert "Embedding variable file must be a UTF-8 JSON object" in result.output


@pytest.mark.parametrize(
    "overrides",
    [
        {"path": "/healthz"},
        {"path": "/{rest:path}"},
        {"path": "/mcp/{name}"},
        {"path": "/mcp\\tools"},
        {"path": "relative"},
        {"public_url": "https://faß.example"},
        {"sql_timeout": float("inf")},
        {"allowed_origins": ("*",)},
    ],
)
def test_python_composition_uses_the_same_configuration_contract(
    overrides: dict[str, object],
) -> None:
    with pytest.raises(ValidationError):
        MCPConfig.model_validate(overrides)


def test_dotenv_is_loaded_before_options_with_process_and_flag_precedence(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from chartcoach import mcp

    captured: list[MCPConfig] = []
    monkeypatch.setattr(mcp, "run", captured.append)
    for name in ("CHARTCOACH_MCP_HOST", "CHARTCOACH_SOURCE", "OPENROUTER_API_KEY"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("CHARTCOACH_MCP_PORT", "8001")
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text(
        "CHARTCOACH_MCP_HOST=0.0.0.0\nCHARTCOACH_MCP_PORT=9000\n"
        "CHARTCOACH_SOURCE=./catalog\nOPENROUTER_API_KEY='dotenv-secret'\n"
    )
    result = CliRunner().invoke(main, ["mcp", "--port", "8002"])
    assert result.exit_code == 0, result.output
    assert captured[-1].host == "0.0.0.0"
    assert captured[-1].port == 8002
    assert captured[-1].source == "./catalog"
    environment = captured[-1].embedding_environment
    assert environment is not None
    assert environment["OPENROUTER_API_KEY"] == "dotenv-secret"
    assert os.environ["CHARTCOACH_MCP_PORT"] == "8001"
    assert "dotenv-secret" not in result.output


def test_explicit_dotenv_file_and_missing_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from chartcoach import mcp

    captured: list[MCPConfig] = []
    monkeypatch.setattr(mcp, "run", captured.append)
    monkeypatch.delenv("CHARTCOACH_MCP_PATH", raising=False)
    file = tmp_path / "deployment.env"
    file.write_text("CHARTCOACH_MCP_PATH=/catalog/mcp\n")
    result = CliRunner().invoke(main, ["mcp", "--env-file", str(file)])
    assert result.exit_code == 0, result.output
    assert captured[-1].path == "/catalog/mcp"
    result = CliRunner().invoke(main, ["mcp", "--env-file", str(tmp_path / "missing")])
    assert result.exit_code == 2
    assert "--env-file" in result.output


def test_direct_config_resolves_variable_file_once(tmp_path: Path) -> None:
    file = tmp_path / "variables.json"
    file.write_text('{"key": "file-secret", "other": "other-secret"}')
    config = MCPConfig(
        embedding_vars=file, embedding_variables={"key": "explicit-secret"}
    )
    file.unlink()
    assert MCPConfig.model_validate(config) is config

    class Deployment(BaseModel):
        mcp: MCPConfig

    assert Deployment(mcp=config).mcp is config
    assert config.embedding_variables == {
        "key": "explicit-secret",
        "other": "other-secret",
    }
    assert "secret" not in config.model_dump_json()


def test_explicit_embedding_environment_overrides_process_snapshot() -> None:
    config = load_config(
        environment={"OPENROUTER_API_KEY": "outer-secret"},
        overrides={"embedding_environment": {"OPENROUTER_API_KEY": "explicit-secret"}},
    )
    assert config.embedding_environment == {"OPENROUTER_API_KEY": "explicit-secret"}
