export type ParsedGuidelineLabel = {
  family: string | null;
  value: string;
  full: string;
  familyLower: string | null;
  fullLower: string;
};

export function parseGuidelineLabel(label: string): ParsedGuidelineLabel {
  const normalized = String(label ?? "").trim();
  const idx = normalized.indexOf(":");

  if (idx === -1) {
    const value = normalized;
    return {
      family: null,
      value,
      full: value,
      familyLower: null,
      fullLower: value.toLowerCase(),
    };
  }

  const family = normalized.slice(0, idx).trim();
  const value = normalized.slice(idx + 1).trim();
  const full = `${family}:${value}`;

  return {
    family,
    value,
    full,
    familyLower: family.toLowerCase(),
    fullLower: full.toLowerCase(),
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
