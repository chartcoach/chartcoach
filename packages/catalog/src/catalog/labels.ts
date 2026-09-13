import { CatalogError } from "./errors";

export type CatalogLabel = {
  value: string;
  family: string;
  category: string;
  modifier?: string;
};

export function parseLabel(value: string, context = "label"): CatalogLabel {
  const parts = value
    .trim()
    .split(":")
    .map((part) => part.trim());

  if ((parts.length !== 2 && parts.length !== 3) || parts.some((part) => part.length === 0)) {
    throw new CatalogError(
      `${context} must use <family>:<category> or <family>:<category>:<modifier>.`,
    );
  }

  const family = parts[0]!;
  const category = parts[1]!;
  const modifier = parts[2];

  return {
    value: modifier === undefined ? `${family}:${category}` : `${family}:${category}:${modifier}`,
    family,
    category,
    modifier,
  };
}

export function normalizeLabel(value: string, context = "label"): string {
  return parseLabel(value, context).value;
}
