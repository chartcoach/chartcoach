import { CatalogError } from "./errors";
import { catalogEntriesDigest, manifestDigest } from "./identity";
import type { Catalog } from "./model";
import type { ProfileMetadata } from "./profile";
import type { ReleaseProfile } from "./profile-layout";

export type DescribeOptions = Readonly<{
  profile?: string;
  signal?: AbortSignal;
}>;

export type VocabularyInfo = Readonly<{
  name: string;
  description: string;
  examples: readonly string[];
}>;

export type ProfileInfo = Readonly<{
  name: string;
  profile_schema_version: 1;
  documents_version: 1;
  embedding_functions: ProfileMetadata["embedding_functions"];
  dimensions: number;
  distance_metric: ProfileMetadata["distance_metric"];
  python_requirements: ProfileMetadata["python_requirements"];
  lancedb_version: string;
  projection: ProfileMetadata["projection"];
}>;

export type CatalogInfo = Readonly<{
  resolved_location: string | null;
  release_digest: string | null;
  entries_digest: string;
  manifest_digest: string;
  section_roles: readonly VocabularyInfo[];
  label_families: readonly VocabularyInfo[];
  profiles: readonly string[];
  profile: ProfileInfo | null;
}>;

export type ProfileLoader = (
  profile: ReleaseProfile,
  signal?: AbortSignal,
) => Promise<ProfileMetadata>;

export type DescriptionContext = Readonly<{
  resolvedLocation: string | null;
  releaseDigest: string | null;
  profiles: readonly ReleaseProfile[];
  profileLoader?: ProfileLoader;
  profileCache: Map<string, ProfileMetadata>;
}>;

type CatalogIdentity = Readonly<{
  entriesDigest: string;
  manifestDigest: string;
}>;

const identityCache = new WeakMap<Catalog, CatalogIdentity>();

export async function describeCatalog(
  catalog: Catalog,
  context: DescriptionContext,
  options: DescribeOptions = {},
): Promise<CatalogInfo> {
  if (Object.prototype.toString.call(options) !== "[object Object]") {
    throw new CatalogError("Description options must be an object.");
  }
  const identity = await catalogIdentity(catalog);
  const selected = selectProfile(context.profiles, options.profile);
  let profile: ProfileInfo | null = null;
  if (selected) {
    options.signal?.throwIfAborted();
    const metadata = await loadProfile(context, selected, options.signal);
    if (metadata.entries_digest !== identity.entriesDigest) {
      throw new CatalogError("Profile entries digest does not match the catalog entries.", {
        code: "incompatible_profile",
        details: { profile: selected.name },
      });
    }
    if (metadata.manifest_digest !== identity.manifestDigest) {
      throw new CatalogError("Profile manifest digest does not match MANIFEST.md.", {
        code: "incompatible_profile",
        details: { profile: selected.name },
      });
    }
    if ((metadata.projection === null) !== (selected.projection === null)) {
      throw new CatalogError("Profile projection metadata does not match the release inventory.", {
        code: "incompatible_profile",
        details: { profile: selected.name },
      });
    }
    context.profileCache.set(selected.name, metadata);
    profile = profileInfo(selected.name, metadata);
  }

  return Object.freeze({
    resolved_location: context.resolvedLocation,
    release_digest: context.releaseDigest,
    entries_digest: identity.entriesDigest,
    manifest_digest: identity.manifestDigest,
    section_roles: vocabulary(Object.values(catalog.manifest.sectionRoles)),
    label_families: vocabulary(Object.values(catalog.manifest.labelFamilies)),
    profiles: Object.freeze(context.profiles.map((item) => item.name)),
    profile,
  });
}

async function catalogIdentity(catalog: Catalog): Promise<CatalogIdentity> {
  const cached = identityCache.get(catalog);
  if (cached) return cached;
  const [entriesDigest, catalogManifestDigest] = await Promise.all([
    catalogEntriesDigest(catalog.guidelines),
    manifestDigest(catalog.manifest.markdown),
  ]);
  const identity = Object.freeze({ entriesDigest, manifestDigest: catalogManifestDigest });
  identityCache.set(catalog, identity);
  return identity;
}

function selectProfile(
  profiles: readonly ReleaseProfile[],
  name: string | undefined,
): ReleaseProfile | undefined {
  if (name === undefined) return undefined;
  if (!name) throw new CatalogError("Profile must be a non-empty string.");
  const profile = profiles.find((item) => item.name === name);
  if (profile) return profile;
  throw new CatalogError(`Unknown profile: ${name}`, {
    code: "lookup",
    details: { profile: name, available: profiles.map((item) => item.name) },
    hints: [
      `Available profiles: ${profiles.map((item) => JSON.stringify(item.name)).join(", ") || "none"}.`,
    ],
  });
}

async function loadProfile(
  context: DescriptionContext,
  profile: ReleaseProfile,
  signal?: AbortSignal,
): Promise<ProfileMetadata> {
  const cached = context.profileCache.get(profile.name);
  if (cached) return cached;
  if (!context.profileLoader) {
    throw new CatalogError("Profile metadata loading is unavailable for caller-provided bytes.", {
      code: "unavailable_capability",
      details: { profile: profile.name },
      hints: ["Use openCatalog with an HTTP or HTTPS release URL."],
    });
  }
  return context.profileLoader(profile, signal);
}

function profileInfo(name: string, metadata: ProfileMetadata): ProfileInfo {
  return Object.freeze({
    name,
    profile_schema_version: metadata.schema_version,
    documents_version: metadata.documents_version,
    embedding_functions: metadata.embedding_functions,
    dimensions: metadata.dimensions,
    distance_metric: metadata.distance_metric,
    python_requirements: metadata.python_requirements,
    lancedb_version: metadata.lancedb_version,
    projection: metadata.projection,
  });
}

function vocabulary(
  definitions: readonly Readonly<{
    name: string;
    description: string;
    examples: readonly string[];
  }>[],
): readonly VocabularyInfo[] {
  return Object.freeze(
    definitions.map((definition) =>
      Object.freeze({
        name: definition.name,
        description: definition.description,
        examples: Object.freeze([...definition.examples]),
      }),
    ),
  );
}
