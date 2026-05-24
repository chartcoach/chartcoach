from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace
from typing import cast

from click.testing import CliRunner
import pytest
import polars as pl

from chartcoach.catalog import Catalog, CatalogEntry
from chartcoach.catalog.storage import load_catalog_entry
from chartcoach.guideline import Guideline
from chartcoach.guideline import format_bibtex_entry
from chartcoach.guideline import parse_bibtex
from chartcoach.guideline import parse_bibtex_entry


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
    assert catalog.entry("direct-labels").id == "direct-labels"
    assert catalog.guidelines().select("id").to_series().to_list() == [
        "direct-labels"
    ]
    assert catalog.sections().select("role").to_series().to_list() == ["advice"]
    assert catalog.guideline_labels().select("label").to_series().to_list() == [
        "chart:line",
        "goal:comparison",
    ]


def test_catalog_write_folder_roundtrips_entries(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    catalog.write_folder(tmp_path / "written")
    reloaded = Catalog.from_folder(tmp_path / "written")

    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_digest_is_entry_order_stable() -> None:
    first = CatalogEntry(
        guideline=Guideline(
            id="direct-labels",
            title="Use direct labels",
            description="Label marks directly when space permits.",
            body="Label marks directly when space permits.",
            labels=("chart:line",),
        )
    )
    second = CatalogEntry(
        guideline=Guideline(
            id="full-axis-bars",
            title="Use full axes",
            description="Keep bar axes honest.",
            body="Keep bar axes honest.",
            labels=("chart:bar",),
        )
    )

    assert Catalog.from_entries([first, second]).digest() == Catalog.from_entries(
        [second, first]
    ).digest()


def test_catalog_select_empty_returns_empty_catalog() -> None:
    entry = CatalogEntry(
        guideline=Guideline(
            id="direct-labels",
            title="Use direct labels",
            description="Label marks directly when space permits.",
            body="Label marks directly when space permits.",
            labels=("chart:line",),
        )
    )
    catalog = Catalog.from_entries([entry])

    selected = catalog.select([])

    assert len(selected) == 0
    assert selected.to_frame().schema == catalog.to_frame().schema


def test_catalog_sections_handles_guidelines_without_sections() -> None:
    catalog = Catalog.from_frame(
        pl.from_dicts(
            [
                {
                    "id": "plain-guideline",
                    "guideline": {
                        "id": "plain-guideline",
                        "title": "Plain guideline",
                        "bibliography": None,
                        "description": "Description.",
                        "labels": [],
                        "body": "No section headings here.",
                        "sections": [],
                    },
                    "references": [],
                }
            ]
        )
    )

    assert catalog.sections().is_empty()


def test_parse_bibtex_entry_does_not_expose_cached_mutable_state() -> None:
    first = parse_bibtex_entry(BIBTEX)
    first["ID"] = "mutated"

    assert parse_bibtex_entry(BIBTEX)["ID"] == "smith2024"


def test_load_catalog_entry_requires_guideline_file(tmp_path: Path) -> None:
    empty_entry = tmp_path / "empty"
    empty_entry.mkdir()

    with pytest.raises(FileNotFoundError, match="No guideline.md file found"):
        load_catalog_entry(empty_entry)


def test_parse_bibtex_ignores_percent_comments() -> None:
    parsed = parse_bibtex(BIBTEX)

    assert len(parsed) == 1
    assert "% generated note" not in parsed[0]
    assert "@article{smith2024" in parsed[0]
    assert "Readable charts" in parsed[0]


def test_parse_bibtex_keeps_at_signs_inside_fields() -> None:
    parsed = parse_bibtex(
        r"""@misc{contact2024,
  title = {Contact chart-team@example.com},
  url = {https://example.com/chart@coach}
}
"""
    )

    assert len(parsed) == 1
    assert "chart-team@example.com" in parsed[0]
    assert "https://example.com/chart@coach" in parsed[0]


def test_format_bibtex_rejects_empty_entries() -> None:
    with pytest.raises(ValueError, match="No BibTeX entry parsed"):
        format_bibtex_entry("% empty bibliography")


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
    assert catalog.guidelines().height == len(catalog)


def test_catalog_write_parquet_roundtrips(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    parquet_path = tmp_path / "catalog.parquet"
    catalog.write_parquet(parquet_path)

    reloaded = Catalog.from_parquet(parquet_path)
    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_rejects_duplicate_ids() -> None:
    guideline = Guideline(
        id="duplicate",
        title="Title",
        description="Description",
        body="Body",
    )
    entry = CatalogEntry(guideline=guideline)

    with pytest.raises(ValueError, match="duplicate guideline ids"):
        Catalog.from_entries([entry, entry])


def test_catalog_entry_rejects_mismatched_row_id() -> None:
    with pytest.raises(ValueError, match="does not match guideline id"):
        CatalogEntry.from_mapping(
            {
                "id": "row-id",
                "guideline": {
                    "id": "guideline-id",
                    "title": "Title",
                    "description": "Description",
                    "body": "Body",
                    "labels": [],
                    "sections": [],
                },
                "references": [],
            }
        )


def test_catalog_from_frame_rejects_mismatched_guideline_id() -> None:
    frame = pl.from_dicts(
        [
            {
                "id": "row-id",
                "guideline": {
                    "id": "guideline-id",
                    "title": "Title",
                    "bibliography": None,
                    "description": "Description",
                    "labels": [],
                    "body": "Body",
                    "sections": [],
                },
                "references": [],
            }
        ]
    )

    with pytest.raises(ValueError, match="row id must match guideline id"):
        Catalog.from_frame(frame)


def test_guideline_from_mapping_requires_serialized_sections() -> None:
    with pytest.raises(TypeError, match="sections is required"):
        Guideline.from_mapping(
            {
                "id": "guideline-id",
                "title": "Title",
                "description": "Description",
                "body": "Body",
                "labels": [],
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


def test_duckdb_import_does_not_load_chroma_dependencies() -> None:
    script = (
        "import sys; "
        "from chartcoach.duckdb import write_duckdb; "
        "assert callable(write_duckdb); "
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
        "missing MCP dependency",
        name="mcp",
    )

    assert _is_missing_optional_dependency(root)


def test_mcp_cli_renders_missing_optional_dependency_without_traceback(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from chartcoach.cli import mcp as mcp_cli

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

    result = CliRunner().invoke(
        mcp_cli.mcp_command,
        ["serve", "--source", "catalog.parquet", "--index-dir", "index"],
    )

    assert result.exit_code == 1
    assert "Install `chartcoach[mcp]` to use it." in result.output
    assert "Traceback" not in result.output


def test_mcp_cli_passes_index_dir_and_renders_value_errors(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from chartcoach.cli import mcp as mcp_cli
    from chartcoach.mcp import server as mcp_server

    monkeypatch.delenv("CHARTCOACH_INDEX_DIR", raising=False)
    monkeypatch.delenv("CHARTCOACH_SOURCE", raising=False)
    monkeypatch.delenv("CHARTCOACH_MCP_HOST", raising=False)
    monkeypatch.delenv("CHARTCOACH_MCP_LOG_LEVEL", raising=False)
    monkeypatch.delenv("CHARTCOACH_MCP_PORT", raising=False)
    monkeypatch.delenv("CHARTCOACH_MCP_TRANSPORT", raising=False)
    monkeypatch.chdir(tmp_path)

    captured: dict[str, object] = {}

    def fake_main(**kwargs: object) -> None:
        captured.update(kwargs)
        raise ValueError("source must be provided")

    monkeypatch.setattr(mcp_server, "main", fake_main)
    monkeypatch.setattr(mcp_cli, "_load_server_module", lambda: mcp_server)

    result = CliRunner().invoke(mcp_cli.mcp_command, ["serve"])

    assert result.exit_code == 1
    settings = cast(dict[str, str | Path], captured["settings"])
    assert Path(settings["index_dir"]).name == "index"
    assert captured["runtime"] == mcp_server.RuntimeConfig()
    assert "source must be provided" in result.output
    assert "Traceback" not in result.output


def test_empty_label_catalog_frames_are_typed() -> None:
    catalog = Catalog.from_entries(
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

    assert catalog.labels().schema["category"].is_(pl.String)
    assert catalog.guideline_labels().schema["label"].is_(pl.String)
    assert catalog.labels().is_empty()
    assert catalog.guideline_labels().is_empty()
