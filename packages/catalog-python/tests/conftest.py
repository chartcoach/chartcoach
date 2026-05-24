from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach import Catalog, CatalogEntry, Guideline, Section


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def sample_catalog() -> Catalog:
    return Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
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
                )
            ),
            CatalogEntry(
                guideline=Guideline(
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
                )
            ),
        ]
    )


@pytest.fixture
def single_guideline_catalog() -> Catalog:
    return Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
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
            )
        ]
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
