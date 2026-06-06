import { parseLabel } from "@chartcoach/catalog";

export type ParsedGuidelineLabel = {
  family: string;
  category: string;
  modifier?: string;
  value: string;
  full: string;
  familyLower: string;
  fullLower: string;
};

export function parseGuidelineLabel(label: string): ParsedGuidelineLabel {
  const parsed = parseLabel(label, "guideline label");
  const value =
    parsed.modifier === undefined
      ? parsed.category
      : `${parsed.category}:${parsed.modifier}`;

  return {
    family: parsed.family,
    category: parsed.category,
    modifier: parsed.modifier,
    value,
    full: parsed.value,
    familyLower: parsed.family.toLowerCase(),
    fullLower: parsed.value.toLowerCase(),
  };
}

export function decodeGuidelineLabelQueryValue(value: string): string {
  const raw = String(value ?? "").trim();
  if (!raw) return "";
  if (raw.includes(":")) return raw;
  const idx = raw.indexOf("--");
  if (idx === -1) return raw;
  return `${raw.slice(0, idx)}:${raw.slice(idx + 2)}`;
}

export function encodeGuidelineLabelQueryValue(value: string): string {
  const raw = String(value ?? "").trim();
  if (!raw) return "";
  return raw.replaceAll(":", "--");
}

export function normalizeGuidelineLabelFilter(value: string): string {
  const raw = decodeGuidelineLabelQueryValue(value);
  if (!raw) return "";

  const idx = raw.indexOf(":");
  if (idx === -1) return raw.toLowerCase();

  const family = raw.slice(0, idx).trim().toLowerCase();
  const rest = raw
    .slice(idx + 1)
    .trim()
    .toLowerCase();
  if (!family) return rest;
  if (!rest) return family;
  return `${family}:${rest}`;
}

export function formatGuidelineLabelFilter(value: string): string {
  const text = String(value ?? "");
  if (!text) return "";
  const idx = text.indexOf(":");
  if (idx === -1) return text.toUpperCase();
  const family = text.slice(0, idx).toUpperCase();
  const rest = text.slice(idx + 1);
  return `${family}: ${rest}`;
}
