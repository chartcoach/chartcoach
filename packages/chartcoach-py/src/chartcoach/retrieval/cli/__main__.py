from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from chartcoach.env import load_env
from chartcoach.retrieval.config import load_run_config, load_run_config_from_doc
from chartcoach.retrieval.manifest import load_manifest
from chartcoach.retrieval.service import (
    EvalArtifactsService,
    RetrievalService,
    create_store,
    default_artifacts_url,
)
from chartcoach.retrieval.strategy.registry import create_default_strategy_registrations


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="chartcoach-retrieval")
    sub = parser.add_subparsers(dest="cmd", required=True)

    list_cmd = sub.add_parser(
        "list-strategies", help="List available retrieval strategies."
    )
    list_cmd.add_argument("--json", action="store_true", help="Output JSON.")

    analyze_cmd = sub.add_parser(
        "analyze-stability",
        help="Compute retrieval stability (top-k overlap) across multiple artifact runs.",
    )
    analyze_cmd.add_argument(
        "--runs",
        type=Path,
        action="append",
        default=[],
        help="Artifacts root directory containing bundles/*.json (repeatable).",
    )
    analyze_cmd.add_argument(
        "-k",
        "--k",
        type=int,
        default=None,
        help="Number of top results to compare (defaults to full returned set).",
    )
    analyze_cmd.add_argument("--json", action="store_true", help="Output JSON.")

    counter_cmd = sub.add_parser(
        "analyze-counterfactual",
        help="Compute overlap across counterfactual scenario variants for each strategy.",
    )
    counter_cmd.add_argument(
        "--run",
        type=Path,
        required=True,
        help="Artifacts root directory containing index.json and bundles/*.json.",
    )
    counter_cmd.add_argument(
        "-k",
        "--k",
        type=int,
        default=None,
        help="Number of top results to compare (defaults to full returned set).",
    )
    counter_cmd.add_argument("--json", action="store_true", help="Output JSON.")

    pool_cmd = sub.add_parser(
        "analyze-pool",
        help="Compute per-scenario pool coverage (unique guidelines in union of top-k across strategies).",
    )
    pool_cmd.add_argument(
        "--run",
        type=Path,
        required=True,
        help="Artifacts root directory containing bundles/*.json.",
    )
    pool_cmd.add_argument(
        "-k",
        "--k",
        type=int,
        default=None,
        help="Pool depth per strategy (defaults to full returned set).",
    )
    pool_cmd.add_argument("--json", action="store_true", help="Output JSON.")

    neg_cmd = sub.add_parser(
        "analyze-negatives",
        help="Compute negative-hit rates for scenarios that define negative guideline ids.",
    )
    neg_cmd.add_argument(
        "--run",
        type=Path,
        required=True,
        help="Artifacts root directory containing index.json and bundles/*.json.",
    )
    neg_cmd.add_argument(
        "-k",
        "--k",
        type=int,
        default=None,
        help="Number of top results to evaluate (defaults to full returned set).",
    )
    neg_cmd.add_argument("--json", action="store_true", help="Output JSON.")

    paper_cmd = sub.add_parser(
        "paper-assets",
        help="Generate paper-facing tables (CSV/Markdown) from one or more artifact runs.",
    )
    paper_cmd.add_argument(
        "--run",
        type=Path,
        action="append",
        default=[],
        help="Artifacts root directory containing index.json and bundles/*.json (repeatable).",
    )
    paper_cmd.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Output directory to write CSV/Markdown assets into.",
    )
    paper_cmd.add_argument(
        "--taxonomy",
        type=Path,
        default=Path("docs/retrieval/strategy_taxonomy.yaml"),
        help="Path to the strategy taxonomy YAML used for grouping.",
    )
    paper_cmd.add_argument(
        "-k",
        "--k",
        type=int,
        default=None,
        help="Number of top results to analyze (defaults to full returned set).",
    )
    paper_cmd.add_argument(
        "--plots",
        action="store_true",
        help="Also render PNG plots (requires optional 'paper' deps).",
    )

    run_cmd = sub.add_parser(
        "run", help="Run retrieval over eval scenarios and upload artifacts."
    )
    run_cmd.add_argument(
        "--scenarios",
        type=Path,
        default=Path("evals/scenarios/spec.yaml"),
        help="Path to scenarios spec.yaml",
    )
    run_cmd.add_argument(
        "--catalog-uri",
        type=str,
        default=None,
        help="Catalog URI (path/file/http(s)/s3). Defaults to CHARTCOACH_CATALOG_PATH if set.",
    )
    run_cmd.add_argument(
        "--strategy",
        dest="strategies",
        action="append",
        default=[],
        help="Strategy id to run (repeatable). Defaults to all.",
    )
    run_cmd.add_argument(
        "-k",
        "--k",
        type=int,
        default=None,
        help="Number of guidelines to retrieve per strategy (omit for unlimited).",
    )
    run_cmd.add_argument(
        "--artifacts-url",
        type=str,
        default=None,
        help="Destination store URL (e.g. s3://bucket/prefix/eval-artifacts/v1/).",
    )
    run_cmd.add_argument(
        "--purge",
        action="store_true",
        help="Delete existing artifacts under this artifacts URL before writing.",
    )
    run_cmd.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to retrieval run config YAML (defaults + env if omitted).",
    )
    run_cmd.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Path to an experiment manifest YAML (freezes run args + config; ignores env defaults).",
    )

    purge_cmd = sub.add_parser("purge", help="Delete previously generated artifacts.")
    purge_cmd.add_argument(
        "--artifacts-url",
        type=str,
        default=None,
        help="Store URL to purge (defaults to S3_PREFIX + eval-artifacts/v1/).",
    )
    purge_cmd.add_argument(
        "--prefix",
        type=str,
        default="",
        help="Prefix within the artifacts store to delete (default: all).",
    )

    return parser


