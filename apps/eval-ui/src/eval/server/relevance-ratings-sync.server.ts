import { GetObjectCommand, ListObjectsV2Command, PutObjectCommand } from "@aws-sdk/client-s3";
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

import { env } from "@chartcoach/eval-ui/env";
import { RelevanceRatingsExportV1Schema } from "@chartcoach/eval-ui/eval/relevance-ratings";
import {
  getS3Client,
  normalizePrefix,
  readObjectBody,
  sendS3,
} from "@chartcoach/eval-ui/eval/server/s3.server";

const UploadRelevanceRatingsInputSchema = z.object({
  deviceId: z.string().min(1),
  export: RelevanceRatingsExportV1Schema,
  digest: z.string().min(1).optional(),
});

const DownloadRelevanceRatingsInputSchema = z.object({
  deviceId: z.string().min(1),
});

function normalizeObjectKeyTimestamp(isoString: string) {
  return isoString.replaceAll(":", "-").replaceAll(".", "-");
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

    await sendS3((forcePathStyle) => getS3Client({ forcePathStyle }).send(cmd));

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
    const response = await sendS3((forcePathStyle) => getS3Client({ forcePathStyle }).send(list));
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
    const objectResponse = await sendS3((forcePathStyle) =>
      getS3Client({ forcePathStyle }).send(get),
    );
    const raw = await readObjectBody(objectResponse.Body);
    const parsed = RelevanceRatingsExportV1Schema.parse(JSON.parse(raw));

    return {
      found: true as const,
      key: latest.Key,
      export: parsed,
    };
  });
