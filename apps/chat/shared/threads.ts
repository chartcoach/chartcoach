import { z } from "zod";
import { catalogFiltersSchema } from "./catalog-filters";
import { catalogSelectionSchema } from "./catalog-selection";

export const threadIdSchema = z.uuid();

const guidelineSelectionSchema = z.object({
  filters: catalogFiltersSchema,
  selection: catalogSelectionSchema,
  matchedGuidelines: z.number().int().nonnegative(),
});

export const threadInputSchema = z.strictObject({
  title: z.string().trim().min(1).max(160),
  connectionId: z.string().min(1).max(80),
  guidelines: guidelineSelectionSchema,
});

export type ThreadInput = z.infer<typeof threadInputSchema>;

export const threadUpdateSchema = z.strictObject({
  title: z.string().trim().min(1).max(160).optional(),
  archived: z.boolean().optional(),
});

export type ThreadUpdate = z.infer<typeof threadUpdateSchema>;

export const threadSchema = z.object({
  id: threadIdSchema,
  title: z.string(),
  connectionId: z.string(),
  sessionId: z.string().nullable(),
  createdAt: z.number().int().nonnegative(),
  updatedAt: z.number().int().nonnegative(),
  archived: z.boolean(),
});

export type SavedThread = z.infer<typeof threadSchema>;

export const threadDetailSchema = threadSchema.extend({ guidelines: guidelineSelectionSchema });

export type ThreadDetail = z.infer<typeof threadDetailSchema>;
