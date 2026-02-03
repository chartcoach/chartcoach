import { z } from "zod";

import {
  isCatalogEntryWire,
  type CatalogEntryWire,
} from "@chartcoach/catalog";
import { ScenarioSpecSchema } from "@chartcoach/eval-ui/eval/schemas";

export const StrategyInfoSchema = z.object({
  id: z.string().min(1),
  name: z.string().min(1),
  description: z.string().optional().default(""),
});

export const ArtifactsIndexSchema = z.looseObject({
  schema_version: z.literal(1),
  generated_at: z.string().min(1).optional(),
  strategies: z.array(StrategyInfoSchema).optional(),
  scenarios: z.array(ScenarioSpecSchema),
});

const CatalogEntryWireSchema = z
  .unknown()
  .refine(isCatalogEntryWire, { message: "Invalid catalog entry wire format." })
  .transform((value) => value as CatalogEntryWire);

const EvidenceSnippetSchema = z.object({
  role: z.string().min(1).nullish(),
  text: z.string().min(1),
  score: z.number().nullish(),
});

const GuidelineResultSchema = z.object({
  rank: z.number().int().positive(),
  score: z.number(),
  entry: CatalogEntryWireSchema,
  evidence: z.array(EvidenceSnippetSchema).nullish(),
});

const StrategyResultSchema = z.object({
  strategy_id: z.string().min(1),
  strategy_name: z.string().min(1),
  meta: z.record(z.string(), z.unknown()).optional().default({}),
  guidelines: z.array(GuidelineResultSchema).default([]),
});

export const ScenarioBundleArtifactSchema = z.looseObject({
  schema_version: z.literal(1),
  scenario: ScenarioSpecSchema,
  strategies: z.array(StrategyResultSchema),
});

