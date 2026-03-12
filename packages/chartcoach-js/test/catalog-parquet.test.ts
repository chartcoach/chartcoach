import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vitest";

import { loadCatalogFromParquet } from "@chartcoach/catalog";
import { loadCatalogFromFolder, loadCatalogFromParquetFile } from "@chartcoach/catalog/node";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const repoRoot = path.resolve(__dirname, "../../..");
const guidelinesRoot = path.join(repoRoot, "guidelines");
const catalogParquetPath = path.join(guidelinesRoot, "catalog.parquet");

describe("guidelines/catalog.parquet", () => {
  function assertCatalogLooksParsed(catalog: {
    entries: Array<{ guideline: { sections: unknown; sectionsIndex: unknown } }>;
  }) {
    expect(catalog.entries.length).toBeGreaterThan(0);

    const entryWithSections = catalog.entries.find((e) => {
      const sections = e.guideline.sections;
      return Array.isArray(sections) && sections.length > 0;
    });
    expect(entryWithSections).toBeDefined();

    const index = (entryWithSections as any).guideline.sectionsIndex as {
      byRole?: Record<string, unknown>;
    };
    expect(index).toBeTruthy();
    expect(index.byRole && Object.keys(index.byRole).length).toBeGreaterThan(0);
  }

  it("loads from file path", async () => {
    const catalog = await loadCatalogFromParquetFile(catalogParquetPath);
    expect(catalog.length).toBeGreaterThan(0);

    const ids = catalog.entries.map((e) => e.guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });

  it("loads from bytes (Uint8Array)", async () => {
    const buf = await readFile(catalogParquetPath);
    const bytes = new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);

    const catalog = await loadCatalogFromParquet(bytes);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.entries[0]?.guideline.id).toBeTypeOf("string");
    assertCatalogLooksParsed(catalog);
  });

  it("loads from folder (guidelines/*)", async () => {
    const catalog = await loadCatalogFromFolder(guidelinesRoot);
    expect(catalog.length).toBeGreaterThan(0);

    const ids = catalog.entries.map((e) => e.guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });
});
