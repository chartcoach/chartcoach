import { appendFileSync } from "node:fs";

const filters = JSON.parse(process.env.FILTERS);

const full = process.env.GITHUB_EVENT_NAME === "push";

if (!full) {
  for (const name of ["quality", "anti_slop", "python", "npm", "catalog", "site", "docs", "chat"]) {
    if (!["true", "false"].includes(filters[name])) {
      throw new Error(`Missing or invalid path filter: ${name}`);
    }
  }
}

const selected = (name) => full || filters[name] === "true";

const npm = selected("npm");

const packages = [];

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

for (const [name, value] of Object.entries(outputs)) {
  appendFileSync(process.env.GITHUB_OUTPUT, `${name}=${value}\n`);
}
