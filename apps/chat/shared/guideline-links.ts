import { z } from "zod";

const urlTemplate = z.string().refine((value) => {
  if (value.split("{id}").length !== 2 || /[{}]/.test(value.replace("{id}", ""))) return false;

  if (/[?#]/.test(value)) return false;
  const sample = value.replace("{id}", "chartcoach-guideline-id");

  if (!URL.canParse(sample)) return false;
  const url = new URL(sample);

  return (
    ["https:", "http:"].includes(url.protocol) &&
    !url.username &&
    !url.password &&
    !url.search &&
    !url.hash &&
    value.indexOf("/", value.indexOf("://") + 3) !== -1 &&
    value.indexOf("{id}") > value.indexOf("/", value.indexOf("://") + 3)
  );
}, "Use an HTTP or HTTPS URL with one {id} placeholder in its path and no credentials, query, or fragment.");

export const guidelineLinksSchema = z.strictObject({
  urlTemplate: urlTemplate.default("https://chartcoach.dev/guidelines/{id}"),
  imageURLTemplate: urlTemplate.optional(),
});

export type GuidelineLinks = z.infer<typeof guidelineLinksSchema>;

export const defaultGuidelineLinks = guidelineLinksSchema.parse({});

export function guidelineURLs(id: string, links: GuidelineLinks) {
  if (!id || id === "." || id === "..") return;
  const encoded = encodeURIComponent(id);
  const url = links.urlTemplate.replace("{id}", encoded);

  return {
    url,
    imageURL:
      links.imageURLTemplate?.replace("{id}", encoded) ?? `${url.replace(/\/$/, "")}/og.png`,
  };
}
