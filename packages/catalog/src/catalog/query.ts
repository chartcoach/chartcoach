import { CatalogError } from "./errors";
import { isJsonString } from "./json";
import type { Catalog, Guideline } from "./model";

export type QueryOptions = Readonly<{
  ids?: readonly string[];
  labels?: readonly string[];
  labelPrefixes?: readonly string[];
  contains?: string;
  limit?: number;
}>;

export type EntryCandidate = Readonly<{
  id: string;
  title: string;
  description: string;
  labels: readonly string[];
}>;

export function queryCatalog(
  catalog: Catalog,
  options: QueryOptions = {},
): readonly EntryCandidate[] {
  if (Object.prototype.toString.call(options) !== "[object Object]") {
    throw new CatalogError("Query options must be an object.");
  }
  const ids = stringArray(options.ids, "ids");
  const labels = stringArray(options.labels, "labels");
  const labelPrefixes = stringArray(options.labelPrefixes, "labelPrefixes");
  const limit = options.limit ?? 50;
  if (!Number.isSafeInteger(limit) || limit < 1) {
    throw new CatalogError("Query limit must be at least 1.");
  }

  validateLabels(catalog, labels);
  validateLabelPrefixes(catalog, labelPrefixes);
  const selected = ids.length > 0 ? ids.map((id) => catalog.require(id)) : [...catalog.guidelines];
  let contains: string | undefined;
  if (options.contains !== undefined) {
    if (!isJsonString(options.contains)) {
      throw new CatalogError("Query contains must be a string.");
    }
    if (options.contains.length > 0) {
      contains = normalizeSearchText(options.contains);
      if (!contains) {
        throw new CatalogError(
          "contains must not consist only of whitespace, hyphens, or underscores.",
        );
      }
    }
  }

  return Object.freeze(
    selected
      .filter((guideline) => labels.every((label) => guideline.labels.includes(label)))
      .filter((guideline) =>
        labelPrefixes.every((prefix) => guideline.labels.some((label) => label.startsWith(prefix))),
      )
      .filter((guideline) => contains === undefined || matchesText(guideline, contains))
      .slice(0, limit)
      .map((guideline) =>
        Object.freeze({
          id: guideline.id,
          title: guideline.title,
          description: guideline.description,
          labels: Object.freeze([...guideline.labels]),
        }),
      ),
  );
}

function validateLabels(catalog: Catalog, labels: readonly string[]): void {
  const available = new Set(catalog.labels());
  const missing = Array.from(new Set(labels.filter((label) => !available.has(label)))).sort();
  if (missing.length === 0) return;
  throw new CatalogError(`Unknown label(s): ${missing.join(", ")}`, {
    code: "lookup",
    details: { labels: missing },
    hints: ["Call `await catalog.describe()` to inspect label families."],
  });
}

function validateLabelPrefixes(catalog: Catalog, prefixes: readonly string[]): void {
  const available = catalog.labels();
  const missing = Array.from(
    new Set(prefixes.filter((prefix) => !available.some((label) => label.startsWith(prefix)))),
  ).sort();
  if (missing.length === 0) return;
  throw new CatalogError(`No labels match prefix(es): ${missing.join(", ")}`, {
    code: "lookup",
    details: { label_prefixes: missing },
    hints: ["Call `await catalog.describe()` to inspect label families."],
  });
}

function stringArray(value: readonly string[] | undefined, name: string): readonly string[] {
  if (value === undefined) return Object.freeze([]);
  if (!Array.isArray(value) || !value.every(isJsonString)) {
    throw new CatalogError(`${name} must be an array of strings.`);
  }
  return value;
}

function matchesText(guideline: Guideline, contains: string): boolean {
  return [guideline.id, guideline.title, guideline.description].some((value) =>
    normalizeSearchText(value).includes(contains),
  );
}

function normalizeSearchText(value: string): string {
  return value
    .toLowerCase()
    .replace(/[-_\s]+/g, " ")
    .trim();
}
