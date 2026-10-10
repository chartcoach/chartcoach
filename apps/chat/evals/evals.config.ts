import { Experimental_DecisionLanguageModel } from "@ai-sdk/provider-utils/experimental-decision";
import { defineEvalConfig } from "eve/evals";
import { Redacted } from "effect";
import { settings } from "../runtime/settings";
import { modelKey } from "../runtime/config";
import { languageModel } from "../lib/app/providers";

const model = settings.model.model;

const key = modelKey(settings);

if (!model) throw new Error("Set CHARTCOACH_TEXT_MODEL to run evaluations.");

if (key === undefined) throw new Error("Set the configured provider's API key to run evaluations.");

export default defineEvalConfig({
  maxConcurrency: 1,
  timeoutMs: 180_000,
  judge: {
    model: new Experimental_DecisionLanguageModel({
      model: languageModel({ ...settings.model, model, name: "Evaluation" }, Redacted.make(key)),
    }),
  },
});
