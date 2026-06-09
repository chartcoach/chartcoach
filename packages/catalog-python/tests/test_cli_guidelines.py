from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from click.testing import CliRunner
import pytest

from chartcoach import Catalog, CatalogManifest
from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error, jsonl_rows


def test_catalog_query_filters_entries(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--label",
            "chart:bar",
            "--format",
            "jsonl",
        ],
    )

    assert [row["id"] for row in jsonl_rows(result)] == ["full-axis-bars"]


def test_catalog_query_composes_base_filters(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--any-label",
            "chart:bar",
            "--any-label",
            "chart:line",
            "--label-prefix",
            "component:",
            "--section-contains",
            "zero",
            "--format",
            "jsonl",
        ],
    )

    assert [row["id"] for row in jsonl_rows(result)] == ["full-axis-bars"]


def test_catalog_read_emits_entry_sections_and_sources(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert rows == [
        {
            "id": "direct-labels",
            "title": "Use direct labels",
            "description": "Label marks directly when space permits.",
            "labels": ["chart:line", "component:label", "task:lookup"],
            "sections": [
                {
                    "role": "advice",
                    "title": "Advice",
                    "content": "Place labels near marks.",
                }
            ],
            "sources": [],
        }
    ]


def test_catalog_read_can_include_full_source_detail(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--source-detail",
            "full",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert rows[0]["sources"] == []
    assert rows[0]["references"] == []


def test_catalog_read_markdown_renders_source_metadata(
    runner: CliRunner,
    sample_manifest: CatalogManifest,
    tmp_path: Path,
) -> None:
    catalog = Catalog.from_entries(
        [
            {
                "id": "direct-labels",
                "title": "Use direct labels",
                "description": "Label marks directly.",
                "body": "## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                "labels": ["chart:line"],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Place labels near marks.",
                    }
                ],
                "references": [
                    """@article{smith2024,
  title = {Readable charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""
                ],
            }
        ],
        manifest=sample_manifest,
    )
    source_path = tmp_path / "entries.parquet"
    catalog.write_parquet(source_path)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(source_path),
            "direct-labels",
            "--section",
            "advice",
            "--source-detail",
            "minimal",
            "--format",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "### Sources" in result.output
    assert "Smith, Ada" in result.output
    assert "Readable charts" in result.output


def test_catalog_read_can_select_section_roles(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "full-axis-bars",
            "--section",
            "advice",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert rows == [
        {
            "id": "full-axis-bars",
            "title": "Use full value axes for bars",
            "description": "Keep bar axes on the honest baseline.",
            "labels": ["chart:bar", "component:axis"],
            "sections": [
                {
                    "role": "advice",
                    "title": "Advice",
                    "content": "Start bar value axes at zero.",
                }
            ],
            "sources": [],
        }
    ]


def test_catalog_read_accepts_manifest_role_with_no_matching_sections(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    manifest = CatalogManifest.from_text(
        """# Sample Catalog

## Section Roles

### advice

Actionable guidance.

### review

Review notes.

## Label Families

### chart

Chart labels such as `chart:line`.
"""
    )
    catalog = Catalog.from_entries(
        [
            {
                "id": "direct-labels",
                "title": "Use direct labels",
                "description": "Label marks directly.",
                "body": "## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                "labels": ["chart:line"],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Place labels near marks.",
                    }
                ],
            }
        ],
        manifest=manifest,
    )
    source_path = catalog.write_bundle(tmp_path / "bundle")

    roles_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "roles",
            "--source",
            str(source_path),
            "--format",
            "jsonl",
        ],
    )
    role_rows = {row["role"]: row["entries"] for row in jsonl_rows(roles_result)}
    assert role_rows == {"advice": 1, "review": 0}

    read_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(source_path),
            "direct-labels",
            "--section",
            "review",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(read_result)
    assert rows[0]["sections"] == []


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (
            ["catalog", "read", "missing-guideline"],
            "Unknown entry id: missing-guideline",
        ),
        (
            ["catalog", "query", "--label", "chart:missing"],
            "Unknown label",
        ),
        (
            ["catalog", "read", "direct-labels", "--section", "missing"],
            "Unknown section role",
        ),
    ],
)
def test_catalog_entry_commands_render_recovery_hints(
    runner: CliRunner,
    sample_catalog_path: Path,
    argv: list[str],
    expected: str,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [*argv[:2], "--source", str(sample_catalog_path), *argv[2:]],
    )

    assert_cli_error(result, expected)


def test_catalog_unknown_section_lists_valid_roles(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--section",
            "missing",
        ],
    )

    assert_cli_error(result, "Unknown section role(s): missing")
    assert "Valid roles: advice" in result.output
    assert "chartcoach catalog roles" in result.output


def test_catalog_unknown_id_suggests_nearest_valid_id(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-lables",
        ],
    )

    assert_cli_error(result, "Unknown entry id: direct-lables")
    assert "Nearest entry ids: direct-labels" in result.output
    assert "chartcoach catalog read ID" in result.output
    assert "chartcoach catalog query" in result.output


def test_catalog_commands_report_no_matches(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    list_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert list_result.exit_code == 0
    assert list_result.output.strip() == "No entries matched."

    query_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert query_result.exit_code == 0
    assert query_result.output.strip() == ""


def test_catalog_list_table_compacts_list_cells_and_machine_formats_preserve_lists(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    table_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "table",
        ],
    )
    assert table_result.exit_code == 0
    assert "chart:line, component:label, task:lookup" in table_result.output

    json_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "json",
        ],
    )
    payload = cast(list[dict[str, object]], json.loads(json_result.output))
    assert payload[0]["labels"] == [
        "chart:line",
        "component:label",
        "task:lookup",
    ]

    jsonl_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "jsonl",
        ],
    )
    assert jsonl_rows(jsonl_result)[0]["labels"] == [
        "chart:line",
        "component:label",
        "task:lookup",
    ]
