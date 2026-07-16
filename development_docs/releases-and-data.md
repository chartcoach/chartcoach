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

## Publication

Validate and publish the immutable release before updating the public
selection:

```sh
chartcoach catalog release validate dist/release
chartcoach catalog release publish dist/release --store s3://chartcoach
chartcoach catalog release select "$RELEASE_DIGEST" --store s3://chartcoach
```

Publication writes through Obspec operations. Obstore provides the concrete
local and S3-compatible stores. The public catalog has one mutable selection
record at `catalog.json`. It contains the selected release record, while
`catalog/releases/<digest>/` remains immutable.

`chartcoach.paths` constructs the object keys used by local stores, S3 stores,
cache code, and release readers.

## Change boundaries

- A catalog row change updates both readers and the shared release fixture.
- A release envelope change updates Python and JavaScript validation together.
- A profile artifact change updates curation build, validation, cache, and
  analysis consumers together.
- A package release changes package versions and the package tag. Catalog
  publication changes the selected digest.
