import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it } from "vite-plus/test";
import { loadConfig, modelKey, embeddingKey, validateStartup } from "../runtime/config";
import { platformDirectories } from "@chartcoach/catalog/node/paths";

it("keeps durable chat data under the application root and shares its native cache", () => {
  const paths = platformDirectories();
  const config = loadConfig({ environment: {}, userConfig: "/missing/config.json" });

  expect(config.storage).toEqual({ dataDir: join(paths.data, "chat"), cacheDir: paths.cache });
});

it("resolves file paths and applies environment and invocation overrides", () => {
  const directory = mkdtempSync(join(tmpdir(), "chartcoach-config-"));

  try {
    const file = join(directory, "config.json");
    writeFileSync(
      file,
      JSON.stringify({
        catalog: { source: "./release" },
        model: { model: "file-model" },
        storage: { dataDir: "./data" },
        server: { port: 5000 },
      }),
    );

    const config = loadConfig({
      cwd: "/",
      configFile: file,
      environment: { CHARTCOACH_TEXT_MODEL: "environment-model", CHARTCOACH_PORT: "5001" },
      overrides: { server: { port: 5002 } },
    });

    expect(config.catalog.source).toBe(join(directory, "release"));
    expect(config.storage.dataDir).toBe(join(directory, "data"));
    expect(config.model.model).toBe("environment-model");
    expect(config.server.port).toBe(5002);
    expect(config.server.host).toBe("127.0.0.1");
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});

it("accepts keyless local models and requires authentication for network listening", () => {
  const config = loadConfig({
    environment: {},
    userConfig: "/missing/config.json",
    overrides: {
      model: {
        provider: "compatible",
        model: "local-vision",
        baseURL: "http://127.0.0.1:1234/v1",
        auth: "none",
      },
    },
  });

  expect(modelKey(config, {})).toBe("");
  expect(() => validateStartup(config, {})).not.toThrow();
  config.server.host = "0.0.0.0";
  expect(() => validateStartup(config, {})).toThrow("requires a password");
  expect(validateStartup(config, { CHARTCOACH_PASSWORD: "private" })).toBe("private");
  config.server.host = "127.0.0.1";
  config.server.publicURL = "https://chat.example.org";
  expect(() => validateStartup(config, {})).toThrow("requires a password");
});

it("rejects misspelled config fields and invalid values without revealing them", () => {
  const directory = mkdtempSync(join(tmpdir(), "chartcoach-config-"));

  try {
    const file = join(directory, "config.json");
    writeFileSync(file, JSON.stringify({ model: { apiKey: "private-secret" } }));
    expect(() => loadConfig({ configFile: file, environment: {} })).toThrow(
      "Invalid configuration",
    );

    try {
      loadConfig({ configFile: file, environment: {} });
    } catch (error) {
      expect(String(error)).not.toContain("private-secret");
    }

    expect(() =>
      loadConfig({ environment: { CHARTCOACH_PORT: "70000" }, userConfig: "/missing/config.json" }),
    ).toThrow("CHARTCOACH_PORT");
    expect(() =>
      loadConfig({
        environment: { CHARTCOACH_MODEL_ORIGINS: "models.example" },
        userConfig: "/missing/config.json",
      }),
    ).toThrow("Invalid configuration: modelOrigins");
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});

it("starts from defaults and typed environment settings when no configuration file exists", () => {
  const config = loadConfig({
    environment: {
      CHARTCOACH_PORT: "0",
      CHARTCOACH_OPEN: "false",
      CHARTCOACH_TEXT_PROVIDER: "google",
      CHARTCOACH_TEXT_MODEL: "vision-model",
    },
    userConfig: "/missing/config.json",
  });

  expect(config.server).toMatchObject({ host: "127.0.0.1", port: 0, open: false });
  expect(config.model).toMatchObject({ provider: "google", model: "vision-model" });
  expect(() => validateStartup(config, {})).toThrow("CHARTCOACH_TEXT_API_KEY");
  expect(() => validateStartup(config, { CHARTCOACH_TEXT_API_KEY: "private-key" })).not.toThrow();
});

it("keeps injected environment immutable while validating empty settings", () => {
  const environment = Object.freeze({ CHARTCOACH_TEXT_MODEL: "", CHARTCOACH_TEXT_API_KEY: "" });
  const config = loadConfig({ environment, userConfig: "/missing/config.json" });

  expect(config.model.model).toBeUndefined();
  expect(environment).toEqual({ CHARTCOACH_TEXT_MODEL: "", CHARTCOACH_TEXT_API_KEY: "" });
});

it("keeps text and embedding endpoints, models, and credentials independent", () => {
  const environment = {
    CHARTCOACH_TEXT_PROVIDER: "compatible",
    CHARTCOACH_TEXT_MODEL: "text-model",
    CHARTCOACH_TEXT_BASE_URL: "https://text.example/v1",
    CHARTCOACH_TEXT_API_KEY: "text-secret",
    CHARTCOACH_EMBEDDING_MODEL: "embedding-model",
    CHARTCOACH_EMBEDDING_BASE_URL: "https://vectors.example/v1",
    CHARTCOACH_EMBEDDING_DIMENSIONS: "4",
    CHARTCOACH_EMBEDDING_API_KEY: "embedding-secret",
  };

  const config = loadConfig({ environment, userConfig: "/missing/config.json" });
  expect(config.model).toMatchObject({
    model: "text-model",
    baseURL: environment.CHARTCOACH_TEXT_BASE_URL,
  });
  expect(config.embedding).toMatchObject({
    model: "embedding-model",
    dimensions: 4,
    baseURL: environment.CHARTCOACH_EMBEDDING_BASE_URL,
  });
  expect(modelKey(config, environment)).toBe("text-secret");
  expect(embeddingKey(config, environment)).toBe("embedding-secret");
  expect(() => validateStartup(config, environment)).not.toThrow();
  expect(JSON.stringify(config)).not.toContain("secret");
});

it("resolves custom credential variable names without falling back to another connection", () => {
  const config = loadConfig({
    environment: {
      CHARTCOACH_TEXT_MODEL: "text-model",
      CHARTCOACH_TEXT_API_KEY_ENV: "TEXT_TOKEN",
      CHARTCOACH_EMBEDDING_MODEL: "embedding-model",
      CHARTCOACH_EMBEDDING_BASE_URL: "https://vectors.example/v1",
      CHARTCOACH_EMBEDDING_DIMENSIONS: "4",
      CHARTCOACH_EMBEDDING_API_KEY_ENV: "VECTOR_TOKEN",
    },
    userConfig: "/missing/config.json",
  });

  expect(modelKey(config, { TEXT_TOKEN: "text-private" })).toBe("text-private");
  expect(embeddingKey(config, { VECTOR_TOKEN: "vector-private" })).toBe("vector-private");
  expect(modelKey(config, { CHARTCOACH_TEXT_API_KEY: "wrong" })).toBeUndefined();
  expect(() => embeddingKey(config, { VECTOR_TOKEN: "invalid secret" })).toThrow(
    "Invalid VECTOR_TOKEN",
  );
});

it("rejects incomplete embedding connections and reports canonical environment names", () => {
  const base = { userConfig: "/missing/config.json" };
  expect(() =>
    loadConfig({ ...base, environment: { CHARTCOACH_EMBEDDING_MODEL: "model" } }),
  ).toThrow("embedding");
  expect(() =>
    loadConfig({ ...base, environment: { CHARTCOACH_TEXT_BASE_URL: "invalid-url" } }),
  ).toThrow("CHARTCOACH_TEXT_BASE_URL");
});

it("composes a partial file embedding connection with environment and invocation settings", () => {
  const directory = mkdtempSync(join(tmpdir(), "chartcoach-config-"));
  const file = join(directory, "config.json");
  writeFileSync(
    file,
    JSON.stringify({ embedding: { model: "file-model", baseURL: "https://vectors.example/v1" } }),
  );

  try {
    const config = loadConfig({
      configFile: file,
      environment: { CHARTCOACH_EMBEDDING_DIMENSIONS: "4" },
      overrides: { embedding: { model: "invocation-model" } },
    });

    expect(config.embedding).toEqual({
      model: "invocation-model",
      baseURL: "https://vectors.example/v1",
      dimensions: 4,
      apiKeyEnv: "CHARTCOACH_EMBEDDING_API_KEY",
    });
    expect(() => loadConfig({ configFile: file, environment: {} })).toThrow("embedding.dimensions");
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});

it("reads embedding origins and requires secure cookies and a matching key", () => {
  const config = loadConfig({
    environment: {
      CHARTCOACH_EMBED_ORIGINS: "https://slides.example/deck/, http://localhost:2731",
    },
    userConfig: "/missing/config.json",
  });

  expect(config.server.embedOrigins).toEqual(["https://slides.example", "http://localhost:2731"]);
  expect(
    loadConfig({
      environment: { CHARTCOACH_EMBED_ORIGINS: "https://slides.example,*" },
      userConfig: "/missing/config.json",
    }).server.embedOrigins,
  ).toEqual(["*"]);
  expect(() =>
    loadConfig({
      environment: { CHARTCOACH_EMBED_ORIGINS: "slides.example" },
      userConfig: "/missing/config.json",
    }),
  ).toThrow("Invalid configuration: server.embedOrigins");

  const secrets = { CHARTCOACH_PASSWORD: "private" };
  expect(() => validateStartup(config, secrets)).not.toThrow();
  config.server.publicURL = "http://chat.example.org";
  expect(() => validateStartup(config, secrets)).toThrow("Embedding requires an HTTPS");
  config.server.publicURL = "https://chat.example.org";
  expect(() =>
    validateStartup(config, { ...secrets, CHARTCOACH_EMBED_KEY: "private-embed-key-0123" }),
  ).not.toThrow();
  expect(() => validateStartup(config, { ...secrets, CHARTCOACH_EMBED_KEY: "short" })).toThrow(
    "Invalid CHARTCOACH_EMBED_KEY",
  );
  config.server.embedOrigins = [];
  expect(() =>
    validateStartup(config, { ...secrets, CHARTCOACH_EMBED_KEY: "private-embed-key-0123" }),
  ).toThrow("requires CHARTCOACH_EMBED_ORIGINS");
});
