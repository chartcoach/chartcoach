import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const dependencyFields = [
  "dependencies",
  "devDependencies",
  "peerDependencies",
  "optionalDependencies",
] as const;

const workspaceContracts = [
  {
    path: "apps/docs/package.json",
    internal: ["@chartcoach/brand"],
  },
  {
    path: "apps/site/package.json",
    internal: ["@chartcoach/brand", "@chartcoach/catalog"],
  },
  { path: "packages/brand/package.json", internal: [] },
  { path: "packages/catalog/package.json", internal: [] },
  { path: "skills/package.json", internal: [] },
  { path: "tools/architecture/package.json", internal: [] },
  { path: "tools/ci/package.json", internal: [] },
  { path: "tools/release/package.json", internal: ["@chartcoach/catalog"] },
  {
    path: "apps/chat/package.json",
    internal: ["@chartcoach/brand", "@chartcoach/catalog", "@chartcoach/skills"],
  },
];

void test("workspace manifests preserve the web dependency graph", async () => {
  for (const contract of workspaceContracts) {
    const manifest = await readManifest(contract.path);

    const internal = dependencyFields
      .flatMap((field) => Object.keys(manifest[field] ?? {}))
      .filter((name) => name.startsWith("@chartcoach/"))
      .sort();

    assert.deepEqual(internal, contract.internal, contract.path);
  }
});

void test("catalog installation leaves native data engines caller-owned", async () => {
  const manifest = await readManifest("packages/catalog/package.json");

  const installed = {
    ...manifest.dependencies,
    ...manifest.optionalDependencies,
  };

  for (const name of ["@lancedb/lancedb", "@duckdb/node-api", "@duckdb/duckdb-wasm"]) {
    assert.equal(Object.hasOwn(installed, name), false);

    if (Object.hasOwn(manifest.peerDependencies ?? {}, name)) {
      assert.equal(manifest.peerDependenciesMeta?.[name]?.optional, true);
    }
  }
});

async function readManifest(path: string) {
  const url = new URL(`../../${path}`, import.meta.url);

  // SAFETY: repository package manifests use npm dependency maps of names to version strings.
  return JSON.parse(await readFile(url, "utf8")) as {
    dependencies?: Record<string, string>;
    devDependencies?: Record<string, string>;
    peerDependencies?: Record<string, string>;
    optionalDependencies?: Record<string, string>;
    peerDependenciesMeta?: Record<string, { optional?: boolean }>;
  };
}
