import { createEnv } from "@t3-oss/env-nextjs";
import { z } from "zod";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { parseEnv } from "node:util";

const optionalText = z.string().min(1).optional();
const httpUrl = z.url({ protocol: /^https?$/ });

function localEnvironment(): Record<string, string | undefined> | undefined {
  try {
    return parseEnv(readFileSync(join(process.cwd(), ".env.local"), "utf8"));
  } catch (error) {
    if (error instanceof Error && "code" in error && error.code === "ENOENT") return undefined;
    throw error;
  }
}

const local = localEnvironment();
// A local connection is one credential set, never a mix of local and inherited keys.
const langfuse = local ?? process.env;

export const env = createEnv({
  server: {
    NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
    VERCEL_ENV: z.enum(["development", "preview", "production"]).optional(),
    OPENAI_BASE: httpUrl.optional(),
    OPENAI_API_KEY: optionalText,
    OPENAI_MODEL: z.string().min(1).default("gpt-5.6-luna"),
    CATALOG_SOURCE: optionalText,
    CHAT_DATA_DIR: optionalText,
    CHAT_MODEL_ORIGINS: z.string().default(""),
    CATALOG_PROFILE: z.string().min(1).default("minilm-l6-v2-cpu"),
    LANGFUSE_PUBLIC_KEY: optionalText,
    LANGFUSE_SECRET_KEY: optionalText,
    LANGFUSE_BASE_URL: httpUrl.default("https://cloud.langfuse.com"),
    LANGFUSE_TRACING_ENVIRONMENT: optionalText,
    LANGFUSE_RELEASE: optionalText,
    EVE_NEXT_PRODUCTION_PORT: z.coerce.number().int().min(1).max(65535).optional(),
  },
  runtimeEnv: {
    NODE_ENV: process.env.NODE_ENV,
    VERCEL_ENV: process.env.VERCEL_ENV,
    OPENAI_BASE: process.env.OPENAI_BASE,
    OPENAI_API_KEY: process.env.OPENAI_API_KEY,
    OPENAI_MODEL: process.env.OPENAI_MODEL,
    CATALOG_SOURCE: process.env.CATALOG_SOURCE,
    CHAT_DATA_DIR: process.env.CHAT_DATA_DIR,
    CHAT_MODEL_ORIGINS: process.env.CHAT_MODEL_ORIGINS,
    CATALOG_PROFILE: process.env.CATALOG_PROFILE,
    LANGFUSE_PUBLIC_KEY: langfuse.LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY: langfuse.LANGFUSE_SECRET_KEY,
    LANGFUSE_BASE_URL: langfuse.LANGFUSE_BASE_URL,
    LANGFUSE_TRACING_ENVIRONMENT:
      local?.LANGFUSE_TRACING_ENVIRONMENT ?? process.env.LANGFUSE_TRACING_ENVIRONMENT,
    LANGFUSE_RELEASE: local?.LANGFUSE_RELEASE ?? process.env.LANGFUSE_RELEASE,
    EVE_NEXT_PRODUCTION_PORT: process.env.EVE_NEXT_PRODUCTION_PORT,
  },
  emptyStringAsUndefined: true,
  createFinalSchema: (shape, isServer) =>
    z.object(shape).superRefine((values, context) => {
      if (isServer && Boolean(values.LANGFUSE_PUBLIC_KEY) !== Boolean(values.LANGFUSE_SECRET_KEY)) {
        context.addIssue({
          code: "custom",
          path: [values.LANGFUSE_PUBLIC_KEY ? "LANGFUSE_SECRET_KEY" : "LANGFUSE_PUBLIC_KEY"],
          message: "Set both Langfuse keys or leave both empty.",
        });
      }
    }),
  onValidationError: (issues) => {
    throw new Error(
      `Invalid chat environment: ${issues.map((issue) => z.string().catch("environment").parse(issue.path?.[0])).join(", ")}. Check these settings in your environment.`,
    );
  },
});
