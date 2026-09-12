import type { Catalog } from "./model";
import { CatalogError } from "./errors";
import { isJsonString } from "./json";
import { tableNames, tableSchemas, type CatalogTables, type TableColumnInfo } from "./tables";

export type RegisterCatalogOptions = Readonly<{ ids?: readonly string[] }>;

export function registrationPlan(
  catalog: Catalog,
  options: RegisterCatalogOptions,
  source: "parameter" | "file",
): readonly Readonly<{ sql: string; rows: string }>[] {
  if (Object.prototype.toString.call(options) !== "[object Object]")
    throw new CatalogError("Registration options must be an object.");

  if (
    options.ids !== undefined &&
    (!Array.isArray(options.ids) || !options.ids.every(isJsonString))
  )
    throw new CatalogError("ids must be an array of strings.");
  const ids = options.ids === undefined ? undefined : new Set(options.ids);

  for (const id of ids ?? []) catalog.require(id);
  const tables = selectedTables(catalog, ids);
  const json = source === "file" ? "(SELECT content FROM read_text(?))" : "?";

  return tableNames.map((name) => {
    const columns = tableSchemas[name]
      .map(({ name, type }) => `"${name}" ${sqlType(type)}`)
      .join(", ");

    return {
      sql: `CREATE OR REPLACE TABLE "${name}" AS SELECT record.*
       FROM UNNEST(CAST(CAST(${json} AS JSON) AS STRUCT(${columns})[])) AS records(record)`,
      rows: JSON.stringify(tables[name]),
    };
  });
}

function selectedTables(catalog: Catalog, ids: ReadonlySet<string> | undefined): CatalogTables {
  const links = catalog.table("guideline_references");
  const selectedLinks = ids ? links.filter(({ guideline_id }) => ids.has(guideline_id)) : links;
  const references = new Set(selectedLinks.map(({ reference_id }) => reference_id));

  return {
    guidelines: ids
      ? catalog.table("guidelines").filter(({ id }) => ids.has(id))
      : catalog.table("guidelines"),
    sections: ids
      ? catalog.table("sections").filter(({ guideline_id }) => ids.has(guideline_id))
      : catalog.table("sections"),
    guideline_labels: ids
      ? catalog.table("guideline_labels").filter(({ guideline_id }) => ids.has(guideline_id))
      : catalog.table("guideline_labels"),
    references: ids
      ? catalog.table("references").filter(({ id }) => references.has(id))
      : catalog.table("references"),
    guideline_references: selectedLinks,
    guideline_sources: ids
      ? catalog.table("guideline_sources").filter(({ guideline_id }) => ids.has(guideline_id))
      : catalog.table("guideline_sources"),
  };
}

function sqlType(type: TableColumnInfo["type"]): string {
  switch (type) {
    case "String":
      return "VARCHAR";
    case "List(String)":
      return "VARCHAR[]";
    case "List(Struct({'role': String, 'title': String, 'content': String}))":
      return "STRUCT(role VARCHAR, title VARCHAR, content VARCHAR)[]";
  }
}
