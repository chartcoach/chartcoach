import { asyncBufferFromUrl } from "hyparquet";

import { CatalogError } from "./errors";
import type { CatalogManifest } from "./manifest";
import { parseManifest } from "./manifest";
import { loadCatalog, type AsyncBuffer } from "./load-parquet-core";

export type FetchCatalogOptions = {
  manifest?: CatalogManifest | string | URL;
  request?: RequestInit;
};

export async function fetchCatalog(
  catalogUrl: string | URL,
  options: FetchCatalogOptions = {},
) {
  const manifest = await resolveManifest(options.manifest, options.request);
  const file = (await asyncBufferFromUrl({
    url: catalogUrl.toString(),
    requestInit: options.request,
  })) as AsyncBuffer;

  return loadCatalog(file, { manifest });
}

async function resolveManifest(
  manifest: CatalogManifest | string | URL | undefined,
  requestInit: RequestInit | undefined,
): Promise<CatalogManifest | undefined> {
  if (manifest === undefined) return undefined;
  if (typeof manifest !== "string" && !(manifest instanceof URL)) return manifest;

  const response = await fetch(manifest.toString(), requestInit);
  if (!response.ok) {
    throw new CatalogError(`Failed to load catalog manifest: ${response.status}`);
  }
  return parseManifest(await response.text());
}
