import { cp, mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { afterEach, beforeEach, describe, expect, it, vi } from "vite-plus/test";
import { parseCatalogRelease, type JsonValue } from "@chartcoach/catalog";

const releaseFixtureRoot = new URL("../../../fixtures/catalog-release/", import.meta.url);

const artifactBaseUrl = "https://artifacts.chartcoach.dev";

describe("site catalog location loading", () => {
  beforeEach(() => {
    vi.resetModules();
    vi.stubEnv("CHARTCOACH_SITE_CATALOG", "");
    vi.stubEnv("CF_PAGES", "");
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.unstubAllEnvs();
  });

  it("reuses one published catalog load across site consumers", async () => {
    const { loadSiteCatalog } = await catalogLocationModule();
    const fixture = await fixtureRelease();
    const responses = releaseResponses(fixture);
    const catalogUrl = `${artifactBaseUrl}/catalog.json`;
    const fetchCatalog = vi.fn(fetchFrom(responses));
    vi.stubGlobal("fetch", fetchCatalog);

    const firstLoad = loadSiteCatalog(new URL(".", import.meta.url), catalogUrl);
    const secondLoad = loadSiteCatalog(new URL("../", import.meta.url), catalogUrl);

    const [catalog, reusedCatalog] = await Promise.all([firstLoad, secondLoad]);

    expect(fetchCatalog.mock.calls.filter(([url]) => requestUrl(url) === catalogUrl)).toHaveLength(
      1,
    );
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
    expect(reusedCatalog).toBe(catalog);
  });

  it("retries after a published catalog load fails", async () => {
    const { loadSiteCatalog } = await catalogLocationModule();
    const fixture = await fixtureRelease();
    const digest = "0".repeat(64);
    const release = { ...fixture.release, digest };
    const responses = releaseResponses({ ...fixture, release });
    vi.stubGlobal("fetch", fetchFrom(responses));

    const catalogUrl = `${artifactBaseUrl}/catalog.json`;
    await expect(loadSiteCatalog(new URL(".", import.meta.url), catalogUrl)).rejects.toThrow(
      "Catalog release digest " + digest + " does not match its artifact set",
    );

    const validResponses = releaseResponses(fixture);
    vi.stubGlobal("fetch", fetchFrom(validResponses));

    const catalog = await loadSiteCatalog(new URL(".", import.meta.url), catalogUrl);
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
  });

  it("records the catalog entry path for published entries", async () => {
    const { catalogLocationRecordPath } = await catalogLocationModule();
    const location = `${artifactBaseUrl}/catalog.json`;
    expect(
      catalogLocationRecordPath(new URL(".", import.meta.url), location, "direct-labels"),
    ).toBe(`${location}#direct-labels`);
  });

  it("uses the shared release fixture for local builds", async () => {
    const { loadSiteCatalog, resolveSiteCatalogLocation } = await catalogLocationModule();
    const root = new URL("../", import.meta.url);

    const location = resolveSiteCatalogLocation(root);
    const catalog = await loadSiteCatalog(root);

    expect(location).toBe(fileURLToPath(releaseFixtureRoot).replace(/\/$/, ""));
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
    expect(catalog.release?.digest).toBe((await fixtureRelease()).release.digest);
  });

  it("verifies local release artifacts", async () => {
    const { loadSiteCatalog } = await catalogLocationModule();
    const directory = await mkdtemp(path.join(tmpdir(), "chartcoach-site-release-"));

    try {
      await cp(fileURLToPath(releaseFixtureRoot), directory, { recursive: true });
      await writeFile(path.join(directory, "entries.parquet"), "corrupt");

      await expect(loadSiteCatalog(new URL(".", import.meta.url), directory)).rejects.toThrow(
        /byte count|SHA-256/,
      );
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  });

  it("loads descriptor-free local bundles as catalog data", async () => {
    const { loadSiteCatalog } = await catalogLocationModule();
    const directory = await mkdtemp(path.join(tmpdir(), "chartcoach-site-bundle-"));

    try {
      await Promise.all([
        cp(
          fileURLToPath(new URL("entries.parquet", releaseFixtureRoot)),
          path.join(directory, "entries.parquet"),
        ),
        cp(
          fileURLToPath(new URL("MANIFEST.md", releaseFixtureRoot)),
          path.join(directory, "MANIFEST.md"),
        ),
      ]);

      const catalog = await loadSiteCatalog(new URL(".", import.meta.url), directory);

      expect(catalog.release).toBeUndefined();
      expect(catalog.require("direct-labels").id).toBe("direct-labels");
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  });

  it("opens a local deployed root through its selected release", async () => {
    const { catalogLocationRecordPath, catalogLocationWatchFiles, loadSiteCatalog } =
      await catalogLocationModule();

    const fixture = await fixtureRelease();
    const directory = await mkdtemp(path.join(tmpdir(), "chartcoach-site-deployed-"));

    try {
      const releaseRoot = path.join(directory, "catalog", "releases", fixture.release.digest);
      await mkdir(path.dirname(releaseRoot), { recursive: true });
      await cp(fileURLToPath(releaseFixtureRoot), releaseRoot, { recursive: true });
      await writeFile(path.join(directory, "catalog.json"), JSON.stringify(fixture.release));

      const catalog = await loadSiteCatalog(new URL(".", import.meta.url), directory);

      expect(catalog.release?.digest).toBe(fixture.release.digest);
      expect(catalog.releaseUrl).toBe(
        pathToFileURL(path.join(releaseRoot, "release.json")).toString(),
      );
      expect(catalogLocationWatchFiles(new URL(".", import.meta.url), directory)).toContain(
        path.join(directory, "catalog.json"),
      );
      expect(
        catalogLocationRecordPath(new URL(".", import.meta.url), directory, "direct-labels"),
      ).toContain(`catalog/releases/${fixture.release.digest}/entries.parquet#direct-labels`);
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  });

  it("rejects ambiguous local deployment descriptors", async () => {
    const { loadSiteCatalog } = await catalogLocationModule();
    const fixture = await fixtureRelease();
    const directory = await mkdtemp(path.join(tmpdir(), "chartcoach-site-ambiguous-"));

    try {
      const descriptor = JSON.stringify(fixture.release);
      await Promise.all([
        writeFile(path.join(directory, "catalog.json"), descriptor),
        writeFile(path.join(directory, "release.json"), descriptor),
      ]);

      await expect(loadSiteCatalog(new URL(".", import.meta.url), directory)).rejects.toThrow(
        "both catalog.json and release.json",
      );
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  });

  it("requires an exact catalog location for Cloudflare Pages builds", async () => {
    vi.stubEnv("CF_PAGES", "1");
    const { resolveSiteCatalogLocation } = await catalogLocationModule();

    expect(() => resolveSiteCatalogLocation(new URL("../", import.meta.url))).toThrow(
      "CHARTCOACH_SITE_CATALOG must name an exact release for deployment",
    );

    vi.stubEnv("CHARTCOACH_SITE_CATALOG", `${artifactBaseUrl}/catalog.json`);
    expect(() => resolveSiteCatalogLocation(new URL("../", import.meta.url))).toThrow(
      "must name an exact HTTPS release.json URL for deployment",
    );

    vi.stubEnv(
      "CHARTCOACH_SITE_CATALOG",
      `${artifactBaseUrl}/catalog/releases/latest/release.json`,
    );
    expect(() => resolveSiteCatalogLocation(new URL("../", import.meta.url))).toThrow(
      "must name an exact HTTPS release.json URL for deployment",
    );

    const releaseUrl = `${artifactBaseUrl}/catalog/releases/${"a".repeat(64)}/release.json`;
    vi.stubEnv("CHARTCOACH_SITE_CATALOG", releaseUrl);
    expect(resolveSiteCatalogLocation(new URL("../", import.meta.url))).toBe(releaseUrl);

    vi.stubEnv("CHARTCOACH_SITE_CATALOG", releaseUrl.replace("https://", "http://"));
    expect(() => resolveSiteCatalogLocation(new URL("../", import.meta.url))).toThrow(
      "must name an exact HTTPS release.json URL for deployment",
    );
  });

  it("loads an exact release URL without resolving it as a local path", async () => {
    const { catalogLocationWatchFiles, loadSiteCatalog, resolveCatalogLocation } =
      await catalogLocationModule();

    const fixture = await fixtureRelease();
    const releaseUrl = releaseUrlFor(fixture.release.digest);
    vi.stubGlobal("fetch", fetchFrom(releaseResponses(fixture)));
    const root = new URL(".", import.meta.url);

    const catalog = await loadSiteCatalog(root, releaseUrl);

    expect(resolveCatalogLocation(releaseUrl, root)).toBe(releaseUrl);
    expect(catalogLocationWatchFiles(root, releaseUrl)).toEqual([]);
    expect(catalog.require("direct-labels").id).toBe("direct-labels");
  });
});

function catalogLocationModule() {
  return import("../src/config/catalog-location");
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
