import { z } from "zod";
import { catalogFiltersSchema } from "./catalog-filters";
import { catalogSelectionSchema } from "./catalog-selection";

export const providerSchema = z.enum(["anthropic", "openai", "google", "compatible"]);
export type Provider = z.infer<typeof providerSchema>;
export const ownerSchema = z.string().regex(/^[a-f0-9]{64}$/);
export const modelSelectionSchema = z.object({
  owner: ownerSchema,
  threadId: z.uuid(),
  connectionId: z.string().min(1).max(80),
});
export const providerNames: Record<Provider, string> = {
  anthropic: "Anthropic",
  openai: "OpenAI",
  google: "Gemini",
  compatible: "OpenAI compatible",
};
export const connectionInputSchema = z.strictObject({
  id: z.uuid().optional(),
  provider: providerSchema,
  name: z.string().trim().min(1).max(80),
  baseURL: z.url().optional(),
  model: z.string().trim().min(1).max(200),
  contextWindow: z.number().int().min(4096).max(2_000_000).default(128_000),
  apiKey: z
    .string()
    .trim()
    .min(1)
    .max(4096)
    .regex(/^[\x21-\x7e]+$/)
    .optional(),
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
