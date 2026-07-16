import { CatalogError } from "./errors";
import type { CatalogManifest } from "./manifest";
import { validateManifestCoverage } from "./manifest";

export type GuidelineSection = {
  role: string;
  title: string;
  content: string;
};

export type Guideline = {
  id: string;
  title: string;
  description: string;
  labels: readonly string[];
  body: string;
  sections: readonly GuidelineSection[];
  references: readonly string[];
};

export class Catalog implements Iterable<Guideline> {
  readonly guidelines: readonly Guideline[];
  readonly manifest: CatalogManifest;
  private readonly byId: Map<string, Guideline>;

  constructor(guidelines: Iterable<Omit<Guideline, "body">>, manifest: CatalogManifest) {
    const records = Array.from(guidelines, copyGuideline);
    const byId = new Map<string, Guideline>();
    for (const guideline of records) {
      if (byId.has(guideline.id)) {
        throw new CatalogError(`Catalog contains duplicate guideline id: ${guideline.id}.`);
      }
      byId.set(guideline.id, guideline);
    }
    validateManifestCoverage(records, manifest);

    this.guidelines = records;
    this.manifest = manifest;
    this.byId = byId;
  }

  get length(): number {
    return this.guidelines.length;
  }

  get(id: string): Guideline | undefined {
    return this.byId.get(id);
  }

  require(id: string): Guideline {
    const guideline = this.get(id);
    if (!guideline) {
      throw new CatalogError(`Unknown guideline id: ${id}.`);
    }
    return guideline;
  }

  labels(): string[] {
    return sortedUnique(this.guidelines.flatMap((guideline) => [...guideline.labels]));
  }

  sectionRoles(): string[] {
    return sortedUnique(
      this.guidelines.flatMap((guideline) =>
        guideline.sections.map((section) => section.role).filter((role) => role !== "__dangling__"),
      ),
    );
  }

  [Symbol.iterator](): Iterator<Guideline> {
    return this.guidelines[Symbol.iterator]();
  }
}

function copyGuideline(guideline: Omit<Guideline, "body">): Guideline {
  const sections = guideline.sections.map((section) => ({
    role: section.role,
    title: section.title,
    content: section.content,
  }));
  return {
    id: guideline.id,
    title: guideline.title,
    description: guideline.description,
    labels: [...guideline.labels],
    body: bodyFromSections(sections),
    sections,
    references: [...guideline.references],
  };
}

function bodyFromSections(sections: readonly GuidelineSection[]): string {
  return sections
    .map((section) => {
      if (section.role === "__dangling__") return section.content;
      return `## ${section.title} <!-- role: ${section.role} -->\n\n${section.content}`;
    })
    .join("\n\n");
}

function sortedUnique(values: Iterable<string>): string[] {
  return Array.from(new Set(values)).sort();
}
