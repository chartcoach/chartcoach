import {
  assertReleaseArtifactBytes,
  assertReleaseDigest,
  assertReleaseLocation,
  catalogUrl,
  parseCatalogRelease,
  releaseArtifact,
  releaseArtifactUrl,
  type CatalogRelease,
  type ReleaseArtifact,
} from "./artifacts";
import { CatalogError } from "./errors";
import type { ProfileLoader } from "./description";
import { parseJson, type JsonValue } from "./json";
import { loadCatalogWithProfileLoader } from "./parquet";
import type { Catalog } from "./model";
import { parseProfileMetadata } from "./profile";

export type FetchLike = (input: string | URL, init?: RequestInit) => Promise<Response>;

export type OpenCatalogOptions = {
  fetch?: FetchLike;
  signal?: AbortSignal;
};

const CATALOG_REQUEST_TIMEOUT_MS = 15 * 60 * 1000;
const CATALOG_BODY_READ_ERROR = "Failed to read catalog resource body.";
const MAX_CATALOG_JSON_BYTES = 1024 * 1024;
const MAX_CORE_ARTIFACT_BYTES = 64 * 1024 * 1024;
const MAX_PROFILE_METADATA_BYTES = 65_536;

type CatalogDescriptor = {
  kind: "catalog" | "release";
  url: string;
};

export async function openCatalog(
  location: string | URL = catalogUrl(),
  options: OpenCatalogOptions = {},
): Promise<Catalog> {
  const fetch = options.fetch ?? globalThis.fetch;
  const descriptor = requireDescriptorUrl(location);
  const release = parseCatalogRelease(
    await fetchJson(
      descriptor.url,
      fetch,
      options.signal,
      descriptor.kind === "catalog" ? "no-cache" : undefined,
    ),
  );
  await assertReleaseDigest(release);
  if (descriptor.kind === "release") assertReleaseLocation(descriptor.url, release);
  const artifactBase =
    descriptor.kind === "catalog"
      ? new URL(`catalog/releases/${release.digest}/`, descriptor.url).toString()
      : new URL(".", descriptor.url).toString();
  const releaseUrl =
    descriptor.kind === "catalog"
      ? new URL(`catalog/releases/${release.digest}/release.json`, descriptor.url).toString()
      : descriptor.url;
  return loadCatalogFromRelease(fetch, artifactBase, releaseUrl, release, options.signal);
}

async function loadCatalogFromRelease(
  fetch: FetchLike,
  artifactBase: string,
  releaseUrl: string,
  release: CatalogRelease,
  signal?: AbortSignal,
): Promise<Catalog> {
  const controller = new AbortController();
  const requestSignal = signal ? AbortSignal.any([controller.signal, signal]) : controller.signal;
  try {
    const [entries, manifest] = await Promise.all([
      fetchReleaseArtifact(
        fetch,
        artifactBase,
        "entries.parquet",
        releaseArtifact(release, "entries.parquet"),
        requestSignal,
      ),
      fetchReleaseArtifact(
        fetch,
        artifactBase,
        "MANIFEST.md",
        releaseArtifact(release, "MANIFEST.md"),
        requestSignal,
      ),
    ]);
    return loadCatalogWithProfileLoader(
      { entries, manifest, release, releaseUrl },
      profileLoader(fetch, artifactBase, release),
    );
  } catch (error) {
    controller.abort(error);
    throw error;
  }
}

