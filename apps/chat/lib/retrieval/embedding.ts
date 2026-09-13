import envPaths from "env-paths";
import { join } from "node:path";
import type { ProfileInfo } from "@chartcoach/catalog";

let embedding: ReturnType<typeof openEmbedding> | undefined;

export async function embedQuery(text: string, info: ProfileInfo) {
  validateProfile(info);

  const { embed, mean_pooling } = await (embedding ??= openEmbedding().catch((error) => {
    embedding = undefined;
    throw error;
  }));

  const inputs = embed.tokenizer(text, {
    padding: true,
    truncation: true,
    max_length: 256,
  });

  // Preserve MiniLM's final separator when Transformers.js truncates to 256 tokens.
  const separator = embed.tokenizer.sep_token_id;

  if (separator === undefined) throw new Error("MiniLM tokenizer has no separator token.");
  inputs.input_ids.data[inputs.input_ids.data.length - 1] = BigInt(separator);
  const output = await embed.model(inputs);
  const vector = mean_pooling(output.last_hidden_state, inputs.attention_mask).normalize(2, -1);

  return Array.from(vector.data, Number);
}

function validateProfile(info: ProfileInfo) {
  const binding = info.embedding_functions[0];

  if (
    info.dimensions !== 384 ||
    info.distance_metric !== "cosine" ||
    binding?.name !== "sentence-transformers" ||
    binding.model.name !== "all-MiniLM-L6-v2" ||
    binding.model.normalize !== true
  ) {
    throw new Error("Choose the normalized all-MiniLM-L6-v2 catalog profile.");
  }
}

async function openEmbedding() {
  const { pipeline, mean_pooling } = await import("@huggingface/transformers");

  const embed = await pipeline("feature-extraction", "Xenova/all-MiniLM-L6-v2", {
    dtype: "fp32",
    device: "cpu",
    cache_dir: join(envPaths("chartcoach", { suffix: "" }).cache, "models"),
  });

  return { embed, mean_pooling };
}
