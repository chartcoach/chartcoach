import { describe, expect, it } from "vite-plus/test";

import { getSiteRuntimeConfig } from "../src/config/site";

describe("site URL resolution", () => {
  it("uses the Portless route during local development", () => {
    expect(
      getSiteRuntimeConfig({
        env: { PORTLESS_URL: "https://search-ui.chartcoach.localhost" },
      }),
    ).toEqual({
      siteUrl: "https://search-ui.chartcoach.localhost/",
      siteUrlSource: "portless",
      isPreviewDeployment: false,
    });
  });

  it("prefers an explicit site URL over deployment and local routes", () => {
    expect(
      getSiteRuntimeConfig({
        env: {
          CHARTCOACH_SITE_URL: "https://preview.example.com",
          CF_PAGES_URL: "https://chartcoach.pages.dev",
          PORTLESS_URL: "https://search-ui.chartcoach.localhost",
        },
      }),
    ).toMatchObject({
      siteUrl: "https://preview.example.com/",
      siteUrlSource: "env",
    });
  });

  it("prefers the Cloudflare Pages URL over a local route", () => {
    expect(
      getSiteRuntimeConfig({
        env: {
          CF_PAGES_URL: "https://chartcoach.pages.dev",
          PORTLESS_URL: "https://search-ui.chartcoach.localhost",
        },
      }),
    ).toMatchObject({
      siteUrl: "https://chartcoach.pages.dev/",
      siteUrlSource: "cloudflare",
    });
  });
});
