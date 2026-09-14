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

export const compatibleProviderPresets = [
  { id: "openrouter", name: "OpenRouter", baseURL: "https://openrouter.ai/api/v1" },
  { id: "xai", name: "xAI / Grok", baseURL: "https://api.x.ai/v1" },
  {
    id: "gemini",
    name: "Google Gemini",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai",
  },
  { id: "togetherai", name: "Together AI", baseURL: "https://api.together.ai/v1" },
  {
    id: "fireworksai",
    name: "Fireworks AI",
    baseURL: "https://api.fireworks.ai/inference/v1",
  },
  { id: "groq", name: "Groq", baseURL: "https://api.groq.com/openai/v1" },
  {
    id: "huggingface",
    name: "Hugging Face",
    baseURL: "https://router.huggingface.co/v1",
  },
  { id: "mistral", name: "Mistral AI", baseURL: "https://api.mistral.ai/v1" },
  { id: "nvidia", name: "NVIDIA NIM", baseURL: "https://integrate.api.nvidia.com/v1" },
  {
    id: "vercelaigateway",
    name: "Vercel AI Gateway",
    baseURL: "https://ai-gateway.vercel.sh/v1",
  },
] as const;

export type CompatibleProviderId = (typeof compatibleProviderPresets)[number]["id"];

export function compatibleProviderPreset(baseURL: string | undefined) {
  if (!baseURL) return;

  const normalized = baseURL.replace(/\/$/, "");

  return compatibleProviderPresets.find((preset) => preset.baseURL === normalized);
}

export const modelFields = {
  provider: providerSchema,
  baseURL: apiBaseURL.optional(),
  model: z.string().trim().min(1).max(200),
  contextWindow: z.number().int().min(4096).max(2_000_000).default(128_000),
  auth: modelAuth.optional(),
};
