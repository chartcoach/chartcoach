import type { ProfileInfo } from "@chartcoach/catalog";
import type { Config } from "../../runtime/schema";
import { embeddingKey, type Environment } from "../../runtime/config";
import { apiBaseURL } from "../../shared/model";
import { openLocalEmbedding } from "./local-embedding";

type Embedding = NonNullable<Config["embedding"]>;

type QueryEmbedding = (text: string, signal?: AbortSignal) => Promise<number[]>;

type QueryEmbedder = (text: string, info: ProfileInfo, signal?: AbortSignal) => Promise<number[]>;

export function createQueryEmbedder(
  config: Pick<Config, "embedding" | "storage">,
  environment: Environment = process.env,
): QueryEmbedder {
  const connection = config.embedding ? { ...config.embedding } : undefined;
  const variables = connection ? { [connection.apiKeyEnv]: environment[connection.apiKeyEnv] } : {};

  const open = connection
    ? () => openCompatibleEmbedding(connection, variables)
    : () => openLocalEmbedding(config.storage.cacheDir);

  let pending: Promise<QueryEmbedding> | undefined;

  return async (text, info, signal) => {
    signal?.throwIfAborted();
    validateEmbeddingProfile(info, connection);

    const embed = await (pending ??= open().catch((error) => {
      pending = undefined;
      throw error;
    }));

    return embed(text, signal);
  };
}

function validateEmbeddingProfile(info: ProfileInfo, connection: Config["embedding"]) {
  const binding = info.embedding_functions[0];

  if (connection) {
    // Native OpenAI profiles serialize a null base_url for the SDK's standard endpoint.
    const endpoint = apiBaseURL.safeParse(
      binding.model.base_url ??
        (binding.name === "openai" ? "https://api.openai.com/v1" : undefined),
    );

    if (
      !["openai", "chartcoach-openai-compatible"].includes(binding.name) ||
      binding.model.name !== connection.model ||
      info.dimensions !== connection.dimensions ||
      binding.model.use_azure === true ||
      !endpoint.success ||
      new URL(endpoint.data).href.replace(/\/$/, "") !==
        new URL(connection.baseURL).href.replace(/\/$/, "")
    )
      throw new Error(
        "Embedding connection must match the selected catalog profile's model, dimensions, and base URL. Build/select a matching profile.",
      );
  } else if (
    info.dimensions !== 384 ||
    info.distance_metric !== "cosine" ||
    binding.name !== "sentence-transformers" ||
    binding.model.name !== "all-MiniLM-L6-v2" ||
    binding.model.normalize !== true
  )
    throw new Error(
      "Configure CHARTCOACH_EMBEDDING_* for this profile, or choose the normalized all-MiniLM-L6-v2 profile.",
    );
}

async function openCompatibleEmbedding(
  connection: Embedding,
  environment: Environment,
): Promise<QueryEmbedding> {
  const key = embeddingKey({ embedding: connection }, environment);

  if (!key) throw new Error(`Set ${connection.apiKeyEnv} for the configured embedding connection.`);

  const [{ createOpenAICompatible }, { embed }] = await Promise.all([
    import("@ai-sdk/openai-compatible"),
    import("ai"),
  ]);

  const model = createOpenAICompatible({
    name: "chartcoach",
    baseURL: connection.baseURL,
    apiKey: key,
  }).embeddingModel(connection.model);

  return async (text, signal) => {
    try {
      const { embedding } = await embed({
        model,
        value: text,
        providerOptions:
          connection.model === "text-embedding-ada-002"
            ? undefined
            : { chartcoach: { dimensions: connection.dimensions } },
        abortSignal: AbortSignal.any([...(signal ? [signal] : []), AbortSignal.timeout(30_000)]),
        maxRetries: 2,
      });

      if (embedding.length !== connection.dimensions || !embedding.every(Number.isFinite))
        throw new Error("Invalid embedding vector.");

      return embedding;
    } catch {
      signal?.throwIfAborted();
      throw new Error(
        "Embedding request failed. Check the configured endpoint, model, credentials, and dimensions.",
      );
    }
  };
}
