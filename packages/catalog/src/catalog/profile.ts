import { CatalogError } from "./errors";
import { isJsonNumber, isJsonObject, isJsonString, type JsonObject, type JsonValue } from "./json";

export type DistanceMetric = "cosine" | "l2" | "dot";

export type EmbeddingBinding = Readonly<{
  name: string;
  model: Readonly<JsonObject>;
  source_column: "text";
  vector_column: "vector";
}>;

export type ProjectionMetadata = Readonly<{
  algorithm: "empty" | "linear" | "umap";
  options: Readonly<JsonObject>;
}>;

export type ProfileMetadata = Readonly<{
  schema_version: 1;
  documents_version: 1;
  entries_digest: string;
  manifest_digest: string;
  embedding_functions: readonly [EmbeddingBinding];
  dimensions: number;
  distance_metric: DistanceMetric;
  python_requirements: Readonly<Record<string, string>>;
  lancedb_version: string;
  projection: ProjectionMetadata | null;
}>;

const profileFields = [
  "schema_version",
  "documents_version",
  "entries_digest",
  "manifest_digest",
  "embedding_functions",
  "dimensions",
  "distance_metric",
  "python_requirements",
  "lancedb_version",
  "projection",
] as const;

const bindingFields = ["name", "model", "source_column", "vector_column"] as const;

const projectionFields = ["algorithm", "options"] as const;

const sha256Pattern = /^[a-f0-9]{64}$/;

const distributionPattern = /^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$/;

const versionPattern = /^[A-Za-z0-9][A-Za-z0-9.!+_-]*$/;

const variablePattern = /^\$var:[^:]+$/;

const sensitiveNamePattern =
  /(?:^|[_-])(?:access[_-]?key|api[_-]?key|authorization|client[_-]?secret|cookie|credential|password|private[_-]?key|secret|signature|token)(?:$|[_-])/i;

const sensitiveQueryNames = new Set([
  "access_key",
  "api_key",
  "apikey",
  "authorization",
  "credential",
  "password",
  "secret",
  "signature",
  "sig",
  "token",
]);

export function parseProfileMetadata(value: JsonValue): ProfileMetadata {
  const record = requireObject(value, "Profile metadata");
  requireExactFields(record, profileFields, "Profile metadata");

  if (record.schema_version !== 1) {
    throw new CatalogError("Profile schema_version must be 1.");
  }

  if (record.documents_version !== 1) {
    throw new CatalogError("Profile documents_version must be 1.");
  }

  const entriesDigest = requireSha256(record.entries_digest, "Profile entries_digest");
  const manifestDigest = requireSha256(record.manifest_digest, "Profile manifest_digest");

  if (!Array.isArray(record.embedding_functions) || record.embedding_functions.length !== 1) {
    throw new CatalogError("Profile must contain exactly one embedding binding.");
  }

  const binding = parseBinding(record.embedding_functions[0]!);
  const dimensions = record.dimensions;

  if (!isJsonNumber(dimensions) || !Number.isSafeInteger(dimensions) || dimensions < 1) {
    throw new CatalogError("Profile dimensions must be a positive safe integer.");
  }

  const distanceMetric = record.distance_metric;

  if (distanceMetric !== "cosine" && distanceMetric !== "l2" && distanceMetric !== "dot") {
    throw new CatalogError("Profile distance_metric must be cosine, l2, or dot.");
  }

  const pythonRequirements = parseRequirements(record.python_requirements);
  const lancedbVersion = requireVersion(record.lancedb_version, "Profile lancedb_version");
  const projection = record.projection === null ? null : parseProjection(record.projection);

  return Object.freeze({
    schema_version: 1,
    documents_version: 1,
    entries_digest: entriesDigest,
    manifest_digest: manifestDigest,
    embedding_functions: Object.freeze([binding] as const),
    dimensions,
    distance_metric: distanceMetric,
    python_requirements: pythonRequirements,
    lancedb_version: lancedbVersion,
    projection,
  });
}

function parseBinding(value: JsonValue): EmbeddingBinding {
  const record = requireObject(value, "Profile embedding binding");
  requireExactFields(record, bindingFields, "Profile embedding binding");
  const name = record.name;

  if (!isJsonString(name) || !name || name !== name.trim()) {
    throw new CatalogError("Profile embedding name must be a non-empty string.");
  }

  if (record.source_column !== "text" || record.vector_column !== "vector") {
    throw new CatalogError("Profile embedding binding must map text to vector.");
  }

  const model = requireObject(record.model, "Profile embedding model");
  validateModel(model);

  return Object.freeze({
    name,
    model: freezeJsonObject(model),
    source_column: "text",
    vector_column: "vector",
  });
}

function parseProjection(value: JsonValue): ProjectionMetadata {
  const record = requireObject(value, "Profile projection");
  requireExactFields(record, projectionFields, "Profile projection");
  const algorithm = record.algorithm;

  if (algorithm !== "empty" && algorithm !== "linear" && algorithm !== "umap") {
    throw new CatalogError("Profile projection algorithm is unsupported.");
  }

  return Object.freeze({
    algorithm,
    options: freezeJsonObject(requireObject(record.options, "Profile projection options")),
  });
}

