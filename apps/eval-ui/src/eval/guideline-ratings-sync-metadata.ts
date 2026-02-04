import type { GuidelineRating } from "@chartcoach/eval-ui/eval/guideline-ratings";

export {
  getLocalStorageItem,
  setLocalStorageItem,
} from "@chartcoach/eval-ui/eval/sync/sync-utils";

import { makeRowsSignature } from "@chartcoach/eval-ui/eval/sync/sync-utils";

export const SYNC_LAST_SIGNATURE_STORAGE_KEY =
  "chartcoach/eval-ui/sync/guideline-ratings/v2:last-signature";
export const SYNC_LAST_SUCCESS_AT_STORAGE_KEY =
  "chartcoach/eval-ui/sync/guideline-ratings/v2:last-success-at";
export const SYNC_LAST_SUCCESS_KEY_STORAGE_KEY =
  "chartcoach/eval-ui/sync/guideline-ratings/v2:last-success-key";

export function makeRatingsSignature(ratings: GuidelineRating[]) {
  const rows = [...ratings]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map((r) => [
      r.id,
      r.scenarioId,
      r.guidelineId,
      r.bucket,
      r.actionability ?? null,
      r.impact ?? null,
      r.risk ?? null,
      r.credibility ?? null,
      r.notes ?? null,
      r.createdAt,
      r.updatedAt,
    ]);
  return makeRowsSignature(rows);
}
