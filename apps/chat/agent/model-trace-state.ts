import { defineState } from "eve/context";
import { z } from "zod";

export const modelTraceSchema = z.object({
  modelConnectionId: z.string(),
  modelConnectionName: z.string(),
  modelProvider: z.string(),
  modelName: z.string(),
  modelEndpointOrigin: z.string().optional(),
  modelContextWindow: z.number(),
  modelManaged: z.boolean(),
});

type ResolvedModelTrace = {
  sessionId: string;
  turnId: string;
  metadata: z.infer<typeof modelTraceSchema>;
};

// Eve shares named state through its active session context, including across
// independently bundled model and instrumentation entries.
export const resolvedModelTrace = defineState(
  "chartcoach.resolved-model-trace",
  (): ResolvedModelTrace | null => null,
);
