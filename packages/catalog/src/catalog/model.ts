import { CatalogError } from "./errors";
import { isJsonObject, isJsonString, type JsonValue } from "./json";
import { normalizeLabel } from "./labels";
import type { CatalogManifest } from "./manifest";
import { copyCatalogManifest, validateManifestCoverage } from "./manifest";
import {
  describeCatalog,
  type CatalogInfo,
  type DescribeOptions,
  type DescriptionContext,
  type ProfileLoader,
} from "./description";
import { queryCatalog, type QueryOptions, type EntryCandidate } from "./query";
import { readCatalog, type ReadOptions, type GuidelineEntryRecord } from "./read";
import { citationRecords, type CitationRecord, type CiteOptions } from "./references";
import { releaseProfiles } from "./profile-layout";
import type { CatalogRelease } from "./artifacts";
import { copyCatalogRelease } from "./artifacts";

export type GuidelineSection = Readonly<{
  role: string;
  title: string;
  content: string;
}>;

export type Guideline = Readonly<{
  id: string;
  title: string;
  description: string;
  labels: readonly string[];
  body: string;
  sections: readonly GuidelineSection[];
  references: readonly string[];
}>;

export type GuidelineInput = Omit<Guideline, "body">;

export type CatalogReleaseContext = Readonly<{
  release: CatalogRelease;
  releaseUrl: string;
  profileLoader?: ProfileLoader;
}>;

const releaseByCatalog = new WeakMap<Catalog, CatalogReleaseContext>();
const descriptionByCatalog = new WeakMap<Catalog, DescriptionContext>();

export class Catalog implements Iterable<Guideline> {
  readonly guidelines: readonly Guideline[];
  readonly manifest: CatalogManifest;
  private readonly byId: Map<string, Guideline>;

  constructor(guidelines: Iterable<GuidelineInput>, manifest: CatalogManifest);
  constructor(guidelines: Iterable<JsonValue>, manifest: CatalogManifest) {
    const records = Array.from(guidelines, copyGuideline);
    const ownedManifest = copyCatalogManifest(manifest);
    const byId = new Map<string, Guideline>();
    for (const guideline of records) {
      if (byId.has(guideline.id)) {
        throw new CatalogError(`Catalog contains duplicate guideline entry ID: ${guideline.id}.`);
      }
      byId.set(guideline.id, guideline);
    }
    validateManifestCoverage(records, ownedManifest);

    this.guidelines = Object.freeze(records);
    this.manifest = ownedManifest;
    this.byId = byId;
    Object.freeze(this);
  }

  get release(): CatalogRelease | undefined {
    return releaseByCatalog.get(this)?.release;
  }

  get releaseUrl(): string | undefined {
    return releaseByCatalog.get(this)?.releaseUrl;
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
      throw new CatalogError(`Unknown guideline entry ID: ${id}`, {
        code: "lookup",
        details: { id },
        hints: ["Call `catalog.query()` to inspect guideline entry IDs."],
      });
    }
    return guideline;
  }

  query(options: QueryOptions = {}): readonly EntryCandidate[] {
    return queryCatalog(this, options);
  }

  read(options: ReadOptions): readonly GuidelineEntryRecord[] {
    return readCatalog(this, options);
  }

  cite(options: CiteOptions): readonly CitationRecord[] {
    return citationRecords(this, options);
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

  describe(options: DescribeOptions = {}): Promise<CatalogInfo> {
    return describeCatalog(
      this,
      descriptionByCatalog.get(this) ?? emptyDescriptionContext(),
      options,
    );
  }

  [Symbol.iterator](): IterableIterator<Guideline> {
    return this.guidelines[Symbol.iterator]();
  }
}

export function catalogWithRelease(catalog: Catalog, context: CatalogReleaseContext): Catalog {
  const release = copyCatalogRelease(context.release);
  const profiles = releaseProfiles(release);
  releaseByCatalog.set(
    catalog,
    Object.freeze({
      release,
      releaseUrl: context.releaseUrl,
    }),
  );
  descriptionByCatalog.set(
    catalog,
    Object.freeze({
      resolvedLocation: context.releaseUrl,
      releaseDigest: release.digest,
      profiles,
      profileLoader: context.profileLoader,
      profileCache: new Map(),
    }),
  );
  return catalog;
}

function emptyDescriptionContext(): DescriptionContext {
  return Object.freeze({
    resolvedLocation: null,
    releaseDigest: null,
    profiles: Object.freeze([]),
    profileCache: new Map(),
  });
}

export function isGuidelineInput(value: JsonValue): value is GuidelineInput {
  if (!isJsonObject(value)) return false;
  const { description, id, labels, references, sections, title } = value;
  if (!isJsonString(id) || id.length === 0) return false;
  if (!isJsonString(title) || !isJsonString(description)) return false;
  if (!isStringArray(labels) || !isStringArray(references)) return false;
  if (!Array.isArray(sections) || sections.length === 0 || !sections.every(isGuidelineSection)) {
    return false;
  }
  const dangling = sections.flatMap((section, index) =>
    section.role === "__dangling__" ? [index] : [],
  );
  if (dangling.length > 0 && (dangling.length !== 1 || dangling[0] !== 0)) return false;
  try {
    return labels.every((label) => normalizeLabel(label) === label);
  } catch {
    return false;
  }
}

function copyGuideline(value: JsonValue): Guideline {
  if (!isGuidelineInput(value)) {
    throw new CatalogError("Invalid guideline record.");
  }
  const sections = Object.freeze(
    value.sections.map((section) =>
      Object.freeze({
        role: section.role,
        title: section.title,
        content: section.content,
      }),
    ),
  );
  return Object.freeze({
    id: value.id,
    title: value.title,
    description: value.description,
    labels: Object.freeze([...value.labels]),
    body: bodyFromSections(sections),
    sections,
    references: Object.freeze([...value.references]),
  });
}

function isGuidelineSection(value: JsonValue): value is GuidelineSection {
  if (!isJsonObject(value)) return false;
  const { content, role, title } = value;
  return (
    isJsonString(role) &&
    role.length > 0 &&
    role === role.trim() &&
    isJsonString(title) &&
    title === title.trim() &&
    isJsonString(content) &&
    content === content.trim() &&
    (role === "__dangling__" ? title.length === 0 && content.length > 0 : title.length > 0)
  );
}

function isStringArray(value: JsonValue | undefined): value is string[] {
  return Array.isArray(value) && value.every(isJsonString);
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
