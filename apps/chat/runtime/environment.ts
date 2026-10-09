import { createEnv } from "@t3-oss/env-core";
import { z } from "zod";
import { configSchema } from "./schema.ts";

const text = z.string().min(1).optional();

const boolean = z
  .enum(["true", "false", "1", "0"])
  .transform((value) => value === "true" || value === "1")
  .optional();

const model = configSchema.shape.model.unwrap().shape;

const server = configSchema.shape.server.unwrap().shape;

export function readEnvironment(environment: Record<string, string | undefined>) {
  return createEnv({
    server: {
      CHARTCOACH_CATALOG: text,
      CHARTCOACH_CATALOG_PROFILE: text,
      CHARTCOACH_PROVIDER: model.provider.unwrap().optional(),
      CHARTCOACH_MODEL: text,
      CHARTCOACH_BASE_URL: model.baseURL,
      CHARTCOACH_MODEL_AUTH: model.auth.unwrap().optional(),
      CHARTCOACH_API_KEY_ENV: text,
      CHARTCOACH_CONTEXT_WINDOW: z.coerce.number().pipe(model.contextWindow.unwrap()).optional(),
      CHARTCOACH_HOST: server.host.unwrap().optional(),
      CHARTCOACH_PORT: z.coerce.number().pipe(server.port.unwrap()).optional(),
      CHARTCOACH_OPEN: boolean,
      CHARTCOACH_PUBLIC_URL: server.publicURL,
      CHARTCOACH_USERNAME: server.username.unwrap().optional(),
      CHARTCOACH_PASSWORD_ENV: text,
      CHARTCOACH_PASSWORD_FILE: text,
      CHARTCOACH_EMBED_ORIGINS: text,
      CHARTCOACH_DATA_DIR: text,
      CHARTCOACH_CACHE_DIR: text,
      CHARTCOACH_MODEL_ORIGINS: text,
      CHARTCOACH_TRACING: boolean,
    },
    runtimeEnv: { ...environment },
    emptyStringAsUndefined: true,
    isServer: true,
    onValidationError: (issues) => {
      const names = issues.map((issue) => z.string().catch("environment").parse(issue.path?.[0]));
      throw new Error(
        `Invalid environment: ${names.join(", ")}. Check these variables or use chartcoach chat --help.`,
      );
    },
  });
}
