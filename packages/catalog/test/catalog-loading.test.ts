import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vite-plus/test";

import {
  loadCatalog,
  loadCatalogData,
  openCatalog,
  parseCatalogRelease,
  type FetchLike,
  type JsonObject,
} from "@chartcoach/catalog";
import { requireGuidelineFromWire } from "../src/catalog/wire";
import {
  catalogResponses,
  entriesParquetPath,
  fetchFrom,
  fixtureRelease,
  manifestPath,
  releaseDigest,
  releaseResponses,
  releaseUrlFor,
  releaseWithArtifact,
  responseBytes,
} from "./catalog-testkit";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const invalidRowsPath = path.join(
  __dirname,
  "..",
  "..",
  "..",
  "fixtures",
  "catalog-contract",
  "invalid-catalog-rows.json",
);

type InvalidRowsFixture = {
  row: JsonObject;
  cases: Array<{ name: string; patch: JsonObject }>;
};

describe("catalog loading", () => {
  it("loads a compiled bundle and derives guideline markdown", async () => {
    const [entries, manifestText] = await Promise.all([
      readFile(entriesParquetPath),
      readFile(manifestPath, "utf8"),
    ]);

    const catalog = await loadCatalogData({ entries, manifestText });

    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest.sectionRoles.advice?.name).toBe("advice");
    expect(catalog.manifest.labelFamilies.chart?.name).toBe("chart");
    expect(catalog.guidelines[0]?.body).toContain("<!-- role:");
    expect(catalog.release).toBeUndefined();
    expect(catalog.releaseUrl).toBeUndefined();
  });

  it("loads typed-array and async-buffer Parquet bytes", async () => {
    const buffer = await readFile(entriesParquetPath);
    const entries = new Uint8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);
    const manifestText = await readFile(manifestPath, "utf8");

    const typedArrayCatalog = await loadCatalogData({ entries, manifestText });
    const asyncBufferCatalog = await loadCatalogData({
      entries: {
        byteLength: entries.byteLength,
        slice(start: number, end?: number) {
          return entries.slice(start, end).buffer;
        },
      },
      manifestText,
    });

    expect(asyncBufferCatalog.guidelines.map(({ id }) => id)).toEqual(
      typedArrayCatalog.guidelines.map(({ id }) => id),
    );
  });

  it("rejects invalid compiled rows", async () => {
    const fixture: InvalidRowsFixture = JSON.parse(await readFile(invalidRowsPath, "utf8"));

    for (const testCase of fixture.cases) {
      expect(
        () => requireGuidelineFromWire({ ...fixture.row, ...testCase.patch }),
        testCase.name,
      ).toThrow("Invalid catalog row format");
    }
  });
});

