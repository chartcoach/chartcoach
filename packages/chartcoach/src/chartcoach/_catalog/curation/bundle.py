from __future__ import annotations

import shutil
from os import PathLike
from pathlib import Path

from ..model import Catalog


def write_bundle(catalog: Catalog, output: str | PathLike[str]) -> Path:
    """Write `MANIFEST.md` and canonical rows into a new bundle directory."""

    root = Path(output)
    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        catalog.manifest.write(root / "MANIFEST.md")
        catalog.to_frame().write_parquet(root / "entries.parquet")
    except BaseException:
        shutil.rmtree(root, ignore_errors=True)
        raise
    return root
