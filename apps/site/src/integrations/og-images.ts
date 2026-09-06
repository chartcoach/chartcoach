import type { AstroIntegration } from "astro";
import type { ComponentType } from "react";

import { renderAsync } from "@resvg/resvg-js";
import { JSDOM } from "jsdom";
import fs from "node:fs/promises";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createElement } from "react";
import satori from "satori";

import { parseJson, type JsonValue } from "../lib/json";

export type OgImageJob<Props> = {
  imagePathname: string;
  props: Props;
};

export type OgPayload<Props> = OgImageJob<Props> & {
  extraImages?: readonly OgImageJob<Props>[];
};

export type OgImagesOptions<Props extends object> = {
  component: ComponentType<Props>;
  name?: string;
  metaName: string;
  parsePayload: (value: JsonValue) => OgPayload<Props> | null;
  width: number;
  height: number;
};

type FontOptions = NonNullable<Parameters<typeof satori>[1]["fonts"]>;
type ReadPayloadResult<Props> = {
  found: boolean;
  html: string;
  payload: OgPayload<Props> | null;
};

const require = createRequire(import.meta.url);
const fontFamilies = [
  {
    name: "Poppins",
    package: "@fontsource/poppins",
    file: "poppins",
    weights: [400, 500, 600, 700],
  },
  {
    name: "JetBrains Mono",
    package: "@fontsource/jetbrains-mono",
    file: "jetbrains-mono",
    weights: [400, 500, 600],
  },
] as const;

function loadFonts(): FontOptions {
  return fontFamilies.flatMap((family) =>
    family.weights.map((weight) => ({
      name: family.name,
      data: readFileSync(
        require.resolve(
          `${family.package}/files/${family.file}-latin-${weight.toString()}-normal.woff`,
        ),
      ),
      weight,
      style: "normal" as const,
    })),
  );
}

async function listHtmlFiles(directory: string): Promise<string[]> {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(
    entries.map(async (entry) => {
      const entryPath = path.join(directory, entry.name);
      if (entry.isDirectory()) return listHtmlFiles(entryPath);
      return entry.isFile() && entry.name.endsWith(".html") ? [entryPath] : [];
    }),
  );
  return nested.flat();
}

function readPayload<Props extends object>(
  html: string,
  metaName: string,
  parsePayload: OgImagesOptions<Props>["parsePayload"],
): ReadPayloadResult<Props> {
  const dom = new JSDOM(html);
  const marker = Array.from(dom.window.document.querySelectorAll("meta[name]")).find(
    (element) => element.getAttribute("name") === metaName,
  );
  if (!marker) {
    dom.window.close();
    return { found: false, html, payload: null };
  }

  const rawPayload = marker.getAttribute("content") ?? "{}";
  marker.remove();
  try {
    return {
      found: true,
      html: dom.serialize(),
      payload: parsePayload(parseJson(rawPayload)),
    };
  } finally {
    dom.window.close();
  }
}

async function mapLimit<T>(
  items: readonly T[],
  limit: number,
  callback: (item: T) => Promise<void>,
): Promise<void> {
  let index = 0;
  await Promise.all(
    Array.from({ length: Math.min(limit, items.length) }, async () => {
      while (index < items.length) {
        const item = items[index];
        index += 1;
        await callback(item);
      }
    }),
  );
}

export function ogImages<Props extends object>(options: OgImagesOptions<Props>): AstroIntegration {
  const integrationName = options.name ?? "chartcoach:og-images";
  return {
    name: integrationName,
    hooks: {
      "astro:build:done": async ({ dir, logger }) => {
        const distDirectory = fileURLToPath(dir);
        const ogLogger = logger.fork(integrationName);
        const jobs: OgImageJob<Props>[] = [];

        for (const htmlPath of await listHtmlFiles(distDirectory)) {
          const html = await fs.readFile(htmlPath, "utf8");
          const result = readPayload(html, options.metaName, options.parsePayload);
          if (!result.found) continue;

          await fs.writeFile(htmlPath, result.html, "utf8");
          if (!result.payload) {
            ogLogger.warn(`Invalid OG payload in ${path.relative(distDirectory, htmlPath)}`);
            continue;
          }
          jobs.push(result.payload, ...(result.payload.extraImages ?? []));
        }

        const fonts = jobs.length > 0 ? loadFonts() : [];
        await mapLimit(jobs, 8, async (job) => {
          const svg = await satori(createElement(options.component, job.props), {
            width: options.width,
            height: options.height,
            fonts,
          });
          const image = await renderAsync(svg, {
            fitTo: { mode: "width", value: options.width },
          });
          const outputPath = path.join(distDirectory, job.imagePathname.replace(/^\/+/, ""));
          await fs.mkdir(path.dirname(outputPath), { recursive: true });
          await fs.writeFile(outputPath, image.asPng());
        });

        ogLogger.info(`Generated ${jobs.length.toLocaleString()} static OG image(s).`);
      },
    },
  };
}
