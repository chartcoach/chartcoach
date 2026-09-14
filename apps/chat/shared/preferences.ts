import { z } from "zod";
import { modelFields, apiKeySchema } from "./model";
import { catalogFiltersSchema } from "./catalog-filters";
import { catalogSelectionSchema } from "./catalog-selection";

export const ownerSchema = z.string().regex(/^[a-f0-9]{64}$/);

export const modelSelectionSchema = z.object({
  owner: ownerSchema,
  threadId: z.uuid(),
  connectionId: z.string().min(1).max(80),
});

export const connectionInputSchema = z.strictObject({
  id: z.uuid().optional(),
  ...modelFields,
  name: z.string().trim().min(1).max(80),
  apiKey: apiKeySchema.optional(),
});

export type ConnectionInput = z.infer<typeof connectionInputSchema>;

export const connectionSchema = connectionInputSchema.omit({ apiKey: true }).extend({
  id: z.string(),
  managed: z.boolean(),
});

export type Connection = z.infer<typeof connectionSchema>;

export const preferencesSchema = z.object({
  connections: z.array(connectionSchema),
  allowedOrigins: z.array(z.string()),
  tracing: z.boolean(),
});

export const modelSchema = z.object({ id: z.string(), name: z.string() });

export type ModelChoice = z.infer<typeof modelSchema>;

const savedSelectionSchema = z.object({
  filters: catalogFiltersSchema,
  selection: catalogSelectionSchema,
  matchedGuidelines: z.number().int().nonnegative(),
});

export const threadInputSchema = z.strictObject({
  title: z.string().trim().min(1).max(160),
  connectionId: z.string().min(1).max(80),
  knowledge: savedSelectionSchema,
});

export const threadSchema = z.object({
  id: z.uuid(),
  title: z.string(),
  connectionId: z.string(),
  sessionId: z.string().nullable(),
  updatedAt: z.number(),
  archived: z.boolean(),
});

export type SavedThread = z.infer<typeof threadSchema>;

export const threadDetailSchema = threadSchema.extend({ knowledge: savedSelectionSchema });

export type ThreadDetail = z.infer<typeof threadDetailSchema>;
