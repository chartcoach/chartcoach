import { createOpenAI } from "@ai-sdk/openai";
import { defineAgent } from "eve";
import { reviewSchema } from "../shared/review";

const openai = createOpenAI({
  baseURL: process.env.OPENAI_BASE,
  apiKey: process.env.OPENAI_API_KEY,
});

export default defineAgent({
  model: openai.chat(process.env.OPENAI_MODEL ?? "gpt-5.6-luna"),
  modelContextWindowTokens: 128_000,
  defaultTools: false,
  outputSchema: reviewSchema,
  build: {
    externalDependencies: [
      "@chartcoach/catalog",
      "@lancedb/lancedb",
      "@huggingface/transformers",
      "@duckdb/node-api",
    ],
  },
});
