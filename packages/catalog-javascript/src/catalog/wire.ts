import { CatalogError } from "./errors";
import { normalizeLabel } from "./labels";
import type { Guideline, GuidelineSection } from "./model";

export type CatalogRowWire = {
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
    value.role.trim().length > 0 &&
    typeof value.title === "string" &&
    typeof value.content === "string"
  );
}

function isSectionArray(value: unknown): value is GuidelineSection[] {
  return Array.isArray(value) && value.every(isGuidelineSection);
}

function sectionsFromWire(value: GuidelineSection[]): GuidelineSection[] {
  return value.map((section) => ({
    role: section.role.trim(),
    title: section.title,
    content: section.content,
  }));
}

export function isCatalogRowWire(value: unknown): value is CatalogRowWire {
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

export function guidelineFromWire(value: unknown): Guideline | null {
  if (!isCatalogRowWire(value)) return null;

  const { guideline, references } = value;
  const sections = sectionsFromWire(guideline.sections);
  let labels: string[];
  try {
    labels = guideline.labels.map((label) => normalizeLabel(label, "guideline label"));
  } catch {
    return null;
  }

  return {
    id: guideline.id,
    title: guideline.title,
    bibliography: typeof guideline.bibliography === "string" ? guideline.bibliography : undefined,
    description: guideline.description,
    labels,
    body: guideline.body,
    sections,
    references: [...references],
  };
}

export function requireGuidelineFromWire(value: unknown, context?: string): Guideline {
  const guideline = guidelineFromWire(value);
  if (guideline) return guideline;

  const suffix = context ? ` (${context})` : "";
  throw new CatalogError(`Invalid catalog row format${suffix}.`);
}
