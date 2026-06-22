# @chartcoach/catalog

JavaScript models and parsers for chartcoach catalog artifacts.

Read the package docs at [docs.chartcoach.dev/javascript](https://docs.chartcoach.dev/javascript).
Read the catalog contract at [docs.chartcoach.dev/catalog](https://docs.chartcoach.dev/catalog).

Install the package from an application root:

```bash
npm install @chartcoach/catalog
```

```ts
import { DEFAULT_CATALOG, loadCatalog } from "@chartcoach/catalog"

const entries = await fetch(DEFAULT_CATALOG.entriesUrl).then((response) =>
  response.arrayBuffer(),
)
const manifestText = await fetch(DEFAULT_CATALOG.manifestUrl).then((response) =>
  response.text(),
)

const catalog = await loadCatalog({ entries, manifestText })
const guideline = catalog.require("compare-percentages-with-bars-not-pies")
```

`@chartcoach/catalog` accepts bytes that the caller already acquired. Use
`fetch`, `fs.readFile`, `Bun.file`, `Deno.readFile`, or a test fixture to read
the artifacts, then pass `entries` and optional manifest data to `loadCatalog`.

```ts
import { readFile } from "node:fs/promises"
import { loadCatalog } from "@chartcoach/catalog"

const catalog = await loadCatalog({
  entries: await readFile("entries.parquet"),
  manifestText: await readFile("MANIFEST.md", "utf8"),
})
```

Parse release metadata when code needs artifact URLs:

```ts
import {
  catalogArtifact,
  catalogArtifactUrl,
  parseCatalogReleaseMetadata,
} from "@chartcoach/catalog"

const metadata = parseCatalogReleaseMetadata(await response.json())
const entriesUrl = catalogArtifactUrl(
  metadataUrl,
  catalogArtifact(metadata, "entries"),
)

const entries = await fetch(entriesUrl).then((response) => response.arrayBuffer())
```

Run package checks from the repository root:

```bash
pnpm --dir packages/catalog-javascript lint
pnpm --dir packages/catalog-javascript typecheck
pnpm --dir packages/catalog-javascript test
pnpm --dir packages/catalog-javascript build
```

## License

Apache-2.0. See [LICENSE](../../LICENSE).
