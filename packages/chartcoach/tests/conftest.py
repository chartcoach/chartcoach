from __future__ import annotations

from pathlib import Path

import pytest
from catalog_testkit import write_catalog_entry, write_manifest
from chartcoach.catalog.guidelines import Guideline, Section
from chartcoach.catalog.manifest import CatalogManifest
from chartcoach.catalog.model import Catalog
from click.testing import CliRunner

SAMPLE_MANIFEST_MARKDOWN = """# Sample Catalog

## Section Roles

### advice

Actionable guidance for applying the guideline.

## Label Families

### chart

Chart-family labels such as `chart:line` and `chart:bar`.

### component

Chart-component labels such as `component:label` and `component:axis`.

### task

Task labels such as `task:lookup`.
"""


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def sample_manifest() -> CatalogManifest:
    return CatalogManifest.from_text(SAMPLE_MANIFEST_MARKDOWN)


@pytest.fixture
def sample_catalog(sample_manifest: CatalogManifest) -> Catalog:
    return Catalog.from_guidelines(
        [
            Guideline(
                id="direct-labels",
                title="Use direct labels",
                description="Label marks directly when space permits.",
                labels=("chart:line", "component:label", "task:lookup"),
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Place labels near marks.",
                    ),
                ),
            ),
            Guideline(
                id="full-axis-bars",
                title="Use full value axes for bars",
                description="Keep bar axes on the honest baseline.",
                labels=("chart:bar", "component:axis"),
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Start bar value axes at zero.",
                    ),
                ),
            ),
        ],
        manifest=sample_manifest,
    )


@pytest.fixture
def sample_catalog_path(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> Path:
    from chartcoach.catalog.curation import write_bundle

    return write_bundle(sample_catalog, tmp_path / "catalog")


@pytest.fixture
def sample_workspace_path(tmp_path: Path) -> Path:
    workspace = tmp_path / "workspace"
    write_manifest(workspace)
    write_catalog_entry(workspace, "direct-labels")
    write_catalog_entry(workspace, "full-axis-bars")
    return workspace
