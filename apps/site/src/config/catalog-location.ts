import { existsSync, readFileSync, statSync } from "node:fs";
import { readFile, stat } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  loadCatalog,
  loadCatalogData,
  openCatalog,
  parseCatalogRelease,
  type Catalog,
  type CatalogRelease,
} from "@chartcoach/catalog";

const SITE_CATALOG_LOCATION_ENV = "CHARTCOACH_SITE_CATALOG";
const LOCAL_CATALOG_LOCATION = "../../fixtures/catalog-release";
const CF_PAGES_ENV = "CF_PAGES";
const MAX_RELEASE_JSON_BYTES = 1024 * 1024;
const MAX_CORE_ARTIFACT_BYTES = 64 * 1024 * 1024;
const remoteCatalogs = new Map<string, Promise<Catalog>>();

type LocalCatalogLayout =
  | { kind: "bundle"; root: string }
  | {
      kind: "release";
      root: string;
      descriptor: string;
      release: CatalogRelease;
      selection?: string;
    };

export function resolveSiteCatalogLocation(root: URL): string {
  const location = process.env[SITE_CATALOG_LOCATION_ENV];
  const deployment = process.env[CF_PAGES_ENV] === "1";
  if (location?.trim()) {
    const resolved = resolveCatalogLocation(location, root);
    if (deployment && !isExactRemoteRelease(resolved)) {
      throw new Error(
        `${SITE_CATALOG_LOCATION_ENV} must name an exact HTTPS release.json URL for deployment.`,
      );
    }
    return resolved;
  }
  if (deployment) {
    throw new Error(`${SITE_CATALOG_LOCATION_ENV} must name an exact release for deployment.`);
  }
  return resolveCatalogLocation(LOCAL_CATALOG_LOCATION, root);
}

export function resolveCatalogLocation(location: string, root: URL): string {
  const scheme = locationScheme(location);
  if (scheme === "http" || scheme === "https") return new URL(location).toString();
  if (scheme === "file") return fileURLToPath(location);
  if (scheme !== undefined) throw new Error(`Unsupported catalog location scheme: ${scheme}.`);
  return path.resolve(fileURLToPath(root), expandHome(location));
}

export function loadSiteCatalog(root: URL, location?: string): Promise<Catalog> {
  const catalogLocation = location
    ? resolveCatalogLocation(location, root)
    : resolveSiteCatalogLocation(root);
  if (isRemoteCatalogLocation(catalogLocation)) return loadRemoteCatalog(catalogLocation);
  return loadLocalCatalog(catalogLocation);
}

export function catalogLocationWatchFiles(root: URL, location?: string): string[] {
  const catalogLocation = location
    ? resolveCatalogLocation(location, root)
    : resolveSiteCatalogLocation(root);
  if (isRemoteCatalogLocation(catalogLocation) || !existsSync(catalogLocation)) {
    return [];
  }
  if (!statSync(catalogLocation).isDirectory()) return [catalogLocation];
  const layout = localCatalogLayout(catalogLocation);
  const files = [path.join(layout.root, "entries.parquet"), path.join(layout.root, "MANIFEST.md")];
  if (layout.kind === "release") {
    files.push(layout.descriptor);
    if (layout.selection) files.push(layout.selection);
  }
  return Array.from(new Set(files));
}

export function catalogLocationRecordPath(root: URL, catalogLocation: string, id: string): string {
  if (isRemoteCatalogLocation(catalogLocation)) return `${catalogLocation}#${id}`;
  const layout = localCatalogLayout(catalogLocation);
  return `${path.relative(fileURLToPath(root), path.join(layout.root, "entries.parquet"))}#${id}`;
}

async function loadLocalCatalog(location: string): Promise<Catalog> {
  const locationStat = await stat(location);
  if (!locationStat.isDirectory()) {
    throw new Error(`Catalog location must be a directory: ${location}`);
  }
  const layout = localCatalogLayout(location);
  await Promise.all([
    assertLocalFileSize(path.join(layout.root, "entries.parquet"), MAX_CORE_ARTIFACT_BYTES),
    assertLocalFileSize(path.join(layout.root, "MANIFEST.md"), MAX_CORE_ARTIFACT_BYTES),
  ]);
  if (layout.kind === "bundle") {
    const [entries, manifestText] = await Promise.all([
      readFile(path.join(layout.root, "entries.parquet")),
      readFile(path.join(layout.root, "MANIFEST.md"), "utf8"),
    ]);
    return loadCatalogData({ entries, manifestText });
  }
  const [entries, manifest] = await Promise.all([
    readFile(path.join(layout.root, "entries.parquet")),
    readFile(path.join(layout.root, "MANIFEST.md")),
  ]);
  return loadCatalog({
    entries,
    manifest,
    release: layout.release,
    releaseUrl: pathToFileURL(layout.descriptor),
  });
}

function localCatalogLayout(location: string): LocalCatalogLayout {
  const selection = path.join(location, "catalog.json");
  const exact = path.join(location, "release.json");
  if (existsSync(selection) && existsSync(exact)) {
    throw new Error(`Catalog directory contains both catalog.json and release.json: ${location}`);
  }
  if (existsSync(selection)) {
    const release = readLocalRelease(selection);
    const root = path.join(location, "catalog", "releases", release.digest);
    return {
      kind: "release",
      root,
      descriptor: path.join(root, "release.json"),
      release,
      selection,
    };
  }
  if (existsSync(exact)) {
    return {
      kind: "release",
      root: location,
      descriptor: exact,
      release: readLocalRelease(exact),
    };
  }
  return { kind: "bundle", root: location };
}

function readLocalRelease(location: string): CatalogRelease {
  const bytes = statSync(location).size;
  if (bytes > MAX_RELEASE_JSON_BYTES) {
    throw new Error(`Catalog release JSON exceeds the 1 MiB limit: ${location}`);
  }
  return parseCatalogRelease(JSON.parse(readFileSync(location, "utf8")));
}

async function assertLocalFileSize(location: string, limit: number): Promise<void> {
  if ((await stat(location)).size > limit) {
    throw new Error(`Catalog artifact exceeds size limit: ${location}`);
  }
}

function loadRemoteCatalog(location: string): Promise<Catalog> {
  const existing = remoteCatalogs.get(location);
  if (existing) return existing;

  const catalog = openCatalog(location).catch((cause: unknown) => {
    remoteCatalogs.delete(location);
    throw cause;
  });
  remoteCatalogs.set(location, catalog);
  return catalog;
}

function expandHome(value: string): string {
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function locationScheme(value: string): string | undefined {
  const index = value.indexOf("://");
  return index < 0 ? undefined : value.slice(0, index).toLowerCase();
}

function isRemoteCatalogLocation(value: string): boolean {
  const scheme = locationScheme(value);
  return scheme === "http" || scheme === "https";
}

function isExactRemoteRelease(value: string): boolean {
  if (!isRemoteCatalogLocation(value)) return false;
  const location = new URL(value);
  return location.protocol === "https:" && /\/[0-9a-f]{64}\/release\.json$/.test(location.pathname);
}
