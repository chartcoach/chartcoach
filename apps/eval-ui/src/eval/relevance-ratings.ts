import { z } from "zod";

export const RelevanceRatingSchema = z.object({
  id: z.string().min(1),
  scenarioId: z.string().min(1),
  guidelineId: z.string().min(1),
  relevance: z.number().int().min(1).max(5),
  createdAt: z.string().min(1),
  updatedAt: z.string().min(1),
});

export type RelevanceRating = z.infer<typeof RelevanceRatingSchema>;

export const RelevanceRatingsExportV1Schema = z.object({
  format: z.literal("chartcoach.relevance-ratings.v1"),
  exportedAt: z.string().min(1),
  ratings: z.array(RelevanceRatingSchema),
});

export type RelevanceRatingsExportV1 = z.infer<typeof RelevanceRatingsExportV1Schema>;
