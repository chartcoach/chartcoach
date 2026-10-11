import { langfuseBaseURL } from "../runtime/schema.ts";
import { settings } from "../runtime/settings.ts";
import { createEnv } from "@t3-oss/env-core";
import { z } from "zod";

const optionalText = z.string().trim().min(1).optional();

const langfuse: Record<string, string | undefined> = settings.tracing ? process.env : {};

export const env = createEnv({
  server: {
    NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
    VERCEL_ENV: z.enum(["development", "preview", "production"]).optional(),
    LANGFUSE_PUBLIC_KEY: optionalText,
    LANGFUSE_SECRET_KEY: optionalText,
    LANGFUSE_BASE_URL: langfuseBaseURL,
    LANGFUSE_TRACING_ENVIRONMENT: optionalText,
    LANGFUSE_RELEASE: optionalText,
  },
  runtimeEnv: {
    NODE_ENV: process.env.NODE_ENV,
    VERCEL_ENV: process.env.VERCEL_ENV,
    LANGFUSE_PUBLIC_KEY: langfuse.LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY: langfuse.LANGFUSE_SECRET_KEY,
    LANGFUSE_BASE_URL: langfuse.LANGFUSE_BASE_URL,
    LANGFUSE_TRACING_ENVIRONMENT: process.env.LANGFUSE_TRACING_ENVIRONMENT,
    LANGFUSE_RELEASE: process.env.LANGFUSE_RELEASE,
  },
  emptyStringAsUndefined: true,
  createFinalSchema: (fields, isServer) =>
    z.object(fields).superRefine((values, context) => {
      if (
        isServer &&
        settings.tracing &&
        (!values.LANGFUSE_PUBLIC_KEY || !values.LANGFUSE_SECRET_KEY)
      ) {
        context.addIssue({
          code: "custom",
          path: [values.LANGFUSE_PUBLIC_KEY ? "LANGFUSE_SECRET_KEY" : "LANGFUSE_PUBLIC_KEY"],
          message: "Tracing requires both Langfuse keys.",
        });
      }
    }),
  onValidationError: (issues) => {
    throw new Error(
      `Invalid chat environment: ${issues.map((issue) => z.string().catch("environment").parse(issue.path?.[0])).join(", ")}. Check these settings in your environment.`,
    );
  },
});

export const langfuseTracingEnabled = Boolean(env.LANGFUSE_PUBLIC_KEY && env.LANGFUSE_SECRET_KEY);
