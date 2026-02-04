import { GetObjectCommand, ListObjectsV2Command, PutObjectCommand } from "@aws-sdk/client-s3";
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

import { env } from "@chartcoach/eval-ui/env";
import { EvalDataExportV1Schema } from "@chartcoach/eval-ui/eval/eval-data";
import {
  getS3Client,
  normalizePrefix,
  readObjectBody,
  sendS3,
} from "@chartcoach/eval-ui/eval/server/s3.server";

const UploadEvalDataInputSchema = z.object({
  deviceId: z.string().min(1),
  export: EvalDataExportV1Schema,
  digest: z.string().min(1).optional(),
});

const DownloadEvalDataInputSchema = z.object({
  deviceId: z.string().min(1),
});

function normalizeObjectKeyTimestamp(isoString: string) {
  return isoString.replaceAll(":", "-").replaceAll(".", "-");
}

export const uploadEvalDataExport = createServerFn({ method: "POST" })
  .inputValidator((input) => UploadEvalDataInputSchema.parse(input))
  .handler(async ({ data }) => {
    const prefix = normalizePrefix(env.S3_PREFIX);
    const safeDeviceId = encodeURIComponent(data.deviceId);
    const safeExportedAt = normalizeObjectKeyTimestamp(data.export.exportedAt);
    const digestSuffix = data.digest ? `-${data.digest.slice(0, 12)}` : "";

    const key = `${prefix}eval-data/v1/${safeDeviceId}/${safeExportedAt}${digestSuffix}.json`;

    const cmd = new PutObjectCommand({
      Bucket: env.S3_BUCKET,
      Key: key,
      Body: JSON.stringify(data.export),
      ContentType: "application/json",
    });

    await sendS3((forcePathStyle) => getS3Client({ forcePathStyle }).send(cmd));

    return { key };
  });

export const downloadLatestEvalDataExport = createServerFn({
  method: "POST",
})
  .inputValidator((input) => DownloadEvalDataInputSchema.parse(input))
  .handler(async ({ data }) => {
    const prefix = normalizePrefix(env.S3_PREFIX);
    const safeDeviceId = encodeURIComponent(data.deviceId);
    const objectPrefix = `${prefix}eval-data/v1/${safeDeviceId}/`;

    const pickLatest = (
      best: { Key?: string; LastModified?: Date } | null,
      obj: { Key?: string; LastModified?: Date },
    ) => {
      if (!obj.Key) return best;
      if (!best) return obj;

      const bestTime = best.LastModified?.getTime();
      const objTime = obj.LastModified?.getTime();

      if (objTime && (!bestTime || objTime > bestTime)) return obj;
      if (!objTime && bestTime) return best;

      return obj.Key > (best.Key ?? "") ? obj : best;
    };

    let latest: { Key?: string; LastModified?: Date } | null = null;
    let continuationToken: string | undefined;

    do {
      const list = new ListObjectsV2Command({
        Bucket: env.S3_BUCKET,
        Prefix: objectPrefix,
        ContinuationToken: continuationToken,
      });

      const response = await sendS3((forcePathStyle) =>
        getS3Client({ forcePathStyle }).send(list),
      );

      for (const obj of response.Contents ?? []) {
        latest = pickLatest(latest, obj);
      }

      continuationToken = response.IsTruncated ? response.NextContinuationToken : undefined;
    } while (continuationToken);

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
    const parsed = EvalDataExportV1Schema.parse(JSON.parse(raw));

    return {
      found: true as const,
      key: latest.Key,
      export: parsed,
    };
  });
