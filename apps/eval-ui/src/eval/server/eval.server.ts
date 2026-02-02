import { GetObjectCommand } from "@aws-sdk/client-s3";
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  isCatalogEntryWire,
  requireCatalogEntryFromWire,
  type CatalogEntryWire,
} from "@chartcoach/catalog";
import { env } from "@chartcoach/eval-ui/env";
import {
  ScenarioSpecSchema,
  type EvalScenarioBundle,
  type EvalStrategyResult,
  type ScenarioSpec,
} from "@chartcoach/eval-ui/eval/schemas";
import {
  getS3Client,
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

const CatalogEntryWireSchema = z
  .unknown()
  .refine(isCatalogEntryWire, { message: "Invalid catalog entry wire format." })
  .transform((value) => value as CatalogEntryWire);

const EvidenceSnippetSchema = z.object({
  role: z.string().min(1).optional(),
  text: z.string().min(1),
  score: z.number().optional(),
});

const GuidelineResultSchema = z.object({
  rank: z.number().int().positive(),
  score: z.number(),
  entry: CatalogEntryWireSchema,
  evidence: z.array(EvidenceSnippetSchema).optional(),
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

const ScenarioIdSchema = z
  .string()
  .min(1)
  .regex(/^[a-z0-9][a-z0-9-]*$/i, {
    message: "Invalid scenario id.",
  });

const ScenarioBundleInputSchema = z.object({
  scenarioId: ScenarioIdSchema,
});

type ArtifactsRoot =
  | { kind: "s3"; bucket: string; keyPrefix: string }
  | { kind: "url"; baseUrl: URL };

let cachedArtifactsRoot: ArtifactsRoot | undefined;

function ensureTrailingSlash(value: string) {
  return value.endsWith("/") ? value : `${value}/`;
}

function defaultFixtureArtifactsBaseUrl() {
  const candidates = [
    path.resolve(process.cwd(), "apps/eval-ui/fixtures/eval-artifacts/v1"),
    path.resolve(process.cwd(), "fixtures/eval-artifacts/v1"),
    fileURLToPath(new URL("../../../fixtures/eval-artifacts/v1/", import.meta.url)),
  ];

  for (const candidate of candidates) {
    if (existsSync(path.join(candidate, "index.json"))) {
      return pathToFileURL(ensureTrailingSlash(candidate));
    }
  }

  throw new Error(
    "No eval artifacts configured. Set EVAL_ARTIFACTS_URL (file://, https://, or s3://).",
  );
}

function parseArtifactsRoot(value: string): ArtifactsRoot {
  const raw = value.trim();
  if (!raw) {
    throw new Error("EVAL_ARTIFACTS_URL is empty.");
  }

  try {
    const url = new URL(raw);

    if (url.protocol === "s3:") {
      const bucket = url.hostname;
      if (!bucket) throw new Error("s3:// URL is missing a bucket name.");
      const keyPrefix = ensureTrailingSlash(url.pathname.replace(/^\//, ""));
      return { kind: "s3", bucket, keyPrefix };
    }

    if (url.protocol === "http:" || url.protocol === "https:" || url.protocol === "file:") {
      return { kind: "url", baseUrl: new URL(ensureTrailingSlash(url.href)) };
    }
    throw new Error(`Unsupported EVAL_ARTIFACTS_URL protocol: ${url.protocol}`);
  } catch (error) {
    console.warn(
      "[eval-ui][server] EVAL_ARTIFACTS_URL is not a supported URL; treating as a filesystem path.",
      { value: raw },
      error,
    );
  }

  const absPath = path.isAbsolute(raw) ? raw : path.resolve(process.cwd(), raw);
  return { kind: "url", baseUrl: pathToFileURL(ensureTrailingSlash(absPath)) };
}

function artifactsRoot(): ArtifactsRoot {
  cachedArtifactsRoot ??=
    env.EVAL_ARTIFACTS_URL
      ? parseArtifactsRoot(env.EVAL_ARTIFACTS_URL)
      : { kind: "url", baseUrl: defaultFixtureArtifactsBaseUrl() };
  return cachedArtifactsRoot;
}

async function fetchArtifactJson(relativePath: string) {
  const root = artifactsRoot();

  if (root.kind === "s3") {
    const cmd = new GetObjectCommand({
      Bucket: root.bucket,
      Key: `${root.keyPrefix}${relativePath}`,
    });

    const response = await sendS3((forcePathStyle) => getS3Client({ forcePathStyle }).send(cmd));
    const raw = await readObjectBody(response.Body);
    return JSON.parse(raw) as unknown;
  }

  if (root.baseUrl.protocol === "file:") {
    const baseDir = fileURLToPath(root.baseUrl);
    const filePath = path.resolve(baseDir, relativePath);
    const relativeToBase = path.relative(baseDir, filePath);
    if (relativeToBase === ".." || relativeToBase.startsWith(`..${path.sep}`)) {
      throw new Error(`Artifact path escapes artifacts root: ${relativePath}`);
    }
    const raw = await readFile(filePath, "utf-8");
    return JSON.parse(raw) as unknown;
  }

  const url = new URL(relativePath, root.baseUrl);
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(
      `Failed to fetch eval artifacts (${response.status} ${response.statusText}) from ${url.toString()}.`,
    );
  }
  return (await response.json()) as unknown;
}

export const getEvalScenarios = createServerFn({ method: "GET" }).handler(
  async (): Promise<ScenarioSpec[]> => {
    const doc = await fetchArtifactJson("index.json");
    const parsed = ArtifactsIndexSchema.parse(doc);
    return parsed.scenarios;
  },
);

export const getEvalScenarioBundle = createServerFn({ method: "POST" })
  .inputValidator((input) => ScenarioBundleInputSchema.parse(input))
  .handler(async ({ data }): Promise<EvalScenarioBundle> => {
    const doc = await fetchArtifactJson(`bundles/${data.scenarioId}.json`);
    const parsed = ScenarioBundleArtifactSchema.parse(doc);

    const strategies: EvalStrategyResult[] = parsed.strategies.map((strategy) => {
      const guidelines = strategy.guidelines.map((g) => {
        const entry = requireCatalogEntryFromWire(
          g.entry,
          `scenario=${parsed.scenario.id} strategy=${strategy.strategy_id} rank=${g.rank}`,
        );
        return { rank: g.rank, score: g.score, entry, evidence: g.evidence };
      });

      return {
        strategyId: strategy.strategy_id,
        strategyName: strategy.strategy_name,
        guidelines,
      };
    });

    return { scenario: parsed.scenario, strategies };
  });