async function fetchJson(
  url: string,
  fetch: FetchLike,
  signal?: AbortSignal,
  cache?: "no-cache",
): Promise<JsonValue> {
  const response = await fetchCatalogResource(url, fetch, signal, cache);
  const data = await readResponseBytes(
    response,
    MAX_CATALOG_JSON_BYTES,
    "Catalog JSON exceeds size limit.",
    signal,
  );
  try {
    const text = new TextDecoder("utf-8", { fatal: true }).decode(data);
    return parseJson(text);
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
  return readArtifactBytes(response, path, artifact, signal);
}

async function readArtifactBytes(
  response: Response,
  path: string,
  artifact: ReleaseArtifact,
  signal?: AbortSignal,
): Promise<ArrayBuffer> {
  const absoluteLimitApplies = artifact.bytes > MAX_CORE_ARTIFACT_BYTES;
  return readResponseBytes(
    response,
    Math.min(artifact.bytes, MAX_CORE_ARTIFACT_BYTES),
    absoluteLimitApplies
      ? `Catalog artifact exceeds size limit: ${path}`
      : `Catalog artifact byte count mismatch: ${path}`,
    signal,
  );
}

async function readResponseBytes(
  response: Response,
  limit: number,
  limitError: string,
  signal?: AbortSignal,
): Promise<ArrayBuffer> {
  signal?.throwIfAborted();
  let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
  try {
    reader = response.body?.getReader();
  } catch {
    throw new CatalogError(CATALOG_BODY_READ_ERROR);
  }
  if (!reader) return new ArrayBuffer(0);

  const chunks: Uint8Array[] = [];
  let size = 0;
  let failure: Error | undefined;
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
      failure = signal?.aborted ? abortReason(signal) : new CatalogError(CATALOG_BODY_READ_ERROR);
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
    if (signal?.aborted) throw abortReason(signal);
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
    try {
      await response.body?.cancel();
    } catch {
      // Preserve the HTTP failure when transport cleanup also fails.
    }
    const message = Number.isInteger(status)
      ? `Failed to load catalog resource: HTTP ${status}.`
      : "Failed to load catalog resource.";
    throw new CatalogError(message);
  }
  return response;
}

function profileLoader(
  fetch: FetchLike,
  artifactBase: string,
  release: CatalogRelease,
): ProfileLoader {
  return async (profile, signal) => {
    const path = profile.metadata;
    const artifact = releaseArtifact(release, path);
    if (artifact.bytes > MAX_PROFILE_METADATA_BYTES) {
      throw new CatalogError("Profile metadata exceeds the 64 KiB limit.", {
        code: "incompatible_profile",
        details: { profile: profile.name },
      });
    }

    let response: Response;
    try {
      response = await fetchCatalogResource(releaseArtifactUrl(artifactBase, path), fetch, signal);
    } catch {
      if (signal?.aborted) throw abortReason(signal);
      throw new CatalogError(`Profile metadata could not be loaded: ${profile.name}.`, {
        code: "integrity",
        details: { profile: profile.name },
      });
    }
    const data = await readResponseBytes(
      response,
      artifact.bytes,
      `Catalog artifact byte count mismatch: ${path}`,
      signal,
    );
    await assertReleaseArtifactBytes(path, artifact, data);
    let value: JsonValue;
    try {
      const text = new TextDecoder("utf-8", { fatal: true }).decode(data);
      value = parseJson(text);
    } catch {
      throw new CatalogError(`Profile metadata is not valid UTF-8 JSON: ${profile.name}.`, {
        code: "incompatible_profile",
        details: { profile: profile.name },
      });
    }
    try {
      return parseProfileMetadata(value);
    } catch (error) {
      if (error instanceof CatalogError) {
        throw new CatalogError(error.message, {
          code: "incompatible_profile",
          details: { profile: profile.name },
        });
      }
      throw error;
    }
  };
}

function abortReason(signal: AbortSignal): Error {
  return signal.reason instanceof Error
    ? signal.reason
    : new DOMException("The operation was aborted.", "AbortError");
}

function requireDescriptorUrl(input: string | URL): CatalogDescriptor {
  const value = input.toString();
  let url: URL;
  try {
    url = new URL(value);
  } catch {
    throw new CatalogError("Catalog location must be an absolute HTTP or HTTPS URL.");
  }
  if (url.protocol !== "http:" && url.protocol !== "https:") {
    throw new CatalogError("Catalog location must use HTTP or HTTPS.");
  }
  const name = url.pathname.split("/").at(-1);
  if (name === "catalog.json") return { kind: "catalog", url: url.toString() };
  if (name === "release.json") return { kind: "release", url: url.toString() };
  throw new CatalogError("Catalog location URL must name catalog.json or release.json.");
}
