import { BibDocument, Document, init, Library, ParseError, Style } from "refkit-js";
import { CatalogError } from "./errors";
import { canonicalJson, compareUnicode } from "./identity";
import { isJsonString, type JsonObject } from "./json";
import type { Catalog } from "./model";

await init();

const citationStyle = Style.load("apa");

const DEFAULT_GUIDELINE_URL_TEMPLATE = "https://chartcoach.dev/guidelines/{id}";

export type MinimalSourceRecord = Readonly<{
  reference_id: string;
  authors_text: string | null;
  year: string | null;
  source_title: string | null;
  doi: string | null;
  url: string | null;
}>;

export type FullSourceRecord = Readonly<{
  guideline_id: string;
  reference_id: string;
  source_type: string | null;
  authors: readonly string[];
  authors_text: string | null;
  year: string | null;
  source_title: string | null;
  journal: string | null;
  booktitle: string | null;
  publisher: string | null;
  url: string | null;
  doi: string | null;
}>;

export type CitationSource = Readonly<{
  reference_id: string;
  source_type: string | null;
  authors_text: string | null;
  year: string | null;
  source_title: string | null;
  journal: string | null;
  booktitle: string | null;
  publisher: string | null;
  doi: string | null;
  url: string | null;
  citation: string;
}>;

export type CiteOptions = Readonly<{
  ids: readonly string[];
  urlTemplate?: string;
}>;

export type CitationRecord = Readonly<{
  id: string;
  title: string;
  url: string;
  guideline_citation: string;
  sources: readonly CitationSource[];
}>;

type ParsedReference = Readonly<{
  id: string;
  bibtex: string;
  sourceType: string;
  authors: readonly string[];
  authorsText: string | null;
  year: string | null;
  title: string | null;
  journal: string | null;
  booktitle: string | null;
  publisher: string | null;
  url: string | null;
  doi: string | null;
  fingerprint: string;
  citation: string;
}>;

type ReferenceIndex = Readonly<{
  byId: ReadonlyMap<string, ParsedReference>;
  idsByGuideline: ReadonlyMap<string, readonly string[]>;
}>;

const indexes = new WeakMap<Catalog, ReferenceIndex>();

export function sourceRecords(
  catalog: Catalog,
  guidelineId: string,
  detail: "minimal" | "full",
): readonly (MinimalSourceRecord | FullSourceRecord)[] {
  const index = referenceIndex(catalog);
  const ids = index.idsByGuideline.get(guidelineId) ?? [];

  return Object.freeze(
    ids.map((id) => {
      const reference = index.byId.get(id)!;

      return detail === "minimal" ? minimalSource(reference) : fullSource(guidelineId, reference);
    }),
  );
}

export function citationRecords(catalog: Catalog, options: CiteOptions): readonly CitationRecord[] {
  if (Object.prototype.toString.call(options) !== "[object Object]") {
    throw new CatalogError("Citation options must be an object.");
  }

  if (!Array.isArray(options.ids) || !options.ids.every(isJsonString)) {
    throw new CatalogError("ids must be an array of strings.");
  }

  const urlTemplate = options.urlTemplate ?? DEFAULT_GUIDELINE_URL_TEMPLATE;

  if (!isJsonString(urlTemplate) || !urlTemplate.includes("{id}")) {
    throw new CatalogError("Guideline URL template must include `{id}`.", {
      hints: [`Use a template such as \`${DEFAULT_GUIDELINE_URL_TEMPLATE}\`.`],
    });
  }

  if (options.ids.length === 0) return Object.freeze([]);

  const index = referenceIndex(catalog);

  return Object.freeze(
    options.ids.map((id) => {
      const guideline = catalog.require(id);
      const url = urlTemplate.replace("{id}", id);

      const sources = Object.freeze(
        (index.idsByGuideline.get(id) ?? []).map((referenceId) =>
          citationSource(index.byId.get(referenceId)!),
        ),
      );

      return Object.freeze({
        id,
        title: guideline.title,
        url,
        guideline_citation: `[${guideline.title}](${url}) (\`${id}\`)`,
        sources,
      });
    }),
  );
}

