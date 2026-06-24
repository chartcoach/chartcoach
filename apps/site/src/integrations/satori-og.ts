import type { AstroIntegration } from "astro";

import { renderAsync } from "@resvg/resvg-js";
import { JSDOM } from "jsdom";
import { createRequire } from "node:module";
import fs from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import { createElement } from "react";
import satori from "satori";

import { outputPathForPathname } from "../lib/site-artifacts";
import OgImage from "../og/component";
import {
  OG_BUILD_PROPS_META,
  OG_IMAGE_HEIGHT,
  OG_IMAGE_WIDTH,
  parseOgBuildPayload,
  type OgBuildPayload,
  type OgImageProps,
} from "../og/schema";

type FontOptions = NonNullable<Parameters<typeof satori>[1]["fonts"]>;
type OgRenderJob = {
  imagePathname: string;
  props: OgImageProps;
};
type Logger = {
  info: (message: string) => void;
  warn: (message: string) => void;
};

const require = createRequire(import.meta.url);
const fontFiles = [
  {
    family: "Poppins",
    weight: 400,
    specifier: "@fontsource/poppins/files/poppins-latin-400-normal.woff",
  },
  {
    family: "Poppins",
    weight: 500,
    specifier: "@fontsource/poppins/files/poppins-latin-500-normal.woff",
  },
  {
    family: "Poppins",
    weight: 600,
    specifier: "@fontsource/poppins/files/poppins-latin-600-normal.woff",
  },
  {
    family: "Poppins",
    weight: 700,
    specifier: "@fontsource/poppins/files/poppins-latin-700-normal.woff",
  },
  {
    family: "JetBrains Mono",
    weight: 400,
    specifier: "@fontsource/jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff",
  },
  {
    family: "JetBrains Mono",
    weight: 500,
    specifier: "@fontsource/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff",
  },
  {
    family: "JetBrains Mono",
    weight: 600,
    specifier: "@fontsource/jetbrains-mono/files/jetbrains-mono-latin-600-normal.woff",
  },
] as const;

function loadFonts(): FontOptions {
  return fontFiles.map((font) => ({
    name: font.family,
    data: readFileSync(require.resolve(font.specifier)),
    weight: font.weight,
    style: "normal",
  }));
}

async function listHtmlFiles(dir: string): Promise<string[]> {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const nested = await Promise.all(
    entries.map(async (entry) => {
      const entryPath = path.join(dir, entry.name);
      if (entry.isDirectory()) return listHtmlFiles(entryPath);
      return entry.isFile() && entry.name.endsWith(".html") ? [entryPath] : [];
    }),
  );
  return nested.flat();
}

function readOgPayload(html: string): { payload: OgBuildPayload | null; serializedHtml: string } {
  const dom = new JSDOM(html);
  const marker = dom.window.document.querySelector(`meta[name="${OG_BUILD_PROPS_META}"]`);
  if (!marker) {
    dom.window.close();
    return { payload: null, serializedHtml: html };
  }

  const rawPayload = marker.getAttribute("content") ?? "{}";
  marker.remove();

  try {
    const parsed = parseOgBuildPayload(JSON.parse(rawPayload));
    return {
      payload: parsed,
      serializedHtml: dom.serialize(),
    };
  } finally {
    dom.window.close();
  }
}

async function renderOgPng(job: OgRenderJob, fonts: FontOptions): Promise<Buffer> {
  const svg = await satori(createElement(OgImage, job.props), {
    width: OG_IMAGE_WIDTH,
    height: OG_IMAGE_HEIGHT,
    fonts,
  });
  const image = await renderAsync(svg, {
    fitTo: {
      mode: "width",
      value: OG_IMAGE_WIDTH,
    },
  });
  return image.asPng();
}

async function mapLimit<T>(
  items: readonly T[],
  limit: number,
  callback: (item: T) => Promise<void>,
): Promise<void> {
  let index = 0;
  const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (index < items.length) {
      const item = items[index];
      index += 1;
      await callback(item);
    }
  });
  await Promise.all(workers);
}

export function satoriOg(): AstroIntegration {
  return {
    name: "chartcoach:satori-og",
    hooks: {
      "astro:build:done": async ({ dir, logger }) => {
        const distDir = new URL(dir).pathname;
        const ogLogger: Logger = logger.fork("chartcoach:satori-og");
        const fonts = loadFonts();
        const htmlFiles = await listHtmlFiles(distDir);
        let generatedCount = 0;

        await mapLimit(htmlFiles, 8, async (htmlPath) => {
          const html = await fs.readFile(htmlPath, "utf-8");
          const { payload, serializedHtml } = readOgPayload(html);
          if (!payload) {
            ogLogger.warn(`No OG payload found in ${path.relative(distDir, htmlPath)}`);
            return;
          }

          const jobs: OgRenderJob[] = [
            { imagePathname: payload.imagePathname, props: payload.props },
            ...payload.extraImages,
          ];
          await Promise.all(
            jobs.map(async (job) => {
              const outputPath = outputPathForPathname(distDir, job.imagePathname);
              const png = await renderOgPng(job, fonts);
              await fs.mkdir(path.dirname(outputPath), { recursive: true });
              await fs.writeFile(outputPath, png);
            }),
          );
          await fs.writeFile(htmlPath, serializedHtml, "utf-8");
          generatedCount += jobs.length;
        });

        ogLogger.info(`Generated ${generatedCount.toLocaleString()} static OG image(s).`);
      },
    },
  };
}
