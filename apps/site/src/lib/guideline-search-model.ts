import type { Guideline } from "@chartcoach/catalog";

import { createGuidelineRecord, type GuidelineRecord } from "./guideline-record";

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
  bibliography: string;
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
  bibliography: "string",
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
  "bibliography",
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
  bibliography: 0.5,
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

const SCRIPT_JSON_ESCAPES: Record<string, string> = {
  "<": "\\u003c",
  "\u2028": "\\u2028",
  "\u2029": "\\u2029",
};

export function createGuidelineSearchModel(guideline: Guideline): GuidelineSearchModel {
  const record = createGuidelineRecord(guideline);
  return {
    ...record,
    description: record.description || undefined,
  };
}

export function createGuidelineSearchDocument(
  model: GuidelineSearchModel,
  path = `/guidelines/${model.id}/`,
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
    bibliography: model.bibliography ?? "",
    references: model.references,
  };
}

export function serializeGuidelineSearchModel(model: GuidelineSearchModel): string {
  return JSON.stringify(model).replace(/[<\u2028\u2029]/g, (match) => SCRIPT_JSON_ESCAPES[match]);
}

export function parseGuidelineSearchModel(value: string): GuidelineSearchModel {
  const model = JSON.parse(value) as Partial<GuidelineSearchModel>;
  if (!model.id || !model.title || !model.body) {
    throw new Error("Guideline search record is missing required fields.");
  }
  if (
    !Array.isArray(model.labels) ||
    !model.labels.every(isString) ||
    !Array.isArray(model.sections) ||
    !Array.isArray(model.references) ||
    !model.references.every(isString)
  ) {
    throw new Error("Guideline search record has invalid collection fields.");
  }

  return {
    id: model.id,
    title: model.title,
    description: model.description,
    labels: model.labels,
    body: model.body,
    sections: model.sections.map((section) => ({
      role: String(section.role ?? ""),
      title: String(section.title ?? ""),
      content: String(section.content ?? ""),
    })),
    bibliography: model.bibliography,
    references: model.references,
  };
}

function isString(value: unknown): value is string {
  return typeof value === "string";
}
