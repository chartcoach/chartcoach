import { z } from "zod";

import type { CatalogEntry } from "@chartcoach/catalog";

export const ScenarioChartSchema = z
  .object({
    uri: z.string().min(1).nullish(),
    mime: z.string().min(1).nullish(),
  })
  .partial();

export const ScenarioSpecSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  lang: z.string().min(1).default("en"),
  chart: ScenarioChartSchema.nullish(),
  query: z.string().min(1).nullish(),
  designer_intent: z.string().min(1).nullish(),
  audience: z.string().min(1).nullish(),
  medium: z.string().min(1).nullish(),
  constraints: z.string().min(1).nullish(),
  domain: z.string().min(1).nullish(),
  risk_tolerance: z.string().min(1).nullish(),
  time_budget: z.string().min(1).nullish(),
  counterfactual_group_id: z.string().min(1).nullish(),
  negative_guideline_ids: z.array(z.string().min(1)).nullish(),
  provenance: z
    .object({
      source: z.string().min(1).nullish(),
    })
    .nullish(),
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
