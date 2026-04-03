import { describe, expect, it } from "vitest";

import { sidebar } from "../astro.sidebar";
import {
  headerNavigation,
  siteNavigation,
  siteSocialLinks,
  sidebarNavigation,
} from "../config/navigation";
import { createStarlightConfig, docsHeadDefaults } from "../config/starlight";
import { createSocialImageHead } from "../src/lib/site-metadata";

describe("apps/site navigation structure", () => {
  it("drives header links from the shared navigation manifest", () => {
    expect(headerNavigation).toEqual(
      siteNavigation.map(({ id, href, headerLabel }) => ({
        id,
        href,
        label: headerLabel,
      })),
    );
  });

  it("builds the sidebar from the same route manifest", () => {
    expect(sidebar).toEqual(sidebarNavigation);
    expect(sidebar).toEqual([
      {
        label: "Start",
        items: [
          { label: "Overview", link: "/" },
          { label: "Catalog structure", link: "/catalog/" },
          { label: "Labels & filters", link: "/labels/" },
          { label: "About", link: "/about/" },
        ],
      },
      {
        label: "Catalog",
        items: [{ label: "Guidelines", link: "/guidelines/" }],
      },
    ]);
  });
});

describe("apps/site starlight config", () => {
  it("keeps shared docs metadata and social links in the extracted starlight config", () => {
    const config = createStarlightConfig({ enableAgentationReview: false });

    expect(config.social).toEqual(siteSocialLinks);
    expect(docsHeadDefaults).toEqual(createSocialImageHead("/social/chartcoach-share-default.png"));
    expect(config.head).toEqual(docsHeadDefaults);
    expect(config.sidebar).toEqual(sidebar);
    expect(config.components).toEqual({
      Header: "./src/components/starlight/Header.astro",
      Pagination: "./src/components/starlight/Pagination.astro",
      TableOfContents: "./src/components/starlight/TableOfContents.astro",
      MobileTableOfContents: "./src/components/starlight/MobileTableOfContents.astro",
    });
  });

  it("keeps agentation quarantined behind explicit opt-in", () => {
    const config = createStarlightConfig({ enableAgentationReview: true });

    expect(config.components).toMatchObject({
      PageFrame: "./src/components/starlight/PageFrameAgentation.astro",
    });
  });
});
