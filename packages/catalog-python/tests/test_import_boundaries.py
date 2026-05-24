from __future__ import annotations

from pathlib import Path
import subprocess
import sys

import polars as pl


def test_package_root_import_does_not_load_optional_dependencies() -> None:
    script = (
        "import sys, chartcoach; "
        "assert 'duckdb' not in sys.modules; "
        "assert 'chromadb' not in sys.modules; "
        "assert 'polars_hash' not in sys.modules; "
        "assert 'mcp' not in sys.modules"
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


def test_catalog_loads_parquet_without_optional_dependencies(
    tmp_path: Path,
) -> None:
    parquet_path = tmp_path / "catalog.parquet"
    pl.DataFrame(
        [
            {
                "id": "wire-guideline",
                "guideline": {
                    "id": "wire-guideline",
                    "title": "Wire guideline",
                    "bibliography": None,
                    "description": "Loaded from explicit wire data.",
                    "labels": ["chart:bar"],
                    "body": "## Advice <!-- role: advice -->\n\nUse bars.",
                    "sections": [
                        {
                            "role": "advice",
                            "title": "Advice",
                            "content": "Use bars.",
                        }
                    ],
                },
                "references": [],
            }
        ]
    ).write_parquet(parquet_path)

    script = r"""
import builtins
import sys

blocked_roots = {"chromadb", "duckdb", "mcp", "polars_hash"}
real_import = builtins.__import__

def blocked_import(name, *args, **kwargs):
    root = name.partition(".")[0]
    if root in blocked_roots:
        raise ModuleNotFoundError(f"blocked optional dependency: {root}", name=root)
    return real_import(name, *args, **kwargs)

builtins.__import__ = blocked_import

from chartcoach import Catalog

catalog = Catalog.from_parquet(sys.argv[1])
assert catalog.guidelines().select("id").to_series().to_list() == [
    "wire-guideline",
]
assert catalog.sections().select("role").to_series().to_list() == ["advice"]
assert catalog.guideline_labels().select("label").to_series().to_list() == ["chart:bar"]
for root in blocked_roots:
    assert root not in sys.modules
"""
    subprocess.run(
        [sys.executable, "-c", script, str(parquet_path)],
        check=True,
    )
