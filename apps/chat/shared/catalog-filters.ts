import { z } from "zod";

const facetIds = z.array(z.number().int().positive()).max(100);
const catalogIdSchema = z.string().regex(/^[a-f0-9]{64}$/);

export const catalogFiltersSchema = z
  .strictObject({
    catalogId: catalogIdSchema,
    includeAuthorIds: facetIds,
    excludeAuthorIds: facetIds,
    sourceTypeIds: facetIds,
    yearFrom: z.int32().nullable(),
    yearTo: z.int32().nullable(),
  })
  .refine(({ yearFrom, yearTo }) => yearFrom === null || yearTo === null || yearFrom <= yearTo, {
    message: "The first year must be at or before the last year.",
  })
  .transform((filters) => ({
    catalogId: filters.catalogId,
    includeAuthorIds: [...new Set(filters.includeAuthorIds)].sort((a, b) => a - b),
    excludeAuthorIds: [...new Set(filters.excludeAuthorIds)].sort((a, b) => a - b),
    sourceTypeIds: [...new Set(filters.sourceTypeIds)].sort((a, b) => a - b),
    yearFrom: filters.yearFrom,
    yearTo: filters.yearTo,
  }));

export type CatalogFilters = z.infer<typeof catalogFiltersSchema>;

const facetSchema = z.object({
  id: z.number().int().positive(),
  name: z.string(),
  guidelineCount: z.number().int().nonnegative(),
});

export const catalogMetadataSchema = z.object({
  catalogId: catalogIdSchema,
  totalGuidelines: z.number().int().nonnegative(),
  authors: z.array(facetSchema),
  sourceTypes: z.array(facetSchema),
  years: z.object({
    min: z.int32().nullable(),
    max: z.int32().nullable(),
    undatedGuidelines: z.number().int().nonnegative(),
  }),
  tables: z.array(
    z.object({
      name: z.string(),
      rows: z.number().int().nonnegative(),
      columns: z.array(z.object({ name: z.string(), type: z.string() })),
    }),
  ),
});

export type CatalogMetadata = z.infer<typeof catalogMetadataSchema>;

export function emptyCatalogFilters(catalogId: string): CatalogFilters {
  return {
    catalogId,
    includeAuthorIds: [],
    excludeAuthorIds: [],
    sourceTypeIds: [],
    yearFrom: null,
    yearTo: null,
  };
}
