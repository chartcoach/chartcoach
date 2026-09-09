import type { ToolContext } from "eve/tools";
import { gunzip } from "node:zlib";
import { promisify } from "node:util";
import { z } from "zod";
import { resolvedSelectionSchema, type ResolvedSelection } from "../lib/catalog/selection";
import {
  catalogSelectionSchema,
  catalogSelectionHeaderSchema,
  maxSelectionBytes,
  type CatalogSelection,
} from "../shared/catalog-selection";

const decompress = promisify(gunzip);

export async function decodeSelection(value: string): Promise<CatalogSelection> {
  const header = catalogSelectionHeaderSchema.parse(value);
  const bytes = Buffer.from(header, "base64");
  if (bytes.toString("base64") !== header)
    throw new Error("The catalog selection header is not canonical base64.");
  const json = await decompress(bytes, { maxOutputLength: maxSelectionBytes });
  return catalogSelectionSchema.parse(
    JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(json)),
  );
}

export function parseSelection(value: string | readonly string[] | undefined): ResolvedSelection {
  try {
    return resolvedSelectionSchema.parse(JSON.parse(z.string().parse(value)));
  } catch (error) {
    throw new Error("This review has no valid catalog selection. Start a new review.", {
      cause: error,
    });
  }
}

export function sessionSelection(session: ToolContext["session"]): ResolvedSelection {
  return parseSelection(session.auth.initiator?.attributes["chartcoach.selection"]);
}
