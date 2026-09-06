import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  loadCatalog,
  parseCatalogRelease,
  type CatalogRelease,
  type FetchLike,
  type JsonValue,
} from "@chartcoach/catalog";

export const releaseFixtureRoot = path.join(
  path.dirname(fileURLToPath(import.meta.url)),
  "..",
  "..",
  "..",
  "fixtures",
  "catalog-release",
);
export const entriesParquetPath = path.join(releaseFixtureRoot, "entries.parquet");
export const manifestPath = path.join(releaseFixtureRoot, "MANIFEST.md");
export const releaseFixtureUrl = pathToFileURL(path.join(releaseFixtureRoot, "release.json"));
export const artifactBaseUrl = "https://files.peter.gy/catalog/chartcoach";
export const catalogUrl = `${artifactBaseUrl}/catalog.json`;

export type CatalogFixture = Readonly<{
  manifest: string;
  entries: Buffer;
  release: CatalogRelease;
}>;

export async function fixtureRelease(): Promise<CatalogFixture> {
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

export async function fixtureCatalog() {
  const fixture = await fixtureRelease();
  return loadCatalog({
    entries: fixture.entries,
    manifest: Buffer.from(fixture.manifest),
    release: fixture.release,
    releaseUrl: releaseFixtureUrl,
  });
}

export function catalogResponses(fixture: CatalogFixture): Map<string, BodyInit> {
  const responses = releaseResponses(fixture);
  responses.set(catalogUrl, JSON.stringify(fixture.release));
  return responses;
}

export function releaseResponses(
  fixture: CatalogFixture,
  digest = fixture.release.digest,
): Map<string, BodyInit> {
  const releaseUrl = releaseUrlFor(digest);
  return new Map<string, BodyInit>([
    [releaseUrl, JSON.stringify(fixture.release)],
    [new URL("MANIFEST.md", releaseUrl).toString(), fixture.manifest],
    [new URL("entries.parquet", releaseUrl).toString(), responseBytes(fixture.entries)],
  ]);
}

export function releaseUrlFor(digest: string): string {
  return `${artifactBaseUrl}/catalog/releases/${digest}/release.json`;
}

export function responseBytes(bytes: Uint8Array): ArrayBuffer {
  return Uint8Array.from(bytes).buffer;
}

export function releaseWithArtifact(
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

export function releaseDigest(artifacts: CatalogRelease["artifacts"]): string {
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

export function fetchFrom(responses: Map<string, BodyInit>): FetchLike {
  return async (input) => {
    const body = responses.get(input.toString());
    if (body === undefined) return new Response("not found", { status: 404 });
    return new Response(body);
  };
}

export function countingFetch(
  responses: Map<string, BodyInit>,
  requests: Map<string, number>,
): FetchLike {
  const fetch = fetchFrom(responses);
  return async (input, init) => {
    const url = input.toString();
    requests.set(url, (requests.get(url) ?? 0) + 1);
    return fetch(input, init);
  };
}

async function readReleaseRecord(): Promise<JsonValue> {
  return JSON.parse(await readFile(path.join(releaseFixtureRoot, "release.json"), "utf8"));
}
