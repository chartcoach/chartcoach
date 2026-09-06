import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import test from "node:test";

const docsRoot = new URL("../../apps/docs/content/docs/", import.meta.url);
const exampleReadmes = [
  new URL("../../README.md", import.meta.url),
  new URL("../../packages/chartcoach/README.md", import.meta.url),
  new URL("../../packages/catalog/README.md", import.meta.url),
];
const hostedWheel =
  "https://files.peter.gy/packages/python/chartcoach/0.2.0/892f120cb377/chartcoach-0.2.0-py3-none-any.whl";
const docsRelease =
  "https://files.peter.gy/packages/python/chartcoach/0.2.0/docs-catalog/c0f6dbec3dd31b07763b46fd458733db0b8b50c5793cf9447458119287129420/release.json";

void test("every live notebook pins the hosted chartcoach wheel", async () => {
  const pages = await markdownFiles(docsRoot);
  const notebooks = [];

  for (const page of pages) {
    const source = await readFile(page, "utf8");
    const configs = source.matchAll(/```marimo-config\n([\s\S]*?)```/g);
    for (const config of configs) {
      notebooks.push(page.pathname);
      assert.ok((config[1] ?? "").includes(hostedWheel), page.pathname);
    }
  }

  assert.ok(notebooks.length > 0);
});

void test("public examples use one immutable real catalog release", async () => {
  const pages = [...(await markdownFiles(docsRoot)), ...exampleReadmes];
  const sources = await Promise.all(pages.map((page) => readFile(page, "utf8")));
  const combined = sources.join("\n");
  const releaseUrls = new Set(
    combined.match(
      /https:\/\/files\.peter\.gy\/packages\/python\/chartcoach\/0\.2\.0\/docs-catalog\/[a-f0-9]+\/release\.json/g,
    ) ?? [],
  );

  assert.deepEqual([...releaseUrls], [docsRelease]);
  const wheelUrls = new Set(
    combined.match(
      /https:\/\/files\.peter\.gy\/packages\/python\/chartcoach\/0\.2\.0\/[a-f0-9]+\/chartcoach-0\.2\.0-py3-none-any\.whl/g,
    ) ?? [],
  );
  assert.deepEqual([...wheelUrls], [hostedWheel]);
});

async function markdownFiles(directory) {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const url = new URL(entry.name, directory);
    if (entry.isDirectory()) {
      url.pathname += "/";
      files.push(...(await markdownFiles(url)));
    } else if (entry.name.endsWith(".mdx")) {
      files.push(url);
    }
  }
  return files;
}