export function referenceIndex(catalog: Catalog): ReferenceIndex {
  const cached = indexes.get(catalog);

  if (cached) return cached;

  const byId = new Map<string, ParsedReference>();
  const parsed = new Map<string, ParsedReference>();
  const idsByGuideline = new Map<string, readonly string[]>();

  for (const guideline of catalog.guidelines) {
    const ids = new Set<string>();

    for (const bibtex of guideline.references) {
      let reference = parsed.get(bibtex);

      if (!reference) {
        reference = parseReference(bibtex);
        parsed.set(bibtex, reference);
      }

      const previous = byId.get(reference.id);

      if (previous && previous.fingerprint !== reference.fingerprint) {
        throw new CatalogError(
          `Conflicting BibTeX definitions for reference id: ${reference.id}.`,
          {
            details: { reference_id: reference.id },
          },
        );
      }

      byId.set(
        reference.id,
        previous && compareUnicode(previous.bibtex, reference.bibtex) <= 0 ? previous : reference,
      );
      ids.add(reference.id);
    }

    idsByGuideline.set(guideline.id, Object.freeze([...ids].sort(compareUnicode)));
  }

  const created = Object.freeze({ byId, idsByGuideline });
  indexes.set(catalog, created);

  return created;
}

function parseReference(bibtex: string): ParsedReference {
  try {
    return parsedReference(bibtex);
  } catch (error) {
    if (error instanceof CatalogError) throw error;

    const details: JsonObject = {
      exception_type: error instanceof Error ? error.name : "Error",
    };

    if (error instanceof ParseError) {
      details.diagnostics = error.diagnostics.map((diagnostic) => ({ ...diagnostic }));
    }

    throw new CatalogError("BibTeX reference could not be parsed.", {
      details,
    });
  }
}

function parsedReference(bibtex: string): ParsedReference {
  const document = BibDocument.parse(bibtex);
  const entries = document.resolve();

  if (entries.length !== 1) {
    throw new CatalogError(`Expected one BibTeX entry, found ${entries.length}.`);
  }

  const entry = entries[0]!;
  const properties = entry.fields;
  const authorsText = textOrNull(properties.author);

  const authors = Object.freeze(
    authorsText === null
      ? []
      : authorsText
          .split(" and ")
          .map((author) => author.trim())
          .filter(Boolean),
  );

  return Object.freeze({
    id: entry.key,
    bibtex,
    sourceType: entry.entryType,
    authors,
    authorsText,
    year: textOrNull(properties.year),
    title: textOrNull(properties.title),
    journal: textOrNull(properties.journal),
    booktitle: textOrNull(properties.booktitle),
    publisher: textOrNull(properties.publisher),
    url: referenceUrl(properties),
    doi: textOrNull(properties.doi),
    citation: new Document(
      Library.parseBibtex(document.tidy().bibtex, { recovery: "report" }),
      citationStyle,
      {
        locale: "en-US",
      },
    ).fullBibliography().text,
    fingerprint: canonicalJson({
      type: entry.entryType,
      label: entry.key,
      properties: { ...properties },
    }),
  });
}

function minimalSource(reference: ParsedReference): MinimalSourceRecord {
  return Object.freeze({
    reference_id: reference.id,
    authors_text: reference.authorsText,
    year: reference.year,
    source_title: reference.title,
    doi: reference.doi,
    url: reference.url,
  });
}

function fullSource(guidelineId: string, reference: ParsedReference): FullSourceRecord {
  return Object.freeze({
    guideline_id: guidelineId,
    reference_id: reference.id,
    source_type: reference.sourceType,
    authors: reference.authors,
    authors_text: reference.authorsText,
    year: reference.year,
    source_title: reference.title,
    journal: reference.journal,
    booktitle: reference.booktitle,
    publisher: reference.publisher,
    url: reference.url,
    doi: reference.doi,
  });
}

function citationSource(reference: ParsedReference): CitationSource {
  const source = {
    reference_id: reference.id,
    source_type: reference.sourceType,
    authors_text: reference.authorsText,
    year: reference.year,
    source_title: reference.title,
    journal: reference.journal,
    booktitle: reference.booktitle,
    publisher: reference.publisher,
    doi: reference.doi,
    url: reference.url,
  };

  const locators = [source.doi ? doiUrl(source.doi) : null, source.url].filter(
    (value): value is string => value !== null && !reference.citation.includes(value),
  );

  return Object.freeze({
    ...source,
    citation: [reference.citation, ...new Set(locators)].join(" "),
  });
}

function textOrNull(value: string | undefined): string | null {
  if (value === undefined) return null;
  const text = value.trim();

  return text || null;
}

function referenceUrl(properties: Readonly<Record<string, string>>): string | null {
  const explicit = textOrNull(properties.url);
  const value = explicit ?? textOrNull(properties.howpublished);

  if (value === null) return null;
  const wrapped = /^\\url\{([^{}]*)\}$/.exec(value);
  const candidate = wrapped?.[1] ?? value;

  return /^https?:\/\/[^\s{}\\/?#]+[^\s{}\\]*$/i.test(candidate) ? candidate : explicit;
}

function doiUrl(value: string): string {
  return `https://doi.org/${value.replace(/^https?:\/\/doi\.org\//, "")}`;
}
