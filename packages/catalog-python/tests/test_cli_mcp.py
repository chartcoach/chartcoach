from __future__ import annotations

from pathlib import Path
from typing import cast

from click.testing import CliRunner
import pytest

from chartcoach.cli import mcp as mcp_cli
from chartcoach.cli.main import main as chartcoach_cli
import chartcoach.mcp as mcp_server

from helpers import assert_cli_error

pytestmark = pytest.mark.mcp


def test_mcp_cli_renders_install_hint_for_missing_optional_dependency(
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

    monkeypatch.setattr(mcp_cli, "_run_server", raise_nested_missing_dependency)

    result = runner.invoke(
        chartcoach_cli,
        ["mcp", "serve", "--source", "entries.parquet", "--index", "index"],
    )

    assert_cli_error(result, "Install `chartcoach[mcp]` to use it.")


def test_mcp_cli_renders_search_hint_for_missing_lancedb(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_lancedb(**_: object) -> None:
        raise ModuleNotFoundError("missing LanceDB dependency", name="lancedb")

    monkeypatch.setattr(mcp_cli, "_run_server", raise_missing_lancedb)

    result = runner.invoke(
        chartcoach_cli,
        ["mcp", "serve", "--source", "entries.parquet", "--index", "index"],
    )

    assert_cli_error(
        result, "Indexed MCP search requires the optional LanceDB dependencies."
    )
    assert "uvx --from 'chartcoach[mcp,index]@latest' chartcoach" in result.output
    assert (
        "uv run --package chartcoach --extra mcp --extra index chartcoach"
        in result.output
    )


def test_mcp_cli_renders_search_hint_for_missing_index(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(mcp_server, "open_index", raise_missing_index)

    result = runner.invoke(
        chartcoach_cli,
        [
            "mcp",
            "serve",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
        ],
    )

    assert_cli_error(result, "missing search index")
    assert "chartcoach catalog index create --source PATH --index PATH" in result.output
    assert "Pass the same index path" in result.output


def test_mcp_cli_passes_explicit_index_and_renders_value_errors(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in (
        "CHARTCOACH_INDEX",
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

    result = runner.invoke(chartcoach_cli, ["mcp", "serve", "--index", "index"])

    settings = cast(dict[str, str | Path], captured["settings"])
    assert settings["index"] == "index"
    assert settings["table"] == "catalog_documents"
    assert captured["runtime"] == mcp_server.Runtime()
    assert_cli_error(result, "source must be provided")