function parseRequirements(value: JsonValue | undefined): Readonly<Record<string, string>> {
  const record = requireObject(value, "Profile Python requirements");
  const requirements: Record<string, string> = Object.create(null);

  for (const [name, requirement] of Object.entries(record)) {
    if (
      !distributionPattern.test(name) ||
      !isJsonString(requirement) ||
      !versionPattern.test(requirement) ||
      !/[0-9]/.test(requirement)
    ) {
      throw new CatalogError(
        "Profile python_requirements must map distribution names to exact versions.",
      );
    }

    requirements[name] = requirement;
  }

  return Object.freeze(requirements);
}

function validateModel(model: JsonObject): void {
  for (const [key, value] of Object.entries(model)) {
    const variables = variableValues(value);

    if (
      variables.some((variable) => !variablePattern.test(variable)) ||
      (variables.length > 0 && !isJsonString(value))
    ) {
      throw new CatalogError(
        `Profile embedding setting ${JSON.stringify(key)} has an invalid variable.`,
      );
    }

    if (
      sensitiveNamePattern.test(key) &&
      value !== null &&
      (!isJsonString(value) || !variablePattern.test(value))
    ) {
      throw new CatalogError(
        `Profile embedding setting ${JSON.stringify(key)} must use a registry variable.`,
      );
    }

    if (
      key === "default_headers" &&
      value !== null &&
      (!isJsonObject(value) || Object.keys(value).length > 0)
    ) {
      throw new CatalogError("Profile embedding default_headers must be empty.");
    }

    if (containsSensitiveKey(value)) {
      throw new CatalogError(
        `Profile embedding setting ${JSON.stringify(key)} contains authentication data.`,
      );
    }

    rejectCredentialUrls(value, key);
  }

  if (Object.hasOwn(model, "trust_remote_code") && model.trust_remote_code !== false) {
    throw new CatalogError("Profile embedding must disable remote model code.");
  }
}

function containsSensitiveKey(value: JsonValue): boolean {
  if (Array.isArray(value)) return value.some(containsSensitiveKey);

  if (!isJsonObject(value)) return false;

  return Object.entries(value).some(
    ([key, item]) => sensitiveNamePattern.test(key) || containsSensitiveKey(item),
  );
}

function rejectCredentialUrls(value: JsonValue, path: string): void {
  if (Array.isArray(value)) {
    value.forEach((item, index) => rejectCredentialUrls(item, `${path}[${index}]`));

    return;
  }

  if (isJsonObject(value)) {
    for (const [key, item] of Object.entries(value)) {
      rejectCredentialUrls(item, `${path}.${key}`);
    }

    return;
  }

  if (!isJsonString(value)) return;
  let parsed: URL;

  try {
    parsed = new URL(value);
  } catch {
    return;
  }

  if (parsed.protocol !== "http:" && parsed.protocol !== "https:") return;

  if (parsed.username || parsed.password) {
    throw new CatalogError(
      `Profile embedding URL setting ${JSON.stringify(path)} contains credentials.`,
    );
  }

  if (
    Array.from(parsed.searchParams.keys()).some(
      (name) => sensitiveQueryNames.has(name.toLowerCase()) || sensitiveNamePattern.test(name),
    )
  ) {
    throw new CatalogError(
      `Profile embedding URL setting ${JSON.stringify(path)} contains authentication parameters.`,
    );
  }
}

function variableValues(value: JsonValue): string[] {
  if (isJsonString(value)) return value.startsWith("$var:") ? [value] : [];

  if (Array.isArray(value)) return value.flatMap(variableValues);

  if (!isJsonObject(value)) return [];

  return Object.values(value).flatMap(variableValues);
}

function freezeJsonObject(value: JsonObject): Readonly<JsonObject> {
  const result: JsonObject = Object.create(null);

  for (const [key, item] of Object.entries(value)) {
    result[key] = freezeJson(item);
  }

  return Object.freeze(result);
}

function freezeJson(value: JsonValue): JsonValue {
  if (Object.prototype.toString.call(value) === "[object Number]" && !isJsonNumber(value)) {
    throw new CatalogError("Profile metadata must contain finite JSON numbers.");
  }

  if (Array.isArray(value)) return Object.freeze(value.map(freezeJson));

  if (isJsonObject(value)) return freezeJsonObject(value);

  return value;
}

function requireObject(value: JsonValue | undefined, label: string): JsonObject {
  if (!isJsonObject(value)) throw new CatalogError(`${label} must be a JSON object.`);

  return value;
}

function requireExactFields(value: JsonObject, fields: readonly string[], label: string): void {
  const actual = Object.keys(value);
  const missing = fields.filter((field) => !Object.hasOwn(value, field));
  const unknown = actual.filter((field) => !fields.includes(field));

  if (missing.length > 0)
    throw new CatalogError(`${label} is missing fields: ${missing.join(", ")}.`);

  if (unknown.length > 0)
    throw new CatalogError(`${label} has unsupported fields: ${unknown.join(", ")}.`);
}

function requireSha256(value: JsonValue | undefined, label: string): string {
  if (!isJsonString(value) || !sha256Pattern.test(value)) {
    throw new CatalogError(`${label} must be a lowercase SHA-256 digest.`);
  }

  return value;
}

function requireVersion(value: JsonValue | undefined, label: string): string {
  if (!isJsonString(value) || !versionPattern.test(value) || !/[0-9]/.test(value)) {
    throw new CatalogError(`${label} must be a non-empty exact version.`);
  }

  return value;
}
