import { createHash } from "node:crypto";
import { existsSync, readFileSync, statSync } from "node:fs";
import { readFile, stat } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  DEFAULT_CATALOG,
  catalogArtifact,
  catalogArtifactUrl,
  loadCatalog,
  parseCatalogReleaseMetadata,
  type Catalog,
} from "@chartcoach/catalog";

const SITE_CATALOG_SOURCE_ENV = "CHARTCOACH_SITE_CATALOG_SOURCE";
const CACHE_DIR_ENV = "CHARTCOACH_CACHE_DIR";

type ArtifactDescriptor = {
  kind?: unknown;
  path?: unknown;
  digest?: unknown;
  bytes?: unknown;
};

type CatalogReleaseMetadata = {
  version?: unknown;
  digest?: unknown;
  artifacts?: unknown;
};

export function resolveSiteCatalogSource(root: URL): string {
  const configuredSource = process.env[SITE_CATALOG_SOURCE_ENV];
  if (configuredSource) return resolveCatalogSource(configuredSource, root);

  const cachedBundle = defaultCachedCatalogBundle();
  if (cachedBundle) return cachedBundle;

  return DEFAULT_CATALOG.metadataUrl;
}

export function resolveCatalogSource(source: string, root: URL): string {
  if (isHttpUrl(source)) return source;
  return path.resolve(fileURLToPath(root), expandHome(source));
}

export async function loadSiteCatalog(root: URL, source?: string): Promise<Catalog> {
  const catalogSource = source
    ? resolveCatalogSource(source, root)
    : resolveSiteCatalogSource(root);
  return loadCatalogFromSource(catalogSource);
}

export function catalogSourceWatchFiles(root: URL, source?: string): string[] {
  const catalogSource = source
    ? resolveCatalogSource(source, root)
    : resolveSiteCatalogSource(root);
  if (isHttpUrl(catalogSource) || !existsSync(catalogSource)) return [];

  const sourceStat = statSync(catalogSource);
  if (!sourceStat.isDirectory()) return [catalogSource];

  return [path.join(catalogSource, "entries.parquet"), path.join(catalogSource, "MANIFEST.md")];
}

export function catalogSourceRecordPath(root: URL, catalogSource: string, id: string): string {
  if (isHttpUrl(catalogSource)) return `${catalogSource}#${id}`;

  const sourceStat = statSync(catalogSource);
  const sourcePath = sourceStat.isDirectory()
    ? path.join(catalogSource, "entries.parquet")
    : catalogSource;
  return `${path.relative(fileURLToPath(root), sourcePath)}#${id}`;
}

export function isHttpUrl(value: string): boolean {
  return value.startsWith("http://") || value.startsWith("https://");
}

async function loadCatalogFromSource(source: string): Promise<Catalog> {
  if (source === DEFAULT_CATALOG.metadataUrl) {
    return loadCatalogFromUrls(DEFAULT_CATALOG.entriesUrl, DEFAULT_CATALOG.manifestUrl);
  }
  if (isHttpUrl(source)) return loadCatalogFromRemoteSource(source);
  return loadCatalogFromLocalSource(source);
}

async function loadCatalogFromLocalSource(source: string): Promise<Catalog> {
  const sourceStat = await stat(source);
  if (!sourceStat.isDirectory()) return loadCatalog(await readFile(source));

  const entriesPath = path.join(source, "entries.parquet");
  const manifestPath = path.join(source, "MANIFEST.md");
  const [entries, manifestText] = await Promise.all([
    readFile(entriesPath),
    readFile(manifestPath, "utf8"),
  ]);
  return loadCatalog({ entries, manifestText });
}

async function loadCatalogFromRemoteSource(source: string): Promise<Catalog> {
  if (source.endsWith(".parquet")) {
    return loadCatalog(await fetchArrayBuffer(source));
  }

  const metadataUrl = source.endsWith("metadata.json")
    ? source
    : new URL("metadata.json", source.endsWith("/") ? source : `${source}/`).toString();
  const metadata = parseCatalogReleaseMetadata(await fetchJson(metadataUrl));
  return loadCatalogFromUrls(
    catalogArtifactUrl(metadataUrl, catalogArtifact(metadata, "entries")),
    catalogArtifactUrl(metadataUrl, catalogArtifact(metadata, "manifest")),
  );
}

async function loadCatalogFromUrls(entriesUrl: string, manifestUrl: string): Promise<Catalog> {
  const [entries, manifestText] = await Promise.all([
    fetchArrayBuffer(entriesUrl),
    fetchText(manifestUrl),
  ]);
  return loadCatalog({ entries, manifestText });
}

async function fetchArrayBuffer(url: string): Promise<ArrayBuffer> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to load catalog artifact: ${response.status} ${url}`);
  }
  return response.arrayBuffer();
}

async function fetchText(url: string): Promise<string> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to load catalog artifact: ${response.status} ${url}`);
  }
  return response.text();
}

async function fetchJson(url: string): Promise<unknown> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to load catalog metadata: ${response.status} ${url}`);
  }
  return response.json();
}

function defaultCachedCatalogBundle(): string | undefined {
  const bundle = path.join(
    cacheRoot(),
    "artifacts",
    "catalog",
    "releases",
    DEFAULT_CATALOG.version,
    DEFAULT_CATALOG.digest,
  );

  return cachedBundleIsValid(bundle) ? bundle : undefined;
}

function cacheRoot(): string {
  const configuredRoot = process.env[CACHE_DIR_ENV];
  if (configuredRoot) return path.resolve(expandHome(configuredRoot));

  const home = os.homedir();
  if (process.platform === "darwin") {
    return path.join(home, "Library", "Caches", "chartcoach");
  }
  if (process.platform === "win32") {
    return path.join(
      process.env.LOCALAPPDATA ?? path.join(home, "AppData", "Local"),
      "chartcoach",
      "Cache",
    );
  }

  return path.join(process.env.XDG_CACHE_HOME ?? path.join(home, ".cache"), "chartcoach");
}

function expandHome(value: string): string {
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function cachedBundleIsValid(bundle: string): boolean {
  const metadataPath = path.join(bundle, "metadata.json");
  if (!existsSync(metadataPath)) return false;

  try {
    const metadata = JSON.parse(readFileSync(metadataPath, "utf8")) as CatalogReleaseMetadata;
    if (
      metadata.version !== DEFAULT_CATALOG.version ||
      metadata.digest !== DEFAULT_CATALOG.digest
    ) {
      return false;
    }
    if (!Array.isArray(metadata.artifacts)) return false;

    return ["manifest", "entries"].every((kind) =>
      cachedArtifactIsValid(bundle, metadata.artifacts as ArtifactDescriptor[], kind),
    );
  } catch {
    return false;
  }
}

function cachedArtifactIsValid(
  bundle: string,
  artifacts: ArtifactDescriptor[],
  kind: string,
): boolean {
  const artifact = artifacts.find((candidate) => candidate.kind === kind);
  if (
    typeof artifact?.path !== "string" ||
    typeof artifact.digest !== "string" ||
    typeof artifact.bytes !== "number"
  ) {
    return false;
  }

  const artifactPath = path.join(bundle, artifact.path);
  if (!existsSync(artifactPath)) return false;

  const stat = statSync(artifactPath);
  return stat.isFile() && stat.size === artifact.bytes && sha256(artifactPath) === artifact.digest;
}

function sha256(filePath: string): string {
  return createHash("sha256").update(readFileSync(filePath)).digest("hex");
}
