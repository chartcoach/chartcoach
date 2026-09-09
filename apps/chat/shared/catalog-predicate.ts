import { and, literal, sql } from "@uwdata/mosaic-sql";
import { catalogFiltersSchema, type CatalogFilters, type CatalogMetadata } from "./catalog-filters";

function validateCatalogFilters(filters: CatalogFilters, metadata: CatalogMetadata) {
  const canonical = catalogFiltersSchema.parse(filters);
  if (canonical.catalogId !== metadata.catalogId)
    throw new Error("The catalog changed. Reload the catalog and start a new review.");
  const authors = new Set(metadata.authors.map(({ id }) => id));
  const types = new Set(metadata.sourceTypes.map(({ id }) => id));
  if ([...canonical.includeAuthorIds, ...canonical.excludeAuthorIds].some((id) => !authors.has(id)))
    throw new Error("An author in your selection is unknown. Reload the catalog.");
  if (canonical.sourceTypeIds.some((id) => !types.has(id)))
    throw new Error("A source type in your selection is unknown. Reload the catalog.");
  return canonical;
}

/** Predicates use g for guideline rows and s for one linked source row. */
export function sourcePredicates(filters: CatalogFilters, metadata: CatalogMetadata) {
  const canonical = validateCatalogFilters(filters, metadata);
  const authors = new Map(metadata.authors.map(({ id, name }) => [id, name]));
  const types = new Map(metadata.sourceTypes.map(({ id, name }) => [id, name]));
  const include = canonical.includeAuthorIds.map((id) => authors.get(id)!);
  const exclude = canonical.excludeAuthorIds.map((id) => authors.get(id)!);
  const selectedTypes = canonical.sourceTypeIds.map((id) => types.get(id)!);
  const years = [
    ...(canonical.yearFrom === null
      ? []
      : [sql`try_cast(s.year AS INTEGER) >= ${literal(canonical.yearFrom)}`]),
    ...(canonical.yearTo === null
      ? []
      : [sql`try_cast(s.year AS INTEGER) <= ${literal(canonical.yearTo)}`]),
  ];
  return {
    authors: include.length
      ? sql`list_has_any(s.authors, CAST(CAST(${literal(JSON.stringify(include))} AS JSON) AS VARCHAR[]))`
      : undefined,
    excludedAuthors: exclude.length
      ? sql`NOT EXISTS (SELECT 1 FROM guideline_sources x WHERE x.guideline_id = g.id
          AND list_has_any(x.authors, CAST(CAST(${literal(JSON.stringify(exclude))} AS JSON) AS VARCHAR[])))`
      : undefined,
    years: years.length ? and(...years) : undefined,
    types: selectedTypes.length
      ? sql`list_contains(CAST(CAST(${literal(JSON.stringify(selectedTypes))} AS JSON) AS VARCHAR[]), s.source_type)`
      : undefined,
  };
}
