# @chartcoach/catalog

`@chartcoach/catalog` loads compiled Guideline Catalog bundles and verified
published releases into a typed `Catalog`.

```bash
npm install @chartcoach/catalog
```

## Open the selected catalog

`open(options?)` reads `catalog.json`, verifies its release record, and loads
the manifest and entries from the immutable release directory.

```ts
import { open } from "@chartcoach/catalog";

const catalog = await open();
const guideline = catalog.require("compare-percentages-with-bars-not-pies");
```

Pass a Fetch-compatible function when the runtime needs one:

```ts
const catalog = await open({ fetch });
```

## Open one release

`openRelease(source, options?)` loads the release named by an absolute
`release.json` URL.

```ts
import { openRelease } from "@chartcoach/catalog";

const catalog = await openRelease(
  "https://artifacts.chartcoach.dev/catalog/releases/<digest>/release.json",
  { fetch },
);
```

The URL digest, release digest, artifact byte count, and artifact SHA-256 must
agree before the catalog is decoded.

## Load a local bundle

`loadCatalog({ entries, manifestText })` accepts `entries.parquet` bytes and
the matching `MANIFEST.md` text.

```ts
import { readFile } from "node:fs/promises";
import { loadCatalog } from "@chartcoach/catalog";

const catalog = await loadCatalog({
  entries: await readFile("dist/catalog/entries.parquet"),
  manifestText: await readFile("dist/catalog/MANIFEST.md", "utf8"),
});
```

Each compiled row has this shape:

```ts
type GuidelineRow = {
  id: string;
  title: string;
  description: string;
  labels: string[];
  sections: Array<{ role: string; title: string; content: string }>;
  references: string[];
};
```

`Catalog` derives `guideline.body` from the ordered sections.

## Inspect a release record

Schema 1 uses artifact paths as keys.

```ts
type CatalogRelease = {
  schema_version: 1;
  digest: string;
  artifacts: Record<string, { sha256: string; bytes: number }>;
};
```

The required core paths are `MANIFEST.md` and `entries.parquet`. Each embedding
profile adds:

- `profiles/<profile>/documents.parquet`
- `profiles/<profile>/index.tar.gz`

Use `parseCatalogRelease` when an application needs to inspect a record before
opening it.

```ts
import { parseCatalogRelease } from "@chartcoach/catalog";

const release = parseCatalogRelease(await response.json());
const entries = release.artifacts["entries.parquet"];
```

The package also exports `Catalog`, `Guideline`, `GuidelineSection`,
`CatalogRelease`, `ReleaseArtifact`, `FetchLike`, `OpenCatalogOptions`, and
`OpenReleaseOptions`.

## Check the package

```bash
pnpm --dir packages/catalog typecheck
pnpm --dir packages/catalog test
pnpm --dir packages/catalog build
```

Run `pnpm ready` for the complete JavaScript workspace gate.

## License

Apache-2.0. See [LICENSE](../../LICENSE).
