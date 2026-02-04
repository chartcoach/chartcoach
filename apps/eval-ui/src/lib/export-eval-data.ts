import type { GuidelineRating, ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";
import type { EvalDataExportV1 } from "@chartcoach/eval-ui/eval/eval-data";
import { createGuidelineRatingsExport } from "@chartcoach/eval-ui/lib/export-guideline-ratings";
import { createSetRatingsExport } from "@chartcoach/eval-ui/lib/export-set-ratings";
import { downloadJsonFile } from "@chartcoach/eval-ui/lib/export-guideline-ratings";

function normalizeExportFilenameTimestamp(date: Date) {
  return date.toISOString().replaceAll(":", "").replaceAll(".", "-");
}

export function createEvalDataExport(
  guidelineRatings: GuidelineRating[],
  setRatings: ScenarioSetRating[],
  exportedAt: Date = new Date(),
): EvalDataExportV1 {
  const guidelinePayload = createGuidelineRatingsExport(guidelineRatings, exportedAt);
  const setPayload = createSetRatingsExport(setRatings, exportedAt);

  return {
    format: "chartcoach.eval-data.v1",
    exportedAt: exportedAt.toISOString(),
    guidelineRatings: guidelinePayload,
    setRatings: setPayload,
  };
}

export function serializeEvalDataExport(payload: EvalDataExportV1) {
  return JSON.stringify(payload, null, 2);
}

export function downloadEvalDataExport(
  guidelineRatings: GuidelineRating[],
  setRatings: ScenarioSetRating[],
  exportedAt: Date = new Date(),
) {
  const payload = createEvalDataExport(guidelineRatings, setRatings, exportedAt);
  const json = serializeEvalDataExport(payload);
  const filename = `chartcoach-eval-data-${normalizeExportFilenameTimestamp(exportedAt)}.json`;
  downloadJsonFile(filename, json);
  return {
    filename,
    guidelineCount: payload.guidelineRatings.ratings.length,
    setCount: payload.setRatings.ratings.length,
  };
}