def _require_catalog_uri(arg: str | None) -> str:
    if arg:
        return arg
    env_catalog = load_env().retrieval_server.catalog_path
    if env_catalog:
        return str(env_catalog)
    raise SystemExit(
        "Missing --catalog-uri (or set CHARTCOACH_CATALOG_PATH in the environment)."
    )


def _resolve_store_url(arg: str | None) -> str:
    if arg:
        return arg
    s3 = load_env().s3.require()
    return default_artifacts_url(s3=s3)


def _create_artifacts_store(url: str):
    env = load_env()
    s3 = env.s3.require() if urlparse(url).scheme == "s3" else None
    return create_store(url, s3=s3)


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    registrations = create_default_strategy_registrations()
    retrieval = RetrievalService(registrations=registrations)

    if args.cmd == "list-strategies":
        infos = [info.model_dump(mode="json") for info in retrieval.list_strategies()]
        if args.json:
            print(json.dumps(infos, ensure_ascii=False, sort_keys=True))
        else:
            for info in infos:
                print(f"{info['id']}  {info['name']}")
        return

    if args.cmd == "analyze-stability":
        from chartcoach.retrieval.analysis.stability import (
            compute_stability,
            format_stability_table,
        )

        runs = [Path(p) for p in (args.runs or [])]
        if len(runs) < 2:
            raise SystemExit("Provide at least two --runs directories.")

        results = compute_stability(runs=runs, k=args.k)
        if args.json:
            payload = [
                {
                    "strategy_id": r.strategy_id,
                    "mean_jaccard": r.mean_jaccard,
                    "scenarios": r.scenarios,
                }
                for r in results
            ]
            print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        else:
            print(format_stability_table(results))
        return

    if args.cmd == "analyze-counterfactual":
        from chartcoach.retrieval.analysis.counterfactual import (
            compute_counterfactual_sensitivity,
            format_counterfactual_table,
        )

        results = compute_counterfactual_sensitivity(
            artifacts_root=Path(args.run), k=args.k
        )
        if args.json:
            payload = [
                {
                    "strategy_id": r.strategy_id,
                    "mean_jaccard": r.mean_jaccard,
                    "groups": r.groups,
                }
                for r in results
            ]
            print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        else:
            print(format_counterfactual_table(results))
        return

    if args.cmd == "analyze-pool":
        from chartcoach.retrieval.analysis.pooling import (
            compute_pool_coverage,
            format_pool_table,
        )

        results = compute_pool_coverage(artifacts_root=Path(args.run), k=args.k)
        if args.json:
            payload = [
                {
                    "scenario_id": r.scenario_id,
                    "strategies": r.strategies,
                    "unique_guidelines": r.unique_guidelines,
                }
                for r in results
            ]
            print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        else:
            print(format_pool_table(results))
        return

    if args.cmd == "analyze-negatives":
        from chartcoach.retrieval.analysis.negatives import (
            compute_negative_hit_rates,
            format_negative_hit_table,
        )

        results = compute_negative_hit_rates(artifacts_root=Path(args.run), k=args.k)
        if args.json:
            payload = [
                {
                    "strategy_id": r.strategy_id,
                    "mean_negative_fraction": r.mean_negative_fraction,
                    "any_negative_fraction": r.any_negative_fraction,
                    "scenarios": r.scenarios,
                }
                for r in results
            ]
            print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        else:
            print(format_negative_hit_table(results))
        return

    if args.cmd == "paper-assets":
        from chartcoach.retrieval.analysis.paper_assets import write_paper_assets

        runs = [Path(p) for p in (args.run or [])]
        if not runs:
            raise SystemExit("Provide at least one --run directory.")
        write_paper_assets(
            runs=runs,
            out_dir=Path(args.out),
            taxonomy_path=Path(args.taxonomy),
            k=args.k,
            plots=bool(getattr(args, "plots", False)),
        )
        print(str(args.out))
        return

    if args.cmd == "purge":
        url = _resolve_store_url(args.artifacts_url)
        store = _create_artifacts_store(url)
        svc = EvalArtifactsService(store=store, retrieval=retrieval)
        deleted = svc.purge(prefix=args.prefix)
        print(f"Deleted {deleted} objects.")
        return

    if args.cmd == "run":
        if args.manifest:
            if (
                args.config is not None
                or args.catalog_uri is not None
                or args.k is not None
                or args.strategies
            ):
                raise SystemExit(
                    "When using --manifest, do not pass --config/--catalog-uri/-k/--strategy."
                )

            manifest = load_manifest(args.manifest)
            run_config = load_run_config_from_doc(manifest.config, use_env=False)
            url = _resolve_store_url(args.artifacts_url or manifest.run.artifacts_url)
            scenarios_path = Path(manifest.run.scenarios)
            catalog_uri = manifest.run.catalog_uri
            strategy_ids = manifest.run.strategies or None
            k = manifest.run.k
            purge = bool(args.purge or manifest.run.purge)
            manifest_meta = manifest.public_dict()
        else:
            run_config = load_run_config(args.config)
            url = _resolve_store_url(args.artifacts_url)
            scenarios_path = args.scenarios
            catalog_uri = _require_catalog_uri(args.catalog_uri)
            strategy_ids = args.strategies or None
            k = args.k
            purge = bool(args.purge)
            manifest_meta = None

        store = _create_artifacts_store(url)
        svc = EvalArtifactsService(store=store, retrieval=retrieval)
        if purge:
            svc.purge(prefix="")

        svc.run(
            scenarios_path=scenarios_path,
            catalog_uri=catalog_uri,
            strategy_ids=strategy_ids,
            k=k,
            run_config=run_config,
            manifest=manifest_meta,
        )
        print("Artifacts written.")
        return

    raise AssertionError("unreachable")  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
