import { createIsomorphicFn } from "@tanstack/react-start";
import { createEnv } from "@t3-oss/env-core";
import { z } from "zod";

const BooleanStringSchema = z.enum(["true", "false"]).transform((value) => value === "true");

const getRuntimeEnv = createIsomorphicFn()
  .server(() => ({ ...import.meta.env, ...process.env }))
  .client(() => import.meta.env);

export const env = createEnv({
  server: {
    EVAL_ARTIFACTS_URL: z.string().min(1).optional(),
    EVAL_ARTIFACTS_VERSION: z.string().min(1).default("v1"),
    S3_ENDPOINT: z.url().optional(),
    S3_REGION: z.string().min(1).optional(),
    S3_ACCESS_KEY_ID: z.string().min(1).optional(),
    S3_SECRET_ACCESS_KEY: z.string().min(1).optional(),
    S3_BUCKET: z.string().min(1).optional(),
    S3_PREFIX: z.string().optional(),
    S3_FORCE_PATH_STYLE: BooleanStringSchema.optional(),
  },

  clientPrefix: "VITE_",

  client: {
    VITE_APP_TITLE: z.string().min(1).optional(),
    VITE_GUIDELINE_DETAIL_URL_TEMPLATE: z.string().min(1).optional(),
  },

  runtimeEnv: getRuntimeEnv(),

  emptyStringAsUndefined: true,
});
