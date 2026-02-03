import type { ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";
import { downloadJsonFile } from "@chartcoach/eval-ui/lib/export-guideline-ratings";

type SetRatingsExportV1 = {
  format: "chartcoach.set-ratings.v1";
  exportedAt: string;
  ratings: ScenarioSetRating[];
};

function normalizeExportFilenameTimestamp(date: Date) {
  return date.toISOString().replaceAll(":", "").replaceAll(".", "-");
}

export function createSetRatingsExport(
  ratings: ScenarioSetRating[],
  exportedAt: Date = new Date(),
): SetRatingsExportV1 {
  const sortedRatings = [...ratings].sort((a, b) => {
    if (a.scenarioId !== b.scenarioId) return a.scenarioId.localeCompare(b.scenarioId);
    if (a.strategyId !== b.strategyId) return a.strategyId.localeCompare(b.strategyId);
    return a.id.localeCompare(b.id);
  });

  return {
    format: "chartcoach.set-ratings.v1",
    exportedAt: exportedAt.toISOString(),
    ratings: sortedRatings,
  };
}

export function serializeSetRatingsExport(payload: SetRatingsExportV1) {
  return JSON.stringify(payload, null, 2);
}

export function downloadSetRatingsExport(
  ratings: ScenarioSetRating[],
  exportedAt: Date = new Date(),
) {
  const payload = createSetRatingsExport(ratings, exportedAt);
  const json = serializeSetRatingsExport(payload);
  const filename = `chartcoach-set-ratings-${normalizeExportFilenameTimestamp(exportedAt)}.json`;
  downloadJsonFile(filename, json);
  return { filename, count: payload.ratings.length };
}
