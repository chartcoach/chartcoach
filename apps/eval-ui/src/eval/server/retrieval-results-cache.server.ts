import crypto from "node:crypto";

import {
  DeleteObjectsCommand,
  type DeleteObjectsCommandOutput,
  GetObjectCommand,
  type GetObjectCommandOutput,
  ListObjectsV2Command,
  type ListObjectsV2CommandOutput,
  PutObjectCommand,
  type PutObjectCommandOutput,
} from "@aws-sdk/client-s3";
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

import { env } from "@chartcoach/eval-ui/env";
import type {
  RetrievalRequestWire,
  RetrievalResponseWire,
} from "@chartcoach/eval-ui/eval/retrieval/chartcoach-retrieval-client";
import {
  getS3Client,
  isLikelyCertError,
  isS3Configured,
  normalizePrefix,
  readObjectBody,
} from "@chartcoach/eval-ui/eval/server/s3.server";

const CacheEntrySchema = z.object({
  schemaVersion: z.literal(1),
  cachedAt: z.string().min(1),
  scenarioId: z.string().min(1),
  strategyId: z.string().min(1),
  catalogUri: z.string().min(1),
  request: z.unknown(),
  response: z.object({
    catalog: z.array(z.unknown()),
    meta: z.record(z.string(), z.unknown()).default({}),
  }),
});

export type RetrievalResultsCacheEntryV1 = z.infer<typeof CacheEntrySchema>;

const inMemoryCache = new Map<string, RetrievalResultsCacheEntryV1>();

function encodePathSegment(value: string) {
  return encodeURIComponent(value);
}

function getCacheBasePrefix() {
  const prefix = normalizePrefix(env.S3_PREFIX);
  return `${prefix}retrieval-results/${env.RETRIEVAL_RESULTS_CACHE_VERSION}/`;
}

export function buildRetrievalResultsCacheKey(args: {
  scenarioId: string;
  strategyId: string;
  digest: string;
}) {
  const base = getCacheBasePrefix();
  return `${base}${encodePathSegment(args.scenarioId)}/${encodePathSegment(args.strategyId)}/${args.digest}.json`;
}

export function computeRetrievalResultsDigest(args: {
  scenarioId: string;
  strategyId: string;
  catalogUri: string;
  request: RetrievalRequestWire;
  baseUrl: string;
}) {
  const payload = JSON.stringify({
    scenarioId: args.scenarioId,
    strategyId: args.strategyId,
    catalogUri: args.catalogUri,
    baseUrl: args.baseUrl,
    request: args.request,
  });
  return crypto.createHash("sha256").update(payload).digest("hex").slice(0, 16);
}

function isNotFoundError(error: unknown) {
  if (!error || typeof error !== "object") return false;
  const anyError = error as any;
  const code = anyError.code ?? anyError.Code ?? anyError.name;
  const status = anyError.$metadata?.httpStatusCode;
  return status === 404 || code === "NoSuchKey" || code === "NotFound";
}

function requireBucket() {
  if (!env.S3_BUCKET) {
    throw new Error("S3 is not configured. Set S3_BUCKET.");
  }
  return env.S3_BUCKET;
}

async function sendS3(cmd: GetObjectCommand, opts?: { forcePathStyle?: boolean }): Promise<GetObjectCommandOutput>;
async function sendS3(cmd: PutObjectCommand, opts?: { forcePathStyle?: boolean }): Promise<PutObjectCommandOutput>;
async function sendS3(
  cmd: ListObjectsV2Command,
  opts?: { forcePathStyle?: boolean },
): Promise<ListObjectsV2CommandOutput>;
async function sendS3(
  cmd: DeleteObjectsCommand,
  opts?: { forcePathStyle?: boolean },
): Promise<DeleteObjectsCommandOutput>;
async function sendS3(
  cmd: GetObjectCommand | PutObjectCommand | ListObjectsV2Command | DeleteObjectsCommand,
  opts?: { forcePathStyle?: boolean },
) {
  const configuredForcePathStyle = env.S3_FORCE_PATH_STYLE ?? false;
  const shouldForcePathStyle = opts?.forcePathStyle ?? configuredForcePathStyle;

  if (!env.S3_ENDPOINT || shouldForcePathStyle) {
    // No custom endpoint or already path-style: just send.
    return await getS3Client({ forcePathStyle: shouldForcePathStyle }).send(cmd);
  }

  try {
    return await getS3Client({ forcePathStyle: false }).send(cmd);
  } catch (error) {
    if (isLikelyCertError(error)) {
      return await getS3Client({ forcePathStyle: true }).send(cmd);
    }
    throw error;
  }
}

