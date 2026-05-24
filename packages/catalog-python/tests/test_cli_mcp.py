from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import cast

from click.testing import CliRunner
import pytest

from chartcoach.cli import mcp as mcp_cli
from chartcoach.cli.main import main as chartcoach_cli
from chartcoach.mcp import server as mcp_server
from chartcoach.paths import default_index_dir

pytestmark = pytest.mark.mcp


def test_mcp_cli_renders_missing_optional_dependency_without_traceback(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_nested_missing_dependency(**_: object) -> None:
        root = ModuleNotFoundError("wrapped optional dependency")
        root.__cause__ = ModuleNotFoundError(
            "missing MCP dependency",
            name="mcp",
        )
        raise root

    fake_server = SimpleNamespace(
        resolve_config=lambda **kwargs: SimpleNamespace(
            settings=kwargs,
            runtime=object(),
        ),
        main=raise_nested_missing_dependency,
    )
    monkeypatch.setattr(mcp_cli, "_load_server_module", lambda: fake_server)

    result = runner.invoke(
        chartcoach_cli,
        ["mcp", "serve", "--source", "catalog.parquet", "--index-dir", "index"],
    )

    assert result.exit_code == 1
    assert "Install `chartcoach[mcp]` to use it." in result.output
    assert "Traceback" not in result.output


def test_mcp_cli_passes_index_dir_and_renders_value_errors(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in (
        "CHARTCOACH_INDEX_DIR",
        "CHARTCOACH_SOURCE",
        "CHARTCOACH_MCP_HOST",
        "CHARTCOACH_MCP_LOG_LEVEL",
        "CHARTCOACH_MCP_PORT",
        "CHARTCOACH_MCP_TRANSPORT",
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.chdir(tmp_path)

    captured: dict[str, object] = {}

    def fake_main(**kwargs: object) -> None:
        captured.update(kwargs)
        raise ValueError("source must be provided")

    monkeypatch.setattr(mcp_server, "main", fake_main)
    monkeypatch.setattr(mcp_cli, "_load_server_module", lambda: mcp_server)

    result = runner.invoke(chartcoach_cli, ["mcp", "serve"])

    assert result.exit_code == 1
    settings = cast(dict[str, str | Path], captured["settings"])
    assert settings["index_dir"] == default_index_dir()
    assert captured["runtime"] == mcp_server.RuntimeConfig()
    assert "source must be provided" in result.output
    assert "Traceback" not in result.output
