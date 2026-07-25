import {
  assertReleaseArtifactBytes,
  assertReleaseDigest,
  catalogUrl,
  parseCatalogRelease,
  releaseArtifact,
  releaseArtifactUrl,
  type CatalogRelease,
  type ReleaseArtifact,
} from "./artifacts";
import { CatalogError } from "./errors";
import { loadCatalog } from "./load-parquet-core";
import type { Catalog } from "./model";

export type FetchLike = (input: string | URL, init?: RequestInit) => Promise<Response>;

export type OpenCatalogOptions = {
  fetch?: FetchLike;
};

const CATALOG_REQUEST_TIMEOUT_MS = 15 * 60 * 1000;
const CATALOG_BODY_READ_ERROR = "Failed to read catalog resource body.";
const MAX_CATALOG_JSON_BYTES = 1024 * 1024;
const MAX_CORE_ARTIFACT_BYTES = 64 * 1024 * 1024;

export async function openCatalog(
  source: string | URL = catalogUrl(),
  options: OpenCatalogOptions = {},
): Promise<Catalog> {
  const fetch = options.fetch ?? globalThis.fetch;
  const descriptor = requireDescriptorUrl(source);
  const release = parseCatalogRelease(
    await fetchJson(descriptor.url, fetch, descriptor.kind === "catalog" ? "no-cache" : undefined),
  );
  await assertReleaseDigest(release);
  const artifactBase =
    descriptor.kind === "catalog"
      ? new URL(`catalog/releases/${release.digest}/`, descriptor.url).toString()
      : new URL(".", descriptor.url).toString();
  return loadCatalogFromRelease(fetch, artifactBase, release);
}

async function loadCatalogFromRelease(
  fetch: FetchLike,
  artifactBase: string,
  release: CatalogRelease,
): Promise<Catalog> {
  const controller = new AbortController();
  try {
    const [entries, manifest] = await Promise.all([
      fetchReleaseArtifact(
        fetch,
        artifactBase,
        "entries.parquet",
        releaseArtifact(release, "entries.parquet"),
        controller.signal,
      ),
      fetchReleaseArtifact(
        fetch,
        artifactBase,
        "MANIFEST.md",
        releaseArtifact(release, "MANIFEST.md"),
        controller.signal,
      ),
    ]);
    let manifestText: string;
    try {
      manifestText = new TextDecoder("utf-8", { fatal: true }).decode(manifest);
    } catch {
      throw new CatalogError("Catalog manifest must contain valid UTF-8.");
    }
    return loadCatalog({ entries, manifestText });
  } catch (error) {
    controller.abort(error);
    throw error;
  }
}

async function fetchJson(url: string, fetch: FetchLike, cache?: "no-cache"): Promise<unknown> {
  const response = await fetchCatalogResource(url, fetch, undefined, cache);
  const data = await readResponseBytes(
    response,
    MAX_CATALOG_JSON_BYTES,
    "Catalog JSON exceeds size limit.",
  );
  try {
    const text = new TextDecoder("utf-8", { fatal: true }).decode(data);
    return JSON.parse(text);
  } catch {
    throw new CatalogError("Catalog JSON must contain valid UTF-8 JSON.");
  }
}

async function fetchReleaseArtifact(
  fetch: FetchLike,
  artifactBase: string,
  path: string,
  artifact: ReleaseArtifact,
  signal: AbortSignal,
): Promise<ArrayBuffer> {
  const response = await fetchCatalogResource(
    releaseArtifactUrl(artifactBase, path),
    fetch,
    signal,
  );
  const data = await readArtifactBytes(response, path, artifact);
  await assertReleaseArtifactBytes(path, artifact, data);
  return data;
}

async function readArtifactBytes(
  response: Response,
  path: string,
  artifact: ReleaseArtifact,
): Promise<ArrayBuffer> {
  const absoluteLimitApplies = artifact.bytes > MAX_CORE_ARTIFACT_BYTES;
  return readResponseBytes(
    response,
    Math.min(artifact.bytes, MAX_CORE_ARTIFACT_BYTES),
    absoluteLimitApplies
      ? `Catalog artifact exceeds size limit: ${path}`
      : `Catalog artifact byte count mismatch: ${path}`,
  );
}

async function readResponseBytes(
  response: Response,
  limit: number,
  limitError: string,
): Promise<ArrayBuffer> {
  let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
  try {
    reader = response.body?.getReader();
  } catch {
    throw new CatalogError(CATALOG_BODY_READ_ERROR);
  }
  if (!reader) return new ArrayBuffer(0);

  const chunks: Uint8Array[] = [];
  let size = 0;
  let failure: CatalogError | undefined;
  while (!failure) {
    try {
      const result = await reader.read();
      if (result.done) break;
      const { value } = result;
      size += value.byteLength;
      if (size > limit) {
        try {
          await reader.cancel();
        } catch {
          // The size error remains the public failure for this request.
        }
        failure = new CatalogError(limitError);
        break;
      }
      chunks.push(value);
    } catch {
      failure = new CatalogError(CATALOG_BODY_READ_ERROR);
    }
  }
  try {
    reader.releaseLock();
  } catch {
    failure ??= new CatalogError(CATALOG_BODY_READ_ERROR);
  }
  if (failure) throw failure;

  try {
    const data = new Uint8Array(size);
    let offset = 0;
    for (const chunk of chunks) {
      data.set(chunk, offset);
      offset += chunk.byteLength;
    }
    return data.buffer;
  } catch {
    throw new CatalogError(CATALOG_BODY_READ_ERROR);
  }
}

async function fetchCatalogResource(
  url: string,
  fetch: FetchLike,
  signal?: AbortSignal,
  cache?: "no-cache",
): Promise<Response> {
  const timeout = AbortSignal.timeout(CATALOG_REQUEST_TIMEOUT_MS);
  const requestSignal = signal ? AbortSignal.any([signal, timeout]) : timeout;
  const init = cache ? { signal: requestSignal, cache } : { signal: requestSignal };
  let response: Response;
  try {
    response = await fetch(url, init);
  } catch {
    throw new CatalogError("Failed to load catalog resource.");
  }
  let ok: boolean;
  let status: number;
  try {
    ok = response.ok;
    status = response.status;
  } catch {
    throw new CatalogError("Failed to load catalog resource.");
  }
  if (!ok) {
    const message = Number.isInteger(status)
      ? `Failed to load catalog resource: HTTP ${status}.`
      : "Failed to load catalog resource.";
    throw new CatalogError(message);
  }
  return response;
}

function requireDescriptorUrl(input: string | URL): { kind: "catalog" | "release"; url: string } {
  const value = input.toString();
  let url: URL;
  try {
    url = new URL(value);
  } catch {
    throw new CatalogError("Catalog source must be an absolute HTTP or HTTPS URL.");
  }
  if (url.protocol !== "http:" && url.protocol !== "https:") {
    throw new CatalogError("Catalog source must use HTTP or HTTPS.");
  }
  const name = url.pathname.split("/").at(-1);
  if (name === "catalog.json") return { kind: "catalog", url: url.toString() };
  if (name === "release.json") return { kind: "release", url: url.toString() };
  throw new CatalogError("Catalog source URL must name catalog.json or release.json.");
}
