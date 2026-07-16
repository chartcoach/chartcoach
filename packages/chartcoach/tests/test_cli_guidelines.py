from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from click.testing import CliRunner

from chartcoach import CatalogManifest
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.entries import Guideline, Section
from chartcoach.cli.main import main as chartcoach_cli


def citation_catalog_path(tmp_path: Path, manifest: CatalogManifest) -> Path:
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id="direct-labels",
                title="Use direct labels",
                description="Label marks directly.",
                labels=("chart:line",),
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Place labels near marks.",
                    ),
                ),
                references=(
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
                ),
            ),
            Guideline(
                id="full-axis-bars",
                title="Use full value axes for bars",
                description="Keep bar axes on the honest baseline.",
                labels=("chart:bar",),
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Start bar value axes at zero.",
                    ),
                ),
            ),
        ],
        manifest=manifest,
    )
    source_path = tmp_path / "citation-catalog"
    catalog.write_bundle(source_path)
    return source_path


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
            "json",
        ],
    )

    rows = json.loads(result.stdout)
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
        "[Use direct labels](https://example.test/g/direct-labels/) (`direct-labels`)"
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
