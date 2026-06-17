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
  bibliography?: string;
  description: string;
  labels: readonly string[];
  body: string;
  sections: readonly GuidelineSection[];
  references: readonly string[];
};

export type CatalogOptions = {
  manifest?: CatalogManifest;
};

export class Catalog implements Iterable<Guideline> {
  readonly guidelines: readonly Guideline[];
  readonly manifest?: CatalogManifest;
  private readonly byId: Map<string, Guideline>;

  constructor(guidelines: Iterable<Guideline> = [], options: CatalogOptions = {}) {
    const records = Array.from(guidelines, copyGuideline);
    const byId = new Map<string, Guideline>();
    for (const guideline of records) {
      if (byId.has(guideline.id)) {
        throw new CatalogError(`Catalog contains duplicate guideline id: ${guideline.id}.`);
      }
      byId.set(guideline.id, guideline);
    }
    if (options.manifest) {
      validateManifestCoverage(records, options.manifest);
    }

    this.guidelines = records;
    this.manifest = options.manifest;
    this.byId = byId;
  }

  get length(): number {
    return this.guidelines.length;
  }

  get size(): number {
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
        guideline.sections.map((section) => section.role),
      ),
    );
  }

  [Symbol.iterator](): Iterator<Guideline> {
    return this.guidelines[Symbol.iterator]();
  }
}

function copyGuideline(guideline: Guideline): Guideline {
  return {
    id: guideline.id,
    title: guideline.title,
    bibliography: guideline.bibliography,
    description: guideline.description,
    labels: [...guideline.labels],
    body: guideline.body,
    sections: guideline.sections.map((section) => ({
      role: section.role,
      title: section.title,
      content: section.content,
    })),
    references: [...guideline.references],
  };
}

function sortedUnique(values: Iterable<string>): string[] {
  return Array.from(new Set(values)).sort();
}
