import { createIsomorphicFn } from "@tanstack/react-start";
import { createEnv } from "@t3-oss/env-core";
import { z } from "zod";

const BooleanStringSchema = z.enum(["true", "false"]).transform((value) => value === "true");

const getRuntimeEnv = createIsomorphicFn()
  .server(() => ({ ...import.meta.env, ...process.env }))
  .client(() => import.meta.env);

export const env = createEnv({
  server: {
    STRATEGY_DISPLAY_MODE: z.enum(["name", "alias"]).default("name"),
    RETRIEVAL_SERVER_BASE_URL: z.url().default("http://127.0.0.1:8000"),
    RETRIEVAL_CATALOG_URI: z.string().min(1).optional(),
    RETRIEVAL_RESULTS_CACHE_VERSION: z.string().min(1).default("v1"),
    RETRIEVAL_STRATEGY_CONCURRENCY: z.coerce.number().int().positive().default(4),
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
