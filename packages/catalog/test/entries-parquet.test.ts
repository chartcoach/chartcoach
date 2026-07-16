import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vite-plus/test";

import {
  loadCatalog,
  open,
  openRelease,
  parseCatalogRelease,
  type CatalogRelease,
  type FetchLike,
} from "@chartcoach/catalog";
import { requireGuidelineFromWire } from "../src/catalog/wire";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const releaseFixtureRoot = path.join(__dirname, "..", "..", "..", "fixtures", "catalog-release");
const entriesParquetPath = path.join(releaseFixtureRoot, "entries.parquet");
const manifestPath = path.join(releaseFixtureRoot, "MANIFEST.md");
const invalidRowsPath = path.join(__dirname, "fixtures", "invalid-catalog-rows.json");
const artifactBaseUrl = "https://artifacts.chartcoach.dev";
const catalogUrl = `${artifactBaseUrl}/catalog.json`;

describe("catalog loading", () => {
  it("loads a compiled bundle and derives guideline markdown", async () => {
    const [entries, manifestText] = await Promise.all([
      readFile(entriesParquetPath),
      readFile(manifestPath, "utf8"),
    ]);

    const catalog = await loadCatalog({ entries, manifestText });

    expect(catalog.length).toBeGreaterThan(0);
    expect(catalog.manifest.sectionRoles.advice?.name).toBe("advice");
    expect(catalog.manifest.labelFamilies.chart?.name).toBe("chart");
    expect(catalog.guidelines[0]?.body).toContain("<!-- role:");
  });

  it("loads typed-array and async-buffer Parquet bytes", async () => {
    const buffer = await readFile(entriesParquetPath);
    const entries = new Uint8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);
    const manifestText = await readFile(manifestPath, "utf8");

    const typedArrayCatalog = await loadCatalog({ entries, manifestText });
    const asyncBufferCatalog = await loadCatalog({
      entries: {
        byteLength: entries.byteLength,
        slice(start, end) {
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
    const fixture = JSON.parse(await readFile(invalidRowsPath, "utf8")) as {
      row: Record<string, unknown>;
      cases: Array<{ name: string; patch: Record<string, unknown> }>;
    };

    for (const testCase of fixture.cases) {
      expect(
        () => requireGuidelineFromWire({ ...fixture.row, ...testCase.patch }),
        testCase.name,
      ).toThrow("Invalid catalog row format");
    }
  });
});

describe("published catalog releases", () => {
  it("opens the selected catalog release", async () => {
    const fixture = await fixtureRelease();

    const catalog = await open({ fetch: fetchFrom(catalogResponses(fixture)) });

    expect(catalog.require("direct-labels").id).toBe("direct-labels");
    expect(catalog.manifest.labelFamilies.chart?.name).toBe("chart");
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

    const catalog = await openRelease(releaseUrl, { fetch: fetchFrom(responses) });

    expect(catalog.require("direct-labels").body).toContain("<!-- role: advice -->");
  });

  it("rejects a release whose digest differs from its artifact set", async () => {
    const fixture = await fixtureRelease();
    const digest = "0".repeat(64);
    const release = { ...fixture.release, digest };

    await expect(
      openRelease(releaseUrlFor(digest), {
        fetch: fetchFrom(releaseResponses({ ...fixture, release }, digest)),
      }),
    ).rejects.toThrow("does not match its artifact set");
  });

  it("rejects artifact bytes that differ from the release descriptor", async () => {
    const fixture = await fixtureRelease();
    const entries = Buffer.from(fixture.entries);
    entries[0] ^= 0xff;

    await expect(
      openRelease(releaseUrlFor(fixture.release.digest), {
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

    await expect(openRelease(releaseUrl, { fetch: fetchFrom(responses) })).rejects.toThrow(
      "Catalog manifest must contain valid UTF-8",
    );
  });

  it("bounds release JSON reads", async () => {
    const digest = "a".repeat(64);
    const oversized = new Uint8Array(1024 * 1024 + 1);
    const fetch: FetchLike = async () => new Response(oversized);

    await expect(openRelease(releaseUrlFor(digest), { fetch })).rejects.toThrow(
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

    await expect(openRelease(releaseUrl, { fetch })).rejects.toThrow(
      "Failed to load catalog resource.",
    );
  });
});

describe("release records", () => {
  it("accepts opaque artifact paths and requires the core bundle paths", async () => {
    const releaseRecord = await readReleaseRecord();
    const artifacts = releaseRecord.artifacts as Record<string, unknown>;
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
    const releaseRecord = await readReleaseRecord();
    const artifacts = releaseRecord.artifacts as Record<string, unknown>;
    const entry = artifacts["entries.parquet"] as Record<string, unknown>;

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

async function fixtureRelease(): Promise<{
  release: CatalogRelease;
  manifest: string;
  entries: Buffer;
}> {
  const [manifest, entries, releaseRecord] = await Promise.all([
    readFile(manifestPath, "utf8"),
    readFile(entriesParquetPath),
    readReleaseRecord(),
  ]);
  return {
    manifest,
    entries,
    release: parseCatalogRelease(releaseRecord),
  };
}

function catalogResponses(
  fixture: Awaited<ReturnType<typeof fixtureRelease>>,
): Map<string, BodyInit> {
  const responses = releaseResponses(fixture);
  responses.set(catalogUrl, JSON.stringify(fixture.release));
  return responses;
}

function releaseResponses(
  fixture: Awaited<ReturnType<typeof fixtureRelease>>,
  digest = fixture.release.digest,
): Map<string, BodyInit> {
  const releaseUrl = releaseUrlFor(digest);
  return new Map<string, BodyInit>([
    [releaseUrl, JSON.stringify(fixture.release)],
    [new URL("MANIFEST.md", releaseUrl).toString(), fixture.manifest],
    [new URL("entries.parquet", releaseUrl).toString(), responseBytes(fixture.entries)],
  ]);
}

function releaseUrlFor(digest: string): string {
  return `https://artifacts.chartcoach.dev/catalog/releases/${digest}/release.json`;
}

function responseBytes(bytes: Uint8Array): ArrayBuffer {
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) as ArrayBuffer;
}

function releaseWithArtifact(
  release: CatalogRelease,
  path: string,
  update: Partial<CatalogRelease["artifacts"][string]>,
): CatalogRelease {
  const artifacts = {
    ...release.artifacts,
    [path]: { ...release.artifacts[path]!, ...update },
  };
  return {
    schema_version: 1,
    artifacts,
    digest: releaseDigest(artifacts),
  };
}

function releaseDigest(artifacts: CatalogRelease["artifacts"]): string {
  const canonicalArtifacts = Object.fromEntries(
    Object.entries(artifacts)
      .sort(([left], [right]) => (left === right ? 0 : left < right ? -1 : 1))
      .map(([artifactPath, artifact]) => [
        artifactPath,
        { bytes: artifact.bytes, sha256: artifact.sha256 },
      ]),
  );
  return createHash("sha256")
    .update(JSON.stringify({ artifacts: canonicalArtifacts, schema_version: 1 }))
    .digest("hex");
}

function fetchFrom(responses: Map<string, BodyInit>): FetchLike {
  return async (input) => {
    const body = responses.get(input.toString());
    if (body === undefined) return new Response("not found", { status: 404 });
    return new Response(body);
  };
}

async function readReleaseRecord(): Promise<Record<string, unknown>> {
  return JSON.parse(
    await readFile(path.join(releaseFixtureRoot, "release.json"), "utf8"),
  ) as Record<string, unknown>;
}
