import type { CatalogRelease } from "./artifacts";
import { CatalogError } from "./errors";

const profileFiles = new Set([
  "profile.json",
  "index.tar.gz",
  "documents.parquet",
  "projection.parquet",
]);

const profileIdPattern = /^[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?$/;

const windowsDeviceNames = new Set(["CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"]);

export type ReleaseProfile = Readonly<{
  name: string;
  metadata: string;
  index: string;
  documents: string | null;
  projection: string | null;
}>;

export function releaseProfiles(release: CatalogRelease): readonly ReleaseProfile[] {
  const profiles = new Map<string, Set<string>>();

  for (const path of Object.keys(release.artifacts)) {
    const parts = path.split("/");

    if (parts[0] !== "profiles") continue;

    if (parts.length < 3) {
      throw new CatalogError(`Invalid profile artifact path: ${JSON.stringify(path)}.`);
    }

    const filename = parts.at(-1)!;

    if (!profileFiles.has(filename)) {
      throw new CatalogError(`Unknown profile artifact: ${JSON.stringify(path)}.`);
    }

    const profile = parts.slice(1, -1).join("/");
    const artifacts = profiles.get(profile) ?? new Set<string>();
    artifacts.add(filename);
    profiles.set(profile, artifacts);
  }

  const result: ReleaseProfile[] = [];

  for (const [profile, artifacts] of profiles) {
    if (!isProfileId(profile)) {
      throw new CatalogError("Profile ID must be a lowercase portable single-component name.");
    }

    if (!artifacts.has("profile.json")) {
      throw new CatalogError(`Profile ${JSON.stringify(profile)} is missing profile.json.`);
    }

    if (!artifacts.has("index.tar.gz")) {
      throw new CatalogError(`Profile ${JSON.stringify(profile)} is missing index.tar.gz.`);
    }

    const root = `profiles/${profile}`;
    result.push(
      Object.freeze({
        name: profile,
        metadata: `${root}/profile.json`,
        index: `${root}/index.tar.gz`,
        documents: artifacts.has("documents.parquet") ? `${root}/documents.parquet` : null,
        projection: artifacts.has("projection.parquet") ? `${root}/projection.parquet` : null,
      }),
    );
  }

  return Object.freeze(result.sort((left, right) => (left.name < right.name ? -1 : 1)));
}

export function releaseProfileNames(release: CatalogRelease): readonly string[] {
  return Object.freeze(releaseProfiles(release).map((profile) => profile.name));
}

function isProfileId(value: string): boolean {
  if (!profileIdPattern.test(value) || value.includes("/")) return false;
  const basename = value.split(".", 1)[0]!.toUpperCase();

  return !windowsDeviceNames.has(basename) && !/^(?:COM|LPT)[1-9]$/.test(basename);
}