export async function readRetrievalResultsCache(
  key: string,
): Promise<RetrievalResultsCacheEntryV1 | undefined> {
  const cached = inMemoryCache.get(key);
  if (cached) return cached;

  if (!isS3Configured()) return undefined;

  const get = new GetObjectCommand({
    Bucket: requireBucket(),
    Key: key,
  });

  try {
    const obj = await sendS3(get);
    const raw = await readObjectBody(obj.Body);
    const parsed = CacheEntrySchema.parse(JSON.parse(raw));
    inMemoryCache.set(key, parsed);
    return parsed;
  } catch (error) {
    if (isNotFoundError(error)) return undefined;
    throw error;
  }
}

export async function writeRetrievalResultsCache(
  key: string,
  entry: {
    scenarioId: string;
    strategyId: string;
    catalogUri: string;
    request: RetrievalRequestWire;
    response: RetrievalResponseWire;
  },
) {
  const doc: RetrievalResultsCacheEntryV1 = {
    schemaVersion: 1,
    cachedAt: new Date().toISOString(),
    scenarioId: entry.scenarioId,
    strategyId: entry.strategyId,
    catalogUri: entry.catalogUri,
    request: entry.request,
    response: entry.response,
  };

  inMemoryCache.set(key, doc);

  if (!isS3Configured()) return;

  const put = new PutObjectCommand({
    Bucket: requireBucket(),
    Key: key,
    Body: JSON.stringify(doc),
    ContentType: "application/json",
  });

  await sendS3(put);
}

export function clearRetrievalResultsInMemoryCache() {
  inMemoryCache.clear();
}

export async function destroyRetrievalResultsCache(args?: {
  scenarioId?: string;
  strategyId?: string;
}) {
  inMemoryCache.clear();

  if (!isS3Configured()) {
    return { deleted: 0, s3: false as const };
  }

  const base = getCacheBasePrefix();
  const prefixParts = [base];
  if (args?.scenarioId) prefixParts.push(`${encodePathSegment(args.scenarioId)}/`);
  if (args?.strategyId) prefixParts.push(`${encodePathSegment(args.strategyId)}/`);
  const prefix = prefixParts.join("");

  let deleted = 0;
  let continuationToken: string | undefined;

  do {
    const list = new ListObjectsV2Command({
      Bucket: requireBucket(),
      Prefix: prefix,
      ContinuationToken: continuationToken,
    });

    const response = await sendS3(list);
    const contents = response.Contents ?? [];
    const keys = contents.map((o) => o.Key).filter((k): k is string => Boolean(k));

    if (keys.length) {
      const del = new DeleteObjectsCommand({
        Bucket: requireBucket(),
        Delete: { Objects: keys.map((Key) => ({ Key })) },
      });
      await sendS3(del);
      deleted += keys.length;
    }

    continuationToken = response.NextContinuationToken;
  } while (continuationToken);

  return { deleted, s3: true as const };
}

const DestroyCacheInputSchema = z.object({
  scenarioId: z.string().min(1).optional(),
  strategyId: z.string().min(1).optional(),
});

export const destroyEvalRetrievalResultsCache = createServerFn({ method: "POST" })
  .inputValidator((input) => DestroyCacheInputSchema.parse(input))
  .handler(async ({ data }) => await destroyRetrievalResultsCache(data));
