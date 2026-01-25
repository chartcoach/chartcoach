import {
  GetObjectCommand,
  ListObjectsV2Command,
  PutObjectCommand,
  S3Client,
} from "@aws-sdk/client-s3";
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

import { env } from "@chartcoach/eval-ui/env";
import { RelevanceRatingsExportV1Schema } from "@chartcoach/eval-ui/eval/relevance-ratings";

const UploadRelevanceRatingsInputSchema = z.object({
  deviceId: z.string().min(1),
  export: RelevanceRatingsExportV1Schema,
  digest: z.string().min(1).optional(),
});

const DownloadRelevanceRatingsInputSchema = z.object({
  deviceId: z.string().min(1),
});

let s3Client: S3Client | undefined;
let s3ClientPathStyle: S3Client | undefined;

function isLikelyCertError(error: unknown) {
  const message = error instanceof Error ? error.message : String(error);
  const anyError = error as any;
  const code = anyError?.code ?? anyError?.Code ?? anyError?.name;

  return (
    code === "DEPTH_ZERO_SELF_SIGNED_CERT" ||
    code === "ERR_TLS_CERT_ALTNAME_INVALID" ||
    message.toLowerCase().includes("self-signed certificate") ||
    message.toLowerCase().includes("certificate") ||
    message.toLowerCase().includes("altname")
  );
}

type GetS3ClientOptions = {
  forcePathStyle?: boolean;
};

function getS3Client({ forcePathStyle }: GetS3ClientOptions = {}) {
  if (!env.S3_ACCESS_KEY_ID || !env.S3_SECRET_ACCESS_KEY || !env.S3_BUCKET) {
    throw new Error(
      "Relevance ratings sync is not configured. Set S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, and S3_BUCKET.",
    );
  }

  // Some S3-compatible endpoints (e.g., MinIO) work fine without a specific region.
  // The AWS SDK still requires *a* region value, so default when not provided.
  const region = env.S3_REGION ?? "us-east-1";

  const shouldForcePathStyle = forcePathStyle ?? env.S3_FORCE_PATH_STYLE ?? false;

  if (shouldForcePathStyle) {
    s3ClientPathStyle ??= new S3Client({
      region,
      credentials: {
        accessKeyId: env.S3_ACCESS_KEY_ID,
        secretAccessKey: env.S3_SECRET_ACCESS_KEY,
      },
      endpoint: env.S3_ENDPOINT,
      forcePathStyle: true,
    });
    return s3ClientPathStyle;
  }

  s3Client ??= new S3Client({
    region,
    credentials: {
      accessKeyId: env.S3_ACCESS_KEY_ID,
      secretAccessKey: env.S3_SECRET_ACCESS_KEY,
    },
    endpoint: env.S3_ENDPOINT,
    forcePathStyle: false,
  });
  return s3Client;
}

function normalizeObjectKeyTimestamp(isoString: string) {
  return isoString.replaceAll(":", "-").replaceAll(".", "-");
}

function normalizePrefix(prefix: string | undefined) {
  if (!prefix) return "";
  return prefix.endsWith("/") ? prefix : `${prefix}/`;
}

async function readObjectBody(body: unknown): Promise<string> {
  if (!body) return "";

  if (typeof body === "string") return body;

  const maybeSdkBody = body as { transformToString?: () => Promise<string> };
  if (typeof maybeSdkBody.transformToString === "function") {
    return await maybeSdkBody.transformToString();
  }

  const { Readable } = await import("node:stream");
  if (body instanceof Readable) {
    const chunks: Buffer[] = [];

    for await (const chunk of body) {
      chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
    }

    return Buffer.concat(chunks).toString("utf8");
  }

  return String(body);
}

export const uploadRelevanceRatingsExport = createServerFn({ method: "POST" })
  .inputValidator((input) => UploadRelevanceRatingsInputSchema.parse(input))
  .handler(async ({ data }) => {
    const prefix = normalizePrefix(env.S3_PREFIX);
    const safeDeviceId = encodeURIComponent(data.deviceId);
    const safeExportedAt = normalizeObjectKeyTimestamp(data.export.exportedAt);
    const digestSuffix = data.digest ? `-${data.digest.slice(0, 12)}` : "";

    const key = `${prefix}relevance-ratings/v1/${safeDeviceId}/${safeExportedAt}${digestSuffix}.json`;

    const cmd = new PutObjectCommand({
      Bucket: env.S3_BUCKET,
      Key: key,
      Body: JSON.stringify(data.export),
      ContentType: "application/json",
    });

    try {
      await getS3Client().send(cmd);
    } catch (error) {
      // When using an S3-compatible endpoint without wildcard certs, virtual-hosted style
      // can fail TLS validation (bucket becomes a subdomain). Retry with path-style.
      const configuredForcePathStyle = env.S3_FORCE_PATH_STYLE ?? false;
      if (env.S3_ENDPOINT && !configuredForcePathStyle && isLikelyCertError(error)) {
        await getS3Client({ forcePathStyle: true }).send(cmd);
      } else {
        throw error;
      }
    }

    return { key };
  });

export const downloadLatestRelevanceRatingsExport = createServerFn({
  method: "POST",
})
  .inputValidator((input) => DownloadRelevanceRatingsInputSchema.parse(input))
  .handler(async ({ data }) => {
    const prefix = normalizePrefix(env.S3_PREFIX);
    const safeDeviceId = encodeURIComponent(data.deviceId);
    const objectPrefix = `${prefix}relevance-ratings/v1/${safeDeviceId}/`;

    const list = new ListObjectsV2Command({
      Bucket: env.S3_BUCKET,
      Prefix: objectPrefix,
    });

    const configuredForcePathStyle = env.S3_FORCE_PATH_STYLE ?? false;

    async function listObjects() {
      if (!env.S3_ENDPOINT || configuredForcePathStyle) {
        return await getS3Client().send(list);
      }

      try {
        return await getS3Client().send(list);
      } catch (error) {
        if (isLikelyCertError(error)) {
          return await getS3Client({ forcePathStyle: true }).send(list);
        }
        throw error;
      }
    }

    const response = await listObjects();
    const objects = response.Contents ?? [];

    const latest = objects.reduce<{ Key?: string; LastModified?: Date } | null>((best, obj) => {
      if (!obj.Key) return best;
      if (!best) return obj;

      const bestTime = best.LastModified?.getTime();
      const objTime = obj.LastModified?.getTime();

      if (objTime && (!bestTime || objTime > bestTime)) return obj;
      if (!objTime && bestTime) return best;

      return obj.Key > (best.Key ?? "") ? obj : best;
    }, null);

    if (!latest?.Key) {
      return { found: false as const };
    }

    const get = new GetObjectCommand({
      Bucket: env.S3_BUCKET,
      Key: latest.Key,
    });

    async function getObject() {
      if (!env.S3_ENDPOINT || configuredForcePathStyle) {
        return await getS3Client().send(get);
      }

      try {
        return await getS3Client().send(get);
      } catch (error) {
        if (isLikelyCertError(error)) {
          return await getS3Client({ forcePathStyle: true }).send(get);
        }
        throw error;
      }
    }

    const objectResponse = await getObject();
    const raw = await readObjectBody(objectResponse.Body);
    const parsed = RelevanceRatingsExportV1Schema.parse(JSON.parse(raw));

    return {
      found: true as const,
      key: latest.Key,
      export: parsed,
    };
  });
