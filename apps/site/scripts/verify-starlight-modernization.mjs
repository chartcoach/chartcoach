#!/usr/bin/env node

import { readdir, readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import process from "node:process";

const distDir = fileURLToPath(new URL("../dist/", import.meta.url));
const leakTokens = ["agentation", "cc-agentation-root", "cc-agentation-toolbar"];
const textExtensions = new Set([".html", ".js", ".mjs", ".json", ".txt", ".xml"]);
const failures = [];

function pass(message) {
  console.log(`PASS ${message}`);
}

function fail(message) {
  console.error(`FAIL ${message}`);
  failures.push(message);
}

async function readDistFile(relativePath) {
  const filePath = path.join(distDir, relativePath);

  try {
    return await readFile(filePath, "utf8");
  } catch (error) {
    fail(`${relativePath} is missing (${error.message})`);
    return null;
  }
}

function expectIncludes(html, route, label, needle) {
  if (html.includes(needle)) {
    pass(`${route} includes ${label}`);
    return;
  }

  fail(`${route} is missing ${label}`);
}

function expectExcludes(html, route, label, needle) {
  if (!html.includes(needle)) {
    pass(`${route} excludes ${label}`);
    return;
  }

  fail(`${route} unexpectedly includes ${label}`);
}

async function* walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const entryPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      yield* walk(entryPath);
      continue;
    }

    yield entryPath;
  }
}

async function verifyRoute(route) {
  const html = await readDistFile(route.file);
  if (!html) return;

  for (const [label, needle] of route.includes) {
    expectIncludes(html, route.label, label, needle);
  }

  for (const [label, needle] of route.excludes) {
    expectExcludes(html, route.label, label, needle);
  }
}

async function verifyAgentationLeakage() {
  const offendingFiles = [];

  for await (const filePath of walk(distDir)) {
    const ext = path.extname(filePath);
    if (!textExtensions.has(ext)) continue;

    const contents = await readFile(filePath, "utf8");
    const lowered = contents.toLowerCase();
    const matchedTokens = leakTokens.filter((token) => lowered.includes(token));

    if (matchedTokens.length > 0) {
      offendingFiles.push(`${path.relative(distDir, filePath)} (${matchedTokens.join(", ")})`);
    }
  }

  if (offendingFiles.length === 0) {
    pass("default dist omits Agentation HTML/JS/text leakage");
    return;
  }

  fail(`default dist leaked Agentation markers outside CSS: ${offendingFiles.join(", ")}`);
}

const sharedShellChecks = [
  ["site search shell", "site-search"],
  ["theme picker", "starlight-theme-select"],
  ["GitHub/social affordance", "http://github.com/peter-gy/chartcoach"],
];

const routes = [
  {
    label: "/",
    file: "index.html",
    includes: [
      ...sharedShellChecks,
      ["home title", "<title>Chart Coach | Chart Coach</title>"],
      ["default social image", "/social/chartcoach-share-default.png"],
    ],
    excludes: [["sidebar shell", "data-has-sidebar"]],
  },
  {
    label: "/catalog/",
    file: "catalog/index.html",
    includes: [
      ...sharedShellChecks,
      ["catalog title", "<title>Catalog structure | Chart Coach</title>"],
      ["default social image", "/social/chartcoach-share-default.png"],
      ["sidebar shell", "data-has-sidebar"],
    ],
    excludes: [],
  },
  {
    label: "/labels/",
    file: "labels/index.html",
    includes: [
      ...sharedShellChecks,
      ["labels title", "<title>Labels & filters | Chart Coach</title>"],
      ["default social image", "/social/chartcoach-share-default.png"],
      ["sidebar shell", "data-has-sidebar"],
    ],
    excludes: [],
  },
  {
    label: "/about/",
    file: "about/index.html",
    includes: [
      ...sharedShellChecks,
      ["about title", "<title>About | Chart Coach</title>"],
      ["default social image", "/social/chartcoach-share-default.png"],
      ["sidebar shell", "data-has-sidebar"],
    ],
    excludes: [],
  },
  {
    label: "/guidelines/",
    file: "guidelines/index.html",
    includes: [
      ...sharedShellChecks,
      ["guidelines title", "<title>Guidelines | Chart Coach</title>"],
      ["guidelines social image", "/social/chartcoach-share-guidelines.png"],
    ],
    excludes: [["sidebar shell", "data-has-sidebar"]],
  },
  {
    label: "/guidelines/adapt-framing-and-format-to-the-publication-outlet/",
    file: "guidelines/adapt-framing-and-format-to-the-publication-outlet/index.html",
    includes: [
      ...sharedShellChecks,
      [
        "guideline detail title",
        "<title>Adapt framing and format to the publication outlet | Chart Coach</title>",
      ],
      ["guidelines social image", "/social/chartcoach-share-guidelines.png"],
    ],
    excludes: [["sidebar shell", "data-has-sidebar"]],
  },
];

await Promise.all(routes.map(verifyRoute));

const sitemapIndex = await readDistFile("sitemap-index.xml");
if (sitemapIndex) {
  expectIncludes(
    sitemapIndex,
    "sitemap-index.xml",
    "generated sitemap shard reference",
    "/sitemap-0.xml",
  );
}

const sitemapShard = await readDistFile("sitemap-0.xml");
if (sitemapShard) {
  expectIncludes(sitemapShard, "sitemap-0.xml", "guidelines index entry", "/guidelines/");
}

await verifyAgentationLeakage();

if (failures.length > 0) {
  console.error(`\nVerification failed with ${failures.length} issue(s).`);
  process.exit(1);
}

console.log(`\nVerified ${routes.length} routes plus sitemap and Agentation leakage checks.`);
