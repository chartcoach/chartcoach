from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

from click.testing import CliRunner
import pytest
import polars as pl

from chartcoach.catalog import Catalog, CatalogEntry
from chartcoach.catalog.storage import load_catalog_entry
from chartcoach.guideline import Guideline
from chartcoach.guideline import format_bibtex_entry
from chartcoach.guideline import parse_bibtex


GUIDELINE_MD = """---
id: direct-labels
title: Use direct labels
description: Label marks directly when space permits.
bibliography: references.bib
labels:
  - chart:line
  - goal:comparison
---

## Advice <!-- role: advice -->

Place the label close to the mark it names [@smith2024].
"""

BIBTEX = """% generated note
@article{smith2024,
  title = {Readable charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""


def write_catalog_entry(root: Path, entry_id: str = "direct-labels") -> Path:
    entry_dir = root / entry_id
    entry_dir.mkdir(parents=True)
    (entry_dir / "guideline.md").write_text(GUIDELINE_MD)
    (entry_dir / "references.bib").write_text(BIBTEX)
    return entry_dir


def test_catalog_loads_folder_entries_and_tables(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path)
    (tmp_path / "__templates__").mkdir()

    catalog = Catalog.from_folder(tmp_path)

    assert len(catalog) == 1
    assert catalog[0].id == "direct-labels"
    assert catalog.frames.guidelines.select("id").to_series().to_list() == [
        "direct-labels"
    ]
    assert catalog.frames.sections.select("role").to_series().to_list() == ["advice"]
    assert catalog.frames.guideline_labels.select("label").to_series().to_list() == [
        "chart:line",
        "goal:comparison",
    ]


def test_catalog_write_folder_roundtrips_entries(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    catalog.write_folder(tmp_path / "written")
    reloaded = Catalog.from_folder(tmp_path / "written")

    assert [entry.model_dump() for entry in reloaded] == [
        entry.model_dump() for entry in catalog
    ]


def test_load_catalog_entry_requires_guideline_file(tmp_path: Path) -> None:
    empty_entry = tmp_path / "empty"
    empty_entry.mkdir()

    with pytest.raises(FileNotFoundError, match="No guideline.md file found"):
        load_catalog_entry(empty_entry)


def test_parse_bibtex_ignores_percent_comments() -> None:
    assert parse_bibtex(BIBTEX) == [BIBTEX.split("\n", 1)[1].strip()]


def test_bibtex_format_handles_spacing_macros() -> None:
    bibtex = r"""@article{macro2024,
  title = {Readable\! charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""

    assert "Readable charts" in format_bibtex_entry(bibtex)


def test_catalog_loads_parquet_without_search_dependencies() -> None:
    repo_root = Path(__file__).parents[3]
    catalog = Catalog.from_parquet(repo_root / "guidelines" / "catalog.parquet")

    assert len(catalog) > 700
    assert catalog.guidelines_df.height == len(catalog)


def test_catalog_write_parquet_roundtrips(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    parquet_path = tmp_path / "catalog.parquet"
    catalog.write_parquet(parquet_path)

    reloaded = Catalog.from_parquet(parquet_path)
    assert [entry.model_dump() for entry in reloaded] == [
        entry.model_dump() for entry in catalog
    ]


def test_catalog_rejects_duplicate_ids() -> None:
    guideline = Guideline(
        id="duplicate",
        title="Title",
        description="Description",
        body="Body",
    )
    entry = CatalogEntry(guideline=guideline)

    with pytest.raises(ValueError, match="duplicate guideline ids"):
        Catalog([entry, entry])


def test_catalog_entry_rejects_mismatched_row_id() -> None:
    with pytest.raises(ValueError, match="does not match guideline id"):
        CatalogEntry.model_validate(
            {
                "id": "row-id",
                "guideline": {
                    "id": "guideline-id",
                    "title": "Title",
                    "description": "Description",
                    "body": "Body",
                    "labels": [],
                },
                "references": [],
            }
        )


def test_package_root_import_does_not_load_search_dependencies() -> None:
    script = (
        "import sys, chartcoach; "
        "assert 'duckdb' not in sys.modules; "
        "assert 'chromadb' not in sys.modules; "
        "assert 'polars_hash' not in sys.modules"
    )
    subprocess.run([sys.executable, "-c", script], check=True)


def test_sql_import_does_not_load_chroma_dependencies() -> None:
    script = (
        "import sys; "
        "from chartcoach.search import connect_catalog; "
        "assert callable(connect_catalog); "
        "assert 'chromadb' not in sys.modules; "
        "assert 'polars_hash' not in sys.modules"
    )
    subprocess.run([sys.executable, "-c", script], check=True)


def test_chroma_index_import_does_not_load_hash_dependency() -> None:
    script = r"""
import builtins

real_import = builtins.__import__

def blocked_import(name, *args, **kwargs):
    if name == "polars_hash":
        raise ModuleNotFoundError("blocked polars_hash", name="polars_hash")
    return real_import(name, *args, **kwargs)

builtins.__import__ = blocked_import
from chartcoach.search import ChromaIndex
assert ChromaIndex.__name__ == "ChromaIndex"
"""
    subprocess.run([sys.executable, "-c", script], check=True)


def test_mcp_cli_classifies_nested_optional_dependency_errors() -> None:
    from chartcoach.cli.mcp import _is_missing_optional_dependency

    root = ModuleNotFoundError("wrapped optional dependency")
    root.__cause__ = ModuleNotFoundError(
        "missing chroma dependency",
        name="chromadb",
    )

    assert _is_missing_optional_dependency(root)


def test_mcp_cli_renders_missing_optional_dependency_without_traceback(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from chartcoach.cli import mcp as mcp_cli

    def raise_nested_missing_dependency(**_: object) -> None:
        root = ModuleNotFoundError("wrapped optional dependency")
        root.__cause__ = ModuleNotFoundError(
            "missing chroma dependency",
            name="chromadb",
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

    result = CliRunner().invoke(
        mcp_cli.mcp_command,
        ["--catalog-path", "catalog.parquet"],
    )

    assert result.exit_code == 1
    assert "Install `chartcoach[mcp]` to use it." in result.output
    assert "Traceback" not in result.output


def test_mcp_cli_passes_cache_mode_and_renders_value_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from chartcoach.cli import mcp as mcp_cli
    from chartcoach.mcp import server as mcp_server

    monkeypatch.delenv("CHARTCOACH_CACHE_DIR", raising=False)
    monkeypatch.delenv("CHARTCOACH_CACHE_MODE", raising=False)
    monkeypatch.delenv("CHARTCOACH_CATALOG_PATH", raising=False)
    monkeypatch.delenv("MCP_HOST", raising=False)
    monkeypatch.delenv("MCP_LOG_LEVEL", raising=False)
    monkeypatch.delenv("MCP_PORT", raising=False)
    monkeypatch.delenv("MCP_TRANSPORT", raising=False)

    captured: dict[str, object] = {}

    def fake_main(**kwargs: object) -> None:
        captured.update(kwargs)
        raise ValueError("catalog must be provided")

    monkeypatch.setattr(mcp_server, "main", fake_main)
    monkeypatch.setattr(mcp_cli, "_load_server_module", lambda: mcp_server)

    result = CliRunner().invoke(
        mcp_cli.mcp_command,
        ["--cache-mode", "reuse_only"],
    )

    assert result.exit_code == 1
    assert captured["settings"] == {"cache_mode": "reuse_only"}
    assert captured["runtime"] == mcp_server.RuntimeConfig()
    assert "catalog must be provided" in result.output
    assert "Traceback" not in result.output


def test_empty_label_catalog_frames_are_typed() -> None:
    catalog = Catalog(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="unlabeled",
                    title="Title",
                    description="Description",
                    body="Body",
                )
            )
        ]
    )

    assert catalog.labels_df.schema["category"].is_(pl.String)
    assert catalog.guideline_labels_df.schema["label"].is_(pl.String)
    assert catalog.labels_df.is_empty()
    assert catalog.guideline_labels_df.is_empty()
