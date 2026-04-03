import { describe, expect, it } from "vitest";

import {
  DEFAULT_SITE_URL,
  getSiteRuntimeConfig,
  isAgentationReviewEnabled,
  resolveSiteUrl,
} from "../config/site";
import {
  createGuidelinePageFrontmatter,
  createSocialImageHead,
  guidelinesShareImage,
} from "../src/lib/site-metadata";

describe("apps/site config helpers", () => {
  it("prefers explicit site url env vars and normalizes valid values", () => {
    expect(
      resolveSiteUrl({
        SITE_URL: "https://chartcoach.example",
        PUBLIC_SITE_URL: "https://fallback.example",
      }),
    ).toBe("https://chartcoach.example/");
  });

  it("skips invalid env vars until it finds a valid candidate", () => {
    expect(
      resolveSiteUrl({
        SITE_URL: "not a url",
        PUBLIC_SITE_URL: "https://public.chartcoach.example",
      }),
    ).toBe("https://public.chartcoach.example/");
  });

  it("treats local dev and explicit env flags as agentation review opt-ins", () => {
    expect(isAgentationReviewEnabled({ env: {}, argv: ["astro", "dev"] })).toBe(true);
    expect(
      isAgentationReviewEnabled({
        env: { PUBLIC_ENABLE_AGENTATION: "true" },
        argv: ["astro", "build"],
      }),
    ).toBe(true);
    expect(isAgentationReviewEnabled({ env: {}, argv: ["astro", "build"] })).toBe(false);
  });

  it("returns a default runtime config when no deploy url is available", () => {
    expect(getSiteRuntimeConfig({ env: {}, argv: ["astro", "build"] })).toEqual({
      siteUrl: DEFAULT_SITE_URL,
      siteUrlSource: "default",
      enableAgentationReview: false,
    });
  });
});
describe("apps/site metadata helpers", () => {
  it("builds guideline frontmatter with no toc and the guidelines share image", () => {
    expect(
      createGuidelinePageFrontmatter({
        title: "Guidelines",
        description: "Browse the Chartcoach guideline catalog.",
      }),
    ).toEqual({
      title: "Guidelines",
      description: "Browse the Chartcoach guideline catalog.",
      tableOfContents: false,
      head: createSocialImageHead(guidelinesShareImage),
    });
  });
});
