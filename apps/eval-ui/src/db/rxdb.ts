import { createRxDatabase } from "rxdb/plugins/core";
import { getRxStorageLocalstorage } from "rxdb/plugins/storage-localstorage";
import type { RxCollection, RxDatabase, RxJsonSchema } from "rxdb";

import type { RelevanceRating } from "@chartcoach/eval-ui/eval/relevance-ratings";

type EvalUiCollections = {
  relevance_ratings: RxCollection<RelevanceRating>;
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
    });

    return db;
  })();

  return databasePromise;
}
