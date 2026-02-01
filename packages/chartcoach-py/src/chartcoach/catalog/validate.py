from __future__ import annotations

import argparse
from collections import Counter
from os import PathLike
from pathlib import Path

import polars as pl

from .load import load_catalog_entry_


def _validate_folder_ids_match_paths(entries: list[tuple[Path, str]]) -> list[str]:
    errors: list[str] = []
    for path, entry_id in entries:
        if path.name != entry_id:
            errors.append(
                f"Folder name {path.name!r} does not match guideline id {entry_id!r}."
            )
    return errors


def _validate_unique_ids(ids: list[str]) -> list[str]:
    errors: list[str] = []
    counts = Counter(ids)
    dupes = sorted([gid for gid, count in counts.items() if count > 1])
    if dupes:
        errors.append(f"Duplicate guideline ids: {dupes}")
    return errors


def _load_folder_ids(
    folder_path: PathLike[str],
) -> tuple[list[tuple[Path, str]], list[str]]:
    root = Path(folder_path)
    if not root.exists():
        return [], [f"Catalog folder does not exist: {root}"]

    entries: list[tuple[Path, str]] = []
    errors: list[str] = []

    for entry_dir in sorted(root.iterdir(), key=lambda p: p.name):
        if not entry_dir.is_dir():
            continue
        if entry_dir.name == "__templates__":
            continue
        try:
            entry = load_catalog_entry_(entry_dir)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{entry_dir.name}: {e}")
            continue
        entries.append((entry_dir, entry.id))

    return entries, errors


def _load_parquet_ids(parquet_path: PathLike[str]) -> tuple[list[str], list[str]]:
    path = Path(parquet_path)
    if not path.exists():
        return [], [f"Catalog parquet does not exist: {path}"]
    if path.suffix != ".parquet":
        return [], [f"Catalog parquet must be a .parquet file: {path}"]

    df = pl.read_parquet(path)
    if "id" not in df.columns:
        return [], [f"Catalog parquet is missing required column 'id': {path}"]

    ids = [gid for gid in df["id"].to_list() if isinstance(gid, str) and gid]
    if len(ids) != df.height:
        return [], [f"Catalog parquet contains non-string or empty ids: {path}"]

    return ids, []


def validate_catalog(
    folder_path: PathLike[str],
    *,
    parquet_path: PathLike[str] | None = None,
) -> None:
    """Validate that the guideline catalog is complete and internally consistent."""

    folder_entries, folder_errors = _load_folder_ids(folder_path)
    folder_ids = [gid for _path, gid in folder_entries]

    errors: list[str] = []
    errors.extend(folder_errors)
    errors.extend(_validate_folder_ids_match_paths(folder_entries))
    errors.extend(_validate_unique_ids(folder_ids))

    if parquet_path is not None:
        parquet_ids, parquet_errors = _load_parquet_ids(parquet_path)
        errors.extend(parquet_errors)
        errors.extend(_validate_unique_ids(parquet_ids))

        if not parquet_errors:
            folder_set = set(folder_ids)
            parquet_set = set(parquet_ids)
            missing_in_parquet = sorted(folder_set - parquet_set)
            missing_on_disk = sorted(parquet_set - folder_set)
            if missing_in_parquet:
                errors.append(f"IDs missing from parquet: {missing_in_parquet}")
            if missing_on_disk:
                errors.append(f"IDs missing on disk: {missing_on_disk}")

    if errors:
        joined = "\n".join(f"- {err}" for err in errors)
        raise ValueError(f"Catalog validation failed:\n{joined}")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="python -m chartcoach.catalog.validate")
    parser.add_argument(
        "--folder",
        type=Path,
        default=Path("guidelines"),
        help="Path to the guidelines folder (default: ./guidelines).",
    )
    parser.add_argument(
        "--parquet",
        type=Path,
        default=None,
        help="Optional path to catalog.parquet to check for ID parity.",
    )

    args = parser.parse_args(argv)

    try:
        validate_catalog(args.folder, parquet_path=args.parquet)
    except ValueError as e:
        raise SystemExit(str(e)) from e


if __name__ == "__main__":  # pragma: no cover
    main()
