import { createCollection, localOnlyCollectionOptions } from "@tanstack/react-db";
import { rxdbCollectionOptions } from "@tanstack/rxdb-db-collection";
import type { RxCollection } from "rxdb";

import { getEvalUiRxDatabase } from "@chartcoach/eval-ui/db/rxdb";
import {
  RelevanceRatingSchema,
  type RelevanceRating,
} from "@chartcoach/eval-ui/eval/relevance-ratings";
export type { RelevanceRating } from "@chartcoach/eval-ui/eval/relevance-ratings";

const LEGACY_RATINGS_STORAGE_KEY = "chartcoach/eval-ui/relevance-ratings/v1";
const LEGACY_MIGRATION_DONE_KEY = "chartcoach/eval-ui/relevance-ratings/v1:migrated-to-rxdb";

let rxCollection: RxCollection<RelevanceRating> | undefined;
if (typeof window !== "undefined") {
  try {
    rxCollection = (await getEvalUiRxDatabase()).relevance_ratings;
  } catch {
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

async function migrateLegacyRelevanceRatings() {
  if (!rxCollection || typeof window === "undefined") return;

  try {
    if (window.localStorage.getItem(LEGACY_MIGRATION_DONE_KEY)) return;

    const raw = window.localStorage.getItem(LEGACY_RATINGS_STORAGE_KEY);
    if (!raw) {
      window.localStorage.setItem(LEGACY_MIGRATION_DONE_KEY, "1");
      return;
    }

    const parsed: unknown = JSON.parse(raw);
    if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
      return;
    }

    let migratedCount = 0;

    for (const value of Object.values(parsed)) {
      if (!value || typeof value !== "object") continue;
      if (!("data" in value)) continue;

      const maybeRating = (value as { data?: unknown }).data;
      const parsedRating = RelevanceRatingSchema.safeParse(maybeRating);
      if (!parsedRating.success) continue;

      const rating = parsedRating.data;
      if (relevanceRatingsCollection.state.has(rating.id)) {
        relevanceRatingsCollection.update(rating.id, (draft) => {
          Object.assign(draft, rating);
        });
      } else {
        relevanceRatingsCollection.insert(rating);
      }
      migratedCount++;
    }

    if (migratedCount > 0) {
      window.localStorage.removeItem(LEGACY_RATINGS_STORAGE_KEY);
    }
    window.localStorage.setItem(LEGACY_MIGRATION_DONE_KEY, "1");
  } catch {
    // ignore parse / privacy errors
  }
}

await migrateLegacyRelevanceRatings();

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
