import type { OgBuildPayload, OgExtraImageInput, OgImageInput, OgImageProps } from "./schema";
import { cleanOgText, truncateOgText } from "./text";

function truncateOgMultilineText(value: string, maxLength: number): string {
  const clean = value
    .replace(/[^\S\n]+/g, " ")
    .replace(/\n[^\S\n]*/g, "\n")
    .trim();
  if (clean.length <= maxLength) return clean;
  return truncateOgText(clean.replace(/\n/g, " "), maxLength);
}

export function buildOgImageProps(
  input: OgImageInput & { title: string; description: string },
): OgImageProps {
  const kind = input.kind ?? "page";
  return {
    kind,
    title: truncateOgText(input.title, 150),
    description: truncateOgText(input.description, 210),
    eyebrow: truncateOgText(input.eyebrow ?? "chartcoach", 64),
    labels: [...(input.labels ?? [])].map(cleanOgText).filter(Boolean).slice(0, 7),
    metaItems: [...(input.metaItems ?? [])].map(cleanOgText).filter(Boolean).slice(0, 4),
    badge: input.badge ? truncateOgText(input.badge, 24) : undefined,
    references: [...(input.references ?? [])]
      .map((reference) => ({
        title: truncateOgText(reference.title, 140),
        meta: reference.meta ? truncateOgText(reference.meta, 120) : undefined,
      }))
      .filter((reference) => reference.title)
      .slice(0, 2),
    roles: [...(input.roles ?? [])].map(cleanOgText).filter(Boolean).slice(0, 8),
    stat: input.stat
      ? {
          value: truncateOgText(input.stat.value, 20),
          label: truncateOgMultilineText(input.stat.label, 72),
        }
      : undefined,
    verbs: [...(input.verbs ?? [])].map(cleanOgText).filter(Boolean).slice(0, 5),
  };
}

export function buildOgPayload(payload: {
  imagePathname: string;
  props: OgImageProps;
  extraImages?: readonly OgExtraImageInput[];
  title: string;
  description: string;
}): string {
  const extraImages = [...(payload.extraImages ?? [])].map((image) => ({
    imagePathname: image.imagePathname,
    props: buildOgImageProps({
      kind: payload.props.kind,
      ...image.props,
      title: image.props.title ?? payload.title,
      description: image.props.description ?? payload.description,
    }),
  }));
  const buildPayload: OgBuildPayload = {
    imagePathname: payload.imagePathname,
    props: payload.props,
    extraImages,
  };
  return JSON.stringify(buildPayload);
}
