import { createRxDatabase } from "rxdb/plugins/core";
import { getRxStorageLocalstorage } from "rxdb/plugins/storage-localstorage";
import type { RxCollection, RxDatabase, RxJsonSchema } from "rxdb";

import type { ScenarioSpec } from "@chartcoach/eval-ui/eval/schemas";
import type { RelevanceRating } from "@chartcoach/eval-ui/eval/relevance-ratings";
import type { EvalScenarioBundle } from "@chartcoach/eval-ui/eval/types";

export type CachedScenarioDoc = {
  id: string;
  index: number;
  cachedAt: string;
  scenario: ScenarioSpec;
};

export type CachedScenarioBundleDoc = {
  id: string;
  cachedAt: string;
  bundle: EvalScenarioBundle;
};

type EvalUiCollections = {
  relevance_ratings: RxCollection<RelevanceRating>;
  scenarios: RxCollection<CachedScenarioDoc>;
  scenario_bundles: RxCollection<CachedScenarioBundleDoc>;
};

export type EvalUiRxDatabase = RxDatabase<EvalUiCollections>;

const RelevanceRatingsRxSchema: RxJsonSchema<RelevanceRating> = {
  title: "relevance_ratings",
  version: 0,
  type: "object",
  primaryKey: "id",
  properties: {
    id: {
      type: "string",
      maxLength: 200,
    },
    scenarioId: {
      type: "string",
    },
    guidelineId: {
      type: "string",
    },
    relevance: {
      type: "integer",
      minimum: 1,
      maximum: 5,
    },
    createdAt: {
      type: "string",
    },
    updatedAt: {
      type: "string",
    },
  },
  required: ["id", "scenarioId", "guidelineId", "relevance", "createdAt", "updatedAt"],
  additionalProperties: false,
};

const ScenariosRxSchema: RxJsonSchema<CachedScenarioDoc> = {
  title: "scenarios",
  version: 0,
  type: "object",
  primaryKey: "id",
  properties: {
    id: {
      type: "string",
      maxLength: 200,
    },
    index: {
      type: "integer",
      minimum: 0,
    },
    cachedAt: {
      type: "string",
    },
    scenario: {
      type: "object",
      additionalProperties: true,
    },
  },
  required: ["id", "index", "cachedAt", "scenario"],
  additionalProperties: false,
};

const ScenarioBundlesRxSchema: RxJsonSchema<CachedScenarioBundleDoc> = {
  title: "scenario_bundles",
  version: 0,
  type: "object",
  primaryKey: "id",
  properties: {
    id: {
      type: "string",
      maxLength: 200,
    },
    cachedAt: {
      type: "string",
    },
    bundle: {
      type: "object",
      additionalProperties: true,
    },
  },
  required: ["id", "cachedAt", "bundle"],
  additionalProperties: false,
};

let databasePromise: Promise<EvalUiRxDatabase> | undefined;

export function getEvalUiRxDatabase(): Promise<EvalUiRxDatabase> {
  if (typeof window === "undefined") {
    throw new Error("Eval UI RxDB is only available in the browser.");
  }

  databasePromise ??= (async () => {
    const db = await createRxDatabase<EvalUiCollections>({
      name: "chartcoach-eval-ui",
      storage: getRxStorageLocalstorage(),
      multiInstance: true,
      ignoreDuplicate: true,
    });

    await db.addCollections({
      relevance_ratings: {
        schema: RelevanceRatingsRxSchema,
      },
      scenarios: {
        schema: ScenariosRxSchema,
      },
      scenario_bundles: {
        schema: ScenarioBundlesRxSchema,
      },
    });

    return db;
  })();

  return databasePromise;
}
