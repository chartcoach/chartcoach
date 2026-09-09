import { defineEvalConfig } from "eve/evals";
import { createOpenAI } from "@ai-sdk/openai";

const provider = createOpenAI({
  baseURL: process.env.OPENAI_BASE,
  apiKey: process.env.OPENAI_API_KEY,
});

export default defineEvalConfig({
  maxConcurrency: 1,
  timeoutMs: 180_000,
  judge: { model: provider.chat(process.env.OPENAI_MODEL ?? "gpt-5.6-luna") },
});
