import path from "node:path";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

import { createServerFn } from "@tanstack/react-start";
import { parse as parseYaml } from "yaml";
import { z } from "zod";

import { env } from "@chartcoach/eval-ui/env";

import { ScenariosFileSchema, type ScenarioSpec } from "../schemas";
import type { EvalScenarioBundle, EvalStrategyResult } from "../types";
import type { CatalogEntry } from "@chartcoach/catalog";
import { ChartCoachRetrievalClient } from "@chartcoach/eval-ui/eval/retrieval/chartcoach-retrieval-client";
import { catalogEntriesFromWire, buildRetrievalRequestFromScenario } from "../retrieval/wire";
import {
  buildRetrievalResultsCacheKey,
  computeRetrievalResultsDigest,
  readRetrievalResultsCache,
  writeRetrievalResultsCache,
} from "./retrieval-results-cache.server";

const repoRoot = fileURLToPath(new URL("../../../../../", import.meta.url));
const scenariosSpecPath = path.join(repoRoot, "evals/scenarios/spec.yaml");
const catalogParquetPath = path.join(repoRoot, "guidelines/catalog.parquet");

const ScenarioBundleInputSchema = z.object({
  scenarioId: z.string().min(1),
});

let scenariosPromise: Promise<ScenarioSpec[]> | undefined;
async function loadScenarios(): Promise<ScenarioSpec[]> {
  scenariosPromise ??= (async () => {
    try {
      const raw = await readFile(scenariosSpecPath, "utf8");
      const parsed = ScenariosFileSchema.parse(parseYaml(raw));
      return parsed.scenarios;
    } catch (error) {
      scenariosPromise = undefined;
      throw error;
    }
  })();
  return scenariosPromise;
}

function indexToLetters(index: number) {
  let n = index;
  let letters = "";
  while (n >= 0) {
    letters = String.fromCharCode(65 + (n % 26)) + letters;
    n = Math.floor(n / 26) - 1;
  }
  return letters;
}

let strategiesPromise: Promise<Array<{ id: string; name: string }>> | undefined;
async function loadStrategyInfos() {
  strategiesPromise ??= (async () => {
    try {
      const client = new ChartCoachRetrievalClient({ baseUrl: env.RETRIEVAL_SERVER_BASE_URL });
      const strategies = await client.listStrategies();
      return strategies.map((s) => ({ id: s.id, name: s.name }));
    } catch (error) {
      strategiesPromise = undefined;
      throw error;
    }
  })();
  return strategiesPromise;
}

async function mapConcurrent<T, R>(
  items: readonly T[],
  concurrency: number,
  run: (item: T, index: number) => Promise<R>,
): Promise<R[]> {
  const results: R[] = [];
  results.length = items.length;
  const limit = Math.max(1, Math.min(concurrency, items.length));
  let nextIndex = 0;

  async function worker() {
    while (true) {
      const current = nextIndex++;
      if (current >= items.length) return;
      results[current] = await run(items[current]!, current);
    }
  }

  await Promise.all(Array.from({ length: limit }, worker));
  return results;
}

function buildEvalStrategyResult(args: {
  strategyId: string;
  strategyName: string;
  catalogEntries: CatalogEntry[];
}): EvalStrategyResult {
  const guidelines = args.catalogEntries.map((entry, i) => {
    const score = Math.max(0.01, 1 - i / Math.max(1, args.catalogEntries.length));
    return { rank: i + 1, score, entry };
  });

  return {
    strategyId: args.strategyId,
    strategyName: args.strategyName,
    guidelines,
  };
}

export const getEvalScenarios = createServerFn({ method: "GET" }).handler(
  async () => await loadScenarios(),
);

export const getEvalScenarioBundle = createServerFn({ method: "POST" })
  .inputValidator((input) => ScenarioBundleInputSchema.parse(input))
  .handler(async ({ data }): Promise<EvalScenarioBundle> => {
    const scenarios = await loadScenarios();
    const scenario = scenarios.find((s) => s.id === data.scenarioId);
    if (!scenario) {
      throw new Error(`Unknown scenarioId: ${data.scenarioId}`);
    }

    const catalogUri = env.RETRIEVAL_CATALOG_URI ?? catalogParquetPath;
    const retrievalRequest = buildRetrievalRequestFromScenario(scenario);

    const client = new ChartCoachRetrievalClient({ baseUrl: env.RETRIEVAL_SERVER_BASE_URL });
    const strategiesInfo = (await loadStrategyInfos()).slice().sort((a, b) => a.id.localeCompare(b.id));

    const strategies = await mapConcurrent(
      strategiesInfo,
      env.RETRIEVAL_STRATEGY_CONCURRENCY,
      async (strategy, idx): Promise<EvalStrategyResult> => {
        const strategyName =
          env.STRATEGY_DISPLAY_MODE === "alias" ? `Strategy ${indexToLetters(idx)}` : strategy.name;

        const digest = computeRetrievalResultsDigest({
          scenarioId: scenario.id,
          strategyId: strategy.id,
          catalogUri,
          request: retrievalRequest,
          baseUrl: env.RETRIEVAL_SERVER_BASE_URL,
        });
        const cacheKey = buildRetrievalResultsCacheKey({
          scenarioId: scenario.id,
          strategyId: strategy.id,
          digest,
        });

        const cached = await readRetrievalResultsCache(cacheKey);
        const response =
          cached?.response ??
          (await client.runStrategy({
            strategyId: strategy.id,
            catalogUri,
            request: retrievalRequest,
          }));

        if (!cached) {
          await writeRetrievalResultsCache(cacheKey, {
            scenarioId: scenario.id,
            strategyId: strategy.id,
            catalogUri,
            request: retrievalRequest,
            response,
          });
        }

        const entries = catalogEntriesFromWire(response.catalog);
        return buildEvalStrategyResult({
          strategyId: strategy.id,
          strategyName,
          catalogEntries: entries,
        });
      },
    );

    return { scenario, strategies };
  });
