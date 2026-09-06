import { fileURLToPath } from "node:url";

import { afterEach, beforeEach, describe, expect, it, vi } from "vite-plus/test";

import { chartcoachLlmPages } from "../src/config/llms";
const fixture = new URL("../../../fixtures/catalog-release/", import.meta.url);
const siteRoot = new URL("../", import.meta.url);

describe("LLM artifacts", () => {
  beforeEach(() => {
    vi.stubEnv("CHARTCOACH_SITE_CATALOG_SOURCE", fileURLToPath(fixture));
  });

  afterEach(() => {
    vi.unstubAllEnvs();
  });

  it("uses each guideline's canonical Markdown route", async () => {
    const pages = await chartcoachLlmPages({ root: siteRoot });
    const guideline = pages.find((page) => page.pathname === "/guidelines/direct-labels/");
    expect(guideline).toBeDefined();
    expect(guideline?.markdownPathname).toBe("/guidelines/direct-labels.md");
    expect(guideline?.writeMarkdown).toBe(false);
    expect(guideline?.markdown).toContain("\n---\n\n```bibtex\n@article{smith2024,");
  });
});
