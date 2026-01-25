import { z } from "zod";

export const ScenarioChartSchema = z
  .object({
    uri: z.string().min(1),
    mime: z.string().min(1),
  })
  .partial();

export const ScenarioSpecSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  lang: z.string().min(1).default("en"),
  chart: ScenarioChartSchema.optional(),
  query: z.string().min(1).optional(),
  designer_intent: z.string().min(1).optional(),
  provenance: z
    .object({
      source: z.string().min(1).optional(),
    })
    .optional(),
});

export const ScenariosFileSchema = z.object({
  scenarios: z.array(ScenarioSpecSchema),
});

export type ScenarioSpec = z.infer<typeof ScenarioSpecSchema>;
