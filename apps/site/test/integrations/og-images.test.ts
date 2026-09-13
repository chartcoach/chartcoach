import { mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { createElement } from "react";
import { afterEach, describe, expect, it } from "vite-plus/test";

import { ogImages, type OgPayload } from "../../src/integrations/og-images";
import type { JsonValue } from "../../src/lib/json";
import { createTestLogger, requireIntegrationHook } from "../astro";

type ImageProps = { color: string };

const temporaryDirectories: string[] = [];

afterEach(() => {
  for (const directory of temporaryDirectories.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function temporaryDirectory() {
  const directory = mkdtempSync(path.join(os.tmpdir(), "chartcoach-og-images-"));
  temporaryDirectories.push(directory);

  return directory;
}

function Image({ color }: ImageProps) {
  return createElement("div", {
    style: { backgroundColor: color, display: "flex", height: "100%", width: "100%" },
  });
}

function integration(parsePayload: (value: JsonValue) => OgPayload<ImageProps> | null) {
  return ogImages({
    component: Image,
    metaName: "test:og-payload",
    parsePayload,
    width: 120,
    height: 63,
  });
}

function htmlWithPayload(payload: JsonValue) {
  const content = JSON.stringify(payload).replaceAll("&", "&amp;").replaceAll('"', "&quot;");

  return `<!doctype html><html><head><meta name="test:og-payload" content="${content}"></head><body>Page</body></html>`;
}

async function runBuild(
  output: string,
  parsePayload: (value: JsonValue) => OgPayload<ImageProps> | null,
) {
  const build = requireIntegrationHook(integration(parsePayload), "astro:build:done");
  const { logger } = createTestLogger();
  await build({
    assets: new Map(),
    dir: pathToFileURL(`${output}/`),
    logger,
    pages: [],
  });
}

describe("ogImages", () => {
  it("renders every image in the payload and removes the build marker", async () => {
    const output = temporaryDirectory();
    const pageDirectory = path.join(output, "guide");
    mkdirSync(pageDirectory);
    const htmlPath = path.join(pageDirectory, "index.html");

    const payload: OgPayload<ImageProps> = {
      imagePathname: "/assets/main.png",
      props: { color: "#ffffff" },
      extraImages: [{ imagePathname: "/assets/extra.png", props: { color: "#111111" } }],
    };

    writeFileSync(htmlPath, htmlWithPayload(payload));

    await runBuild(output, () => payload);

    expect(readFileSync(htmlPath, "utf8")).not.toContain("test:og-payload");

    for (const name of ["main.png", "extra.png"]) {
      expect([...readFileSync(path.join(output, "assets", name)).subarray(0, 8)]).toEqual([
        137, 80, 78, 71, 13, 10, 26, 10,
      ]);
    }
  });

  it("removes a marker whose payload the site rejects", async () => {
    const output = temporaryDirectory();
    const htmlPath = path.join(output, "index.html");
    writeFileSync(htmlPath, htmlWithPayload({ unexpected: true }));

    await runBuild(output, () => null);

    expect(readFileSync(htmlPath, "utf8")).not.toContain("test:og-payload");
  });
});
