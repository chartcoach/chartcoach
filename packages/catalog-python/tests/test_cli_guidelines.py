from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from click.testing import CliRunner
import pytest

from chartcoach import Catalog, CatalogManifest
from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error, csv_rows, jsonl_rows


def citation_catalog_path(tmp_path: Path, manifest: CatalogManifest) -> Path:
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
  journal = {Journal of Charts},
  doi = {10.0000/charts}
}
""",
                    """@inproceedings{lee2022,
  title = {Interactive labels},
  author = {Lee, Bea},
  year = {2022},
  booktitle = {VIS Proceedings},
  url = {https://example.test/labels}
}
""",
                ],
            },
            {
                "id": "full-axis-bars",
                "title": "Use full value axes for bars",
                "description": "Keep bar axes on the honest baseline.",
                "body": "## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
                "labels": ["chart:bar"],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Start bar value axes at zero.",
                    }
                ],
                "references": [],
            },
        ],
        manifest=manifest,
    )
    source_path = tmp_path / "citation-entries.parquet"
    catalog.write_parquet(source_path)
    return source_path


def test_catalog_help_exits_successfully(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["catalog", "--help"])

    assert result.exit_code == 0


def test_catalog_without_command_exits_successfully(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["catalog"])

    assert result.exit_code == 0


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


def test_catalog_cite_markdown_renders_guideline_url_and_all_sources(
    runner: CliRunner,
    sample_manifest: CatalogManifest,
    tmp_path: Path,
) -> None:
    source_path = citation_catalog_path(tmp_path, sample_manifest)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cite",
            "--source",
            str(source_path),
            "direct-labels",
        ],
    )

    assert result.exit_code == 0, result.output
    assert "## direct-labels" in result.output
    assert (
        "Guideline: [Use direct labels]"
        "(https://chartcoach.github.io/guidelines/direct-labels) (`direct-labels`)"
    ) in result.output
    assert (
        "- Lee, Bea (2022). Interactive labels. VIS Proceedings. "
        "https://example.test/labels"
    ) in result.output
    assert (
        "- Smith, Ada (2024). Readable charts. Journal of Charts. "
        "https://doi.org/10.0000/charts"
    ) in result.output
    assert "@article" not in result.output
    assert "title = {" not in result.output


def test_catalog_cite_jsonl_preserves_requested_id_order_and_empty_sources(
    runner: CliRunner,
    sample_manifest: CatalogManifest,
    tmp_path: Path,
) -> None:
    source_path = citation_catalog_path(tmp_path, sample_manifest)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cite",
            "--source",
            str(source_path),
            "full-axis-bars",
            "direct-labels",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert [row["id"] for row in rows] == ["full-axis-bars", "direct-labels"]
    assert rows[0]["url"] == "https://chartcoach.github.io/guidelines/full-axis-bars"
    assert rows[0]["sources"] == []
    sources = cast(list[dict[str, object]], rows[1]["sources"])
    assert [source["reference_id"] for source in sources] == ["lee2022", "smith2024"]
    assert all("bibtex" not in source for source in sources)


def test_catalog_cite_json_includes_structured_source_citations(
    runner: CliRunner,
    sample_manifest: CatalogManifest,
    tmp_path: Path,
) -> None:
    source_path = citation_catalog_path(tmp_path, sample_manifest)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cite",
            "--source",
            str(source_path),
            "direct-labels",
            "--url-template",
            "https://example.test/g/{id}/",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    payload = cast(list[dict[str, object]], json.loads(result.output))
    assert payload[0]["url"] == "https://example.test/g/direct-labels/"
    assert payload[0]["guideline_citation"] == (
        "[Use direct labels](https://example.test/g/direct-labels/) "
        "(`direct-labels`)"
    )
    sources = cast(list[dict[str, object]], payload[0]["sources"])
    assert sources[0] == {
        "reference_id": "lee2022",
        "source_type": "inproceedings",
        "authors_text": "Lee, Bea",
        "year": "2022",
        "source_title": "Interactive labels",
        "journal": None,
        "booktitle": "VIS Proceedings",
        "publisher": None,
        "doi": None,
        "url": "https://example.test/labels",
        "citation": (
            "Lee, Bea (2022). Interactive labels. VIS Proceedings. "
            "https://example.test/labels"
        ),
    }
    assert "bibtex" not in json.dumps(payload)


def test_catalog_cite_reports_invalid_ids_and_url_templates(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    missing_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cite",
            "--source",
            str(sample_catalog_path),
            "direct-lables",
        ],
    )

    assert_cli_error(missing_result, "Unknown entry id: direct-lables")

    template_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cite",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--url-template",
            "https://example.test/guidelines",
        ],
    )

    assert_cli_error(template_result, "Guideline URL template must include `{id}`.")


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
    assert list_result.stdout.strip() == "No entries matched."
    assert "Try a broader --contains term" in list_result.stderr

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
    assert query_result.stdout.strip() == ""
    assert "--body-contains" in query_result.stderr
    assert "--section-contains" in query_result.stderr


def test_catalog_empty_label_results_report_recovery_hints_on_stderr(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "labels",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0
    assert json.loads(result.stdout) == []
    assert "Try a shorter or broader --contains term." in result.stderr
    assert "catalog query --section-contains" in result.stderr


def test_catalog_empty_query_with_strict_labels_suggests_any_label(
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
            "--label",
            "task:lookup",
            "--format",
            "jsonl",
        ],
    )

    assert result.exit_code == 0
    assert result.stdout == ""
    assert "Repeated --label filters are all-of." in result.stderr
    assert "--any-label" in result.stderr


def test_catalog_empty_values_json_preserves_parseable_stdout(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "values",
            "labels",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0
    assert json.loads(result.stdout) == []
    assert "Use aliases such as labels, roles" in result.stderr
    assert "catalog schema" in result.stderr


def test_catalog_empty_csv_preserves_parseable_stdout(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "labels",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
            "--format",
            "csv",
        ],
    )

    assert result.exit_code == 0
    assert csv_rows(result) == []
    assert "Guidance:" in result.stderr


def test_catalog_query_show_matches_reports_title_and_description_hits(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    title_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "Use direct",
            "--show-matches",
            "--format",
            "jsonl",
        ],
    )
    title_matches = cast(
        list[dict[str, object]], jsonl_rows(title_result)[0]["matches"]
    )
    assert {
        "predicate": "contains",
        "field": "title",
        "query": "Use direct",
        "snippet": "Use direct labels",
    } in title_matches

    description_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "space permits",
            "--show-matches",
            "--format",
            "jsonl",
        ],
    )
    description_matches = cast(
        list[dict[str, object]], jsonl_rows(description_result)[0]["matches"]
    )
    assert {
        "predicate": "contains",
        "field": "description",
        "query": "space permits",
        "snippet": "Label marks directly when space permits.",
    } in description_matches


def test_catalog_query_show_matches_reports_body_and_section_hits(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    body_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--body-contains",
            "near marks",
            "--show-matches",
            "--format",
            "json",
        ],
    )
    body_payload = cast(list[dict[str, object]], json.loads(body_result.stdout))
    body_matches = cast(list[dict[str, object]], body_payload[0]["matches"])
    assert body_matches == [
        {
            "predicate": "body-contains",
            "field": "body",
            "query": "near marks",
            "snippet": "## Advice <!-- role: advice --> Place labels near marks.",
        }
    ]

    section_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--section-contains",
            "zero",
            "--show-matches",
            "--format",
            "jsonl",
        ],
    )
    section_matches = cast(
        list[dict[str, object]], jsonl_rows(section_result)[0]["matches"]
    )
    assert section_matches == [
        {
            "predicate": "section-contains",
            "field": "section.content",
            "role": "advice",
            "title": "Advice",
            "query": "zero",
            "snippet": "Start bar value axes at zero.",
        }
    ]


def test_catalog_query_show_matches_table_adds_short_matches_column(
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
            "--contains",
            "space permits",
            "--show-matches",
            "--format",
            "table",
        ],
    )

    assert result.exit_code == 0
    assert "ID" in result.stdout
    assert "Title" in result.stdout
    assert "Description" in result.stdout
    assert "Labels" in result.stdout
    assert "Matches" in result.stdout
    assert "description: Label marks" in result.stdout
    assert "directly when space" in result.stdout
    assert "permits." in result.stdout


def test_catalog_query_without_show_matches_keeps_default_shape(
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
            "--contains",
            "space permits",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert list(rows[0]) == ["id", "title", "description", "labels"]


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
    assert "chart:line," in table_result.output
    assert "component:label," in table_result.output
    assert "task:lookup" in table_result.output

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
