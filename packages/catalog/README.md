# @chartcoach/catalog

`@chartcoach/catalog` fetches a selected or exact Guideline Catalog release,
verifies its files, and returns immutable `Guideline` values for querying,
reading, and citation.

chartcoach is alpha software. `openCatalog` requires a browser or server
runtime with `fetch`, Web Crypto, `AbortSignal.timeout`, and `AbortSignal.any`.
Node.js consumers require Node 22.19 or later.
`loadCatalog` verifies release files that the application already holds.
`loadCatalogData` parses descriptor-free bundle data.

## Query and read guidance

```bash
npm install @chartcoach/catalog
```

```ts
import { openCatalog } from "@chartcoach/catalog";

const catalog = await openCatalog();
const candidates = catalog.query({ contains: "direct labels", limit: 5 });
const ids = candidates.map(({ id }) => id);
const records = catalog.read({ ids, sourceDetail: "minimal" });
const citations = catalog.cite({ ids });
const info = await catalog.describe();

console.log(records[0]?.title);
```

```text
Directly label colored series instead of relying on a color key
```

`query`, `read`, and `cite` run synchronously over the loaded `Catalog`.
`describe` is asynchronous because it computes SHA-256 digests and can fetch
selected profile metadata.

Reference parsing and APA citations use [RefKit](https://peter-gy.github.io/refkit/).
The module initializes its WebAssembly engine during import. Browser builds must
serve RefKit's bundled `.wasm` asset at its module-relative URL. A restrictive
[Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
must allow `'wasm-unsafe-eval'` in `script-src` and the asset origin in `connect-src`.

`contains` matches a contiguous phrase in the ID, title, or description,
ignoring case and normalizing whitespace, hyphens, and underscores. For empty
matches, shorten the phrase or follow [Find guidelines](https://docs.chartcoach.dev/querying)
to query section text with the application's data engine.

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
| `table(name)`                          | Cached, immutable rows for a canonical catalog table.                            |
| `describe({ profile?, signal? })`      | Catalog identity, table schemas and counts, vocabulary, and profile information. |
| `get(id)`                              | A `Guideline` or `undefined`.                                                    |
| `require(id)`                          | A `Guideline` or a `CatalogError` with code `"lookup"`.                          |

`catalog.guidelines`, iteration, `catalog.length`, `catalog.labels()`,
`catalog.sectionRoles()`, `catalog.release`, `catalog.releaseUrl`, and
`toMarkdown(guideline)` support direct application composition.

JavaScript option names use camel case. Shared JSON result fields use snake
case, including `source_title`, `reference_id`, and `release_digest`.

## Query canonical tables

`catalog.table(name)` exposes the same six relations as Python: `guidelines`,
`sections`, `guideline_labels`, `references`, `guideline_references`, and
`guideline_sources`. Rows and nested values are immutable. Unknown names raise
`CatalogError` with code `"lookup"`. `describe().tables` supplies names, row counts,
and logical column types, including for empty tables.

```ts
const sources = catalog.table("guideline_sources");
console.log(sources[0]?.authors);
console.log((await catalog.describe()).tables);
```

For native SQL, install [DuckDB's Node.js client](https://duckdb.org/docs/stable/clients/node_neo/overview)
alongside the catalog package:

```bash
npm install @chartcoach/catalog @duckdb/node-api
```

```ts
import { DuckDBInstance } from "@duckdb/node-api";
import { registerCatalog } from "@chartcoach/catalog/duckdb";

const db = await DuckDBInstance.create(":memory:");
const connection = await db.connect();
try {
  await registerCatalog(connection, catalog);
  const result = await connection.runAndReadAll(
    'SELECT source_type, count(*) FROM "references" GROUP BY source_type',
  );
  console.log(result.getRowsJson());
} finally {
  connection.closeSync();
  db.closeSync();
}
```

`registerCatalog(connection, catalog, { ids? })` creates or replaces the six
catalog tables and returns the same connection. The caller owns configuration,
transactions, and closing. Omit `ids` for the full catalog. An empty array creates
six empty typed tables. Selected IDs retain all their linked source records.
Unknown IDs and invalid references fail before table replacement.

## Query in the browser with DuckDB-WASM

The optional `@chartcoach/catalog/duckdb-wasm` adapter registers the same six
tables in a caller-owned [DuckDB-WASM](https://duckdb.org/docs/stable/clients/wasm/overview)
connection. DuckDB-WASM runs SQL in a browser worker. With a loaded `catalog` and
an `AsyncDuckDBConnection` named `connection`:

```ts
import { registerCatalog } from "@chartcoach/catalog/duckdb-wasm";

await registerCatalog(connection, catalog, { ids });
const result = await connection.query('SELECT * FROM "references"');
console.log(result.toArray());
```

Install `@duckdb/duckdb-wasm` alongside this package. The adapter accepts the same
`{ ids? }` option as the Node adapter and preserves caller-owned connections and
transactions. It releases its temporary in-memory files after registration.
The caller owns worker creation and database shutdown.

Catalog artifacts can also be read directly by DuckDB. Use the verified bytes
already retained by a release-backed catalog:

```ts
await connection.bindings.registerFileBuffer(
  "entries.parquet",
  await catalog.artifact("entries.parquet"),
);
const rows = await connection.query(
  "SELECT id, title FROM read_parquet('entries.parquet') LIMIT 5",
);
console.log(rows.toArray());
await connection.bindings.dropFile("entries.parquet");
```

Use DuckDB's EH bundle in a browser with WebAssembly exception handling, and serve
its worker and WASM assets through your application. Its
first JSON query loads a version-matched extension from `extensions.duckdb.org`
unless you configure another extension repository. Your Content Security Policy
must permit WASM compilation, workers, and that extension origin. The
[chat app](../../apps/chat) demonstrates same-origin assets, verified HTTPS
Parquet loading, and linked filters with Mosaic.

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

## Compose verified artifacts

```ts
const entries = await catalog.artifact("entries.parquet");
const paths = Object.keys(catalog.release?.artifacts ?? {});
```

`artifact(path, { signal? })` returns a caller-owned `Uint8Array` after checking
its byte count and SHA-256 hash. The release inventory lists optional files
such as `profiles/<profile>/documents.parquet` and
`profiles/<profile>/projection.parquet`. Pass Parquet bytes to your data library.
Core bytes and small metadata are reused in memory.
`loadCatalog` makes its supplied core bytes available through the same method.

`openCatalog` accepts an optional `cache` with asynchronous `get(sha256, bytes)` and
`put(sha256, bytes)` methods. Cached bytes are verified before reuse. A custom
`fetch` can resolve other URI schemes, including S3, using the caller's storage
client and credentials. Return a standard `Response` and forward its request
signal to the client.

## Open local files and cache releases in Node.js

```ts
import { openCatalog, artifactPath } from "@chartcoach/catalog/node";

const catalog = await openCatalog("./dist/release");
const entriesPath = await artifactPath(catalog, "entries.parquet");
```

The Node entry point accepts local bundles, release directories, deployed
roots, descriptor paths, and remote descriptor URLs. It caches verified bytes
in the per-user platform cache directory, sharing the `chartcoach` cache layout
with Python. `cacheDirectory` overrides that location.

`platformDirectories()` from `@chartcoach/catalog/node/paths` returns the per-user
`data`, `config`, and `cache` roots. It follows Python's
`PlatformDirs("chartcoach", appauthor=False)` defaults, including Linux XDG
overrides and non-roaming Windows directories. This lightweight Node entry point
can resolve paths before loading a catalog. The chat app stores its state under
`data/chat` and shares the catalog cache root.

`artifactPath(catalog, path, { signal? })` streams a missing artifact to disk and
returns a verified local path for native DuckDB, Arrow, or other file readers.
It verifies an existing file before reuse. Each artifact is capped at 1 GiB,
and core files at 64 MiB.

Opening `catalog.json` refreshes the selection. A digest-addressed
`release.json` URL can reopen offline after its descriptor and core files have
been cached. Optional files become available offline after they are requested.

Use the browser entry point in browser applications. Node filesystem imports
are confined to `@chartcoach/catalog/node`.

## Open a native search index

Install [LanceDB](https://lancedb.github.io/lancedb/js/), the application's
vector and full-text database client:

```bash
npm install @lancedb/lancedb
```

Open a release built with an index profile. This example uses `./dist/release`:

```ts
import { connect } from "@lancedb/lancedb";
import { openCatalog, indexPath } from "@chartcoach/catalog/node";

const catalog = await openCatalog("./dist/release");
const [profile] = (await catalog.describe()).profiles;
if (!profile) throw new Error("Choose a catalog release with an index profile.");

const db = await connect(await indexPath(catalog, profile));
const table = await db.openTable("documents");
try {
  await table.checkout(await table.version());
  const matches = await table.query().fullTextSearch("direct labels").limit(5).toArray();
  const ids = [...new Set(matches.map((row) => row.parent_id))];
  console.log(catalog.read({ ids }));
} finally {
  table.close();
  db.close();
}
```

`indexPath(catalog, profile, { directory?, signal? })` verifies the profile and
archive, then returns an extracted database directory containing `documents.lance`.
The default extraction is a read-only generation in the catalog's cache directory
on POSIX systems. Repeated calls reuse a completed generation. Pin the native
table with `checkout` before querying shared cached data.

Pass a new `directory` for a writable, caller-owned extraction. This option is
required on Windows. Existing directories are rejected. The caller owns cleanup.
Extraction rejects unsafe paths, links, colliding names, and oversized archives.
Cancellation rejects the operation and cleans its incomplete extraction.

Use `table.vectorSearch(vector)` for application-supplied query embeddings and
`table.query().fullTextSearch(text)` for provider-free search. String-based
embedding search requires the application to configure a compatible LanceDB
embedding function. A stored Python embedding binding is not a JavaScript
provider registration.

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
