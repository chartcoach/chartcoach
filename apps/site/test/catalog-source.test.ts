import { readFile } from "node:fs/promises";

import { afterEach, beforeEach, describe, expect, it, vi } from "vite-plus/test";
import { parseCatalogRelease, type JsonValue } from "@chartcoach/catalog";

const releaseFixtureRoot = new URL("../../../fixtures/catalog-release/", import.meta.url);
const artifactBaseUrl = "https://files.peter.gy/catalog/chartcoach";

describe("site catalog source loading", () => {
  beforeEach(() => {
    vi.resetModules();
    vi.stubEnv("CHARTCOACH_SITE_CATALOG_SOURCE", "");
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.unstubAllEnvs();
  });

  it("reuses one published catalog load across site consumers", async () => {
    const { loadSiteCatalog } = await catalogSourceModule();
    const fixture = await fixtureRelease();
    const responses = releaseResponses(fixture);
    const catalogUrl = `${artifactBaseUrl}/catalog.json`;
    const fetchCatalog = vi.fn(fetchFrom(responses));
    vi.stubGlobal("fetch", fetchCatalog);

    const firstLoad = loadSiteCatalog(new URL(".", import.meta.url));
    const secondLoad = loadSiteCatalog(new URL("../", import.meta.url));

    const [catalog, reusedCatalog] = await Promise.all([firstLoad, secondLoad]);

    expect(fetchCatalog.mock.calls.filter(([url]) => requestUrl(url) === catalogUrl)).toHaveLength(
      1,
    );
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
    expect(reusedCatalog.require("direct-labels").id).toBe("direct-labels");
    expect(catalog.manifest.sectionRoles.advice?.name).toBe("advice");
    expect(catalog.manifest.labelFamilies.chart?.name).toBe("chart");
  });

  it("retries after a published catalog load fails", async () => {
    const { loadSiteCatalog } = await catalogSourceModule();
    const fixture = await fixtureRelease();
    const digest = "0".repeat(64);
    const release = { ...fixture.release, digest };
    const responses = releaseResponses({ ...fixture, release });
    vi.stubGlobal("fetch", fetchFrom(responses));

    await expect(loadSiteCatalog(new URL(".", import.meta.url))).rejects.toThrow(
      "Catalog release digest " + digest + " does not match its artifact set",
    );

    const validResponses = releaseResponses(fixture);
    vi.stubGlobal("fetch", fetchFrom(validResponses));

    const catalog = await loadSiteCatalog(new URL(".", import.meta.url));
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
  });

  it("records the catalog entry path for published entries", async () => {
    const { catalogSourceRecordPath } = await catalogSourceModule();
    expect(catalogSourceRecordPath(new URL(".", import.meta.url), undefined, "direct-labels")).toBe(
      "chartcoach://catalog.json#direct-labels",
    );
  });

  it("loads an exact release URL without resolving it as a local path", async () => {
    const { catalogSourceWatchFiles, loadSiteCatalog, resolveCatalogSource } =
      await catalogSourceModule();
    const fixture = await fixtureRelease();
    const releaseUrl = releaseUrlFor(fixture.release.digest);
    vi.stubGlobal("fetch", fetchFrom(releaseResponses(fixture)));
    const root = new URL(".", import.meta.url);

    const catalog = await loadSiteCatalog(root, releaseUrl);

    expect(resolveCatalogSource(releaseUrl, root)).toBe(releaseUrl);
    expect(catalogSourceWatchFiles(root, releaseUrl)).toEqual([]);
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
  });
});

function catalogSourceModule() {
  return import("../src/config/catalog-source");
}

async function fixtureRelease() {
  const [manifest, entries, release] = await Promise.all([
    readFile(new URL("MANIFEST.md", releaseFixtureRoot), "utf8"),
    readFile(new URL("entries.parquet", releaseFixtureRoot)),
    readJsonFixture("release.json"),
  ]);
  return {
    manifest,
    entries,
    release: parseCatalogRelease(release),
  };
}

function releaseUrlFor(digest: string): string {
  return `${artifactBaseUrl}/catalog/releases/${digest}/release.json`;
}

function releaseResponses(
  fixture: Awaited<ReturnType<typeof fixtureRelease>>,
): Map<string, BodyInit> {
  const releaseUrl = releaseUrlFor(fixture.release.digest);
  return new Map<string, BodyInit>([
    [`${artifactBaseUrl}/catalog.json`, JSON.stringify(fixture.release)],
    [releaseUrl, JSON.stringify(fixture.release)],
    [new URL("MANIFEST.md", releaseUrl).toString(), fixture.manifest],
    [new URL("entries.parquet", releaseUrl).toString(), responseBytes(fixture.entries)],
  ]);
}

function responseBytes(bytes: Uint8Array): ArrayBuffer {
  return Uint8Array.from(bytes).buffer;
}

function fetchFrom(responses: Map<string, BodyInit>) {
  return async (url: string | URL | Request) => {
    const body = responses.get(requestUrl(url));
    if (body === undefined) return new Response("not found", { status: 404 });
    return new Response(body);
  };
}

function requestUrl(input: string | URL | Request): string {
  return input instanceof Request ? input.url : input.toString();
}

async function readJsonFixture(name: string): Promise<JsonValue> {
  return JSON.parse(await readFile(new URL(name, releaseFixtureRoot), "utf8"));
}
