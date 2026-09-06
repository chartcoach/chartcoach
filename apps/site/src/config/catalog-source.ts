import { existsSync, statSync } from "node:fs";
import { readFile, stat } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { loadCatalog, open, type Catalog } from "@chartcoach/catalog";

const SITE_CATALOG_SOURCE_ENV = "CHARTCOACH_SITE_CATALOG_SOURCE";
const DEFAULT_CATALOG_RECORD_SOURCE = "chartcoach://catalog.json";
let remoteCatalog: Promise<Catalog> | undefined;

export function resolveSiteCatalogSource(root: URL): string | undefined {
  const source = process.env[SITE_CATALOG_SOURCE_ENV];
  return source ? resolveCatalogSource(source, root) : undefined;
}

export function resolveCatalogSource(source: string, root: URL): string {
  return path.resolve(fileURLToPath(root), expandHome(source));
}

export function loadSiteCatalog(root: URL, source?: string): Promise<Catalog> {
  const catalogSource = source
    ? resolveCatalogSource(source, root)
    : resolveSiteCatalogSource(root);
  if (catalogSource === undefined) return loadRemoteCatalog();
  return loadLocalBundle(catalogSource);
}

export function catalogSourceWatchFiles(root: URL, source?: string): string[] {
  const catalogSource = source
    ? resolveCatalogSource(source, root)
    : resolveSiteCatalogSource(root);
  if (catalogSource === undefined || !existsSync(catalogSource)) return [];
  if (!statSync(catalogSource).isDirectory()) return [catalogSource];
  return [path.join(catalogSource, "entries.parquet"), path.join(catalogSource, "MANIFEST.md")];
}

export function catalogSourceRecordPath(
  root: URL,
  catalogSource: string | undefined,
  id: string,
): string {
  if (catalogSource === undefined) return `${DEFAULT_CATALOG_RECORD_SOURCE}#${id}`;
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

function loadRemoteCatalog(): Promise<Catalog> {
  if (remoteCatalog) return remoteCatalog;

  remoteCatalog = open().catch((error: unknown) => {
    remoteCatalog = undefined;
    throw error;
  });
  return remoteCatalog;
}

function expandHome(value: string): string {
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}
