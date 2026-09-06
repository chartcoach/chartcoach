# @chartcoach/catalog

`@chartcoach/catalog` loads verified Guideline Catalog releases in browser and
server runtimes.

```bash
npm install @chartcoach/catalog
```

## Open a catalog

`openCatalog(source?, options?)` accepts an absolute HTTP or HTTPS URL ending
in `catalog.json` or `release.json`. The default is the official selected
catalog.

```ts
import { openCatalog } from "@chartcoach/catalog";

const selected = await openCatalog();
const exact = await openCatalog(
  "https://artifacts.chartcoach.dev/catalog/releases/<digest>/release.json",
);

const guideline = selected.require("compare-percentages-with-bars-not-pies");
```

Pass a Fetch-compatible function when the runtime supplies its own transport:

```ts
const catalog = await openCatalog(source, { fetch });
```

The loader verifies the release digest, artifact byte counts, and artifact
SHA-256 values before decoding the catalog.

## Load caller-provided bytes

`loadCatalog({ entries, manifestText })` constructs a catalog from compiled
bundle data:

```ts
import { readFile } from "node:fs/promises";
import { loadCatalog } from "@chartcoach/catalog";

const catalog = await loadCatalog({
  entries: await readFile("dist/catalog/entries.parquet"),
  manifestText: await readFile("dist/catalog/MANIFEST.md", "utf8"),
});
```

Each row contains `id`, `title`, `description`, `labels`, `sections`, and
`references`. `Catalog` derives each guideline Markdown body from its ordered
sections.

## Release records

Schema 1 uses artifact paths as keys:

```ts
type CatalogRelease = {
  schema_version: 1;
  digest: string;
  artifacts: Record<string, { sha256: string; bytes: number }>;
};
```

`parseCatalogRelease(value)` accepts a `JsonValue` and returns a validated
`CatalogRelease`:

```ts
import { parseCatalogRelease, type JsonValue } from "@chartcoach/catalog";

const value: JsonValue = JSON.parse(text);
const release = parseCatalogRelease(value);
```

The function throws `CatalogError` when the record has an unsupported shape,
an invalid artifact descriptor, or a missing core path. The required core paths
are `MANIFEST.md` and `entries.parquet`.

The package exports `Catalog`, `CatalogError`, `CatalogRelease`, `FetchLike`,
`Guideline`, `GuidelineSection`, `JsonObject`, `JsonValue`, `OpenCatalogOptions`,
`ReleaseArtifact`, `loadCatalog`, `openCatalog`, `parseCatalogRelease`, and
`toMarkdown`.

## Check the package

```bash
pnpm --dir packages/catalog check
pnpm --dir packages/catalog typecheck
pnpm --dir packages/catalog test
pnpm --dir packages/catalog build
```

Run `pnpm ready` for the complete JavaScript workspace gate.

## License

Apache-2.0. See [LICENSE](../../LICENSE).
