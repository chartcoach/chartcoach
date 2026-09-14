import envPaths from "env-paths";
import { z } from "zod";
import {
  apiBaseURL,
  compatibleProviderPresets,
  modelFields,
  modelAuth,
  providerSchema,
} from "../shared/model.ts";

const text = z.string().trim().min(1);

export const configSchema = z.strictObject({
  catalog: z
    .strictObject({
      source: text.default("https://artifacts.chartcoach.dev/catalog.json"),
      profile: text.default("minilm-l6-v2-cpu"),
    })
    .prefault({}),
  model: z
    .strictObject({
      ...modelFields,
      provider: providerSchema.default("openai"),
      model: modelFields.model.optional(),
      auth: modelAuth.default("api-key"),
      apiKeyEnv: text.optional(),
    })
    .prefault({}),
  server: z
    .strictObject({
      host: z.enum(["127.0.0.1", "0.0.0.0", "::1", "::"]).default("127.0.0.1"),
      port: z.number().int().min(0).max(65535).default(4273),
      open: z.boolean().default(true),
      publicURL: apiBaseURL.optional(),
      username: text.regex(/^[^:]+$/).default("chartcoach"),
      passwordEnv: text.default("CHARTCOACH_PASSWORD"),
      passwordFile: text.optional(),
    })
    .prefault({}),
  storage: z
    .strictObject({
      dataDir: text.default(envPaths("chartcoach-chat").data),
      cacheDir: text.default(envPaths("chartcoach", { suffix: "" }).cache),
    })
    .prefault({}),
  modelOrigins: z
    .array(apiBaseURL)
    .default([...new Set(compatibleProviderPresets.map(({ baseURL }) => new URL(baseURL).origin))]),
  tracing: z.boolean().default(false),
});

export type Config = z.infer<typeof configSchema>;

export type ConfigInput = z.input<typeof configSchema>;
