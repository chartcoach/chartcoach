import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vite-plus/test";

import { loadCatalog } from "@chartcoach/catalog";

const entriesPath = fileURLToPath(
  new URL("../../../fixtures/catalog-release/entries.parquet", import.meta.url),
);

describe("catalog manifest validation", () => {
  it("rejects a manifest without the required vocabulary headings", async () => {
    const entries = await readFile(entriesPath);

    await expect(
      loadCatalog({
        entries,
        manifestText: "# Catalog\n\n## Section Roles\n\n### advice\n\nActionable guidance.\n",
      }),
    ).rejects.toThrow("MANIFEST.md is missing required heading(s): Label Families.");
  });

  it("rejects catalog entries whose vocabulary is absent from the manifest", async () => {
    const entries = await readFile(entriesPath);
    const manifestText = `# Catalog

## Section Roles

### advice

Actionable guidance.

## Label Families

### chart

Chart-family labels such as \`chart:bar\`.
`;

    await expect(loadCatalog({ entries, manifestText })).rejects.toThrow(
      "Catalog manifest validation failed:",
    );
  });
});
