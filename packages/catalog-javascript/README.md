# @chartcoach/catalog

JavaScript package for loading manifest-described ChartCoach guideline catalogs as typed records.

```ts
import { readCatalog } from "@chartcoach/catalog/server";

const catalog = await readCatalog();
catalog.guidelines.map((guideline) => guideline.title);
```

Use `@chartcoach/catalog/server` to read the default artifact metadata URL, explicit metadata URLs, catalog bundles, source folders, or parquet files from server runtimes.
Use `@chartcoach/catalog/browser` with resolved artifact URLs from release metadata:

```ts
import { artifact, artifactUrl, fetchCatalogRelease } from "@chartcoach/catalog";
import { fetchCatalog } from "@chartcoach/catalog/browser";

const release = await fetchCatalogRelease();
const entries = artifactUrl(release.metadataUrl, artifact(release.metadata, "entries"));
const manifest = artifactUrl(release.metadataUrl, artifact(release.metadata, "manifest"));

const catalog = await fetchCatalog(entries, { manifest });
```

Build this package with `pnpm --dir packages/catalog-javascript build`.

## License

Apache-2.0. See [LICENSE](../../LICENSE).
