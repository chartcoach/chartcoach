import { z } from "zod";

import { GuidelineRatingsExportV2Schema } from "@chartcoach/eval-ui/eval/guideline-ratings";
import { SetRatingsExportV1Schema } from "@chartcoach/eval-ui/eval/set-ratings";

export const EvalDataExportV1Schema = z.object({
  format: z.literal("chartcoach.eval-data.v1"),
  exportedAt: z.string().min(1),
  guidelineRatings: GuidelineRatingsExportV2Schema,
  setRatings: SetRatingsExportV1Schema,
});

export type EvalDataExportV1 = z.infer<typeof EvalDataExportV1Schema>;

