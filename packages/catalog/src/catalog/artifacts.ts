import { CatalogError } from "./errors";
import { canonicalJson, compareUnicode, sha256Bytes } from "./identity";
import { isJsonNumber, isJsonObject, isJsonString, type JsonObject, type JsonValue } from "./json";

const CATALOG_ARTIFACT_BASE_URL = "https://files.peter.gy/catalog/chartcoach/";

const RELEASE_SCHEMA_VERSION = 1;

const REQUIRED_ARTIFACTS = ["MANIFEST.md", "entries.parquet"] as const;

const FORBIDDEN_PATH_CHARACTERS = new Set('<>:"\\|?*#%');

const WINDOWS_DEVICE_NAMES = new Set(["CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"]);

export type ReleaseArtifact = Readonly<{
  sha256: string;
  bytes: number;
}>;

export type CatalogRelease = Readonly<{
  schema_version: 1;
  digest: string;
  artifacts: Readonly<Record<string, ReleaseArtifact>>;
}>;

export function parseCatalogRelease(value: JsonValue): CatalogRelease {
  const record = requireRecord(value, "Catalog release");
  requireExactKeys(record, ["schema_version", "digest", "artifacts"], "Catalog release");
  requireSchemaVersion(record);
  const artifactRecords = requireRecord(record.artifacts, "Catalog artifacts");
  const artifacts: Record<string, ReleaseArtifact> = Object.create(null);

  for (const [path, artifact] of Object.entries(artifactRecords)
    .map(([path, value]): [string, ReleaseArtifact] => [
      requireRelativePath(path, "Catalog artifact path"),
      parseReleaseArtifact(value),
    ])
    .sort(([left], [right]) => compareUnicode(left, right))) {
    artifacts[path] = artifact;
  }

  validateArtifactPaths(Object.keys(artifacts));

  for (const path of REQUIRED_ARTIFACTS) {
    if (!Object.hasOwn(artifacts, path)) {
      throw new CatalogError(`Catalog release is missing artifact: ${path}.`);
    }
  }

  return Object.freeze({
    schema_version: RELEASE_SCHEMA_VERSION,
    digest: requiredSha256(record, "digest", "Catalog release"),
    artifacts: Object.freeze(artifacts),
  });
}

export function copyCatalogRelease(release: CatalogRelease): CatalogRelease {
  return parseCatalogRelease({
    schema_version: release.schema_version,
    digest: release.digest,
    artifacts: Object.fromEntries(
      Object.entries(release.artifacts).map(([path, artifact]) => [
        path,
        { sha256: artifact.sha256, bytes: artifact.bytes },
      ]),
    ),
  });
}

export async function assertReleaseDigest(
  release: CatalogRelease,
  expected = release.digest,
  label = "Catalog release",
): Promise<void> {
  const actual = await catalogReleaseDigest(release);

  if (release.digest !== actual) {
    throw new CatalogError(`${label} digest ${release.digest} does not match its artifact set.`, {
      code: "integrity",
      details: { expected_digest: release.digest, actual_digest: actual },
    });
  }

  if (release.digest !== expected) {
    throw new CatalogError(`${label} digest ${release.digest} does not match ${expected}.`, {
      code: "integrity",
      details: { expected_digest: expected, actual_digest: release.digest },
    });
  }
}

export async function assertReleaseArtifactBytes(
  path: string,
  artifact: ReleaseArtifact,
  data: ArrayBuffer | ArrayBufferView,
): Promise<void> {
  const bytes = bytesView(data);

  if (bytes.byteLength !== artifact.bytes) {
    throw new CatalogError(`Catalog artifact byte count mismatch: ${path}`, {
      code: "integrity",
      details: { path, expected_bytes: artifact.bytes, actual_bytes: bytes.byteLength },
    });
  }

  const actual = await sha256Bytes(bytes);

  if (actual !== artifact.sha256) {
    throw new CatalogError(`Catalog artifact SHA-256 mismatch: ${path}`, {
      code: "integrity",
      details: { path, expected_sha256: artifact.sha256, actual_sha256: actual },
    });
  }
}

export function catalogUrl(): string {
  return new URL("catalog.json", CATALOG_ARTIFACT_BASE_URL).toString();
}

export function releaseArtifact(release: CatalogRelease, path: string): ReleaseArtifact {
  const artifact = release.artifacts[path];

  if (artifact === undefined) {
    throw new CatalogError(`Catalog release is missing artifact: ${path}.`, {
      code: "integrity",
      details: { path },
    });
  }

  return artifact;
}

export function releaseArtifactUrl(releaseUrl: string | URL, path: string): string {
  return new URL(path, releaseUrl).toString();
}

export function assertReleaseLocation(releaseUrl: string | URL, release: CatalogRelease): void {
  const url = requireReleaseUrl(releaseUrl);

  if (url.pathname.split("/").at(-1) !== "release.json") return;
  const parent = url.pathname.split("/").at(-2);

  if (parent && /^[a-f0-9]{64}$/.test(parent) && parent !== release.digest) {
    throw new CatalogError("Catalog release digest does not match its digest-addressed location.", {
      code: "integrity",
      details: { expected_digest: parent, actual_digest: release.digest },
    });
  }
}

