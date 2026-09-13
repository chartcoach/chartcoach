import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it } from "vite-plus/test";

function loadEnv(values: Record<string, string> = {}, browser = false, local?: string) {
  const directory = mkdtempSync(join(tmpdir(), "chartcoach-env-"));

  try {
    if (local !== undefined) writeFileSync(join(directory, ".env.local"), local);

    return spawnSync(
      process.execPath,
      [
        "--input-type=module",
        "-e",
        `
    ${browser ? "globalThis.window = {};" : ""}
    try {
      const { env } = await import(${JSON.stringify(new URL("../lib/env.ts", import.meta.url).href)});
      console.log(JSON.stringify({
        model: env.OPENAI_MODEL, profile: env.CATALOG_PROFILE,
        source: env.CATALOG_SOURCE, port: env.EVE_NEXT_PRODUCTION_PORT,
        tracing: Boolean(env.LANGFUSE_PUBLIC_KEY && env.LANGFUSE_SECRET_KEY),
        tracingHost: env.LANGFUSE_BASE_URL,
        localKeys: env.LANGFUSE_PUBLIC_KEY === "local-public" && env.LANGFUSE_SECRET_KEY === "local-secret",
      }));
    } catch (error) {
      console.error(error.message);
      process.exitCode = 1;
    }
  `,
      ],
      {
        encoding: "utf8",
        cwd: directory,
        env: {
          ...process.env,
          NODE_ENV: "test",
          VERCEL_ENV: "",
          OPENAI_BASE: "",
          OPENAI_API_KEY: "",
          OPENAI_MODEL: "",
          CATALOG_SOURCE: "",
          CATALOG_PROFILE: "",
          LANGFUSE_PUBLIC_KEY: "",
          LANGFUSE_SECRET_KEY: "",
          LANGFUSE_BASE_URL: "",
          LANGFUSE_TRACING_ENVIRONMENT: "",
          LANGFUSE_RELEASE: "",
          EVE_NEXT_PRODUCTION_PORT: "",
          ...values,
        },
      },
    );
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
}

it("loads defaults with optional services unconfigured", () => {
  const result = loadEnv();
  expect(result.status, result.stderr).toBe(0);
  expect(JSON.parse(result.stdout)).toEqual({
    model: "gpt-5.6-luna",
    profile: "minilm-l6-v2-cpu",
    tracing: false,
    tracingHost: "https://cloud.langfuse.com",
    localKeys: false,
  });
});

it("accepts provider overrides, a local catalog, and a complete tracing configuration", () => {
  const result = loadEnv({
    OPENAI_BASE: "http://127.0.0.1:8317/v1",
    OPENAI_MODEL: "vision-model",
    CATALOG_SOURCE: "/catalog files/release",
    CATALOG_PROFILE: "local-embedding",
    LANGFUSE_PUBLIC_KEY: "pk-lf-test",
    LANGFUSE_SECRET_KEY: "sk-lf-test",
    LANGFUSE_BASE_URL: "https://tracing.example.test",
    EVE_NEXT_PRODUCTION_PORT: "4274",
  });

  expect(result.status, result.stderr).toBe(0);
  expect(JSON.parse(result.stdout)).toEqual({
    model: "vision-model",
    profile: "local-embedding",
    source: "/catalog files/release",
    port: 4274,
    tracing: true,
    tracingHost: "https://tracing.example.test",
    localKeys: false,
  });
});

it.each([
  ["OPENAI_BASE", { OPENAI_BASE: "private-invalid-url" }],
  ["LANGFUSE_BASE_URL", { LANGFUSE_BASE_URL: "file:///private-path" }],
  ["EVE_NEXT_PRODUCTION_PORT", { EVE_NEXT_PRODUCTION_PORT: "70000" }],
  ["LANGFUSE_SECRET_KEY", { LANGFUSE_PUBLIC_KEY: "private-public-key" }],
  ["LANGFUSE_PUBLIC_KEY", { LANGFUSE_SECRET_KEY: "private-secret-key" }],
])("rejects invalid %s configuration without logging values", (field, values) => {
  const result = loadEnv(values);
  expect(result.status).toBe(1);
  expect(result.stderr).toContain(field);

  for (const value of Object.values(values)) expect(result.stderr).not.toContain(value);
});

it("rejects access to server settings in a browser runtime", () => {
  const result = loadEnv({ OPENAI_API_KEY: "private-provider-key" }, true);
  expect(result.status).toBe(1);
  expect(result.stderr).toContain("server-side environment variable");
  expect(result.stderr).not.toContain("private-provider-key");
});

it("takes the complete Langfuse connection from the local file", () => {
  const result = loadEnv(
    {
      LANGFUSE_PUBLIC_KEY: "global-public",
      LANGFUSE_SECRET_KEY: "global-secret",
      LANGFUSE_BASE_URL: "https://global.example.test",
    },
    false,
    "LANGFUSE_PUBLIC_KEY=local-public\nLANGFUSE_SECRET_KEY=local-secret\nLANGFUSE_BASE_URL=https://local.example.test\n",
  );

  expect(result.status, result.stderr).toBe(0);
  expect(JSON.parse(result.stdout)).toMatchObject({
    localKeys: true,
    tracing: true,
    tracingHost: "https://local.example.test",
  });
});

it("uses the default host when a local connection omits its URL", () => {
  const result = loadEnv(
    { LANGFUSE_BASE_URL: "https://global.example.test" },
    false,
    "LANGFUSE_PUBLIC_KEY=local-public\nLANGFUSE_SECRET_KEY=local-secret\n",
  );

  expect(result.status, result.stderr).toBe(0);
  expect(JSON.parse(result.stdout)).toMatchObject({
    localKeys: true,
    tracingHost: "https://cloud.langfuse.com",
  });
});

it("keeps tracing disabled when the local file omits credentials", () => {
  const result = loadEnv(
    { LANGFUSE_PUBLIC_KEY: "global-public", LANGFUSE_SECRET_KEY: "global-secret" },
    false,
    "OPENAI_MODEL=vision-model\n",
  );

  expect(result.status, result.stderr).toBe(0);
  expect(JSON.parse(result.stdout)).toMatchObject({ tracing: false });
});

it("rejects a partial local key pair even when inherited keys are complete", () => {
  const result = loadEnv(
    { LANGFUSE_PUBLIC_KEY: "global-public", LANGFUSE_SECRET_KEY: "global-secret" },
    false,
    "LANGFUSE_PUBLIC_KEY=local-public\n",
  );

  expect(result.status).toBe(1);
  expect(result.stderr).toContain("LANGFUSE_SECRET_KEY");
  expect(result.stderr).not.toContain("global-secret");
});
