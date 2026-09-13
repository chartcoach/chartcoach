import { z } from "zod";

export const resolvedSelectionSchema = z
  .strictObject({
    catalogId: z.string().regex(/^[a-f0-9]{64}$/),
    ids: z.array(z.string()).readonly(),
  })
  .readonly();

export type ResolvedSelection = z.infer<typeof resolvedSelectionSchema>;
