import { defineCollection, z } from "astro:content";
import { docsLoader } from "@astrojs/starlight/loaders";
import { docsSchema } from "@astrojs/starlight/schema";

import { guidelinesLoader } from "@chartcoach/site/loaders/guidelines-loader";

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
  guidelines: defineCollection({
    loader: guidelinesLoader(),
    schema: z.object({
      id: z.string(),
      title: z.string(),
      description: z.string().optional(),
      labels: z.array(z.string()).default([]),
      bibliography: z.string().optional(),
      referencesBib: z.string().optional(),
      citations: z.array(z.string()).default([]),
      bibliographyHtml: z.string().optional(),
    }),
  }),
};
