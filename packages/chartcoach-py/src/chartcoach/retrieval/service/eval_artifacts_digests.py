from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

from chartcoach.retrieval.config import RetrievalRunConfig
from chartcoach.retrieval.service.eval_artifacts_schema import ScenarioSpec


def compute_digest(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def _find_repo_root(start: Path) -> Path | None:
    """Walk up from `start` to find a git repo root (directory containing `.git`)."""

    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists():
            return candidate
    return None


def _run_git(args: list[str], *, cwd: Path) -> str | None:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=str(cwd),
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout.strip() or None


def resolve_repo_commit() -> str:
    """Best-effort git commit identifier for reproducibility metadata."""

    repo_root = _find_repo_root(Path.cwd()) or _find_repo_root(Path(__file__).resolve())
    if repo_root is None:
        return "unknown"

    commit = _run_git(["rev-parse", "HEAD"], cwd=repo_root)
    if not commit:
        return "unknown"

    dirty = False
    # Treat both staged and unstaged changes as "dirty".
    for cmd in (["diff", "--quiet"], ["diff", "--cached", "--quiet"]):
        try:
            proc = subprocess.run(
                ["git", *cmd],
                cwd=str(repo_root),
                check=False,
                capture_output=True,
            )
        except OSError:
            proc = None
        if proc is not None and proc.returncode != 0:
            dirty = True
            break

    short = commit[:12]
    return f"{short}-dirty" if dirty else short


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_catalog_digest(catalog_uri: str) -> str:
    """Compute a stable digest for the catalog backing a run.

    This is best-effort: for local paths and file:// URLs, hash file/directory
    contents; for remote URIs, fall back to a digest of the URI string.
    """

    uri = str(catalog_uri or "").strip()
    if not uri:
        return "unknown"

    parsed = urlparse(uri)
    if parsed.scheme == "file":
        path = Path(parsed.path)
    elif parsed.scheme in {"", "s3"}:
        path = Path(uri) if parsed.scheme == "" else None
    else:
        path = None

    if path is None or not path.exists():
        return compute_digest({"catalog_uri": uri})

    if path.is_file():
        return _sha256_file(path)[:16]

    # Directory: prefer hashing a catalog parquet if present, otherwise hash the tree.
    parquet = path / "catalog.parquet"
    if parquet.exists() and parquet.is_file():
        return _sha256_file(parquet)[:16]

    h = hashlib.sha256()
    for child in sorted(p for p in path.rglob("*") if p.is_file()):
        rel = child.relative_to(path).as_posix().encode("utf-8")
        h.update(rel)
        h.update(b"\0")
        h.update(_sha256_file(child).encode("utf-8"))
        h.update(b"\0")
    return h.hexdigest()[:16]


def resolve_scenarios_digest(scenarios_path: Path) -> str:
    """Compute a stable digest for the scenario spec file."""

    try:
        raw = scenarios_path.read_bytes()
    except OSError:
        return "unknown"
    return hashlib.sha256(raw).hexdigest()[:16]


def build_bundle_digest(
    *,
    scenario: ScenarioSpec,
    catalog_uri: str,
    strategy_ids: list[str],
    k: int | None,
    config: dict[str, object] | None = None,
) -> str:
    return compute_digest(
        {
            "scenario": scenario.model_dump(mode="json"),
            "catalog_uri": catalog_uri,
            "strategy_ids": strategy_ids,
            "k": k,
            "config": config or {},
        }
    )


def resolve_artifacts_config(*, run_config: RetrievalRunConfig) -> dict[str, object]:
    """Resolve a non-secret configuration snapshot for digesting + debugging."""

    return {
        "repo_commit": resolve_repo_commit(),
        **run_config.public_dict(),
    }
