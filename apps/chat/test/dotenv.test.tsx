import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, expect, it, vi } from "vite-plus/test";
import { loadEnvironmentFile } from "../runtime/dotenv";
import { loadConfig, modelKey, embeddingKey } from "../runtime/config";

afterEach(() => vi.unstubAllEnvs());

it("loads dedicated text and embedding credentials while preserving process overrides", () => {
  const directory = mkdtempSync(join(tmpdir(), "chartcoach-dotenv-"));
  const file = join(directory, ".env");

  const values = {
    CHARTCOACH_TEXT_MODEL: "file-model",
    CHARTCOACH_TEXT_API_KEY: "text-private",
    CHARTCOACH_EMBEDDING_MODEL: "embedding-model",
    CHARTCOACH_EMBEDDING_BASE_URL: "https://vectors.example/v1",
    CHARTCOACH_EMBEDDING_DIMENSIONS: "4",
    CHARTCOACH_EMBEDDING_API_KEY: "vector-private",
  };

  for (const name of Object.keys(process.env))
    if (name.startsWith("CHARTCOACH_")) vi.stubEnv(name, undefined);

  for (const name of Object.keys(values)) vi.stubEnv(name, undefined);
  vi.stubEnv("CHARTCOACH_TEXT_MODEL", "process-model");
  writeFileSync(
    file,
    Object.entries(values)
      .map(([key, value]) => `${key}=${JSON.stringify(value)}`)
      .join("\n"),
  );

  try {
    loadEnvironmentFile(file);
    const config = loadConfig({ userConfig: join(directory, "missing.json") });
    expect(config.model.model).toBe("process-model");
    expect(modelKey(config)).toBe("text-private");
    expect(embeddingKey(config)).toBe("vector-private");
    expect(JSON.stringify(config)).not.toContain("private");
    expect(() => loadEnvironmentFile(join(directory, "missing.env"))).toThrow(
      "Cannot read --env-file",
    );
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});
