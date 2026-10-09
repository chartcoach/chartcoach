import { appendFileSync } from "node:fs";

const filterInput = process.env.FILTERS;

if (!filterInput) throw new Error("Missing path filters");

// SAFETY: paths-filter emits string outputs. Required boolean strings are checked below.
const filters = JSON.parse(filterInput) as Record<string, string>;

const full = process.env.GITHUB_EVENT_NAME === "push";

if (!full) {
  for (const name of ["quality", "anti_slop", "python", "npm", "catalog", "site", "docs", "chat"]) {
    if (filters[name] !== "true" && filters[name] !== "false") {
      throw new Error(`Missing or invalid path filter: ${name}`);
    }
  }
}

const selected = (name: string) => full || filters[name] === "true";

const npm = selected("npm");

const packages: string[] = [];

// Consumer jobs install the same SDK and chat tarballs from this build.
if (selected("catalog") || npm) packages.push("@chartcoach/catalog");

if (selected("site")) packages.push("@chartcoach/site");

if (selected("docs")) packages.push("@chartcoach/docs");

if (selected("chat") || npm) packages.push("chartcoach");

if (npm) packages.push("@chartcoach/release");

const outputs = {
  quality: selected("quality"),
  anti_slop: selected("anti_slop"),
  python: selected("python"),
  npm,
  javascript: packages.length > 0,
  packages: JSON.stringify(packages),
};

const output = process.env.GITHUB_OUTPUT;

if (!output) throw new Error("Missing GitHub output path");

for (const [name, value] of Object.entries(outputs)) {
  appendFileSync(output, `${name}=${value}\n`);
}
