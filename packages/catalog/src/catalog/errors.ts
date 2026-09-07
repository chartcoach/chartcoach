import type { JsonObject } from "./json";

export type CatalogErrorCode =
  | "lookup"
  | "invalid_input"
  | "integrity"
  | "unavailable_capability"
  | "incompatible_profile"
  | "embedding_failure"
  | "operation_failed"
  | "response_too_large";

export type CatalogErrorOptions = Readonly<{
  code?: CatalogErrorCode;
  details?: JsonObject;
  hints?: readonly string[];
}>;

export class CatalogError extends Error {
  readonly code: CatalogErrorCode;
  readonly details: Readonly<JsonObject>;
  readonly hints: readonly string[];

  constructor(message: string, options: CatalogErrorOptions = {}) {
    super(message);
    this.name = "CatalogError";
    this.code = options.code ?? "invalid_input";
    this.details = Object.freeze({ ...options.details });
    this.hints = Object.freeze([...(options.hints ?? [])]);
  }
}
