import { loadCatalog, openCatalog, parseCatalogRelease, type Catalog } from "@chartcoach/catalog";
import type { IndexPathOptions, NodeOpenCatalogOptions } from "@chartcoach/catalog/node";

// Type-only Node imports verify declarations while keeping the browser graph separate.
const options: NodeOpenCatalogOptions & IndexPathOptions = { cacheDirectory: "cache" };

void options;

function check(catalog: Catalog): void {
  if (!catalog.length) throw new Error("Expected guideline entries");
  const candidates = catalog.query({ limit: catalog.length });
  const ids = candidates.map(({ id }) => id);

  if (catalog.read({ ids }).length !== ids.length) throw new Error("Guideline reads failed");
  const citations = catalog.cite({ ids });

  if (catalog.table("guidelines").length !== catalog.length)
    throw new Error("Canonical guideline table failed");

  if (!catalog.table("references")[0]?.bibtex) throw new Error("Reference table failed");

  if (!catalog.table("guideline_references").length) throw new Error("Reference links failed");

  if (!citations.some(({ sources }) => sources.some(({ citation }) => citation.length > 0)))
    throw new Error("Source citation formatting failed");
}

const location = new URL("/catalog/release.json", window.location.href);

const catalog = await openCatalog(location);

check(catalog);

const info = await catalog.describe();

if (info.tables.length !== 6) throw new Error("Catalog table description failed");

if (info.release_digest !== catalog.release?.digest) throw new Error("Release identity mismatch");

const release = parseCatalogRelease(await (await fetch(location)).json());

const loaded = await loadCatalog({
  release,
  releaseUrl: location,
  entries: await (await fetch(new URL("entries.parquet", location))).arrayBuffer(),
  manifest: await (await fetch(new URL("MANIFEST.md", location))).arrayBuffer(),
});

check(loaded);

document.body.textContent = "Verified browser catalog loading, reads, citations and identity";

document.body.dataset.verified = "true";
