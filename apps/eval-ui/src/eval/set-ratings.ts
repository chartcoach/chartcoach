import { z } from "zod";

export const ScenarioSetRatingSchema = z.object({
  id: z.string().min(1),
  scenarioId: z.string().min(1),
  strategyId: z.string().min(1),

  // Set-level outcomes (optional to keep evaluation fast).
  sufficiency: z.number().int().min(1).max(5).optional(),
  redundancy: z.number().int().min(1).max(5).optional(),
  coherence: z.number().int().min(1).max(5).optional(),
  harm: z.number().int().min(1).max(5).optional(),
  notes: z.string().optional(),

  createdAt: z.string().min(1),
  updatedAt: z.string().min(1),
});

export type ScenarioSetRating = z.infer<typeof ScenarioSetRatingSchema>;

export const SetRatingsExportV1Schema = z.object({
  format: z.literal("chartcoach.set-ratings.v1"),
  exportedAt: z.string().min(1),
  ratings: z.array(ScenarioSetRatingSchema),
});

export type SetRatingsExportV1 = z.infer<typeof SetRatingsExportV1Schema>;

