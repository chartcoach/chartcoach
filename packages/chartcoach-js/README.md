# `@chartcoach/catalog`

TypeScript/Node.js utilities to load and parse the Chartcoach guideline catalog:

- From the filesystem folder structure (`guidelines/*/guideline.md` + optional `references.bib`)
- From a Parquet file (using the vendored `nogit/ctxt/hyparquet`)

## Usage

```ts
import { loadCatalogFromParquet } from "@chartcoach/catalog";
import { loadCatalogFromFolder, loadCatalogFromParquetFile } from "@chartcoach/catalog/node";
import {
  loadCatalogFromParquetBytes,
  loadCatalogFromParquetUrl,
} from "@chartcoach/catalog/browser";

// Environment-agnostic: provide an ArrayBuffer or AsyncBuffer
const catalog = await loadCatalogFromParquet(arrayBuffer);

// Node.js
const fromFolder = await loadCatalogFromFolder("../../guidelines");
const fromParquetFile = await loadCatalogFromParquetFile("../../guidelines/catalog.parquet");

// Browser
const fromParquetUrl = await loadCatalogFromParquetUrl("https://example.com/catalog.parquet");

// Browser (bytes)
const bytes = await (await fetch("https://example.com/catalog.parquet")).arrayBuffer();
const fromParquetBytes = await loadCatalogFromParquetBytes(bytes);
```
