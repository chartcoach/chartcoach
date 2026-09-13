import { settings } from "../runtime/settings.ts";
import { createEnv } from "@t3-oss/env-core";
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
const langfuse = settings.tracing ? (local ?? process.env) : {};

export const env = createEnv({
  server: {
    NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
    VERCEL_ENV: z.enum(["development", "preview", "production"]).optional(),
    LANGFUSE_PUBLIC_KEY: optionalText,
    LANGFUSE_SECRET_KEY: optionalText,
    LANGFUSE_BASE_URL: httpUrl.default("https://cloud.langfuse.com"),
    LANGFUSE_TRACING_ENVIRONMENT: optionalText,
    LANGFUSE_RELEASE: optionalText,
  },
  runtimeEnv: {
    NODE_ENV: process.env.NODE_ENV,
    VERCEL_ENV: process.env.VERCEL_ENV,
    LANGFUSE_PUBLIC_KEY: langfuse.LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY: langfuse.LANGFUSE_SECRET_KEY,
    LANGFUSE_BASE_URL: langfuse.LANGFUSE_BASE_URL,
    LANGFUSE_TRACING_ENVIRONMENT:
      local?.LANGFUSE_TRACING_ENVIRONMENT ?? process.env.LANGFUSE_TRACING_ENVIRONMENT,
    LANGFUSE_RELEASE: local?.LANGFUSE_RELEASE ?? process.env.LANGFUSE_RELEASE,
  },
  emptyStringAsUndefined: true,
  createFinalSchema: (fields, isServer) =>
    z.object(fields).superRefine((values, context) => {
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
