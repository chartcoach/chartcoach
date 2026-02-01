import { createCollection, localOnlyCollectionOptions } from "@tanstack/react-db";
import { rxdbCollectionOptions } from "@tanstack/rxdb-db-collection";
import type { RxCollection } from "rxdb";

import { getEvalUiRxDatabase } from "@chartcoach/eval-ui/db/rxdb";
import {
  GuidelineRatingSchema,
  type GuidelineRating,
} from "@chartcoach/eval-ui/eval/guideline-ratings";
export type { GuidelineRating } from "@chartcoach/eval-ui/eval/guideline-ratings";

let rxCollection: RxCollection<GuidelineRating> | undefined;
if (typeof window !== "undefined") {
  try {
    rxCollection = (await getEvalUiRxDatabase()).guideline_ratings;
  } catch (error) {
    console.warn(
      "[eval-ui] Failed to initialize RxDB guideline ratings collection; falling back to local-only collection.",
      error,
    );
    rxCollection = undefined;
  }
}

export const guidelineRatingsCollection = createCollection(
  rxCollection
    ? rxdbCollectionOptions({
        rxCollection,
        startSync: true,
        schema: GuidelineRatingSchema,
      })
    : localOnlyCollectionOptions({
        getKey: (rating) => rating.id,
        schema: GuidelineRatingSchema,
      }),
);

export function clearGuidelineRatings() {
  for (const id of guidelineRatingsCollection.state.keys()) {
    guidelineRatingsCollection.delete(id);
  }
}

export function makeGuidelineRatingId(scenarioId: string, guidelineId: string) {
  return `${scenarioId}::${guidelineId}`;
}

export function upsertGuidelineRating({
  scenarioId,
  guidelineId,
  patch,
  now = new Date().toISOString(),
}: {
  scenarioId: string;
  guidelineId: string;
  patch: Partial<Omit<GuidelineRating, "id" | "scenarioId" | "guidelineId" | "createdAt" | "updatedAt">>;
  now?: string;
}) {
  const id = makeGuidelineRatingId(scenarioId, guidelineId);

  if (guidelineRatingsCollection.state.has(id)) {
    guidelineRatingsCollection.update(id, (draft) => {
      for (const [key, value] of Object.entries(patch)) {
        if (value === undefined) {
          if (key === "bucket") continue;
          // Remove optional fields cleanly (avoids storing invalid `undefined` values in RxDB).
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

  if (!patch.bucket) {
    throw new Error("Cannot insert guideline rating without a bucket.");
  }

  const insert: GuidelineRating = {
    id,
    scenarioId,
    guidelineId,
    bucket: patch.bucket,
    createdAt: now,
    updatedAt: now,
    ...(patch.actionability === undefined ? {} : { actionability: patch.actionability }),
    ...(patch.impact === undefined ? {} : { impact: patch.impact }),
    ...(patch.risk === undefined ? {} : { risk: patch.risk }),
    ...(patch.credibility === undefined ? {} : { credibility: patch.credibility }),
    ...(patch.notes === undefined ? {} : { notes: patch.notes }),
  };

  guidelineRatingsCollection.insert(insert);
}

export function deleteGuidelineRating({
  scenarioId,
  guidelineId,
}: {
  scenarioId: string;
  guidelineId: string;
}) {
  const id = makeGuidelineRatingId(scenarioId, guidelineId);
  if (guidelineRatingsCollection.state.has(id)) {
    guidelineRatingsCollection.delete(id);
  }
}

export function mergeGuidelineRatings(ratings: GuidelineRating[]) {
  const optionalKeys: Array<keyof GuidelineRating> = [
    "actionability",
    "impact",
    "risk",
    "credibility",
    "notes",
  ];

  for (const rating of ratings) {
    const existing = guidelineRatingsCollection.state.get(rating.id);

    if (!existing) {
      guidelineRatingsCollection.insert(rating);
      continue;
    }

    if (existing.updatedAt >= rating.updatedAt) continue;

    guidelineRatingsCollection.update(rating.id, (draft) => {
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