describe("catalog release loading", () => {
  it("verifies caller-provided release bytes", async () => {
    const fixture = await fixtureRelease();
    const catalog = await loadCatalog({
      entries: fixture.entries,
      manifest: Buffer.from(fixture.manifest),
      release: fixture.release,
      releaseUrl: `file:///catalog/releases/${fixture.release.digest}/release.json`,
    });

    expect(catalog.release?.digest).toBe(fixture.release.digest);
    expect(catalog.releaseUrl).toBe(
      `file:///catalog/releases/${fixture.release.digest}/release.json`,
    );
  });

  it("bounds caller-provided release artifacts", async () => {
    const fixture = await fixtureRelease();
    const release = releaseWithArtifact(fixture.release, "entries.parquet", {
      bytes: 64 * 1024 * 1024 + 1,
    });

    await expect(
      loadCatalog({
        entries: fixture.entries,
        manifest: Buffer.from(fixture.manifest),
        release,
        releaseUrl: `file:///catalog/releases/${release.digest}/release.json`,
      }),
    ).rejects.toThrow("Catalog artifact exceeds size limit: entries.parquet");
  });

  it("requires an absolute release locator for caller-provided bytes", async () => {
    const fixture = await fixtureRelease();

    await expect(
      loadCatalog({
        entries: fixture.entries,
        manifest: Buffer.from(fixture.manifest),
        release: fixture.release,
        releaseUrl: "relative/release.json",
      }),
    ).rejects.toThrow("Catalog release URL must be absolute");
  });

  it("opens the selected catalog release", async () => {
    const fixture = await fixtureRelease();

    const catalog = await openCatalog(undefined, {
      fetch: fetchFrom(catalogResponses(fixture)),
    });

    expect(catalog.require("direct-labels").id).toBe("direct-labels");
    expect(catalog.manifest.labelFamilies.chart?.name).toBe("chart");
    expect(catalog.release).toEqual(fixture.release);
    expect(catalog.release).not.toBe(fixture.release);
    expect(catalog.releaseUrl).toBe(releaseUrlFor(fixture.release.digest));
    expect(Object.isFrozen(catalog.release)).toBe(true);
    expect(Object.isFrozen(catalog.release?.artifacts)).toBe(true);
    expect((await catalog.describe()).release_digest).toBe(fixture.release.digest);
  });

  it("opens an exact release below a custom URL prefix", async () => {
    const fixture = await fixtureRelease();
    const releaseUrl =
      `https://catalog.example.test/team/artifacts/catalog/releases/` +
      `${fixture.release.digest}/release.json`;
    const responses = new Map<string, BodyInit>([
      [releaseUrl, JSON.stringify(fixture.release)],
      [new URL("MANIFEST.md", releaseUrl).toString(), fixture.manifest],
      [new URL("entries.parquet", releaseUrl).toString(), responseBytes(fixture.entries)],
    ]);

    const catalog = await openCatalog(releaseUrl, { fetch: fetchFrom(responses) });

    expect(catalog.require("direct-labels").body).toContain("<!-- role: advice -->");
    expect(catalog.release?.digest).toBe(fixture.release.digest);
    expect(catalog.releaseUrl).toBe(releaseUrl);
  });

  it("rejects a release whose digest differs from its artifact set", async () => {
    const fixture = await fixtureRelease();
    const digest = "0".repeat(64);
    const release = { ...fixture.release, digest };

    await expect(
      openCatalog(releaseUrlFor(digest), {
        fetch: fetchFrom(releaseResponses({ ...fixture, release }, digest)),
      }),
    ).rejects.toThrow("does not match its artifact set");
  });

  it("rejects profile metadata without its index archive", async () => {
    const fixture = await fixtureRelease();
    const artifacts = {
      ...fixture.release.artifacts,
      "profiles/minilm-normalized/profile.json": {
        sha256: "c".repeat(64),
        bytes: 1,
      },
    };
    const release = {
      schema_version: 1 as const,
      artifacts,
      digest: releaseDigest(artifacts),
    };

    await expect(
      openCatalog(releaseUrlFor(release.digest), {
        fetch: fetchFrom(releaseResponses({ ...fixture, release })),
      }),
    ).rejects.toThrow("missing index.tar.gz");
  });

  it("rejects a self-consistent release under another digest path", async () => {
    const fixture = await fixtureRelease();
    const wrongDigest = "0".repeat(64);

    await expect(
      openCatalog(releaseUrlFor(wrongDigest), {
        fetch: fetchFrom(releaseResponses(fixture, wrongDigest)),
      }),
    ).rejects.toThrow("digest-addressed location");
  });

  it("composes a caller abort signal with catalog requests", async () => {
    const controller = new AbortController();
    const fetch: FetchLike = async (_input, init) => {
      controller.abort();
      if (init?.signal?.aborted) throw new DOMException("Aborted", "AbortError");
      return new Response();
    };

    await expect(
      openCatalog(releaseUrlFor("a".repeat(64)), {
        fetch,
        signal: controller.signal,
      }),
    ).rejects.toMatchObject({ name: "AbortError" });
  });

  it("rejects artifact bytes that differ from the release descriptor", async () => {
    const fixture = await fixtureRelease();
    const entries = Buffer.from(fixture.entries);
    entries[0] ^= 0xff;

    await expect(
      openCatalog(releaseUrlFor(fixture.release.digest), {
        fetch: fetchFrom(releaseResponses({ ...fixture, entries })),
      }),
    ).rejects.toThrow("Catalog artifact SHA-256 mismatch: entries.parquet");
  });

  it("rejects a manifest that is not valid UTF-8", async () => {
    const fixture = await fixtureRelease();
    const manifest = new Uint8Array([0xc3, 0x28]);
    const release = releaseWithArtifact(fixture.release, "MANIFEST.md", {
      bytes: manifest.byteLength,
      sha256: createHash("sha256").update(manifest).digest("hex"),
    });
    const releaseUrl = releaseUrlFor(release.digest);
    const responses = releaseResponses({ ...fixture, release });
    responses.set(new URL("MANIFEST.md", releaseUrl).toString(), manifest);

    await expect(openCatalog(releaseUrl, { fetch: fetchFrom(responses) })).rejects.toThrow(
      "Catalog manifest must contain valid UTF-8",
    );
  });

  it("bounds release JSON reads", async () => {
    const digest = "a".repeat(64);
    const oversized = new Uint8Array(1024 * 1024 + 1);
    const fetch: FetchLike = async () => new Response(oversized);

    await expect(openCatalog(releaseUrlFor(digest), { fetch })).rejects.toThrow(
      "Catalog JSON exceeds size limit",
    );
  });

  it("keeps request failures independent of release URL credentials", async () => {
    const digest = "a".repeat(64);
    const releaseUrl =
      `https://catalog-user:catalog-password@artifacts.example.test/catalog/releases/` +
      `${digest}/release.json?signed=token#fragment`;
    const fetch = async () => {
      throw new Error(`Failed to fetch ${releaseUrl}`);
    };

    await expect(openCatalog(releaseUrl, { fetch })).rejects.toThrow(
      "Failed to load catalog resource.",
    );
  });

  it("exposes a sanitized exact release URL", async () => {
    const fixture = await fixtureRelease();
    const releaseUrl =
      `https://catalog-user:catalog-password@artifacts.example.test/catalog/releases/` +
      `${fixture.release.digest}/release.json?signed=token#fragment`;
    const responses = new Map<string, BodyInit>([
      [releaseUrl, JSON.stringify(fixture.release)],
      [new URL("MANIFEST.md", releaseUrl).toString(), fixture.manifest],
      [new URL("entries.parquet", releaseUrl).toString(), responseBytes(fixture.entries)],
    ]);

    const catalog = await openCatalog(releaseUrl, { fetch: fetchFrom(responses) });

    expect(catalog.releaseUrl).toBe(
      `https://artifacts.example.test/catalog/releases/${fixture.release.digest}/release.json`,
    );
  });

  it("cancels unsuccessful response bodies", async () => {
    const digest = "a".repeat(64);
    let cancelled = false;
    const fetch: FetchLike = async () =>
      new Response(
        new ReadableStream({
          cancel() {
            cancelled = true;
          },
        }),
        { status: 503 },
      );

    await expect(openCatalog(releaseUrlFor(digest), { fetch })).rejects.toThrow("HTTP 503");
    expect(cancelled).toBe(true);
  });

  it("requires a catalog descriptor URL", async () => {
    await expect(openCatalog("https://example.test/catalog/")).rejects.toThrow(
      "must name catalog.json or release.json",
    );
    await expect(openCatalog("file:///tmp/catalog.json")).rejects.toThrow("must use HTTP or HTTPS");
  });
});

