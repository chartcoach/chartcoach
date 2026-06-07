# @chartcoach/catalog

JavaScript package for loading manifest-described ChartCoach guideline catalogs as typed records.

```ts
import { readCatalog } from "@chartcoach/catalog/server";

const catalog = await readCatalog("guidelines");
catalog.guidelines.map((guideline) => guideline.title);
```

Use `@chartcoach/catalog/server` to read catalog bundles, source folders, or parquet files from server runtimes with filesystem support.
Use `@chartcoach/catalog/browser` to fetch parquet files by URL.

Build this package with `pnpm --dir packages/catalog-javascript build`.

## License

MIT. See [LICENSE](../../LICENSE).
