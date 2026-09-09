import { CatalogError } from "./errors";
import { isJsonObject, type JsonObject, type JsonValue } from "./json";
import { isGuidelineInput, type GuidelineInput, type GuidelineSection } from "./model";

type CatalogRowWire = {
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

function isCatalogRowWire(value: JsonValue): value is CatalogRowWire {
  if (!isJsonObject(value) || !hasFields(value, catalogRowFields)) return false;
  const sections = value.sections;
  if (!Array.isArray(sections) || !sections.every(sectionHasExactFields)) return false;
  return isGuidelineInput(value);
}

function guidelineFromWire(value: JsonValue): GuidelineInput | null {
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

export function requireGuidelineFromWire(value: JsonValue, context?: string): GuidelineInput {
  const guideline = guidelineFromWire(value);
  if (guideline) return guideline;

  const suffix = context ? ` (${context})` : "";
  throw new CatalogError(`Invalid catalog row format${suffix}.`);
}

function sectionHasExactFields(value: JsonValue): value is GuidelineSection {
  return isJsonObject(value) && hasFields(value, sectionFields);
}
