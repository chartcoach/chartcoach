import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import test from "node:test";

const docsRoot = new URL("../../apps/docs/content/docs/", import.meta.url);

void test("documentation navigation includes every authored page", async () => {
  await checkNavigation(docsRoot);
});

async function checkNavigation(directory: URL) {
  const entries = await readdir(directory, { withFileTypes: true });

  // SAFETY: Fumadocs navigation metadata declares its page names as strings.
  const meta = JSON.parse(await readFile(new URL("meta.json", directory), "utf8")) as {
    pages: string[];
  };

  const content = entries.filter((entry) => entry.isDirectory() || entry.name.endsWith(".mdx"));
  assert.deepEqual(
    [...meta.pages].sort((a, b) => a.localeCompare(b)),
    content.map((entry) => entry.name.replace(/\.mdx$/, "")).sort(),
    directory.pathname,
  );

  for (const entry of content) {
    if (entry.isDirectory()) await checkNavigation(new URL(`${entry.name}/`, directory));
  }
}
