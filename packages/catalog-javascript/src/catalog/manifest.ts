import { CatalogError } from "./errors";
import { parseLabel } from "./labels";
import type { Guideline } from "./model";

export const REQUIRED_MANIFEST_HEADINGS = ["Section Roles", "Label Families"] as const;

export type ManifestDefinition = {
  name: string;
  description: string;
  examples: string[];
};

export type CatalogManifest = {
  markdown: string;
  sectionRoles: Record<string, ManifestDefinition>;
  labelFamilies: Record<string, ManifestDefinition>;
};

const headingPattern = /^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$/;
const codeSpanPattern = /`([^`\n]+)`/g;

export function parseCatalogManifest(markdown: string): CatalogManifest {
  const requiredSeen = new Set<string>();
  const definitions: {
    "Section Roles": Record<string, ManifestDefinition>;
    "Label Families": Record<string, ManifestDefinition>;
  } = {
    "Section Roles": {},
    "Label Families": {},
  };
  let currentHeading: keyof typeof definitions | string | undefined;
  let currentName: string | undefined;
  let currentLines: string[] = [];

  function flushDefinition() {
    if (
      currentHeading !== "Section Roles" &&
      currentHeading !== "Label Families"
    ) {
      currentLines = [];
      return;
    }
    if (currentName === undefined) {
      currentLines = [];
      return;
    }

    const description = currentLines.join("\n").trim();
    if (!description) {
      throw new CatalogError(
        `Manifest definition ${currentHeading}/${currentName} must include prose.`,
      );
    }
    definitions[currentHeading][currentName] = {
      name: currentName,
      description,
      examples: Array.from(description.matchAll(codeSpanPattern), (match) => match[1] ?? ""),
    };
    currentName = undefined;
    currentLines = [];
  }

  for (const line of markdown.split("\n")) {
    const match = headingPattern.exec(line);
    if (!match) {
      if (currentName !== undefined) currentLines.push(line);
      continue;
    }

    const level = match[1]!.length;
    const title = match[2]!.trim();

    if (level === 2) {
      flushDefinition();
      currentHeading = title;
      currentName = undefined;
      currentLines = [];
      if (title === "Section Roles" || title === "Label Families") {
        requiredSeen.add(title);
      }
      continue;
    }

    if (
      level === 3 &&
      (currentHeading === "Section Roles" || currentHeading === "Label Families")
    ) {
      flushDefinition();
      if (!title) {
        throw new CatalogError(
          `Manifest heading ${currentHeading} contains an empty subheading.`,
        );
      }
      currentName = title;
      currentLines = [];
      continue;
    }

    if (currentName !== undefined) currentLines.push(line);
  }

  flushDefinition();

  const missing = REQUIRED_MANIFEST_HEADINGS.filter((heading) => !requiredSeen.has(heading));
  if (missing.length > 0) {
    throw new CatalogError(`MANIFEST.md is missing required heading(s): ${missing.join(", ")}.`);
  }
  for (const heading of REQUIRED_MANIFEST_HEADINGS) {
    if (Object.keys(definitions[heading]).length === 0) {
      throw new CatalogError(`Manifest heading ${heading} must define entries.`);
    }
  }
  validateLabelFamilyExamples(Object.values(definitions["Label Families"]));

  return {
    markdown: markdown.endsWith("\n") ? markdown : `${markdown}\n`,
    sectionRoles: definitions["Section Roles"],
    labelFamilies: definitions["Label Families"],
  };
}

export function validateManifestCoverage(guidelines: readonly Guideline[], manifest: CatalogManifest) {
  const usedRoles = new Set<string>();
  const usedFamilies = new Set<string>();

  for (const guideline of guidelines) {
    for (const section of guideline.sections) {
      const role = section.role.trim();
      if (!role) {
        throw new CatalogError("Section role values must not be empty.");
      }
      usedRoles.add(role);
    }
    for (const label of guideline.labels) {
      usedFamilies.add(parseLabel(label, `label ${JSON.stringify(label)}`).family);
    }
  }

  const missingRoles = Array.from(usedRoles)
    .filter((role) => manifest.sectionRoles[role] === undefined)
    .sort();
  const missingFamilies = Array.from(usedFamilies)
    .filter((family) => manifest.labelFamilies[family] === undefined)
    .sort();

  const errors: string[] = [];
  if (missingRoles.length > 0) {
    errors.push(`undefined section role(s): ${missingRoles.join(", ")}`);
  }
  if (missingFamilies.length > 0) {
    errors.push(`undefined label family/families: ${missingFamilies.join(", ")}`);
  }
  if (errors.length > 0) {
    throw new CatalogError(`Catalog manifest validation failed: ${errors.join("; ")}.`);
  }
}

function validateLabelFamilyExamples(definitions: ManifestDefinition[]) {
  for (const definition of definitions) {
    const familyExamples: string[] = [];
    const invalidExamples: string[] = [];
    for (const example of definition.examples) {
      let parsed;
      try {
        parsed = parseLabel(example, `manifest label example ${JSON.stringify(example)}`);
      } catch {
        continue;
      }
      if (parsed.family === definition.name) {
        familyExamples.push(parsed.value);
      } else if (example.includes(":")) {
        invalidExamples.push(example);
      }
    }
    if (invalidExamples.length > 0) {
      throw new CatalogError(
        `Label family ${definition.name} has example(s) from another family: ${invalidExamples.join(", ")}.`,
      );
    }
    if (familyExamples.length === 0) {
      throw new CatalogError(
        `Label family ${definition.name} must include at least one label example.`,
      );
    }
  }
}
