import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { describe, expect, it } from "vitest";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

describe("apps/site custom.css aggregation", () => {
  it("loads the decomposed starlight styles in a stable pass-1 order", async () => {
    const customCss = await readFile(path.join(__dirname, "../src/styles/custom.css"), "utf8");

    expect(customCss).toContain('@import "./starlight/foundations.css";');
    expect(customCss).toContain('@import "./starlight/header-shell.css";');
    expect(customCss).toContain('@import "./starlight/route-shell.css";');
    expect(customCss).toContain('@import "./starlight/content.css";');
    expect(customCss).toContain('@import "./starlight/responsive.css";');

    const importSequence = [
      "./starlight/foundations.css",
      "./starlight/header-shell.css",
      "./starlight/route-shell.css",
      "./starlight/content.css",
      "./starlight/responsive.css",
    ];

    const importIndexes = importSequence.map((importPath) => customCss.indexOf(importPath));
    expect(importIndexes.every((index) => index >= 0)).toBe(true);
    expect(importIndexes).toEqual([...importIndexes].sort((a, b) => a - b));
  });
});
