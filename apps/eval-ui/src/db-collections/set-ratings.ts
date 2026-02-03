import { createCollection, localOnlyCollectionOptions } from "@tanstack/react-db";
import { rxdbCollectionOptions } from "@tanstack/rxdb-db-collection";
import type { RxCollection } from "rxdb";

import { getEvalUiRxDatabase } from "@chartcoach/eval-ui/db/rxdb";
import {
  ScenarioSetRatingSchema,
  type ScenarioSetRating,
} from "@chartcoach/eval-ui/eval/set-ratings";

let rxCollection: RxCollection<ScenarioSetRating> | undefined;
if (typeof window !== "undefined") {
  try {
    rxCollection = (await getEvalUiRxDatabase()).set_ratings;
  } catch (error) {
    console.warn(
      "[eval-ui] Failed to initialize RxDB set ratings collection; falling back to local-only collection.",
      error,
    );
    rxCollection = undefined;
  }
}

export const setRatingsCollection = createCollection(
  rxCollection
    ? rxdbCollectionOptions({
        rxCollection,
        startSync: true,
        schema: ScenarioSetRatingSchema,
      })
    : localOnlyCollectionOptions({
        getKey: (rating) => rating.id,
        schema: ScenarioSetRatingSchema,
      }),
);

export function clearSetRatings() {
  for (const id of setRatingsCollection.state.keys()) {
    setRatingsCollection.delete(id);
  }
}

export function makeSetRatingId(scenarioId: string, strategyId: string) {
  return `${scenarioId}::${strategyId}`;
}

export function upsertSetRating({
  scenarioId,
  strategyId,
  patch,
  now = new Date().toISOString(),
}: {
  scenarioId: string;
  strategyId: string;
  patch: Partial<Omit<ScenarioSetRating, "id" | "scenarioId" | "strategyId" | "createdAt" | "updatedAt">>;
  now?: string;
}) {
  const id = makeSetRatingId(scenarioId, strategyId);

  if (setRatingsCollection.state.has(id)) {
    setRatingsCollection.update(id, (draft) => {
      for (const [key, value] of Object.entries(patch)) {
        if (value === undefined) {
          // eslint-disable-next-line @typescript-eslint/no-dynamic-delete
          delete (draft as Record<string, unknown>)[key];
          continue;
        }
        (draft as Record<string, unknown>)[key] = value;
      }
      draft.updatedAt = now;
    });
    return;
  }

  const insert: ScenarioSetRating = {
    id,
    scenarioId,
    strategyId,
    createdAt: now,
    updatedAt: now,
    ...(patch.sufficiency === undefined ? {} : { sufficiency: patch.sufficiency }),
    ...(patch.redundancy === undefined ? {} : { redundancy: patch.redundancy }),
    ...(patch.coherence === undefined ? {} : { coherence: patch.coherence }),
    ...(patch.harm === undefined ? {} : { harm: patch.harm }),
    ...(patch.notes === undefined ? {} : { notes: patch.notes }),
  };

  setRatingsCollection.insert(insert);
}

export function deleteSetRating({
  scenarioId,
  strategyId,
}: {
  scenarioId: string;
  strategyId: string;
}) {
  const id = makeSetRatingId(scenarioId, strategyId);
  if (setRatingsCollection.state.has(id)) {
    setRatingsCollection.delete(id);
  }
}

export function mergeSetRatings(ratings: ScenarioSetRating[]) {
  const optionalKeys: Array<keyof ScenarioSetRating> = [
    "sufficiency",
    "redundancy",
    "coherence",
    "harm",
    "notes",
  ];

  for (const rating of ratings) {
    const existing = setRatingsCollection.state.get(rating.id);

    if (!existing) {
      setRatingsCollection.insert(rating);
      continue;
    }

    if (existing.updatedAt >= rating.updatedAt) continue;

    setRatingsCollection.update(rating.id, (draft) => {
      Object.assign(draft, rating);
      for (const key of optionalKeys) {
        if (!(key in rating)) {
          // eslint-disable-next-line @typescript-eslint/no-dynamic-delete
          delete (draft as Record<string, unknown>)[key as string];
        }
      }
    });
  }
}

export type { ScenarioSetRating } from "@chartcoach/eval-ui/eval/set-ratings";

