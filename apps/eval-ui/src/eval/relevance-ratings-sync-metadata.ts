import type { RelevanceRating } from "@chartcoach/eval-ui/eval/relevance-ratings";

export const SYNC_LAST_SIGNATURE_STORAGE_KEY =
  "chartcoach/eval-ui/sync/relevance-ratings/v1:last-signature";
export const SYNC_LAST_SUCCESS_AT_STORAGE_KEY =
  "chartcoach/eval-ui/sync/relevance-ratings/v1:last-success-at";
export const SYNC_LAST_SUCCESS_KEY_STORAGE_KEY =
  "chartcoach/eval-ui/sync/relevance-ratings/v1:last-success-key";

export function getLocalStorageItem(key: string) {
  if (typeof window === "undefined") return null;
  try {
    return window.localStorage.getItem(key);
  } catch {
    return null;
  }
}

export function setLocalStorageItem(key: string, value: string) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(key, value);
  } catch {
    // ignore quota / privacy errors
  }
}

export function makeRatingsSignature(ratings: RelevanceRating[]) {
  const rows = [...ratings]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map((r) => [r.id, r.scenarioId, r.guidelineId, r.relevance, r.createdAt, r.updatedAt]);
  return JSON.stringify(rows);
}
