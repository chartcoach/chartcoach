# Releases and catalog data

Software packages and catalog data use separate release identities. PyPI and
npm packages use semantic versions. A catalog release uses the digest of its
artifact envelope.

## Software packages

`packages/chartcoach` publishes `chartcoach` to PyPI.
`packages/catalog` publishes `@chartcoach/catalog` to npm. A package
tag must match both package versions:

```sh
./scripts/release.sh check-version "$RELEASE_TAG"
```

Pull requests and main-branch pushes run the complete workspace gates in CI.
Pushing a matching `X.Y.Z` or `vX.Y.Z` tag starts the publish workflow, which
requires successful main-branch CI for the tagged commit, checks both package
versions, builds the Python and npm artifacts, and publishes them through
trusted publishing.

## Catalog forms

The catalog moves through three file contracts:

```text
authored folder       MANIFEST.md + entries/<id>/guideline.md
compiled bundle       MANIFEST.md + entries.parquet
immutable release     release.json + bundle + profile artifacts
```

The package version that builds or reads a release is separate from the release
digest.

## Release layout

```text
catalog/releases/<digest>/
├── release.json
├── MANIFEST.md
├── entries.parquet
└── profiles/
    └── <profile>/
        ├── documents.parquet
        └── index.tar.gz
```

`release.json` maps each artifact path to its SHA-256 digest and byte count. Its
release digest covers the schema version and complete artifact map.

Each embedding profile represents one vector space. `documents.parquet`
contains document metadata, vectors, UMAP coordinates, and nearest neighbors.
`index.tar.gz` contains one native LanceDB table named `documents`.

## Catalog lifecycle

Build and validate a release locally:

```sh
chartcoach catalog release validate dist/release
```

Publish its immutable objects:

```sh
chartcoach catalog release publish dist/release --store s3://chartcoach
```

Publication can happen before public selection. The exact release URL can be
verified and used for a site build before selection:

```sh
RELEASE_URL="https://artifacts.chartcoach.dev/catalog/releases/$RELEASE_DIGEST/release.json"
chartcoach catalog overview --source "$RELEASE_URL"
CHARTCOACH_SITE_CATALOG_SOURCE="$RELEASE_URL" pnpm --dir apps/site build
```

Select the verified release:

```sh
chartcoach catalog release select "$RELEASE_DIGEST" --store s3://chartcoach
```

The public catalog has one mutable selection record at `catalog.json`.
`catalog/releases/<digest>/` remains immutable. Curation owns selection writes.
Runtime readers fetch the selected record on each open and reuse verified
immutable artifacts through their content digests.

Package tags run `.github/workflows/publish.yml`. Catalog publication and
selection use the curation commands. A catalog update keeps both package
versions unchanged.

## Change boundaries

- A catalog row change updates both readers and the shared release fixture.
- A release envelope change updates Python and JavaScript validation together.
- A profile artifact change updates curation build, validation, runtime index
  loading, and analysis consumers together.
- A package release changes package versions and the package tag. Catalog
  publication changes the selected digest.
