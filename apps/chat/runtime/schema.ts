import { platformDirectories } from "@chartcoach/catalog/node/paths";
import { join } from "node:path";
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
  embedding: z
    .strictObject({
      model: text,
      baseURL: apiBaseURL,
      dimensions: z.number().int().positive(),
      apiKeyEnv: text.default("CHARTCOACH_EMBEDDING_API_KEY"),
    })
    .optional(),
  server: z
    .strictObject({
      host: z.enum(["127.0.0.1", "0.0.0.0", "::1", "::"]).default("127.0.0.1"),
      port: z.number().int().min(0).max(65535).default(4273),
      open: z.boolean().default(true),
      publicURL: apiBaseURL.optional(),
      username: text.regex(/^[^:]+$/).default("chartcoach"),
      passwordEnv: text.default("CHARTCOACH_PASSWORD"),
      passwordFile: text.optional(),
      embedOrigins: z.array(z.union([z.literal("*"), apiBaseURL])).default([]),
    })
    .prefault({}),
  storage: z
    .strictObject({
      dataDir: text.default(join(platformDirectories().data, "chat")),
      cacheDir: text.default(platformDirectories().cache),
    })
    .prefault({}),
  modelOrigins: z
    .array(apiBaseURL)
    .default([...new Set(compatibleProviderPresets.map(({ baseURL }) => new URL(baseURL).origin))]),
  tracing: z.boolean().default(false),
});

export type Config = z.infer<typeof configSchema>;

type SchemaInput = z.input<typeof configSchema>;

export type ConfigInput = Omit<SchemaInput, "embedding"> & {
  embedding?: Partial<NonNullable<SchemaInput["embedding"]>>;
};
