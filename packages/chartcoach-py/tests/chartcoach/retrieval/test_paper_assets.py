from __future__ import annotations

from pathlib import Path

import polars as pl

from chartcoach.retrieval.analysis.paper_assets import write_paper_assets


def _repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here, *here.parents]:
        if (parent / "pyproject.toml").exists() and (parent / "apps").exists():
            return parent
    raise RuntimeError("Failed to locate repo root from test file location.")


def test_paper_assets_writes_outputs(tmp_path: Path) -> None:
    repo = _repo_root()
    run = repo / "apps/eval-ui/fixtures/eval-artifacts/v1"
    taxonomy = repo / "docs/retrieval/strategy_taxonomy.yaml"

    out = tmp_path / "paper-assets"
    write_paper_assets(runs=[run], out_dir=out, taxonomy_path=taxonomy, k=5)

    summary_csv = out / "v1.strategy-summary.csv"
    assert summary_csv.exists()
    df = pl.read_csv(summary_csv)
    assert df.height > 0
    assert "strategy_id" in df.columns
    assert "mean_elapsed_ms" in df.columns

    assert (out / "v1.strategy-summary.md").exists()
    assert (out / "v1.pool.md").exists()
    assert (out / "v1.counterfactual.md").exists()

