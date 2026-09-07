import { createHash, randomUUID } from "node:crypto";
import { createReadStream } from "node:fs";
import { mkdir, open, rename, stat, unlink, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { Readable } from "node:stream";
import { fileURLToPath, pathToFileURL } from "node:url";

import { CatalogError } from "./catalog/errors";
import { assertReleaseDigest, parseCatalogRelease, releaseArtifact } from "./catalog/artifacts";
import { parseJson } from "./catalog/json";
import { loadCatalogData } from "./catalog/parquet";
import {
  openCatalog as openRemoteCatalog,
  type FetchLike,
  type OpenCatalogOptions,
} from "./catalog/open";
import type { ArtifactOptions, Catalog } from "./catalog/model";

type NodeContext = { cacheDirectory: string; fetch: FetchLike };
const contexts = new WeakMap<Catalog, NodeContext>();

export type NodeOpenCatalogOptions = OpenCatalogOptions & { cacheDirectory?: string };

export async function openCatalog(
  location?: string | URL,
  options: NodeOpenCatalogOptions = {},
): Promise<Catalog> {
  const cacheDirectory = options.cacheDirectory ?? defaultCacheDirectory();
  const fetch = options.fetch ?? globalThis.fetch;
  const uri = location === undefined ? undefined : locationUrl(location);
  if (uri?.protocol === "file:") {
    const local = fileURLToPath(uri);
    if ((await stat(local)).isDirectory()) {
      const selection = await existingFile(join(local, "catalog.json"));
      const release = await existingFile(join(local, "release.json"));
      if (selection && release)
        throw new CatalogError("Catalog directory contains both descriptors.");
      if (selection || release)
        return openCatalog(
          pathToFileURL(join(local, selection ? "catalog.json" : "release.json")),
          options,
        );
      const [entries, manifest] = await Promise.all([
        readBytes(join(local, "entries.parquet"), 64 * 1024 ** 2, options.signal),
        readBytes(join(local, "MANIFEST.md"), 64 * 1024 ** 2, options.signal),
      ]);
      return loadCatalogData({
        entries,
        manifestText: new TextDecoder("utf-8", { fatal: true }).decode(manifest),
      });
    }
  }
  const fetchResource: FetchLike = async (input, init) => {
    const url = new URL(input);
    init?.signal?.throwIfAborted();
    if (url.protocol === "file:") {
      // SAFETY: createReadStream emits Buffer chunks and toWeb preserves those byte chunks.
      const body = Readable.toWeb(
        createReadStream(fileURLToPath(url)),
      ) as ReadableStream<Uint8Array>;
      return new Response(body);
    }
    const parent = url.pathname.split("/").at(-2) ?? "";
    if (url.pathname.endsWith("/release.json") && /^[a-f0-9]{64}$/.test(parent)) {
      const cached = await readCached(
        join(cacheDirectory, "descriptors", `${parent}.json`),
        1024 ** 2,
      );
      if (cached) {
        try {
          const release = parseCatalogRelease(parseJson(new TextDecoder().decode(cached)));
          await assertReleaseDigest(release, parent);
          return new Response(Uint8Array.from(cached));
        } catch (error) {
          if (!(error instanceof CatalogError) && !(error instanceof SyntaxError)) throw error;
        }
      }
    }
    return fetch(input, init);
  };
  const catalog = await openRemoteCatalog(uri, {
    signal: options.signal,
    cache: options.cache ?? {
      get: async (digest, bytes) => readCached(join(cacheDirectory, "artifacts", digest), bytes),
      put: async (digest, bytes) => atomicWrite(join(cacheDirectory, "artifacts", digest), bytes),
    },
    fetch: fetchResource,
  });
  if (catalog.release)
    await atomicWrite(
      join(cacheDirectory, "descriptors", `${catalog.release.digest}.json`),
      new TextEncoder().encode(JSON.stringify(catalog.release)),
    );
  contexts.set(catalog, { cacheDirectory, fetch: fetchResource });
  return catalog;
}

export async function artifactPath(
  catalog: Catalog,
  path: string,
  options: ArtifactOptions = {},
): Promise<string> {
  if (!catalog.release)
    throw new CatalogError("Artifact access requires a catalog release.", {
      code: "unavailable_capability",
    });
  const artifact = releaseArtifact(catalog.release, path);
  if (artifact.bytes > 1024 ** 3) throw new CatalogError("Catalog artifact exceeds 1 GiB.");
  const context = contexts.get(catalog);
  const target = join(
    context?.cacheDirectory ?? defaultCacheDirectory(),
    "artifacts",
    artifact.sha256,
  );
  const timeout = AbortSignal.timeout(900_000);
  const signal = options.signal ? AbortSignal.any([options.signal, timeout]) : timeout;
  signal.throwIfAborted();
  if (await verifiedFile(target, artifact.sha256, artifact.bytes, signal)) return target;
  if (!context || !catalog.releaseUrl) {
    await atomicWrite(target, await catalog.artifact(path, { signal }));
    signal.throwIfAborted();
    return target;
  }
  const response = await context.fetch(new URL(path, catalog.releaseUrl), { signal });
  if (!response.ok) {
    void response.body?.cancel().catch(() => {});
    throw new CatalogError("Artifact could not be loaded.");
  }
  if (!response.body) {
    if (artifact.bytes !== 0 || artifact.sha256 !== createHash("sha256").digest("hex"))
      throw new CatalogError("Artifact integrity check failed.", { code: "integrity" });
    signal.throwIfAborted();
    await atomicWrite(target, new Uint8Array());
    return target;
  }
  const temporary = `${target}.${randomUUID()}.tmp`;
  const reader = response.body.getReader();
  const abort = () => {
    void reader.cancel(signal.reason).catch(() => {});
  };
  signal.addEventListener("abort", abort, { once: true });
  if (signal.aborted) abort();
  try {
    await mkdir(dirname(target), { recursive: true });
    const file = await open(temporary, "wx");
    const hash = createHash("sha256");
    let size = 0;
    try {
      while (true) {
        const chunk = await reader.read();
        signal.throwIfAborted();
        if (chunk.done) break;
        size += chunk.value.byteLength;
        if (size > artifact.bytes)
          throw new CatalogError("Artifact byte count mismatch.", { code: "integrity" });
        hash.update(chunk.value);
        await file.writeFile(chunk.value);
      }
    } finally {
      await file.close();
    }
    if (size !== artifact.bytes || hash.digest("hex") !== artifact.sha256)
      throw new CatalogError("Artifact integrity check failed.", { code: "integrity" });
    signal.throwIfAborted();
    await rename(temporary, target);
    return target;
  } finally {
    signal.removeEventListener("abort", abort);
    void reader.cancel().catch(() => {});
    reader.releaseLock();
    await removeTemporary(temporary);
  }
}

async function verifiedFile(
  path: string,
  digest: string,
  bytes: number,
  signal: AbortSignal,
): Promise<boolean> {
  try {
    if ((await stat(path)).size !== bytes) return false;
    const hash = createHash("sha256");
    let size = 0;
    for await (const chunk of createReadStream(path, { signal })) {
      size += chunk.length;
      if (size > bytes) return false;
      hash.update(chunk);
    }
    signal.throwIfAborted();
    return size === bytes && hash.digest("hex") === digest;
  } catch (error) {
    if (error instanceof Error && "code" in error && error.code === "ENOENT") return false;
    throw error;
  }
}

function locationUrl(location: string | URL): URL {
  if (location instanceof URL) return location;
  return /^[a-z][a-z0-9+.-]*:\/\//i.test(location)
    ? new URL(location)
    : pathToFileURL(resolve(location));
}

function defaultCacheDirectory(): string {
  if (process.platform === "darwin") return join(homedir(), "Library", "Caches", "chartcoach");
  if (process.platform === "win32")
    return join(
      process.env.LOCALAPPDATA ?? join(homedir(), "AppData", "Local"),
      "chartcoach",
      "Cache",
    );
  return join(process.env.XDG_CACHE_HOME ?? join(homedir(), ".cache"), "chartcoach");
}

async function existingFile(path: string): Promise<boolean> {
  try {
    return (await stat(path)).isFile();
  } catch (error) {
    if (error instanceof Error && "code" in error && error.code === "ENOENT") return false;
    throw error;
  }
}

async function readBytes(path: string, maximum: number, signal?: AbortSignal): Promise<Uint8Array> {
  if ((await stat(path)).size > maximum) throw new CatalogError("Catalog file exceeds size limit.");
  const chunks: Uint8Array[] = [];
  let size = 0;
  for await (const chunk of createReadStream(path, { signal })) {
    size += chunk.length;
    if (size > maximum) throw new CatalogError("Catalog file exceeds size limit.");
    chunks.push(chunk);
  }
  signal?.throwIfAborted();
  return Buffer.concat(chunks);
}

async function readCached(path: string, maximum: number): Promise<Uint8Array | undefined> {
  try {
    return await readBytes(path, maximum);
  } catch (error) {
    if (
      error instanceof CatalogError ||
      (error instanceof Error && "code" in error && error.code === "ENOENT")
    )
      return undefined;
    throw error;
  }
}

async function atomicWrite(path: string, bytes: Uint8Array): Promise<void> {
  await mkdir(dirname(path), { recursive: true });
  const temporary = `${path}.${randomUUID()}.tmp`;
  try {
    await writeFile(temporary, bytes, { flag: "wx" });
    await rename(temporary, path);
  } finally {
    await removeTemporary(temporary);
  }
}

async function removeTemporary(path: string): Promise<void> {
  try {
    await unlink(path);
  } catch (error) {
    if (!(error instanceof Error && "code" in error && error.code === "ENOENT")) throw error;
  }
}
