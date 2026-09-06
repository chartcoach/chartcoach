import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const dependencyFields = [
  "dependencies",
  "devDependencies",
  "peerDependencies",
  "optionalDependencies",
];

const workspaceContracts = [
  {
    path: "apps/docs/package.json",
    internal: ["@chartcoach/brand", "@chartcoach/catalog"],
  },
  {
    path: "apps/site/package.json",
    internal: ["@chartcoach/brand", "@chartcoach/catalog"],
  },
  { path: "packages/brand/package.json", internal: [] },
  { path: "packages/catalog/package.json", internal: [] },
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

void test("the browser catalog keeps its dependency set deliberate", async () => {
  const manifest = await readManifest("packages/catalog/package.json");
  assert.deepEqual(Object.keys(manifest.dependencies ?? {}).sort(), [
    "bibtex-parse",
    "hyparquet",
    "hyparquet-compressors",
    "yaml",
  ]);
});

async function readManifest(path) {
  const url = new URL(`../../${path}`, import.meta.url);
  return JSON.parse(await readFile(url, "utf8"));
}
