from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Any

from obstore.store import ObjectStore

from chartcoach.retrieval.config import RetrievalRunConfig
from chartcoach.retrieval.service.eval_artifacts_builder import (
    build_artifacts_index,
    build_scenario_bundle,
    load_scenarios,
)
from chartcoach.retrieval.service.eval_artifacts_digests import (
    build_bundle_digest,
    resolve_artifacts_config,
    resolve_catalog_digest,
    resolve_scenarios_digest,
)
from chartcoach.retrieval.service.eval_artifacts_store import (
    delete_paths,
    list_paths,
    read_json,
    write_json,
)
from chartcoach.retrieval.service.retrieval_service import RetrievalService


class EvalArtifactsService:
    def __init__(self, *, store: ObjectStore, retrieval: RetrievalService) -> None:
        self._store = store
        self._retrieval = retrieval

    @staticmethod
    def _bundle_has_errors(bundle: dict[str, Any]) -> bool:
        strategies = bundle.get("strategies")
        if not isinstance(strategies, list):
            return False
        for strategy in strategies:
            if not isinstance(strategy, dict):
                continue
            meta = strategy.get("meta")
            if isinstance(meta, dict) and meta.get("error"):
                return True
        return False

    def purge(self, *, prefix: str = "") -> int:
        paths = list_paths(self._store, prefix=prefix)
        delete_paths(self._store, paths)
        return len(paths)

    def run(
        self,
        *,
        scenarios_path: Path,
        catalog_uri: str,
        strategy_ids: Sequence[str] | None,
        k: int | None,
        run_config: RetrievalRunConfig,
        manifest: dict[str, object] | None = None,
    ) -> None:
        scenarios = load_scenarios(scenarios_path)

        strategies = self._retrieval.instantiate_strategies(
            catalog_uri=catalog_uri, strategy_ids=strategy_ids, run_config=run_config
        )
        # strategy ids are needed for stable digests even when some scenarios are skipped
        resolved_strategy_ids = [info.id for info, _strategy in strategies]
        config = resolve_artifacts_config(run_config=run_config)
        config = {
            **config,
            "catalog_digest": resolve_catalog_digest(catalog_uri),
            "scenario_digest": resolve_scenarios_digest(scenarios_path),
        }
        if manifest:
            config["manifest"] = dict(manifest)

        for scenario in scenarios:
            digest = build_bundle_digest(
                scenario=scenario,
                catalog_uri=catalog_uri,
                strategy_ids=resolved_strategy_ids,
                k=k,
                config=config,
            )
            bundle_path = f"bundles/{scenario.id}.json"
            existing = read_json(self._store, bundle_path)
            if (
                existing
                and existing.get("digest") == digest
                and not self._bundle_has_errors(existing)
            ):
                continue

            bundle = build_scenario_bundle(
                scenario=scenario,
                catalog_uri=catalog_uri,
                strategies=strategies,
                k=k,
                strategy_timeout_seconds=run_config.strategy_timeout_seconds,
                config=config,
            )
            write_json(self._store, bundle_path, bundle.model_dump(mode="json"))

        index = build_artifacts_index(
            scenarios=scenarios,
            strategies=strategies,
            config=config,
        )
        write_json(self._store, "index.json", index.model_dump(mode="json"))
