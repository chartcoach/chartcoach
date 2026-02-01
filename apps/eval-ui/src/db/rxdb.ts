import { createRxDatabase } from "rxdb/plugins/core";
import { getRxStorageLocalstorage } from "rxdb/plugins/storage-localstorage";
import type { RxCollection, RxDatabase, RxJsonSchema } from "rxdb";

import type { GuidelineRating } from "@chartcoach/eval-ui/eval/guideline-ratings";

type EvalUiCollections = {
  guideline_ratings: RxCollection<GuidelineRating>;
};

export type EvalUiRxDatabase = RxDatabase<EvalUiCollections>;

const GuidelineRatingsRxSchema: RxJsonSchema<GuidelineRating> = {
  title: "guideline_ratings",
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
    bucket: {
      type: "string",
      enum: ["hard_constraint", "soft_constraint", "not_useful", "not_applicable"],
    },
    actionability: {
      type: "integer",
      minimum: 1,
      maximum: 5,
    },
    impact: {
      type: "integer",
      minimum: 1,
      maximum: 5,
    },
    risk: {
      type: "integer",
      minimum: 1,
      maximum: 5,
    },
    credibility: {
      type: "integer",
      minimum: 1,
      maximum: 5,
    },
    notes: {
      type: "string",
    },
    createdAt: {
      type: "string",
    },
    updatedAt: {
      type: "string",
    },
  },
  required: ["id", "scenarioId", "guidelineId", "bucket", "createdAt", "updatedAt"],
  additionalProperties: false,
};

let databasePromise: Promise<EvalUiRxDatabase> | undefined;

export function getEvalUiRxDatabase(): Promise<EvalUiRxDatabase> {
  if (typeof window === "undefined") {
    throw new Error("Eval UI RxDB is only available in the browser.");
  }

  const globalScope = globalThis as unknown as {
    __chartcoachEvalUiRxDbPromise?: Promise<EvalUiRxDatabase>;
  };

  databasePromise ??= globalScope.__chartcoachEvalUiRxDbPromise ??= (async () => {
    const db = await createRxDatabase<EvalUiCollections>({
      name: "chartcoach-eval-ui",
      storage: getRxStorageLocalstorage(),
      multiInstance: true,
    });

    await db.addCollections({
      guideline_ratings: {
        schema: GuidelineRatingsRxSchema,
      },
    });

    return db;
  })();

  return databasePromise;
}
