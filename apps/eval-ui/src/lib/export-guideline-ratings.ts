import type { GuidelineRating } from "@chartcoach/eval-ui/db-collections";

type GuidelineRatingsExportV2 = {
  format: "chartcoach.guideline-ratings.v2";
  exportedAt: string;
  ratings: GuidelineRating[];
};

function normalizeExportFilenameTimestamp(date: Date) {
  return date.toISOString().replaceAll(":", "").replaceAll(".", "-");
}

export function createGuidelineRatingsExport(
  ratings: GuidelineRating[],
  exportedAt: Date = new Date(),
): GuidelineRatingsExportV2 {
  const sortedRatings = [...ratings].sort((a, b) => {
    if (a.scenarioId !== b.scenarioId) return a.scenarioId.localeCompare(b.scenarioId);
    if (a.guidelineId !== b.guidelineId) return a.guidelineId.localeCompare(b.guidelineId);
    return a.id.localeCompare(b.id);
  });

  return {
    format: "chartcoach.guideline-ratings.v2",
    exportedAt: exportedAt.toISOString(),
    ratings: sortedRatings,
  };
}

export function serializeGuidelineRatingsExport(payload: GuidelineRatingsExportV2) {
  return JSON.stringify(payload, null, 2);
}

export function downloadJsonFile(filename: string, json: string) {
  const blob = new Blob([json], { type: "application/json;charset=utf-8" });
  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.rel = "noreferrer";

  document.body.appendChild(link);
  link.click();
  link.remove();

  URL.revokeObjectURL(url);
}

export function downloadGuidelineRatingsExport(
  ratings: GuidelineRating[],
  exportedAt: Date = new Date(),
) {
  const payload = createGuidelineRatingsExport(ratings, exportedAt);
  const json = serializeGuidelineRatingsExport(payload);
  const filename = `chartcoach-guideline-ratings-${normalizeExportFilenameTimestamp(exportedAt)}.json`;
  downloadJsonFile(filename, json);
  return { filename, count: payload.ratings.length };
}

