from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach import Catalog, CatalogManifest, Guideline, Section


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
    return Catalog.from_entries(
        [
            Guideline(
                id="direct-labels",
                title="Use direct labels",
                description="Label marks directly when space permits.",
                body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
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
                body="## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
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
def single_guideline_catalog(sample_manifest: CatalogManifest) -> Catalog:
    return Catalog.from_entries(
        [
            Guideline(
                id="direct-labels",
                title="Use direct labels",
                description="Label marks directly when space permits.",
                body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                labels=("chart:line",),
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Place labels near marks.",
                    ),
                ),
            )
        ],
        manifest=sample_manifest,
    )


@pytest.fixture
def catalog_path_factory(
    tmp_path: Path,
) -> Callable[[Catalog], Path]:
    def write_catalog(catalog: Catalog) -> Path:
        path = tmp_path / "catalog.parquet"
        catalog.write_parquet(path)
        return path

    return write_catalog


@pytest.fixture
def sample_catalog_path(
    catalog_path_factory: Callable[[Catalog], Path],
    sample_catalog: Catalog,
) -> Path:
    return catalog_path_factory(sample_catalog)


@pytest.fixture
def sample_workspace_path(tmp_path: Path, sample_catalog: Catalog) -> Path:
    workspace = tmp_path / "workspace"
    sample_catalog.write_folder(workspace)
    return workspace
