import path from "node:path";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

import { createServerFn } from "@tanstack/react-start";
import { parse as parseYaml } from "yaml";
import { z } from "zod";

import { loadCatalogFromParquetFile } from "@chartcoach/catalog/node";
import { env } from "@chartcoach/eval-ui/env";

import { ScenariosFileSchema, type ScenarioSpec } from "../schemas";
import type { EvalScenarioBundle, EvalStrategyResult } from "../types";
import type { CatalogEntry } from "@chartcoach/catalog";

const repoRoot = fileURLToPath(new URL("../../../../../", import.meta.url));
const scenariosSpecPath = path.join(repoRoot, "evals/scenarios/spec.yaml");
const catalogParquetPath = path.join(repoRoot, "guidelines/catalog.parquet");

const ScenarioBundleInputSchema = z.object({
  scenarioId: z.string().min(1),
});

type StrategySpec = {
  name: string;
  k: number;
};

const STRATEGIES: StrategySpec[] = [
  { name: "Head", k: 8 },
  { name: "Guideline Browser", k: 8 },
  { name: "Vector Search", k: 8 },
];

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

let catalogEntriesPromise: Promise<CatalogEntry[]> | undefined;
async function loadCatalogEntries(): Promise<CatalogEntry[]> {
  catalogEntriesPromise ??= (async () => {
    try {
      const catalog = await loadCatalogFromParquetFile(catalogParquetPath);
      return catalog.entries;
    } catch (error) {
      catalogEntriesPromise = undefined;
      throw error;
    }
  })();
  return catalogEntriesPromise;
}

function hashStringToSeed(input: string): number {
  let hash = 2166136261;
  for (let i = 0; i < input.length; i++) {
    hash ^= input.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

function strategyIdFromName(name: string) {
  const hash = hashStringToSeed(`strategy:${name}`);
  return `s_${hash.toString(16).padStart(8, "0")}`;
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

function mulberry32(seed: number): () => number {
  return () => {
    let t = (seed += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function sampleUniqueIndexes(count: number, k: number, rng: () => number) {
  const selected = new Set<number>();
  while (selected.size < Math.min(k, count)) {
    selected.add(Math.floor(rng() * count));
  }
  return [...selected];
}

function buildDummyStrategyResults(
  catalogEntries: CatalogEntry[],
  scenarioId: string,
): EvalStrategyResult[] {
  const strategies = STRATEGIES.slice().sort((a, b) => a.name.localeCompare(b.name));

  return strategies.map((strategy, idx) => {
    const strategyId = strategyIdFromName(strategy.name);
    const strategyName =
      env.STRATEGY_DISPLAY_MODE === "alias" ? `Strategy ${indexToLetters(idx)}` : strategy.name;

    const rng = mulberry32(hashStringToSeed(`${scenarioId}::${strategyId}`));
    const idxs = sampleUniqueIndexes(catalogEntries.length, strategy.k, rng);

    const guidelines = idxs.map((idx, i) => {
      const score = Math.max(0.01, 1 - i / Math.max(1, idxs.length));
      return { rank: i + 1, score, entry: catalogEntries[idx]! };
    });

    return {
      strategyId,
      strategyName,
      guidelines,
    };
  });
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

    const catalogEntries = await loadCatalogEntries();
    const strategies = buildDummyStrategyResults(catalogEntries, scenario.id);

    return { scenario, strategies };
  });
