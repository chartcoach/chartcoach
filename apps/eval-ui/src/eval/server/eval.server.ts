import { GetObjectCommand } from "@aws-sdk/client-s3";
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

import {
  indexGuidelineSections,
  parseGuidelineSections,
  type CatalogEntry,
} from "@chartcoach/catalog";
import { env } from "@chartcoach/eval-ui/env";
import { ScenarioSpecSchema, type ScenarioSpec } from "@chartcoach/eval-ui/eval/schemas";
import type { EvalScenarioBundle, EvalStrategyResult } from "@chartcoach/eval-ui/eval/types";
import {
  getS3Client,
  isS3Configured,
  normalizePrefix,
  readObjectBody,
  sendS3,
} from "@chartcoach/eval-ui/eval/server/s3.server";

const StrategyInfoSchema = z.object({
  id: z.string().min(1),
  name: z.string().min(1),
  description: z.string().optional().default(""),
});

const ArtifactsIndexSchema = z.looseObject({
  schema_version: z.literal(1),
  generated_at: z.string().min(1).optional(),
  strategies: z.array(StrategyInfoSchema).optional(),
  scenarios: z.array(ScenarioSpecSchema),
});

const GuidelineResultSchema = z.object({
  rank: z.number().int().positive(),
  score: z.number(),
  entry: z.unknown(),
});

const StrategyResultSchema = z.object({
  strategy_id: z.string().min(1),
  strategy_name: z.string().min(1),
  meta: z.record(z.string(), z.unknown()).optional().default({}),
  guidelines: z.array(GuidelineResultSchema).default([]),
});

const ScenarioBundleArtifactSchema = z.looseObject({
  schema_version: z.literal(1),
  scenario: ScenarioSpecSchema,
  strategies: z.array(StrategyResultSchema),
});

const ScenarioBundleInputSchema = z.object({
  scenarioId: z.string().min(1),
});

function requireS3() {
  if (!isS3Configured()) {
    throw new Error(
      "S3 is not configured. Set S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, and S3_BUCKET.",
    );
  }
  if (!env.S3_BUCKET) {
    throw new Error("S3 is not configured. Set S3_BUCKET.");
  }
  return env.S3_BUCKET;
}

function artifactsBaseKey() {
  const prefix = normalizePrefix(env.S3_PREFIX);
  return `${prefix}eval-artifacts/${env.EVAL_ARTIFACTS_VERSION}/`;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

function catalogEntryFromWire(row: unknown): CatalogEntry | null {
  if (!isRecord(row)) return null;

  const id = row.id;
  const guideline = row.guideline;
  const references = row.references;

  if (typeof id !== "string" || !isRecord(guideline)) return null;

  const entry: CatalogEntry = {
    guideline: {
      id,
      title: typeof guideline.title === "string" ? guideline.title : id,
      bibliography: typeof guideline.bibliography === "string" ? guideline.bibliography : undefined,
      description: typeof guideline.description === "string" ? guideline.description : "",
      labels: Array.isArray(guideline.labels)
        ? guideline.labels.filter((l): l is string => typeof l === "string")
        : [],
      body: typeof guideline.body === "string" ? guideline.body : "",
      sections: [],
      sectionsIndex: { byRole: {} },
    },
    references: Array.isArray(references)
      ? references.filter((r): r is string => typeof r === "string")
      : [],
  };

  entry.guideline.sections = parseGuidelineSections(entry.guideline.body);
  entry.guideline.sectionsIndex = indexGuidelineSections(entry.guideline.sections);
  return entry;
}

async function fetchArtifactJson(key: string) {
  const cmd = new GetObjectCommand({
    Bucket: requireS3(),
    Key: key,
  });

  const response = await sendS3((forcePathStyle) => getS3Client({ forcePathStyle }).send(cmd));
  const raw = await readObjectBody(response.Body);
  return JSON.parse(raw) as unknown;
}

export const getEvalScenarios = createServerFn({ method: "GET" }).handler(
  async (): Promise<ScenarioSpec[]> => {
    const key = `${artifactsBaseKey()}index.json`;
    const doc = await fetchArtifactJson(key);
    const parsed = ArtifactsIndexSchema.parse(doc);
    return parsed.scenarios;
  },
);

export const getEvalScenarioBundle = createServerFn({ method: "POST" })
  .inputValidator((input) => ScenarioBundleInputSchema.parse(input))
  .handler(async ({ data }): Promise<EvalScenarioBundle> => {
    const key = `${artifactsBaseKey()}bundles/${encodeURIComponent(data.scenarioId)}.json`;
    const doc = await fetchArtifactJson(key);
    const parsed = ScenarioBundleArtifactSchema.parse(doc);

    const strategies: EvalStrategyResult[] = parsed.strategies.map((strategy) => {
      const guidelines = strategy.guidelines
        .map((g) => {
          const entry = catalogEntryFromWire(g.entry);
          if (!entry) return null;
          return { rank: g.rank, score: g.score, entry };
        })
        .filter((g): g is NonNullable<typeof g> => Boolean(g));

      return {
        strategyId: strategy.strategy_id,
        strategyName: strategy.strategy_name,
        guidelines,
      };
    });

    return { scenario: parsed.scenario, strategies };
  });
