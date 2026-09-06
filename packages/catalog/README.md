# @chartcoach/catalog

`@chartcoach/catalog` fetches a selected or exact Guideline Catalog release,
verifies its files, and returns immutable `Guideline` values for querying,
reading, and citation.

chartcoach is alpha software. `openCatalog` requires a browser or server
runtime with `fetch`, Web Crypto, `AbortSignal.timeout`, and `AbortSignal.any`.
`loadCatalog` verifies release files that the application already holds.
`loadCatalogData` parses descriptor-free bundle data.

## Query and read guidance

```bash
npm install @chartcoach/catalog@0.2.0
```

```ts
import { openCatalog } from "@chartcoach/catalog";

const catalog = await openCatalog(
  "https://files.peter.gy/packages/python/chartcoach/0.2.0/docs-catalog/c0f6dbec3dd31b07763b46fd458733db0b8b50c5793cf9447458119287129420/release.json",
);
const candidates = catalog.query({ contains: "direct labels", limit: 5 });
const ids = candidates.map(({ id }) => id);
const records = catalog.read({ ids, sourceDetail: "minimal" });
const citations = catalog.cite({ ids });
const info = await catalog.describe();

console.log(records[0]?.title);
```

`query`, `read`, and `cite` run synchronously over the loaded `Catalog`.
`describe` is asynchronous because it computes SHA-256 digests and can fetch
selected profile metadata.

```text
Directly label colored series instead of relying on a color key
```

## Choose a release URL

`openCatalog(location, { fetch, signal })` accepts an absolute HTTP or HTTPS URL:

| Location       | Behavior                                      |
| -------------- | --------------------------------------------- |
| `catalog.json` | Follows the currently selected public release |
| `release.json` | Keeps one release digest across calls         |
| Omitted        | Opens the official selected catalog           |

The loader verifies the release digest, then checks the byte count and SHA-256
hash of `MANIFEST.md` and `entries.parquet` before parsing them. Pass a custom
`fetch` implementation when the runtime does not use `globalThis.fetch`. Pass
an `AbortSignal` to cancel descriptor and artifact requests.
The returned catalog exposes the verified descriptor as `catalog.release` and
its sanitized exact `release.json` URL as `catalog.releaseUrl`.

## Load files your app already has

`loadCatalogData` accepts Parquet bytes and manifest text:

```ts
import { readFile } from "node:fs/promises";
import { loadCatalogData } from "@chartcoach/catalog";

const catalog = await loadCatalogData({
  entries: await readFile("dist/catalog/entries.parquet"),
  manifestText: await readFile("dist/catalog/MANIFEST.md", "utf8"),
});
```

`loadCatalogData` validates the manifest vocabulary and guideline fields.
Release integrity remains caller-owned because this input contains no
`release.json`.

Use `loadCatalog` when the application already has a parsed release and the
files listed by its descriptor:

```ts
import { readFile } from "node:fs/promises";
import { pathToFileURL } from "node:url";
import { loadCatalog, parseCatalogRelease } from "@chartcoach/catalog";

const releasePath = "dist/release/release.json";
const release = parseCatalogRelease(JSON.parse(await readFile(releasePath, "utf8")));
const catalog = await loadCatalog({
  release,
  releaseUrl: pathToFileURL(releasePath),
  entries: await readFile("dist/release/entries.parquet"),
  manifest: await readFile("dist/release/MANIFEST.md"),
});
```

`loadCatalog` verifies the release digest and both core files before returning
a catalog with its exact release URL. Each core file is capped at 64 MiB.

## Catalog methods

| Method                                 | Result                                                                           |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| `query(options?)`                      | Compact guideline entry candidates. The default limit is 50.                     |
| `read({ ids, roles?, sourceDetail? })` | Guideline entry records with ordered sections and parsed sources.                |
| `cite({ ids, urlTemplate? })`          | Guideline links, formatted guideline citations, and structured source citations. |
| `describe({ profile?, signal? })`      | Catalog identity, vocabulary, profile names, and optional profile information.   |
| `get(id)`                              | A `Guideline` or `undefined`.                                                    |
| `require(id)`                          | A `Guideline` or a `CatalogError` with code `"lookup"`.                          |

`catalog.guidelines`, iteration, `catalog.length`, `catalog.labels()`,
`catalog.sectionRoles()`, `catalog.release`, `catalog.releaseUrl`, and
`toMarkdown(guideline)` support direct application composition.

JavaScript option names use camel case. Shared JSON result fields use snake
case, including `source_title`, `reference_id`, and `release_digest`.

## Inspect a profile

```ts
const info = await catalog.describe();
const profile = info.profiles[0];

if (profile !== undefined) {
  const controller = new AbortController();
  const details = await catalog.describe({ profile, signal: controller.signal });
  console.log(details.profile?.distance_metric, details.profile?.dimensions);
}
```

`describe({ profile })` verifies `profile.json` against the release byte count,
SHA-256 hash, 64 KiB limit, catalog entries digest, and manifest digest. It
keeps the index unopened and caches verified metadata per `Catalog` instance.
Each call has its own cancellation signal.

`ProfileInfo` contains the profile and document schema versions, embedding
binding, dimensions, `distance_metric`, `python_requirements`, LanceDB version,
and projection metadata.

Catalogs created with `loadCatalog` retain the release descriptor and profile
names from caller-held bytes. Use `openCatalog` to fetch profile metadata over
HTTP.

`Guideline` values, operation results, their nested arrays, and manifest
definitions are frozen. Pass changed record objects to a new `Catalog`. Use
`loadCatalogData` after writing changed rows to `entries.parquet`.

`CatalogError` exposes `code`, `details`, and `hints`. Its codes use the shared
Python and JavaScript error vocabulary.

`parseProfileMetadata(value)` validates and freezes `profile.json`. Profiles use
flat lowercase IDs such as `minilm-normalized` and contain `profile.json` plus
`index.tar.gz`. A release may also contain `documents.parquet` and
`projection.parquet` exports. The package exports `EntryCandidate`,
`GuidelineEntryRecord`, `ProfileInfo`, constructor and loader inputs, operation
options, manifest types, release types, and profile metadata types.

| Page                                                 | Details                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| [JavaScript](https://docs.chartcoach.dev/javascript) | Release loading, catalog methods, and Markdown serialization |
| [Catalog data](https://docs.chartcoach.dev/catalog)  | Guideline fields and published file layouts                  |

Licensed under Apache-2.0.
