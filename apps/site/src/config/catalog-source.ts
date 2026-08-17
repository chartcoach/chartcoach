import { existsSync, statSync } from "node:fs";
import { readFile, stat } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { loadCatalog, openCatalog, type Catalog } from "@chartcoach/catalog";

const SITE_CATALOG_SOURCE_ENV = "CHARTCOACH_SITE_CATALOG_SOURCE";
const LOCAL_CATALOG_SOURCE = "../../fixtures/catalog-release";
const CF_PAGES_ENV = "CF_PAGES";
const remoteCatalogs = new Map<string, Promise<Catalog>>();

export function resolveSiteCatalogSource(root: URL): string {
  const source = process.env[SITE_CATALOG_SOURCE_ENV];
  const deployment = process.env[CF_PAGES_ENV] === "1";
  if (source?.trim()) {
    const resolved = resolveCatalogSource(source, root);
    if (deployment && !isExactRemoteRelease(resolved)) {
      throw new Error(
        `${SITE_CATALOG_SOURCE_ENV} must name an exact HTTPS release.json URL for deployment.`,
      );
    }
    return resolved;
  }
  if (deployment) {
    throw new Error(`${SITE_CATALOG_SOURCE_ENV} must name an exact release for deployment.`);
  }
  return resolveCatalogSource(LOCAL_CATALOG_SOURCE, root);
}

export function resolveCatalogSource(source: string, root: URL): string {
  const scheme = sourceScheme(source);
  if (scheme === "http" || scheme === "https") return new URL(source).toString();
  if (scheme === "file") return fileURLToPath(source);
  if (scheme !== undefined) throw new Error(`Unsupported catalog source scheme: ${scheme}.`);
  return path.resolve(fileURLToPath(root), expandHome(source));
}

export function loadSiteCatalog(root: URL, source?: string): Promise<Catalog> {
  const catalogSource = source
    ? resolveCatalogSource(source, root)
    : resolveSiteCatalogSource(root);
  if (isRemoteSource(catalogSource)) return loadRemoteCatalog(catalogSource);
  return loadLocalBundle(catalogSource);
}

export function catalogSourceWatchFiles(root: URL, source?: string): string[] {
  const catalogSource = source
    ? resolveCatalogSource(source, root)
    : resolveSiteCatalogSource(root);
  if (isRemoteSource(catalogSource) || !existsSync(catalogSource)) {
    return [];
  }
  if (!statSync(catalogSource).isDirectory()) return [catalogSource];
  return [path.join(catalogSource, "entries.parquet"), path.join(catalogSource, "MANIFEST.md")];
}

export function catalogSourceRecordPath(root: URL, catalogSource: string, id: string): string {
  if (isRemoteSource(catalogSource)) return `${catalogSource}#${id}`;
  return `${path.relative(fileURLToPath(root), path.join(catalogSource, "entries.parquet"))}#${id}`;
}

async function loadLocalBundle(source: string): Promise<Catalog> {
  const sourceStat = await stat(source);
  if (!sourceStat.isDirectory()) {
    throw new Error(`Catalog bundle must be a directory: ${source}`);
  }
  const [entries, manifestText] = await Promise.all([
    readFile(path.join(source, "entries.parquet")),
    readFile(path.join(source, "MANIFEST.md"), "utf8"),
  ]);
  return loadCatalog({ entries, manifestText });
}

function loadRemoteCatalog(source: string): Promise<Catalog> {
  const existing = remoteCatalogs.get(source);
  if (existing) return existing;

  const catalog = openCatalog(source).catch((cause: unknown) => {
    remoteCatalogs.delete(source);
    throw cause;
  });
  remoteCatalogs.set(source, catalog);
  return catalog;
}

function expandHome(value: string): string {
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function sourceScheme(value: string): string | undefined {
  const index = value.indexOf("://");
  return index < 0 ? undefined : value.slice(0, index).toLowerCase();
}

function isRemoteSource(value: string): boolean {
  const scheme = sourceScheme(value);
  return scheme === "http" || scheme === "https";
}

function isExactRemoteRelease(value: string): boolean {
  if (!isRemoteSource(value)) return false;
  const source = new URL(value);
  return source.protocol === "https:" && /\/[0-9a-f]{64}\/release\.json$/.test(source.pathname);
}
