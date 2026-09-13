import { z } from "zod";

export const guidelinePageSchema = z.object({
  id: z.string(),
  title: z.string(),
  description: z.string(),
  sections: z.array(z.object({ title: z.string(), content: z.string() })),
  sources: z.array(
    z.object({ reference_id: z.string(), citation: z.string(), url: z.string().nullable() }),
  ),
  release: z.string().nullable(),
});

export function localGuidelineURL(id: string) {
  return `/guideline?id=${encodeURIComponent(id)}`;
}
