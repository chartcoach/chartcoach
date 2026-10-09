from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from chartcoach import Catalog
from chartcoach.curation import EmbeddingProfile, build_release
from lancedb.embeddings import get_registry
from lancedb_embedding_fixture import variable_embedding_definition

pytestmark = [pytest.mark.curation, pytest.mark.search, pytest.mark.mcp]
_PROFILE = "test-variables"
_VARIABLE = "chartcoach-runtime-secret"


def test_cli_embedding_variable_file_activates_semantic_search_without_leaking_values(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _variable_release(sample_catalog, tmp_path)
    variables = tmp_path / "embedding-vars.json"
    secret = "runtime-secret-value"
    variables.write_text(json.dumps({_VARIABLE: secret}))
    script = f"""
from lancedb_embedding_fixture import variable_embedding_definition
variable_embedding_definition()
from chartcoach.cli.main import main
from click.testing import CliRunner
result = CliRunner().invoke(main, [
    "catalog", "search", "--source", {str(release)!r},
    "--profile", {_PROFILE!r}, "--mode", "vector",
    "--embedding-vars", {str(variables)!r}, "direct labels",
])
print(result.output)
raise SystemExit(result.exit_code)
"""

    result = _run(script)

    assert result.returncode == 0, result.stderr
    assert '"score_kind": "distance"' in result.stdout
    assert secret not in result.stdout
    assert secret not in result.stderr


def test_missing_embedding_variable_is_a_redacted_semantic_error(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _variable_release(sample_catalog, tmp_path)
    script = f"""
from lancedb_embedding_fixture import variable_embedding_definition
variable_embedding_definition()
from chartcoach.cli.main import main
from click.testing import CliRunner
result = CliRunner().invoke(main, [
    "catalog", "search", "--source", {str(release)!r},
    "--profile", {_PROFILE!r}, "--mode", "vector", "direct labels",
])
print(result.output)
raise SystemExit(result.exit_code)
"""

    result = _run(script)

    assert result.returncode == 1
    assert "Required LanceDB embedding variables are unset" in result.stdout
    assert _VARIABLE in result.stdout
    assert "--embedding-vars" in result.stdout
    assert "producer-secret-value" not in result.stdout
    assert "producer-secret-value" not in result.stderr


def test_mcp_embedding_variable_file_activates_semantic_search(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _variable_release(sample_catalog, tmp_path)
    variables = tmp_path / "embedding-vars.json"
    secret = "mcp-runtime-secret"
    variables.write_text(json.dumps({_VARIABLE: secret}))
    script = f"""
import asyncio
from lancedb_embedding_fixture import variable_embedding_definition
variable_embedding_definition()
from chartcoach import open_catalog
from chartcoach.mcp import create_server, load_config
from mcp.types import CallToolResult
async def run():
    config = load_config(environment={{
        "CHARTCOACH_SOURCE": {str(release)!r},
        "CHARTCOACH_INDEX_PROFILE": {_PROFILE!r},
        "CHARTCOACH_EMBEDDING_VARS": {str(variables)!r},
    }})
    server = create_server(
        open_catalog(config.source),
        profile=config.profile,
        embedding_variables=config.embedding_variables,
        embedding_environment=config.embedding_environment,
    )
    result = await server.call_tool("search", {{"text": "direct labels", "mode": "vector"}})
    assert isinstance(result, CallToolResult)
    assert result.is_error is False
    print(result.structured_content["score_kind"])
asyncio.run(run())
"""

    result = _run(script)

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "distance"
    assert secret not in result.stdout
    assert secret not in result.stderr


def test_mcp_missing_variable_reports_setup_and_allows_fts(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release = _variable_release(sample_catalog, tmp_path)
    script = f"""
import asyncio
from lancedb_embedding_fixture import variable_embedding_definition
variable_embedding_definition()
from chartcoach import open_catalog
from chartcoach.mcp import create_server
from mcp.types import CallToolResult
async def run():
    server = create_server(open_catalog({str(release)!r}), profile={_PROFILE!r})
    failed = await server.call_tool("search", {{"text": "direct labels", "mode": "vector"}})
    assert isinstance(failed, CallToolResult)
    assert failed.is_error is True
    error = failed.structured_content["error"]
    assert error["code"] == "unavailable_capability"
    assert error["details"]["variables"] == [{_VARIABLE!r}]
    assert error["hints"]
    print(failed.model_dump_json())
    recovered = await server.call_tool("search", {{"text": "direct labels", "mode": "fts"}})
    assert isinstance(recovered, CallToolResult)
    assert recovered.is_error is False
asyncio.run(run())
"""

    result = _run(script)

    assert result.returncode == 0, result.stderr
    assert "--embedding-vars" in result.stdout
    assert "producer-secret-value" not in result.stdout
    assert "producer-secret-value" not in result.stderr


def _variable_release(catalog: Catalog, tmp_path: Path) -> Path:
    definition = variable_embedding_definition()
    get_registry().set_var(_VARIABLE, "producer-secret-value")
    embedding = definition.create(api_key=f"$var:{_VARIABLE}", max_retries=0)
    release = tmp_path / "release"
    build_release(
        catalog,
        release,
        profiles={_PROFILE: EmbeddingProfile(embedding)},
    )
    metadata = (release / "profiles" / _PROFILE / "profile.json").read_text()
    assert f"$var:{_VARIABLE}" in metadata
    assert "producer-secret-value" not in metadata
    return release


def _run(script: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-c", script],
        env={**os.environ, "PYTHONPATH": str(Path(__file__).parent)},
        check=False,
        capture_output=True,
        text=True,
    )
