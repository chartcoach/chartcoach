import { count, create, load } from "@orama/orama";
import { build } from "astro";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { afterAll, beforeAll, describe, expect, it, vi } from "vite-plus/test";

import { GUIDELINE_SEARCH_SCHEMA } from "../src/lib/guideline-search-model";
import { OG_BUILD_PROPS_META } from "../src/og/schema";

const fixture = new URL("../../../fixtures/catalog-release/", import.meta.url);
const siteRoot = new URL("../", import.meta.url);
let outputDirectory: string;
let outputFiles: string[];

beforeAll(async () => {
  outputDirectory = await fs.mkdtemp(path.join(os.tmpdir(), "chartcoach-site-"));
  vi.stubEnv("CHARTCOACH_SITE_CATALOG", fileURLToPath(fixture));
  await build({
    logLevel: "silent",
    outDir: outputDirectory,
    root: fileURLToPath(siteRoot),
  });
  outputFiles = await fs.readdir(outputDirectory, { recursive: true });
}, 30_000);

afterAll(async () => {
  vi.unstubAllEnvs();
  await fs.rm(outputDirectory, { force: true, recursive: true });
});

describe("generated site artifacts", () => {
  it("indexes every generated guideline", async () => {
    const guidelineJsonFiles = outputFiles.filter((file) => /^guidelines\/[^/]+\.json$/.test(file));
    const raw = JSON.parse(
      await fs.readFile(path.join(outputDirectory, "assets/search-guidelines.json"), "utf8"),
    );
    const database = create({ schema: GUIDELINE_SEARCH_SCHEMA });
    load(database, raw);

    expect(count(database)).toBe(guidelineJsonFiles.length);
  });

  it("writes every referenced and guideline-specific Open Graph image", async () => {
    const expectedImages = new Set<string>();

    for (const file of outputFiles) {
      if (/^guidelines\/[^/]+\.json$/.test(file)) {
        const id = path.basename(file, ".json");
        expectedImages.add(`guidelines/${id}/og.png`);
        expectedImages.add(`guidelines/${id}.json.png`);
        expectedImages.add(`guidelines/${id}.md.png`);
      }
      if (!file.endsWith(".html")) continue;

      const html = await fs.readFile(path.join(outputDirectory, file), "utf8");
      expect(html).not.toContain(OG_BUILD_PROPS_META);
      const image = /<meta property="og:image" content="([^"]+)"/.exec(html)?.[1];
      expect(image, file).toBeDefined();
      if (image) expectedImages.add(new URL(image).pathname.replace(/^\/+/, ""));
    }

    for (const image of expectedImages) {
      const bytes = await fs.readFile(path.join(outputDirectory, image));
      expect(bytes.readUInt32BE(16), image).toBe(1200);
      expect(bytes.readUInt32BE(20), image).toBe(630);
    }
  });
});