export function sanitizeReleaseUrl(value: string | URL): string {
  const url = requireReleaseUrl(value);
  url.username = "";
  url.password = "";
  url.search = "";
  url.hash = "";

  return url.toString();
}

function requireReleaseUrl(value: string | URL): URL {
  try {
    return new URL(value);
  } catch {
    throw new CatalogError("Catalog release URL must be absolute.");
  }
}

function parseReleaseArtifact(value: JsonValue): ReleaseArtifact {
  const record = requireRecord(value, "Catalog release artifact");
  requireExactKeys(record, ["sha256", "bytes"], "Catalog release artifact");

  return Object.freeze({
    sha256: requiredSha256(record, "sha256", "Catalog release artifact"),
    bytes: requiredInteger(record, "bytes", "Catalog release artifact"),
  });
}

function validateArtifactPaths(paths: string[]): void {
  const seen = new Map<string, string>();

  for (const path of paths) {
    const folded = asciiLower(path);
    const previous = seen.get(folded);

    if (previous !== undefined) {
      throw new CatalogError(`Catalog artifact paths collide: ${previous}, ${path}.`);
    }

    seen.set(folded, path);
  }

  for (const [folded, path] of seen) {
    const parts = folded.split("/");

    if (folded === "release.json") {
      throw new CatalogError(`Catalog artifact path is reserved: ${path}.`);
    }

    for (let length = 1; length < parts.length; length += 1) {
      const ancestor = parts.slice(0, length).join("/");
      const previous = seen.get(ancestor);

      if (previous !== undefined) {
        throw new CatalogError(`Catalog artifact paths collide: ${previous}, ${path}.`);
      }
    }
  }
}

async function catalogReleaseDigest(release: CatalogRelease): Promise<string> {
  return sha256Bytes(
    new TextEncoder().encode(
      canonicalJson({
        schema_version: release.schema_version,
        artifacts: release.artifacts,
      }),
    ),
  );
}

function bytesView(data: ArrayBuffer | ArrayBufferView): Uint8Array {
  if (data instanceof ArrayBuffer) return new Uint8Array(data);

  return new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
}

function requireRecord(value: JsonValue, label: string): JsonObject {
  if (!isJsonObject(value)) throw new CatalogError(`${label} must be an object.`);

  return value;
}

function requireExactKeys(value: JsonObject, expected: readonly string[], label: string): void {
  const actual = Object.keys(value);
  const missing = expected.filter((key) => !actual.includes(key)).sort();
  const unexpected = actual.filter((key) => !expected.includes(key)).sort();

  if (missing.length > 0) {
    throw new CatalogError(`${label} is missing fields: ${missing.join(", ")}.`);
  }

  if (unexpected.length > 0) {
    throw new CatalogError(`${label} has unsupported fields: ${unexpected.join(", ")}.`);
  }
}

function requireSchemaVersion(value: JsonObject): void {
  const version = requiredInteger(value, "schema_version", "Catalog release");

  if (version !== RELEASE_SCHEMA_VERSION) {
    throw new CatalogError(`Catalog release schema_version must be ${RELEASE_SCHEMA_VERSION}.`);
  }
}

function requireRelativePath(path: string, label: string): string {
  const parts = path.split("/");

  if (!pathIsAscii(path) || parts.some((part) => !isPortablePathSegment(part))) {
    throw new CatalogError(`${label} must be relative: ${path}`);
  }

  return path;
}

function isPortablePathSegment(value: string): boolean {
  if (
    value === "" ||
    value === "." ||
    value === ".." ||
    value.endsWith(".") ||
    Array.from(value).some((character) => FORBIDDEN_PATH_CHARACTERS.has(character))
  ) {
    return false;
  }

  const basename = value.split(".", 1)[0]!.toUpperCase();

  return !WINDOWS_DEVICE_NAMES.has(basename) && !/^(?:COM|LPT)[1-9]$/.test(basename);
}

function requiredString(value: JsonObject, key: string, label: string): string {
  const raw = value[key];

  if (!isJsonString(raw) || raw.length === 0) {
    throw new CatalogError(`${label} ${key} must be a string.`);
  }

  return raw;
}

function requiredInteger(value: JsonObject, key: string, label: string): number {
  const raw = value[key];

  if (!isJsonNumber(raw) || !Number.isSafeInteger(raw) || raw < 0) {
    throw new CatalogError(
      `${label} ${key} must be an integer from 0 through ${Number.MAX_SAFE_INTEGER}.`,
    );
  }

  return raw;
}

function requiredSha256(value: JsonObject, key: string, label: string): string {
  const digest = requiredString(value, key, label);
  requireSha256(digest, `${label} ${key}`);

  return digest;
}

function requireSha256(value: string, label: string): void {
  if (!/^[a-f0-9]{64}$/.test(value)) {
    throw new CatalogError(`${label} must be a lowercase SHA-256 digest.`);
  }
}

function pathIsAscii(value: string): boolean {
  if (value.length === 0) return false;

  for (const character of value) {
    const code = character.charCodeAt(0);

    if (code < 0x21 || code > 0x7e) return false;
  }

  return true;
}

function asciiLower(value: string): string {
  return value.replace(/[A-Z]/g, (character) => character.toLowerCase());
}
