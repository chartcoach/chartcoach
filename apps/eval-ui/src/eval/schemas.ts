import { z } from "zod";

import type { CatalogEntry } from "@chartcoach/catalog";

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
  audience: z.string().min(1).optional(),
  medium: z.string().min(1).optional(),
  constraints: z.string().min(1).optional(),
  domain: z.string().min(1).optional(),
  risk_tolerance: z.string().min(1).optional(),
  time_budget: z.string().min(1).optional(),
  counterfactual_group_id: z.string().min(1).optional(),
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

export type EvidenceSnippet = {
  role?: string;
  text: string;
  score?: number;
};

export type EvalGuidelineResult = {
  rank: number;
  score: number;
  entry: CatalogEntry;
  evidence?: EvidenceSnippet[];
};

export type EvalStrategyResult = {
  strategyId: string;
  strategyName: string;
  guidelines: EvalGuidelineResult[];
};

export type EvalScenarioBundle = {
  scenario: ScenarioSpec;
  strategies: EvalStrategyResult[];
};
