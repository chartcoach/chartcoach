import { createOpenAI } from "@ai-sdk/openai";
import { defineAgent } from "eve";
import { env } from "../lib/env";

const openai = createOpenAI({
  baseURL: env.OPENAI_BASE,
  apiKey: env.OPENAI_API_KEY,
});

export default defineAgent({
  model: openai.chat(env.OPENAI_MODEL),
  modelContextWindowTokens: 128_000,
  defaultTools: false,
  experimental: { instrumentationProviders: true },
  build: {
    externalDependencies: [
      "@chartcoach/catalog",
      "@lancedb/lancedb",
      "@huggingface/transformers",
      "@duckdb/node-api",
    ],
  },
});
