import { z } from "zod";

export const catalogSelectionSchema = z.strictObject({
  catalogId: z.string().regex(/^[a-f0-9]{64}$/),
  sql: z.string().trim().min(1).max(16_000),
});

export type CatalogSelection = z.infer<typeof catalogSelectionSchema>;

export const maxSelectionBytes = 64_000;

export const maxSelectionHeaderLength = 8_000;

export const catalogSelectionHeaderSchema = z
  .string()
  .min(1)
  .max(maxSelectionHeaderLength)
  .regex(/^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/);
