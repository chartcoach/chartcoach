import { PutObjectCommand, S3Client } from '@aws-sdk/client-s3'
import { createServerFn } from '@tanstack/react-start'
import { z } from 'zod'

import { env } from '@chartcoach/eval-ui/env'
import { RelevanceRatingsExportV1Schema } from '@chartcoach/eval-ui/eval/relevance-ratings'

const UploadRelevanceRatingsInputSchema = z.object({
  deviceId: z.string().min(1),
  export: RelevanceRatingsExportV1Schema,
  digest: z.string().min(1).optional(),
})

let s3Client: S3Client | undefined
function getS3Client() {
  if (
    !env.S3_REGION ||
    !env.S3_ACCESS_KEY_ID ||
    !env.S3_SECRET_ACCESS_KEY ||
    !env.S3_BUCKET
  ) {
    throw new Error(
      'Relevance ratings sync is not configured. Set S3_REGION, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, and S3_BUCKET.',
    )
  }

  s3Client ??= new S3Client({
    region: env.S3_REGION,
    credentials: {
      accessKeyId: env.S3_ACCESS_KEY_ID,
      secretAccessKey: env.S3_SECRET_ACCESS_KEY,
    },
    endpoint: env.S3_ENDPOINT,
    forcePathStyle: env.S3_FORCE_PATH_STYLE,
  })
  return s3Client
}

function normalizeObjectKeyTimestamp(isoString: string) {
  return isoString.replaceAll(':', '-').replaceAll('.', '-')
}

function normalizePrefix(prefix: string | undefined) {
  if (!prefix) return ''
  return prefix.endsWith('/') ? prefix : `${prefix}/`
}

export const uploadRelevanceRatingsExport = createServerFn({ method: 'POST' })
  .inputValidator((input) => UploadRelevanceRatingsInputSchema.parse(input))
  .handler(async ({ data }) => {
    if (!env.S3_BUCKET) {
      throw new Error(
        'Relevance ratings sync is not configured. Missing S3_BUCKET env var.',
      )
    }

    const prefix = normalizePrefix(env.S3_PREFIX)
    const safeDeviceId = encodeURIComponent(data.deviceId)
    const safeExportedAt = normalizeObjectKeyTimestamp(data.export.exportedAt)
    const digestSuffix = data.digest ? `-${data.digest.slice(0, 12)}` : ''

    const key = `${prefix}relevance-ratings/v1/${safeDeviceId}/${safeExportedAt}${digestSuffix}.json`

    await getS3Client().send(
      new PutObjectCommand({
        Bucket: env.S3_BUCKET,
        Key: key,
        Body: JSON.stringify(data.export),
        ContentType: 'application/json',
      }),
    )

    return { key }
  })
