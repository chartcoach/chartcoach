import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vitest";

import { loadCatalog } from "@chartcoach/catalog";
import { readCatalog } from "@chartcoach/catalog/server";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const repoRoot = path.resolve(__dirname, "../../..");
const guidelinesRoot = path.join(repoRoot, "guidelines");
const catalogParquetPath = path.join(guidelinesRoot, "catalog.parquet");
const folderFixtureRoot = path.join(__dirname, "fixtures", "folder-catalog");

describe("guidelines/catalog.parquet", () => {
  function assertCatalogLooksParsed(catalog: {
    guidelines: Array<{ sections: unknown }>;
  }) {
    expect(catalog.guidelines.length).toBeGreaterThan(0);

    const guidelineWithSections = catalog.guidelines.find((guideline) => {
      const sections = guideline.sections;
      return Array.isArray(sections) && sections.length > 0;
    });
    expect(guidelineWithSections).toBeDefined();
  }

  it("loads from file path", async () => {
    const catalog = await readCatalog(catalogParquetPath);
    expect(catalog.length).toBeGreaterThan(0);

    const ids = catalog.guidelines.map((guideline) => guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });

  it("loads from catalog bundle with manifest validation", async () => {
    const catalog = await readCatalog(guidelinesRoot);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest?.sectionRoles.advice?.name).toBe("advice");
    expect(catalog.manifest?.labelFamilies.chart?.name).toBe("chart");
    assertCatalogLooksParsed(catalog);
  });

  it("loads from bytes (Uint8Array)", async () => {
    const buf = await readFile(catalogParquetPath);
    const bytes = new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);

    const catalog = await loadCatalog(bytes);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.guidelines[0]?.id).toBeTypeOf("string");
    assertCatalogLooksParsed(catalog);
  });

  it("loads from folder (guidelines/*)", async () => {
    const catalog = await readCatalog(folderFixtureRoot);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest?.sectionRoles.advice?.name).toBe("advice");

    const ids = catalog.guidelines.map((guideline) => guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });
});
