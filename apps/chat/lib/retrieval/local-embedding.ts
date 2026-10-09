import { join } from "node:path";

export async function openLocalEmbedding(cacheDirectory: string) {
  const { pipeline, mean_pooling } = await import("@huggingface/transformers");

  const embed = await pipeline("feature-extraction", "Xenova/all-MiniLM-L6-v2", {
    dtype: "fp32",
    device: "cpu",
    cache_dir: join(cacheDirectory, "models"),
  });

  return async (text: string) => {
    const inputs = embed.tokenizer(text, { padding: true, truncation: true, max_length: 256 });
    // Preserve MiniLM's final separator when Transformers.js truncates to 256 tokens.
    const separator = embed.tokenizer.sep_token_id;

    if (separator === undefined) throw new Error("MiniLM tokenizer has no separator token.");
    inputs.input_ids.data[inputs.input_ids.data.length - 1] = BigInt(separator);
    const output = await embed.model(inputs);
    const vector = mean_pooling(output.last_hidden_state, inputs.attention_mask).normalize(2, -1);

    return Array.from(vector.data, Number);
  };
}
