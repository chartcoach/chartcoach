import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it } from "vite-plus/test";

function loadEnv({
  environment,
  browser = false,
  local,
}: {
  environment: Record<string, string>;
  browser?: boolean;
  local?: string;
}) {
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
      const { env, langfuseTracingEnabled } = await import(${JSON.stringify(new URL("../lib/env.ts", import.meta.url).href)});
      console.log(JSON.stringify({
        enabled: langfuseTracingEnabled,
        publicKey: env.LANGFUSE_PUBLIC_KEY ?? null,
        secretKey: env.LANGFUSE_SECRET_KEY ?? null,
        baseURL: env.LANGFUSE_BASE_URL,
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
          CHARTCOACH_TRACING: "true",
          VERCEL_ENV: "",
          LANGFUSE_PUBLIC_KEY: "",
          LANGFUSE_SECRET_KEY: "",
          LANGFUSE_BASE_URL: "",
          LANGFUSE_TRACING_ENVIRONMENT: "",
          LANGFUSE_RELEASE: "",
          ...environment,
        },
      },
    );
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
}

const inherited = {
  LANGFUSE_PUBLIC_KEY: "global-public",
  LANGFUSE_SECRET_KEY: "global-secret",
  LANGFUSE_BASE_URL: "https://global.example.test",
};

const localKeys = "LANGFUSE_PUBLIC_KEY=local-public\nLANGFUSE_SECRET_KEY=local-secret\n";

it.each([
  {
    source: "disabled tracing despite inherited credentials",
    environment: { ...inherited, CHARTCOACH_TRACING: "false" },
    expected: {
      enabled: false,
      publicKey: null,
      secretKey: null,
      baseURL: "https://cloud.langfuse.com",
    },
  },
  {
    source: "the inherited connection when no local file exists",
    environment: inherited,
    expected: {
      enabled: true,
      publicKey: "global-public",
      secretKey: "global-secret",
      baseURL: "https://global.example.test",
    },
  },
  {
    source: "the complete local connection",
    environment: inherited,
    local: localKeys + "LANGFUSE_BASE_URL=https://local.example.test\n",
    expected: {
      enabled: true,
      publicKey: "local-public",
      secretKey: "local-secret",
      baseURL: "https://local.example.test",
    },
  },
  {
    source: "the default host when the local connection omits its URL",
    environment: inherited,
    local: localKeys,
    expected: {
      enabled: true,
      publicKey: "local-public",
      secretKey: "local-secret",
      baseURL: "https://cloud.langfuse.com",
    },
  },
  {
    source: "no connection when the local file omits credentials",
    environment: inherited,
    local: "CHARTCOACH_MODEL=vision-model\n",
    expected: {
      enabled: false,
      publicKey: null,
      secretKey: null,
      baseURL: "https://cloud.langfuse.com",
    },
  },
])("uses $source", ({ expected, ...options }) => {
  const result = loadEnv(options);
  expect(result.status, result.stderr).toBe(0);
  expect(JSON.parse(result.stdout)).toEqual(expected);
});

it.each([
  ["LANGFUSE_BASE_URL", { LANGFUSE_BASE_URL: "file:///private-path" }],
  ["LANGFUSE_SECRET_KEY", { LANGFUSE_PUBLIC_KEY: "private-public-key" }],
  ["LANGFUSE_PUBLIC_KEY", { LANGFUSE_SECRET_KEY: "private-secret-key" }],
])("rejects invalid %s configuration without logging values", (field, environment) => {
  const result = loadEnv({ environment });
  expect(result.status).toBe(1);
  expect(result.stderr).toContain(field);

  for (const value of Object.values(environment)) expect(result.stderr).not.toContain(value);
});

it("rejects access to server settings in a browser runtime", () => {
  const result = loadEnv({ environment: inherited, browser: true });
  expect(result.status).toBe(1);
  expect(result.stderr).toContain("server-side environment variable");
  expect(result.stderr).not.toContain("global-secret");
});

it("rejects a partial local key pair even when inherited keys are complete", () => {
  const result = loadEnv({ environment: inherited, local: "LANGFUSE_PUBLIC_KEY=local-public\n" });
  expect(result.status).toBe(1);
  expect(result.stderr).toContain("LANGFUSE_SECRET_KEY");
  expect(result.stderr).not.toContain("global-secret");
});
