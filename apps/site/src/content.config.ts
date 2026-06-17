import { defineCollection } from "astro:content";
import { z } from "astro/zod";

import { guidelinesLoader } from "@/loaders/guidelines-loader";

export const collections = {
  guidelines: defineCollection({
    loader: guidelinesLoader(),
    schema: z.object({
      id: z.string(),
      title: z.string(),
      description: z.string().optional(),
      labels: z.array(z.string()).default([]),
      markdown: z.string(),
      search: z.object({
        id: z.string(),
        title: z.string(),
        description: z.string().optional(),
        labels: z.array(z.string()).default([]),
        body: z.string(),
        sections: z
          .array(
            z.object({
              role: z.string(),
              title: z.string(),
              content: z.string(),
            }),
          )
          .default([]),
        bibliography: z.string().optional(),
        references: z.array(z.string()).default([]),
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
