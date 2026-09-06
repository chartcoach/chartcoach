# @chartcoach/catalog

`@chartcoach/catalog` fetches a selected or exact Guideline Catalog release,
verifies its required files, and returns a `Catalog` of guideline records.

chartcoach is alpha software. `openCatalog` requires a browser or server
runtime with `fetch`, Web Crypto, `AbortSignal.timeout`, and `AbortSignal.any`.
`loadCatalog` parses files that the application already holds.

## Read one guideline

```bash
npm install @chartcoach/catalog@0.2.0
```

```ts
import { openCatalog } from "@chartcoach/catalog";

const catalog = await openCatalog(
  "https://files.peter.gy/packages/python/chartcoach/0.2.0/docs-catalog/c0f6dbec3dd31b07763b46fd458733db0b8b50c5793cf9447458119287129420/release.json",
);
const guideline = catalog.require("directly-label-series-instead-of-using-a-color-key");

console.log(guideline.title);
```

Expected output:

```text
Directly label colored series instead of relying on a color key
```

## Choose a release URL

`openCatalog(source, { fetch })` accepts an absolute HTTP or HTTPS URL:

| Source         | Behavior                                      |
| -------------- | --------------------------------------------- |
| `catalog.json` | Follows the currently selected public release |
| `release.json` | Keeps one release digest across calls         |
| Omitted        | Opens the official selected catalog           |

The loader verifies the release digest, then checks the byte count and SHA-256
hash of `MANIFEST.md` and `entries.parquet` before parsing them. Pass a custom
`fetch` implementation when the runtime does not use `globalThis.fetch`.

## Load files your app already has

`loadCatalog` accepts Parquet bytes and manifest text:

```ts
import { readFile } from "node:fs/promises";
import { loadCatalog } from "@chartcoach/catalog";

const catalog = await loadCatalog({
  entries: await readFile("dist/catalog/entries.parquet"),
  manifestText: await readFile("dist/catalog/MANIFEST.md", "utf8"),
});
```

`loadCatalog` validates the manifest vocabulary and guideline fields. It
cannot verify a release digest or file hashes because it receives no
`release.json`. Verify the two files before this call when release integrity is
required.

## Catalog methods

- `catalog.guidelines` and iteration enumerate guideline records.
- `catalog.length` returns the number of records.
- `catalog.get(id)` returns a guideline or `undefined`.
- `catalog.require(id)` returns a guideline or throws `CatalogError`.
- `catalog.labels()` returns the sorted labels in the catalog.
- `catalog.sectionRoles()` returns the sorted section roles.
- `toMarkdown(guideline)` serializes one guideline to Markdown.

| Page                                                 | Details                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| [JavaScript](https://docs.chartcoach.dev/javascript) | Release loading, catalog methods, and Markdown serialization |
| [Catalog data](https://docs.chartcoach.dev/catalog)  | Guideline fields and published file layouts                  |

Licensed under Apache-2.0.
