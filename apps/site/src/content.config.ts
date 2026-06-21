import { defineCollection } from "astro:content";
import { z } from "astro/zod";

import { guidelinesLoader } from "@/loaders/guidelines-loader";

const guidelineSectionSchema = z.object({
  role: z.string(),
  title: z.string(),
  content: z.string(),
});

const guidelineRecordSchema = z.object({
  id: z.string(),
  title: z.string(),
  bibliography: z.string().optional(),
  description: z.string(),
  labels: z.array(z.string()).default([]),
  body: z.string(),
  sections: z.array(guidelineSectionSchema).default([]),
  references: z.array(z.string()).default([]),
});

export const collections = {
  guidelines: defineCollection({
    loader: guidelinesLoader(),
    schema: z.object({
      id: z.string(),
      title: z.string(),
      description: z.string().optional(),
      labels: z.array(z.string()).default([]),
      markdown: z.string(),
      record: guidelineRecordSchema,
      search: guidelineRecordSchema.extend({
        description: z.string().optional(),
      }),
      sections: z
        .array(
          z.object({
            role: z.string(),
            title: z.string(),
            html: z.string(),
          }),
        )
        .default([]),
      bibliography: z.string().optional(),
      referencesBib: z.string().optional(),
      citations: z.array(z.string()).default([]),
      bibliographyHtml: z.string().optional(),
    }),
  }),
};
