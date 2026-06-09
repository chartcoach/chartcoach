import { createServer, type Server } from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";
import type { AddressInfo } from "node:net";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vitest";

import { loadCatalog, parseCatalogReleaseMetadata } from "@chartcoach/catalog";
import { readCatalog } from "@chartcoach/catalog/server";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const bundleFixtureRoot = path.join(__dirname, "fixtures", "bundle");
const entriesParquetPath = path.join(bundleFixtureRoot, "entries.parquet");
const folderFixtureRoot = path.join(__dirname, "fixtures", "folder-catalog");

describe("entries parquet loading", () => {
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
    const catalog = await readCatalog(entriesParquetPath);
    expect(catalog.length).toBeGreaterThan(0);

    const ids = catalog.guidelines.map((guideline) => guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });

  it("loads from catalog bundle with manifest validation", async () => {
    const catalog = await readCatalog(bundleFixtureRoot);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest?.sectionRoles.advice?.name).toBe("advice");
    expect(catalog.manifest?.labelFamilies.chart?.name).toBe("chart");
    assertCatalogLooksParsed(catalog);
  });

  it("loads from bytes (Uint8Array)", async () => {
    const buf = await readFile(entriesParquetPath);
    const bytes = new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);

    const catalog = await loadCatalog(bytes);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.guidelines[0]?.id).toBeTypeOf("string");
    assertCatalogLooksParsed(catalog);
  });

  it("loads from authored entries folder", async () => {
    const catalog = await readCatalog(folderFixtureRoot);
    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest?.sectionRoles.advice?.name).toBe("advice");

    const ids = catalog.guidelines.map((guideline) => guideline.id);
    expect(new Set(ids).size).toBe(ids.length);
    assertCatalogLooksParsed(catalog);
  });

  it("loads from catalog metadata URL", async () => {
    await withFixtureServer(async (baseUrl) => {
      const catalog = await readCatalog(`${baseUrl}/metadata.json`);

      expect(catalog.length).toBe(1);
      expect(catalog.manifest?.sectionRoles.advice?.name).toBe("advice");
      assertCatalogLooksParsed(catalog);
    });
  });

  it("loads through a catalog metadata pointer URL", async () => {
    await withFixtureServer(async (baseUrl) => {
      const catalog = await readCatalog(`${baseUrl}/pointer/metadata.json`);

      expect(catalog.length).toBe(1);
      expect(catalog.manifest?.labelFamilies.chart?.name).toBe("chart");
      assertCatalogLooksParsed(catalog);
    });
  });

  it("preserves index artifact bodies in release metadata", () => {
    const metadata = parseCatalogReleaseMetadata({
      version: "0.0.0",
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
          path: "indexes/lancedb/openrouter/openai-text-embedding-3-large/catalog_documents.tar.gz",
          digest: "index-digest",
          bytes: 3,
          format: "tar+gzip",
          table: "catalog_documents",
          embedding: {
            registry: "openai",
            model: "openai/text-embedding-3-large",
          },
        },
      ],
    });

    const indexArtifact = metadata.artifacts.find((item) => item.kind === "lancedb-index");
    expect(indexArtifact?.table).toBe("catalog_documents");
    expect(indexArtifact?.embedding).toEqual({
      registry: "openai",
      model: "openai/text-embedding-3-large",
    });
  });
});

async function withFixtureServer(
  run: (baseUrl: string) => Promise<void>,
): Promise<void> {
  const server = createServer(async (request, response) => {
    const pathname = new URL(request.url ?? "/", "http://127.0.0.1").pathname;
    if (pathname === "/pointer/metadata.json") {
      const body = Buffer.from(
        JSON.stringify({
          kind: "chartcoach-release-pointer",
          target: "/metadata.json",
          version: "0.0.0",
          digest: "fixture-digest",
        }),
      );
      response.writeHead(200, {
        "content-length": body.length,
        "content-type": "application/json",
      });
      response.end(body);
      return;
    }
    const fileName = pathname === "/" ? "metadata.json" : pathname.slice(1);
    const filePath = path.join(bundleFixtureRoot, fileName);
    try {
      const data = await readFile(filePath);
      const range = request.headers.range;
      if (range) {
        const match = /^bytes=(\d+)-(\d+)?$/.exec(range);
        if (!match) {
          response.writeHead(416);
          response.end();
          return;
        }
        const start = Number(match[1]);
        const end = match[2] ? Number(match[2]) : data.length - 1;
        const body = data.subarray(start, end + 1);
        response.writeHead(206, {
          "accept-ranges": "bytes",
          "content-length": body.length,
          "content-range": `bytes ${start}-${end}/${data.length}`,
          "content-type": contentType(fileName),
        });
        response.end(body);
        return;
      }
      response.writeHead(200, {
        "accept-ranges": "bytes",
        "content-length": data.length,
        "content-type": contentType(fileName),
      });
      response.end(data);
    } catch {
      response.writeHead(404);
      response.end();
    }
  });
  await listen(server);
  const address = server.address() as AddressInfo;
  try {
    await run(`http://127.0.0.1:${address.port}`);
  } finally {
    await close(server);
  }
}

function listen(server: Server): Promise<void> {
  return new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
}

function close(server: Server): Promise<void> {
  return new Promise((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
}

function contentType(fileName: string): string {
  if (fileName.endsWith(".json")) return "application/json";
  if (fileName.endsWith(".md")) return "text/markdown; charset=utf-8";
  return "application/octet-stream";
}
