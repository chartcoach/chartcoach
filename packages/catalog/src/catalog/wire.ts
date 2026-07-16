import { CatalogError } from "./errors";
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

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

function hasFields(value: Record<string, unknown>, fields: readonly string[]): boolean {
  const keys = Object.keys(value);
  return keys.length === fields.length && fields.every((field) => Object.hasOwn(value, field));
}

function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}

function isGuidelineSection(value: unknown): value is GuidelineSection {
  return (
    isRecord(value) &&
    hasFields(value, sectionFields) &&
    typeof value.role === "string" &&
    value.role.length > 0 &&
    value.role === value.role.trim() &&
    typeof value.title === "string" &&
    value.title === value.title.trim() &&
    typeof value.content === "string" &&
    value.content === value.content.trim() &&
    (value.role === "__dangling__"
      ? value.title.length === 0 && value.content.length > 0
      : value.title.length > 0)
  );
}

function isSectionArray(value: unknown): value is GuidelineSection[] {
  if (!Array.isArray(value) || value.length === 0 || !value.every(isGuidelineSection)) return false;
  const dangling = value.flatMap((section, index) =>
    section.role === "__dangling__" ? [index] : [],
  );
  return dangling.length === 0 || (dangling.length === 1 && dangling[0] === 0);
}

export function isCatalogRowWire(value: unknown): value is CatalogRowWire {
  if (!isRecord(value) || !hasFields(value, catalogRowFields)) return false;
  if (typeof value.id !== "string" || value.id.length === 0) return false;
  if (typeof value.title !== "string" || typeof value.description !== "string") return false;
  if (!isStringArray(value.labels) || !isSectionArray(value.sections)) return false;
  if (!isStringArray(value.references)) return false;
  try {
    return value.labels.every((label) => normalizeLabel(label) === label);
  } catch {
    return false;
  }
}

export function guidelineFromWire(value: unknown): Omit<Guideline, "body"> | null {
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
  value: unknown,
  context?: string,
): Omit<Guideline, "body"> {
  const guideline = guidelineFromWire(value);
  if (guideline) return guideline;

  const suffix = context ? ` (${context})` : "";
  throw new CatalogError(`Invalid catalog row format${suffix}.`);
}
