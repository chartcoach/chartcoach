import { S3Client } from "@aws-sdk/client-s3";

import { env } from "@chartcoach/eval-ui/env";

let s3Client: S3Client | undefined;
let s3ClientPathStyle: S3Client | undefined;

export function isS3Configured() {
  return Boolean(env.S3_ACCESS_KEY_ID && env.S3_SECRET_ACCESS_KEY && env.S3_BUCKET);
}

export type GetS3ClientOptions = {
  forcePathStyle?: boolean;
};

export function getS3Client({ forcePathStyle }: GetS3ClientOptions = {}) {
  if (!env.S3_ACCESS_KEY_ID || !env.S3_SECRET_ACCESS_KEY || !env.S3_BUCKET) {
    throw new Error(
      "S3 is not configured. Set S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, and S3_BUCKET.",
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

export function isLikelyCertError(error: unknown) {
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

export function normalizePrefix(prefix: string | undefined) {
  if (!prefix) return "";
  return prefix.endsWith("/") ? prefix : `${prefix}/`;
}

export async function readObjectBody(body: unknown): Promise<string> {
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