describe("release records", () => {
  it("accepts opaque artifact paths and requires the core bundle paths", async () => {
    const releaseRecord = (await fixtureRelease()).release;
    const artifacts = releaseRecord.artifacts;
    const opaque = { sha256: "4".repeat(64), bytes: 64 };

    expect(
      parseCatalogRelease({
        ...releaseRecord,
        artifacts: { ...artifacts, "thumbnails/overview.png": opaque },
      }).artifacts["thumbnails/overview.png"],
    ).toEqual(opaque);
    for (const path of ["MANIFEST.md", "entries.parquet"]) {
      const { [path]: _, ...missing } = artifacts;
      expect(() =>
        parseCatalogRelease({
          ...releaseRecord,
          artifacts: missing,
        }),
      ).toThrow(`missing artifact: ${path}`);
    }
  });

  it("rejects malformed artifact paths and descriptors", async () => {
    const releaseRecord = (await fixtureRelease()).release;
    const artifacts = releaseRecord.artifacts;
    const entry = artifacts["entries.parquet"]!;

    expect(() =>
      parseCatalogRelease({
        ...releaseRecord,
        artifacts: { ...artifacts, "../entries.parquet": entry },
      }),
    ).toThrow("must be relative");
    expect(() =>
      parseCatalogRelease({
        ...releaseRecord,
        artifacts: {
          ...artifacts,
          "entries.parquet": { ...entry, format: "parquet" },
        },
      }),
    ).toThrow("unsupported fields");
  });
});
