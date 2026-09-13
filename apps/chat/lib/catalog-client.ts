import { z } from "zod";
import { catalogMetadataSchema } from "../shared/catalog-filters";
import {
  catalogSelectionSchema,
  maxSelectionHeaderLength,
  maxSelectionBytes,
  type CatalogSelection,
} from "../shared/catalog-selection";

const errorResponse = z.object({ error: z.string() });

async function readResponse<T>(response: Response, schema: z.ZodType<T>): Promise<T> {
  if (!response.ok) {
    const detail = errorResponse.safeParse(await response.json().catch(() => null)).data;
    throw new Error(detail?.error ?? `Catalog request failed (${response.status}). Try again.`);
  }

  return schema.parse(await response.json());
}

export async function loadCatalogMetadata(signal?: AbortSignal) {
  return readResponse(
    await fetch("/eve/v1/catalog", {
      signal: AbortSignal.any([...(signal ? [signal] : []), AbortSignal.timeout(30_000)]),
      cache: "no-store",
    }),
    catalogMetadataSchema,
  );
}

export async function encodeCatalogSelection(selection: CatalogSelection, signal?: AbortSignal) {
  signal?.throwIfAborted();
  const input = new TextEncoder().encode(JSON.stringify(catalogSelectionSchema.parse(selection)));

  if (input.byteLength > maxSelectionBytes)
    throw new Error("This catalog selection is too large. Select fewer authors or source types.");

  const bytes = new Uint8Array(
    await new Response(
      new Blob([input]).stream().pipeThrough(new CompressionStream("gzip"), { signal }),
    ).arrayBuffer(),
  );

  signal?.throwIfAborted();

  if (4 * Math.ceil(bytes.byteLength / 3) > maxSelectionHeaderLength)
    throw new Error("This catalog selection is too large. Select fewer authors or source types.");

  return btoa(String.fromCharCode(...bytes));
}
