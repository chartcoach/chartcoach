import type { OgImageJob, OgPayload } from "../integrations/og-images";
import { isJsonObject, isJsonString, type JsonValue } from "../lib/json";

export const OG_IMAGE_WIDTH = 1200;

export const OG_IMAGE_HEIGHT = 630;

export const OG_BUILD_PROPS_META = "chartcoach:og-props";

type OgImageKind = "home" | "catalog" | "guideline" | "guideline-json" | "guideline-md" | "page";

type OgImageStat = {
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

function parseStringArray(value: JsonValue | undefined): string[] {
  if (!Array.isArray(value)) return [];

  return value.filter(isJsonString);
}

function parseStat(value: JsonValue | undefined): OgImageStat | undefined {
  if (!isJsonObject(value)) return undefined;

  if (!isJsonString(value.value) || !isJsonString(value.label)) return undefined;

  return { value: value.value, label: value.label };
}

function parseReferences(value: JsonValue | undefined): OgReferenceSummary[] {
  if (!Array.isArray(value)) return [];

  return value.filter(isJsonObject).flatMap((item) => {
    if (!isJsonString(item.title)) return [];

    return [
      {
        title: item.title,
        meta: isJsonString(item.meta) ? item.meta : undefined,
      },
    ];
  });
}

function parseOgImageProps(value: JsonValue | undefined): OgImageProps | null {
  if (!isJsonObject(value)) return null;
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
    !isJsonString(value.title) ||
    !isJsonString(value.description) ||
    !isJsonString(value.eyebrow)
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
    badge: isJsonString(value.badge) ? value.badge : undefined,
    references: parseReferences(value.references),
    roles: parseStringArray(value.roles),
    stat: parseStat(value.stat),
    verbs: parseStringArray(value.verbs),
  };
}

export function parseOgBuildPayload(value: JsonValue): OgBuildPayload | null {
  if (!isJsonObject(value) || !isJsonString(value.imagePathname)) return null;
  const props = parseOgImageProps(value.props);

  if (!props) return null;

  const extraImages = Array.isArray(value.extraImages)
    ? value.extraImages.flatMap((item) => {
        if (!isJsonObject(item) || !isJsonString(item.imagePathname)) return [];
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
