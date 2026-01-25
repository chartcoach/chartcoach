import { env } from "@chartcoach/eval-ui/env";

const DEV_FALLBACK_TEMPLATE = "http://localhost:4321/guidelines/{id}/";

export function getGuidelineDetailHref(guidelineId: string) {
  const template =
    env.VITE_GUIDELINE_DETAIL_URL_TEMPLATE ??
    (import.meta.env.DEV ? DEV_FALLBACK_TEMPLATE : undefined);

  if (!template) return;

  return template.replaceAll("{id}", encodeURIComponent(guidelineId));
}
