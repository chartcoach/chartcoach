import type { Guideline } from "@chartcoach/catalog";

import { createGuidelineRecord, type GuidelineRecord } from "./guideline-record";
import { isJsonObject, isJsonString, parseJson, type JsonValue } from "./json";
import { guidelinePath } from "./routes";

export type GuidelineSearchModel = Omit<GuidelineRecord, "description"> & {
  description?: string;
};

export type GuidelineSearchDocument = {
  path: string;
  slug: string;
  title: string;
  description: string;
  labels: string[];
  body: string;
  sectionRoles: string[];
  sectionTitles: string[];
  sectionContent: string[];
  references: string[];
};

export const GUIDELINE_SEARCH_SCHEMA = {
  path: "string",
  slug: "string",
  title: "string",
  description: "string",
  labels: "string[]",
  body: "string",
  sectionRoles: "string[]",
  sectionTitles: "string[]",
  sectionContent: "string[]",
  references: "string[]",
} as const;

export const GUIDELINE_SEARCH_PROPERTIES = [
  "title",
  "slug",
  "labels",
  "description",
  "sectionTitles",
  "sectionRoles",
  "body",
  "sectionContent",
  "references",
] as const;

export const GUIDELINE_SEARCH_BOOST = {
  title: 5,
  slug: 4,
  labels: 4,
  description: 3,
  sectionTitles: 3,
  sectionRoles: 2,
  body: 1.6,
  sectionContent: 1.3,
  references: 0.4,
} as const;

function decodePathSegment(segment: string) {
  try {
    return decodeURIComponent(segment);
  } catch {
    return segment;
  }
}

function createSlugSearchText(path: string) {
  const slug = path.split("/").filter(Boolean).at(-1);
  if (!slug) return "";

  const decodedSlug = decodePathSegment(slug);
  const readableSlug = decodedSlug.replace(/[-_]+/g, " ");
  return [...new Set([decodedSlug, readableSlug])].join(" ");
}

const SCRIPT_JSON_ESCAPES = new Map([
  ["<", "\\u003c"],
  ["\u2028", "\\u2028"],
  ["\u2029", "\\u2029"],
]);

export function createGuidelineSearchModel(guideline: Guideline): GuidelineSearchModel {
  const record = createGuidelineRecord(guideline);
  return {
    ...record,
    description: record.description || undefined,
  };
}

export function createGuidelineSearchDocument(
  model: GuidelineSearchModel,
  path = guidelinePath(model.id),
): GuidelineSearchDocument {
  return {
    path,
    slug: createSlugSearchText(path),
    title: model.title,
    description: model.description ?? "",
    labels: model.labels,
    body: model.body,
    sectionRoles: model.sections.map((section) => section.role),
    sectionTitles: model.sections.map((section) => section.title),
    sectionContent: model.sections.map((section) => section.content),
    references: model.references,
  };
}

export function serializeGuidelineSearchModel(model: GuidelineSearchModel): string {
  return JSON.stringify(model).replace(
    /[<\u2028\u2029]/g,
    (match) => SCRIPT_JSON_ESCAPES.get(match) ?? match,
  );
}

export function parseGuidelineSearchModel(value: string): GuidelineSearchModel {
  const model = parseJson(value);
  if (
    !isJsonObject(model) ||
    !isJsonString(model.id) ||
    model.id.length === 0 ||
    !isJsonString(model.title) ||
    model.title.length === 0 ||
    !isJsonString(model.body) ||
    model.body.length === 0
  ) {
    throw new Error("Guideline search entry is missing required fields.");
  }
  if (
    !Array.isArray(model.labels) ||
    !model.labels.every(isJsonString) ||
    !Array.isArray(model.sections) ||
    !model.sections.every(isSearchSection) ||
    !Array.isArray(model.references) ||
    !model.references.every(isJsonString) ||
    (model.description !== undefined && !isJsonString(model.description))
  ) {
    throw new Error("Guideline search entry has invalid collection fields.");
  }

  return {
    id: model.id,
    title: model.title,
    description: model.description,
    labels: model.labels,
    body: model.body,
    sections: model.sections,
    references: model.references,
  };
}

function isSearchSection(value: JsonValue): value is GuidelineSearchModel["sections"][number] {
  return (
    isJsonObject(value) &&
    isJsonString(value.role) &&
    isJsonString(value.title) &&
    isJsonString(value.content)
  );
}
