import { CatalogError } from "./errors";

export type CatalogLabel = {
  value: string;
  family: string;
  category: string;
  modifier?: string;
};

export function parseLabel(value: unknown, context = "label"): CatalogLabel {
  if (typeof value !== "string") {
    throw new CatalogError(`${context} must be a string.`);
  }
  const parts = value
    .trim()
    .split(":")
    .map((part) => part.trim());
  if ((parts.length !== 2 && parts.length !== 3) || parts.some((part) => part.length === 0)) {
    throw new CatalogError(`${context} must use <family>:<category> or <family>:<category>:<modifier>.`);
  }
  const [family, category, modifier] = parts as [string, string, string | undefined];
  return {
    value: modifier === undefined ? `${family}:${category}` : `${family}:${category}:${modifier}`,
    family,
    category,
    modifier,
  };
}

export function normalizeLabel(value: unknown, context = "label"): string {
  return parseLabel(value, context).value;
}
