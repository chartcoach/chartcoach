import { z } from "zod";

export const providerSchema = z.enum(["anthropic", "openai", "google", "compatible"]);

export type Provider = z.infer<typeof providerSchema>;

export const providerNames: Record<Provider, string> = {
  anthropic: "Anthropic",
  openai: "OpenAI",
  google: "Gemini",
  compatible: "OpenAI compatible",
};

export const apiBaseURL = z.url({ protocol: /^https?$/ }).refine((value) => {
  const url = new URL(value);

  return !url.username && !url.password && !url.search && !url.hash;
}, "Use an HTTP or HTTPS API URL without credentials, a query, or a fragment.");

export const apiKeySchema = z
  .string()
  .trim()
  .min(1)
  .max(4096)
  .regex(/^[\x21-\x7e]+$/);

export const modelAuth = z.enum(["api-key", "none"]);

export const modelFields = {
  provider: providerSchema,
  baseURL: apiBaseURL.optional(),
  model: z.string().trim().min(1).max(200),
  contextWindow: z.number().int().min(4096).max(2_000_000).default(128_000),
  auth: modelAuth.optional(),
};
