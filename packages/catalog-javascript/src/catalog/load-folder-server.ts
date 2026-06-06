import { readdir, readFile, stat } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { CatalogError } from "./errors";
import { Catalog, type Guideline } from "./model";
import {
  parseManifest,
  type CatalogManifest,
} from "./manifest";
import { parseBibliographyEntries, parseGuidelineMarkdown } from "./parse";
import { readCatalogFile } from "./load-parquet-server";

export type ReadCatalogOptions = {
  manifest?: CatalogManifest | string | URL;
};

export async function readCatalog(
  sourcePath: string | URL,
  options: ReadCatalogOptions = {},
): Promise<Catalog> {
  const source = resolvePath(sourcePath);
  const sourceStat = await stat(source);
  const manifest = await resolveManifest(source, sourceStat.isDirectory(), options.manifest);

  if (sourceStat.isDirectory()) {
    const parquetPath = join(source, "catalog.parquet");
    try {
      await stat(parquetPath);
      return readCatalogFile(parquetPath, { manifest });
    } catch (error) {
      if (!isMissingFile(error)) throw error;
      if (!manifest) {
        throw new CatalogError("Catalog folders require MANIFEST.md or an explicit manifest.");
      }
      return readCatalogFolder(source, manifest);
    }
  }

  return readCatalogFile(source, { manifest });
}

async function readGuidelineFromFolder(entryDir: string): Promise<Guideline> {
  const files = await readdir(entryDir);
  const mdFiles = files.filter((f) => f.endsWith(".md"));

  if (mdFiles.length === 0) {
    throw new Error(`No guideline markdown file found in catalog entry directory: ${entryDir}`);
  }
  if (mdFiles.length > 1) {
    throw new Error(
      `Multiple markdown files found in catalog entry directory: ${entryDir}. Expected only one.`,
    );
  }

  const guidelineMdPath = join(entryDir, mdFiles[0]!);
  const guidelineMd = await readFile(guidelineMdPath, "utf-8");
  const guideline = parseGuidelineMarkdown(guidelineMd);

  let references: string[] = [];
  if (guideline.bibliography) {
    try {
      const bibPath = join(entryDir, guideline.bibliography);
      const bib = await readFile(bibPath, "utf-8");
      references = parseBibliographyEntries(bib);
    } catch {
      guideline.bibliography = undefined;
    }
  }

  return { ...guideline, references };
}

async function readCatalogFolder(folderPath: string, manifest: CatalogManifest): Promise<Catalog> {
  const guidelines: Guideline[] = [];
  const children = await readdir(folderPath);
  for (const name of children) {
    const full = join(folderPath, name);
    let s;
    try {
      s = await stat(full);
    } catch {
      continue;
    }
    if (!s.isDirectory()) continue;

    try {
      const guideline = await readGuidelineFromFolder(full);
      guidelines.push(guideline);
    } catch {
      // Authored folders can contain local notes. Only valid guideline folders enter the catalog.
    }
  }

  return new Catalog(guidelines, { manifest });
}

async function readManifest(manifestPath: string): Promise<CatalogManifest> {
  return parseManifest(await readFile(manifestPath, "utf-8"));
}

async function resolveManifest(
  sourcePath: string,
  isDirectory: boolean,
  manifest: CatalogManifest | string | URL | undefined,
): Promise<CatalogManifest | undefined> {
  if (manifest && isCatalogManifest(manifest)) return manifest;
  if (manifest) return readManifest(resolvePath(manifest));
  if (isDirectory) return readManifest(join(sourcePath, "MANIFEST.md"));
  return undefined;
}

function resolvePath(path: string | URL): string {
  return path instanceof URL ? fileURLToPath(path) : path;
}

function isMissingFile(error: unknown): boolean {
  return Boolean(
    error &&
      typeof error === "object" &&
      "code" in error &&
      error.code === "ENOENT",
  );
}

function isCatalogManifest(value: unknown): value is CatalogManifest {
  return Boolean(
    value &&
      typeof value === "object" &&
      "sectionRoles" in value &&
      "labelFamilies" in value,
  );
}
