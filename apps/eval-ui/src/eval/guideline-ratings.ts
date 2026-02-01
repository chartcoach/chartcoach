import { z } from "zod";

export const GuidelineRatingBucketSchema = z.enum([
  "hard_constraint",
  "soft_constraint",
  "not_useful",
  "not_applicable",
]);

export type GuidelineRatingBucket = z.infer<typeof GuidelineRatingBucketSchema>;

export const GuidelineRatingSchema = z.object({
  id: z.string().min(1),
  scenarioId: z.string().min(1),
  guidelineId: z.string().min(1),

  // Primary label for progress/analysis (fast to apply, can be bucketed later).
  bucket: GuidelineRatingBucketSchema,

  // Optional dimensions for richer analysis (keep optional to preserve rating speed).
  actionability: z.number().int().min(1).max(5).optional(),
  impact: z.number().int().min(1).max(5).optional(),
  risk: z.number().int().min(1).max(5).optional(),
  credibility: z.number().int().min(1).max(5).optional(),
  notes: z.string().optional(),

  createdAt: z.string().min(1),
  updatedAt: z.string().min(1),
});

export type GuidelineRating = z.infer<typeof GuidelineRatingSchema>;

export const GuidelineRatingsExportV2Schema = z.object({
  format: z.literal("chartcoach.guideline-ratings.v2"),
  exportedAt: z.string().min(1),
  ratings: z.array(GuidelineRatingSchema),
});

export type GuidelineRatingsExportV2 = z.infer<typeof GuidelineRatingsExportV2Schema>;

