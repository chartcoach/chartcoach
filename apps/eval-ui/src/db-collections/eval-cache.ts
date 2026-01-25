import { createCollection, localOnlyCollectionOptions } from "@tanstack/react-db";
import { rxdbCollectionOptions } from "@tanstack/rxdb-db-collection";
import type { RxCollection } from "rxdb";
import { z } from "zod";

import {
  getEvalUiRxDatabase,
  type CachedScenarioBundleDoc,
  type CachedScenarioDoc,
} from "@chartcoach/eval-ui/db/rxdb";
import type { EvalScenarioBundle } from "@chartcoach/eval-ui/eval/types";
import { ScenarioSpecSchema } from "@chartcoach/eval-ui/eval/schemas";

const CachedScenarioDocSchema = z.object({
  id: z.string().min(1),
  index: z.number().int().nonnegative(),
  cachedAt: z.string().min(1),
  scenario: ScenarioSpecSchema,
});

const CachedScenarioBundleDocSchema = z.object({
  id: z.string().min(1),
  cachedAt: z.string().min(1),
  bundle: z.custom<EvalScenarioBundle>(() => true),
});

let scenariosRxCollection: RxCollection<CachedScenarioDoc> | undefined;
let scenarioBundlesRxCollection: RxCollection<CachedScenarioBundleDoc> | undefined;

if (typeof window !== "undefined") {
  try {
    const db = await getEvalUiRxDatabase();
    scenariosRxCollection = db.scenarios;
    scenarioBundlesRxCollection = db.scenario_bundles;
  } catch {
    scenariosRxCollection = undefined;
    scenarioBundlesRxCollection = undefined;
  }
}

export const scenariosCacheCollection = createCollection(
  scenariosRxCollection
    ? rxdbCollectionOptions({
        rxCollection: scenariosRxCollection,
        startSync: true,
        schema: CachedScenarioDocSchema,
      })
    : localOnlyCollectionOptions({
        getKey: (doc) => doc.id,
        schema: CachedScenarioDocSchema,
      }),
);

export const scenarioBundlesCacheCollection = createCollection(
  scenarioBundlesRxCollection
    ? rxdbCollectionOptions({
        rxCollection: scenarioBundlesRxCollection,
        startSync: true,
        schema: CachedScenarioBundleDocSchema,
      })
    : localOnlyCollectionOptions({
        getKey: (doc) => doc.id,
        schema: CachedScenarioBundleDocSchema,
      }),
);
