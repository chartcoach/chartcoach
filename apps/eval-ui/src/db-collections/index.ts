import { createCollection, localOnlyCollectionOptions } from "@tanstack/react-db";
import { rxdbCollectionOptions } from "@tanstack/rxdb-db-collection";
import type { RxCollection } from "rxdb";

import { getEvalUiRxDatabase } from "@chartcoach/eval-ui/db/rxdb";
import {
  RelevanceRatingSchema,
  type RelevanceRating,
} from "@chartcoach/eval-ui/eval/relevance-ratings";
export type { RelevanceRating } from "@chartcoach/eval-ui/eval/relevance-ratings";

let rxCollection: RxCollection<RelevanceRating> | undefined;
if (typeof window !== "undefined") {
  try {
    rxCollection = (await getEvalUiRxDatabase()).relevance_ratings;
  } catch (error) {
    console.warn(
      "[eval-ui] Failed to initialize RxDB relevance ratings collection; falling back to local-only collection.",
      error,
    );
    rxCollection = undefined;
  }
}

export const relevanceRatingsCollection = createCollection(
  rxCollection
    ? rxdbCollectionOptions({
        rxCollection,
        startSync: true,
        schema: RelevanceRatingSchema,
      })
    : localOnlyCollectionOptions({
        getKey: (rating) => rating.id,
        schema: RelevanceRatingSchema,
      }),
);

export function clearRelevanceRatings() {
  for (const id of relevanceRatingsCollection.state.keys()) {
    relevanceRatingsCollection.delete(id);
  }
}

export function makeRelevanceRatingId(scenarioId: string, guidelineId: string) {
  return `${scenarioId}::${guidelineId}`;
}

export function upsertRelevanceRating({
  scenarioId,
  guidelineId,
  relevance,
  now = new Date().toISOString(),
}: {
  scenarioId: string;
  guidelineId: string;
  relevance: number;
  now?: string;
}) {
  const id = makeRelevanceRatingId(scenarioId, guidelineId);

  if (relevanceRatingsCollection.state.has(id)) {
    relevanceRatingsCollection.update(id, (draft) => {
      draft.relevance = relevance;
      draft.updatedAt = now;
    });
    return;
  }

  relevanceRatingsCollection.insert({
    id,
    scenarioId,
    guidelineId,
    relevance,
    createdAt: now,
    updatedAt: now,
  });
}

export function deleteRelevanceRating({
  scenarioId,
  guidelineId,
}: {
  scenarioId: string;
  guidelineId: string;
}) {
  const id = makeRelevanceRatingId(scenarioId, guidelineId);
  if (relevanceRatingsCollection.state.has(id)) {
    relevanceRatingsCollection.delete(id);
  }
}

export function mergeRelevanceRatings(ratings: RelevanceRating[]) {
  for (const rating of ratings) {
    const existing = relevanceRatingsCollection.state.get(rating.id);

    if (!existing) {
      relevanceRatingsCollection.insert(rating);
      continue;
    }

    if (existing.updatedAt >= rating.updatedAt) continue;

    relevanceRatingsCollection.update(rating.id, (draft) => {
      Object.assign(draft, rating);
    });
  }
}
