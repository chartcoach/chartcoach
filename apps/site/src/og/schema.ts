import type { OgImageJob, OgPayload } from "../integrations/og-images";

export const OG_IMAGE_WIDTH = 1200;
export const OG_IMAGE_HEIGHT = 630;
export const OG_BUILD_PROPS_META = "chartcoach:og-props";

export type OgImageKind =
  | "home"
  | "catalog"
  | "guideline"
  | "guideline-json"
  | "guideline-md"
  | "page";

export type OgImageStat = {
  value: string;
  label: string;
};

export type OgReferenceSummary = {
  title: string;
  meta?: string;
};

export type OgImageProps = {
  kind: OgImageKind;
  title: string;
  description: string;
  eyebrow: string;
  labels: string[];
  metaItems: string[];
  badge?: string;
  references: OgReferenceSummary[];
  roles: string[];
  stat?: OgImageStat;
  verbs: string[];
};

export type OgImageInput = Partial<
  Omit<OgImageProps, "labels" | "metaItems" | "references" | "roles" | "verbs">
> & {
  labels?: readonly string[];
  metaItems?: readonly string[];
  references?: readonly OgReferenceSummary[];
  roles?: readonly string[];
  verbs?: readonly string[];
};

export type OgExtraImageInput = {
  imagePathname: string;
  props: OgImageInput;
};

export type OgImageInputWithExtras = OgImageInput & {
  extraImages?: readonly OgExtraImageInput[];
};

export type OgBuildPayload = OgPayload<OgImageProps> & {
  extraImages: OgImageJob<OgImageProps>[];
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}

function parseStringArray(value: unknown): string[] {
  if (!Array.isArray(value)) return [];
  return value.filter((item): item is string => typeof item === "string");
}

function parseStat(value: unknown): OgImageStat | undefined {
  if (!isRecord(value)) return undefined;
  if (typeof value.value !== "string" || typeof value.label !== "string") return undefined;
  return { value: value.value, label: value.label };
}

function parseReferences(value: unknown): OgReferenceSummary[] {
  if (!Array.isArray(value)) return [];
  return value.filter(isRecord).flatMap((item) => {
    if (typeof item.title !== "string") return [];
    return [
      {
        title: item.title,
        meta: typeof item.meta === "string" ? item.meta : undefined,
      },
    ];
  });
}

export function parseOgImageProps(value: unknown): OgImageProps | null {
  if (!isRecord(value)) return null;
  const kind = value.kind;
  if (
    kind !== "home" &&
    kind !== "catalog" &&
    kind !== "guideline" &&
    kind !== "guideline-json" &&
    kind !== "guideline-md" &&
    kind !== "page"
  ) {
    return null;
  }
  if (
    typeof value.title !== "string" ||
    typeof value.description !== "string" ||
    typeof value.eyebrow !== "string"
  ) {
    return null;
  }

  return {
    kind,
    title: value.title,
    description: value.description,
    eyebrow: value.eyebrow,
    labels: parseStringArray(value.labels),
    metaItems: parseStringArray(value.metaItems),
    badge: typeof value.badge === "string" ? value.badge : undefined,
    references: parseReferences(value.references),
    roles: parseStringArray(value.roles),
    stat: parseStat(value.stat),
    verbs: parseStringArray(value.verbs),
  };
}

export function parseOgBuildPayload(value: unknown): OgBuildPayload | null {
  if (!isRecord(value) || typeof value.imagePathname !== "string") return null;
  const props = parseOgImageProps(value.props);
  if (!props) return null;
  const extraImages = Array.isArray(value.extraImages)
    ? value.extraImages.flatMap((item) => {
        if (!isRecord(item) || typeof item.imagePathname !== "string") return [];
        const extraProps = parseOgImageProps(item.props);
        return extraProps ? [{ imagePathname: item.imagePathname, props: extraProps }] : [];
      })
    : [];
  return {
    imagePathname: value.imagePathname,
    props,
    extraImages,
  };
}
