import type { GuidelineRating, ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";

export {
  getLocalStorageItem,
  removeLocalStorageItem,
  setLocalStorageItem,
} from "@chartcoach/eval-ui/eval/sync/sync-utils";

import { makeRowsSignature } from "@chartcoach/eval-ui/eval/sync/sync-utils";

export const SYNC_LAST_SIGNATURE_STORAGE_KEY =
  "chartcoach/eval-ui/sync/eval-data/v1:last-signature";
export const SYNC_LAST_SUCCESS_AT_STORAGE_KEY =
  "chartcoach/eval-ui/sync/eval-data/v1:last-success-at";
export const SYNC_LAST_SUCCESS_KEY_STORAGE_KEY =
  "chartcoach/eval-ui/sync/eval-data/v1:last-success-key";

export function makeEvalDataSignature({
  guidelineRatings,
  setRatings,
}: {
  guidelineRatings: GuidelineRating[];
  setRatings: ScenarioSetRating[];
}) {
  const guidelineRows = [...guidelineRatings]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map((r) => [
      "guideline",
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

  const setRows = [...setRatings]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map((r) => [
      "set",
      r.id,
      r.scenarioId,
      r.strategyId,
      r.sufficiency ?? null,
      r.redundancy ?? null,
      r.coherence ?? null,
      r.harm ?? null,
      r.notes ?? null,
      r.createdAt,
      r.updatedAt,
    ]);

  const rows = [...guidelineRows, ...setRows].sort((a, b) => {
    const typeCompare = String(a[0]).localeCompare(String(b[0]));
    if (typeCompare !== 0) return typeCompare;
    return String(a[1]).localeCompare(String(b[1]));
  });

  return makeRowsSignature(rows);
}
