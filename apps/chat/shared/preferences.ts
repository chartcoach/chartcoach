import { guidelineLinksSchema } from "./guideline-links";
import { z } from "zod";
import { modelFields, apiKeySchema } from "./model";
import { threadIdSchema } from "./threads";

export const ownerSchema = z.string().regex(/^[a-f0-9]{64}$/);

export const modelSelectionSchema = z.object({
  owner: ownerSchema,
  threadId: threadIdSchema,
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
  guidelines: guidelineLinksSchema,
});

export const modelSchema = z.object({ id: z.string(), name: z.string() });

export type ModelChoice = z.infer<typeof modelSchema>;
