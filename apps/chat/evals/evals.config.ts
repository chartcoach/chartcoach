import { defineEvalConfig } from "eve/evals";
import { createOpenAI } from "@ai-sdk/openai";
import { env } from "../lib/env";

const provider = createOpenAI({
  baseURL: env.OPENAI_BASE,
  apiKey: env.OPENAI_API_KEY,
});

export default defineEvalConfig({
  maxConcurrency: 1,
  timeoutMs: 180_000,
  judge: { model: provider.chat(env.OPENAI_MODEL) },
});
