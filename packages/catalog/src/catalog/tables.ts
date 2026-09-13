import { CatalogError } from "./errors";
import { compareUnicode } from "./identity";
import { parseLabel } from "./labels";
import type { Catalog, Guideline, GuidelineSection } from "./model";
import { referenceIndex } from "./references";

type ReferenceRow = Readonly<{
  id: string;
  source_type: string | null;
  authors: readonly string[];
  authors_text: string | null;
  year: string | null;
  title: string | null;
  journal: string | null;
  booktitle: string | null;
  publisher: string | null;
  url: string | null;
  doi: string | null;
  bibtex: string;
}>;

type GuidelineReferenceRow = Readonly<{
  guideline_id: string;
  reference_id: string;
}>;

export type CatalogTables = Readonly<{
  guidelines: readonly Omit<Guideline, "references">[];
  sections: readonly Readonly<GuidelineSection & { guideline_id: string }>[];
  guideline_labels: readonly Readonly<{
    guideline_id: string;
    label: string;
    family: string;
    category: string;
    modifier: string | null;
  }>[];
  references: readonly ReferenceRow[];
  guideline_references: readonly GuidelineReferenceRow[];
  guideline_sources: readonly Readonly<
    Omit<ReferenceRow, "id" | "title"> & GuidelineReferenceRow & { source_title: string | null }
  >[];
}>;

export type TableName = keyof CatalogTables;

export type TableColumnInfo = Readonly<{
  name: string;
  type:
    | "String"
    | "List(String)"
    | "List(Struct({'role': String, 'title': String, 'content': String}))";
}>;

export type TableInfo = Readonly<{
  name: TableName;
  rows: number;
  columns: readonly TableColumnInfo[];
}>;

function columns(
  schema: Readonly<Record<string, TableColumnInfo["type"]>>,
): readonly TableColumnInfo[] {
  return Object.freeze(Object.entries(schema).map(([name, type]) => Object.freeze({ name, type })));
}

export const tableSchemas: Readonly<Record<TableName, readonly TableColumnInfo[]>> = Object.freeze({
  guidelines: columns({
    id: "String",
    title: "String",
    description: "String",
    labels: "List(String)",
    body: "String",
    sections: "List(Struct({'role': String, 'title': String, 'content': String}))",
  }),
  sections: columns({ guideline_id: "String", role: "String", title: "String", content: "String" }),
  guideline_labels: columns({
    guideline_id: "String",
    label: "String",
    family: "String",
    category: "String",
    modifier: "String",
  }),
  references: columns({
    id: "String",
    source_type: "String",
    authors: "List(String)",
    authors_text: "String",
    year: "String",
    title: "String",
    journal: "String",
    booktitle: "String",
    publisher: "String",
    url: "String",
    doi: "String",
    bibtex: "String",
  }),
  guideline_references: columns({ guideline_id: "String", reference_id: "String" }),
  guideline_sources: columns({
    guideline_id: "String",
    reference_id: "String",
    source_type: "String",
    authors: "List(String)",
    authors_text: "String",
    year: "String",
    source_title: "String",
    journal: "String",
    booktitle: "String",
    publisher: "String",
    url: "String",
    doi: "String",
    bibtex: "String",
  }),
});

export const tableNames: readonly TableName[] = Object.freeze<TableName[]>([
  "guidelines",
  "sections",
  "guideline_labels",
  "references",
  "guideline_references",
  "guideline_sources",
]);

const tablesByCatalog = new WeakMap<Catalog, Map<TableName, CatalogTables[TableName]>>();

export function catalogTable<Name extends TableName>(
  catalog: Catalog,
  name: Name,
): CatalogTables[Name] {
  if (!Object.hasOwn(tableSchemas, name)) {
    throw new CatalogError(`Unknown table: ${name}`, {
      code: "lookup",
      details: { table: name, available: tableNames },
      hints: ["Call catalog.describe() to inspect catalog tables."],
    });
  }

  let tables = tablesByCatalog.get(catalog);

  if (!tables) {
    tables = new Map();
    tablesByCatalog.set(catalog, tables);
  }

  let rows = tables.get(name);

  if (!rows) {
    rows = tableBuilders[name](catalog);
    Object.freeze(rows);
    tables.set(name, rows);
  }

  // SAFETY: Each cached value comes from the builder indexed by the same validated table name.
  return rows as CatalogTables[Name];
}

export function catalogTableInfo(catalog: Catalog): readonly TableInfo[] {
  return Object.freeze(
    tableNames.map((name) =>
      Object.freeze({
        name,
        rows: catalog.table(name).length,
        columns: tableSchemas[name],
      }),
    ),
  );
}

const tableBuilders: { [Name in TableName]: (catalog: Catalog) => CatalogTables[Name] } = {
  guidelines: (catalog) =>
    catalog.guidelines.map(({ id, title, description, labels, body, sections }) =>
      Object.freeze({ id, title, description, labels, body, sections }),
    ),
  sections: (catalog) =>
    catalog.guidelines.flatMap((guideline) =>
      guideline.sections.map((section) =>
        Object.freeze({ guideline_id: guideline.id, ...section }),
      ),
    ),
  guideline_labels: (catalog) =>
    catalog.guidelines
      .flatMap((guideline) =>
        [...new Set(guideline.labels)].map((label) => {
          const parsed = parseLabel(label);

          return Object.freeze({
            guideline_id: guideline.id,
            label,
            family: parsed.family,
            category: parsed.category,
            modifier: parsed.modifier ?? null,
          });
        }),
      )
      .sort(
        (left, right) =>
          compareUnicode(left.guideline_id, right.guideline_id) ||
          compareUnicode(left.label, right.label),
      ),
  references: (catalog) =>
    [...referenceIndex(catalog).byId.values()]
      .sort((left, right) => compareUnicode(left.id, right.id))
      .map((reference) =>
        Object.freeze({
          id: reference.id,
          source_type: reference.sourceType,
          authors: reference.authors,
          authors_text: reference.authorsText,
          year: reference.year,
          title: reference.title,
          journal: reference.journal,
          booktitle: reference.booktitle,
          publisher: reference.publisher,
          url: reference.url,
          doi: reference.doi,
          bibtex: reference.bibtex,
        }),
      ),
  guideline_references: (catalog) =>
    [...referenceIndex(catalog).idsByGuideline]
      .sort(([left], [right]) => compareUnicode(left, right))
      .flatMap(([guideline_id, ids]) =>
        ids.map((reference_id) => Object.freeze({ guideline_id, reference_id })),
      ),
  guideline_sources: (catalog) => {
    const references = new Map(
      catalog.table("references").map((reference) => [reference.id, reference]),
    );

    return catalog.table("guideline_references").map(({ guideline_id, reference_id }) => {
      const reference = references.get(reference_id)!;

      return Object.freeze({
        guideline_id,
        reference_id,
        source_type: reference.source_type,
        authors: reference.authors,
        authors_text: reference.authors_text,
        year: reference.year,
        source_title: reference.title,
        journal: reference.journal,
        booktitle: reference.booktitle,
        publisher: reference.publisher,
        url: reference.url,
        doi: reference.doi,
        bibtex: reference.bibtex,
      });
    });
  },
};
