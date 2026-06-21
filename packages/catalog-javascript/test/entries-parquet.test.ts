import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vitest";

import {
  DEFAULT_CATALOG,
  catalogArtifact,
  catalogArtifactUrl,
  loadCatalog,
  parseCatalogReleaseMetadata,
} from "@chartcoach/catalog";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const bundleFixtureRoot = path.join(__dirname, "fixtures", "bundle");
const entriesParquetPath = path.join(bundleFixtureRoot, "entries.parquet");
const manifestPath = path.join(bundleFixtureRoot, "MANIFEST.md");

describe("catalog artifact loading", () => {
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

  it("loads caller-owned bytes with manifest text", async () => {
    const [entries, manifestText] = await Promise.all([
      readFile(entriesParquetPath),
      readFile(manifestPath, "utf8"),
    ]);
    const catalog = await loadCatalog({ entries, manifestText });
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest?.sectionRoles.advice?.name).toBe("advice");
    expect(catalog.manifest?.labelFamilies.chart?.name).toBe("chart");

    const ids = catalog.guidelines.map((guideline) => guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });

  it("loads raw parquet bytes", async () => {
    const buf = await readFile(entriesParquetPath);
    const bytes = new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);

    const catalog = await loadCatalog(bytes);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.guidelines[0]?.id).toBeTypeOf("string");
    assertCatalogLooksParsed(catalog);
  });

  it("loads caller-owned async buffers", async () => {
    const buf = await readFile(entriesParquetPath);
    const bytes = new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);
    const catalog = await loadCatalog({
      byteLength: bytes.byteLength,
      slice(start, end) {
        return bytes.slice(start, end).buffer;
      },
    });

    expect(catalog.length).toBeGreaterThan(0);
    assertCatalogLooksParsed(catalog);
  });

  it("rejects ambiguous manifest input", async () => {
    const [entries, manifestText] = await Promise.all([
      readFile(entriesParquetPath),
      readFile(manifestPath, "utf8"),
    ]);

    await expect(
      loadCatalog({
        entries,
        manifest: {
          markdown: manifestText,
          sectionRoles: {},
          labelFamilies: {},
        },
        manifestText,
      }),
    ).rejects.toThrow("Pass manifest or manifestText, not both.");
  });

  it("preserves index artifact bodies in release metadata", () => {
    const metadata = parseCatalogReleaseMetadata({
      version: "0.1.2",
      digest: "catalog-digest",
      artifacts: [
        {
          kind: "manifest",
          path: "MANIFEST.md",
          digest: "manifest-digest",
          bytes: 1,
        },
        {
          kind: "entries",
          path: "entries.parquet",
          digest: "entries-digest",
          bytes: 2,
        },
        {
          kind: "lancedb-index",
          path: "indexes/lancedb/openrouter/openai-text-embedding-3-large/index.tar.gz",
          digest: "index-digest",
          bytes: 3,
          format: "tar+gzip",
          table: "catalog_documents",
          catalog: {
            version: "0.1.2",
            digest: "catalog-digest",
          },
          embedding: {
            registry: "openai",
            provider: "openrouter",
            model: "openai/text-embedding-3-large",
            options: {
              name: "text-embedding-3-large",
              dim: 3072,
            },
          },
        },
        {
          kind: "lancedb-index",
          path: "indexes/lancedb/openrouter/openai-text-embedding-3-large/db",
          digest: "tree-digest",
          bytes: 4,
          format: "lancedb",
          table: "catalog_documents",
          uri: "s3://chartcoach/catalog/releases/0.1.2/catalog-digest/indexes/lancedb/openrouter/openai-text-embedding-3-large/db",
          catalog: {
            version: "0.1.2",
            digest: "catalog-digest",
          },
          embedding: {
            registry: "openai",
            provider: "openrouter",
            model: "openai/text-embedding-3-large",
            options: {
              name: "text-embedding-3-large",
              dim: 3072,
            },
          },
        },
      ],
    });

    const entriesArtifact = catalogArtifact(metadata, "entries");
    expect(catalogArtifactUrl("https://example.test/catalog/metadata.json", entriesArtifact)).toBe(
      "https://example.test/catalog/entries.parquet",
    );

    const indexArtifact = metadata.artifacts.find((item) => item.kind === "lancedb-index");
    expect(indexArtifact?.table).toBe("catalog_documents");
    expect(indexArtifact?.embedding).toEqual({
      registry: "openai",
      provider: "openrouter",
      model: "openai/text-embedding-3-large",
      options: {
        name: "text-embedding-3-large",
        dim: 3072,
      },
    });
    const directArtifact = metadata.artifacts.find(
      (item) => item.kind === "lancedb-index" && item.format === "lancedb",
    );
    expect(directArtifact?.uri).toBe(
      "s3://chartcoach/catalog/releases/0.1.2/catalog-digest/indexes/lancedb/openrouter/openai-text-embedding-3-large/db",
    );
  });

  it("exposes package-pinned default artifact URLs", () => {
    expect(DEFAULT_CATALOG.version).toBe("0.1.2");
    expect(DEFAULT_CATALOG.metadataUrl).toContain(DEFAULT_CATALOG.digest);
    expect(DEFAULT_CATALOG.entriesUrl).toBe(
      new URL("entries.parquet", DEFAULT_CATALOG.releaseRootUrl).toString(),
    );
    expect(DEFAULT_CATALOG.manifestUrl).toBe(
      new URL("MANIFEST.md", DEFAULT_CATALOG.releaseRootUrl).toString(),
    );
  });
});
