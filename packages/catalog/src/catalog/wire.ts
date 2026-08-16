import { CatalogError } from "./errors";
import { isJsonObject, isJsonString, type JsonObject, type JsonValue } from "./json";
import { normalizeLabel } from "./labels";
import type { Guideline, GuidelineSection } from "./model";

export type CatalogRowWire = {
  id: string;
  title: string;
  description: string;
  labels: string[];
  sections: GuidelineSection[];
  references: string[];
};

const catalogRowFields = [
  "id",
  "title",
  "description",
  "labels",
  "sections",
  "references",
] as const;
const sectionFields = ["role", "title", "content"] as const;

function hasFields(value: JsonObject, fields: readonly string[]): boolean {
  const keys = Object.keys(value);
  return keys.length === fields.length && fields.every((field) => Object.hasOwn(value, field));
}

function isStringArray(value: JsonValue | undefined): value is string[] {
  return Array.isArray(value) && value.every(isJsonString);
}

function isGuidelineSection(value: JsonValue): value is GuidelineSection {
  if (!isJsonObject(value) || !hasFields(value, sectionFields)) return false;
  const { content, role, title } = value;
  return (
    isJsonString(role) &&
    role.length > 0 &&
    role === role.trim() &&
    isJsonString(title) &&
    title === title.trim() &&
    isJsonString(content) &&
    content === content.trim() &&
    (role === "__dangling__" ? title.length === 0 && content.length > 0 : title.length > 0)
  );
}

function isSectionArray(value: JsonValue | undefined): value is GuidelineSection[] {
  if (!Array.isArray(value) || value.length === 0 || !value.every(isGuidelineSection)) return false;
  const dangling = value.flatMap((section, index) =>
    section.role === "__dangling__" ? [index] : [],
  );
  return dangling.length === 0 || (dangling.length === 1 && dangling[0] === 0);
}

export function isCatalogRowWire(value: JsonValue): value is CatalogRowWire {
  if (!isJsonObject(value) || !hasFields(value, catalogRowFields)) return false;
  const { description, id, labels, references, sections, title } = value;
  if (!isJsonString(id) || id.length === 0) return false;
  if (!isJsonString(title) || !isJsonString(description)) return false;
  if (!isStringArray(labels) || !isSectionArray(sections)) return false;
  if (!isStringArray(references)) return false;
  try {
    return labels.every((label) => normalizeLabel(label) === label);
  } catch {
    return false;
  }
}

export function guidelineFromWire(value: JsonValue): Omit<Guideline, "body"> | null {
  if (!isCatalogRowWire(value)) return null;

  const sections = value.sections.map((section) => ({ ...section }));
  return {
    id: value.id,
    title: value.title,
    description: value.description,
    labels: [...value.labels],
    sections,
    references: [...value.references],
  };
}

export function requireGuidelineFromWire(
  value: JsonValue,
  context?: string,
): Omit<Guideline, "body"> {
  const guideline = guidelineFromWire(value);
  if (guideline) return guideline;

  const suffix = context ? ` (${context})` : "";
  throw new CatalogError(`Invalid catalog row format${suffix}.`);
}
