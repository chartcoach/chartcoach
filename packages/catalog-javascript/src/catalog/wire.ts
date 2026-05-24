import type { CatalogEntry, GuidelineSection } from "./model.js";
import { indexGuidelineSections } from "./parse.js";

export type CatalogEntryWire = {
  id: string;
  guideline: {
    id: string;
    title: string;
    bibliography?: string | null;
    description: string;
    labels: string[];
    body: string;
    sections: GuidelineSection[];
  };
  references: string[];
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}

function isGuidelineSection(value: unknown): value is GuidelineSection {
  return (
    isRecord(value) &&
    typeof value.role === "string" &&
    typeof value.title === "string" &&
    typeof value.content === "string"
  );
}

function isSectionArray(value: unknown): value is GuidelineSection[] {
  return Array.isArray(value) && value.every(isGuidelineSection);
}

function sectionsFromWire(value: GuidelineSection[]): GuidelineSection[] {
  return value.map((section) => ({
    role: section.role,
    title: section.title,
    content: section.content,
  }));
}

export function isCatalogEntryWire(value: unknown): value is CatalogEntryWire {
  if (!isRecord(value)) return false;
  if (typeof value.id !== "string" || value.id.length === 0) return false;
  if (!isRecord(value.guideline)) return false;
  if (value.guideline.id !== value.id) return false;
  if (typeof value.guideline.title !== "string") return false;
  if (typeof value.guideline.description !== "string") return false;
  if (typeof value.guideline.body !== "string") return false;
  if (!isStringArray(value.guideline.labels)) return false;
  if (!isSectionArray(value.guideline.sections)) return false;
  if (!isStringArray(value.references)) return false;
  return true;
}

export function catalogEntryFromWire(value: unknown): CatalogEntry | null {
  if (!isCatalogEntryWire(value)) return null;

  const { guideline, references } = value;
  const sections = sectionsFromWire(guideline.sections);

  const entry: CatalogEntry = {
    guideline: {
      id: guideline.id,
      title: guideline.title,
      bibliography: typeof guideline.bibliography === "string" ? guideline.bibliography : undefined,
      description: guideline.description,
      labels: [...guideline.labels],
      body: guideline.body,
      sections,
      sectionsIndex: indexGuidelineSections(sections),
    },
    references: [...references],
  };

  return entry;
}

export function requireCatalogEntryFromWire(value: unknown, context?: string): CatalogEntry {
  const entry = catalogEntryFromWire(value);
  if (entry) return entry;

  const suffix = context ? ` (${context})` : "";
  throw new Error(`Invalid CatalogEntry wire format${suffix}.`);
}
