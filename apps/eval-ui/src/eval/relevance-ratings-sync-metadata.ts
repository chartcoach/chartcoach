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

const FNV_OFFSET_BASIS_64 = 14695981039346656037n;
const FNV_PRIME_64 = 1099511628211n;
const FNV_MASK_64 = 0xffff_ffff_ffff_ffffn;

function fnv1a64Hex(input: string) {
  let hash = FNV_OFFSET_BASIS_64;
  for (let i = 0; i < input.length; i++) {
    hash ^= BigInt(input.charCodeAt(i));
    hash = (hash * FNV_PRIME_64) & FNV_MASK_64;
  }
  return hash.toString(16).padStart(16, "0");
}

export function makeRatingsSignature(ratings: RelevanceRating[]) {
  const rows = [...ratings]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map((r) => [r.id, r.scenarioId, r.guidelineId, r.relevance, r.createdAt, r.updatedAt]);
  const raw = JSON.stringify(rows);
  const digest = fnv1a64Hex(raw);
  return `fnv1a64:${digest}:${rows.length}`;
}
