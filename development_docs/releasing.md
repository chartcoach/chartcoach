# Releasing packages and catalog data

Python and JavaScript packages use matching version tags. Catalog data
uses a SHA-256 digest computed from the files in one release. Either can change
without changing the other.

| Lifecycle                | Identity                                  |
| ------------------------ | ----------------------------------------- |
| Guideline entries        | Entries digest plus manifest digest       |
| Compiled catalog release | SHA-256 digest over its artifact envelope |
| Python and npm software  | Coordinated package version               |

Public selection points `catalog.json` at an already published release. Site
deployment consumes an exact release and does not create catalog identity.

## Publish the packages

`packages/chartcoach` publishes `chartcoach` to PyPI.
`packages/catalog` publishes `@chartcoach/catalog` to npm. Both manifests must
contain the same version.

Set the proposed tag and compare it with both manifests:

```bash
./scripts/release.sh check-version "$RELEASE_TAG"
```

Run the repository checks before creating the tag:

```bash
make check
```

A matching `X.Y.Z` or `vX.Y.Z` tag starts
`.github/workflows/publish.yml`. The workflow requires an existing successful
main CI run for that commit, builds both packages, publishes them through
trusted publishing, and updates the GitHub release notes.

When package contents change, inspect the wheel, source distribution, and npm
tarball through their published entry points before announcing the release.

## Publish catalog data

The catalog passes through three local states before publication:

```text
authored Markdown
  -> dist/catalog/ with MANIFEST.md and entries.parquet
  -> dist/release/ with release.json and the listed files
  -> remote catalog/releases/<digest>/
```

`./authored-catalog` in the build command is a caller-provided authored catalog.
The commands also require `jq`. Both `dist/catalog` and `dist/release` must be
absent before the build begins.

Build the compiled catalog, then build a local release:

```bash
uv run --locked --package chartcoach --extra curation \
  chartcoach catalog build \
  --source ./authored-catalog \
  --out ./dist/catalog
```

```bash
uv run --locked --package chartcoach --extra curation python - <<'PY'
from pathlib import Path

from chartcoach import open_catalog
from chartcoach.curation import build_release

release = build_release(
    open_catalog("dist/catalog"),
    Path("dist/release"),
)
print(release.digest)
PY
```

Validate the release and capture its digest:

```bash
RELEASE_DIGEST="$(
  uv run --locked --package chartcoach --extra curation \
    chartcoach catalog release validate dist/release --format json |
    jq -r '.digest'
)"
```

Set `CATALOG_STORE` to the destination object-store URI and `PUBLIC_BASE` to
the HTTPS base URL serving the same files.

Configure the serving layer before promotion:

| Resource                        | Serving contract                                              |
| ------------------------------- | ------------------------------------------------------------- |
| `catalog/releases/<digest>/...` | Immutable caching and stable retention                        |
| `catalog.json`                  | Revalidation-friendly caching and an ETag where available     |
| Browser-readable artifacts      | Cross-origin `GET` and `HEAD` access from the product origins |

Discovery reads descriptors rather than listing storage prefixes. Release
artifacts stay relative to their release directory and contain no deployment
paths or credentials.

Preview the remote paths, then publish the release:

```bash
uv run --locked --package chartcoach --extra curation \
  chartcoach catalog release publish dist/release \
  --store "$CATALOG_STORE" \
  --dry-run

uv run --locked --package chartcoach --extra curation \
  chartcoach catalog release publish dist/release \
  --store "$CATALOG_STORE"
```

Publication uploads the listed files and writes `release.json` last. Repeating
publication verifies the committed objects before returning success.

Validate the candidate from fresh object-store bytes:

```bash
uv run --locked --package chartcoach --extra curation \
  chartcoach catalog release validate \
  --store "$CATALOG_STORE" \
  --digest "$RELEASE_DIGEST"
```

Published validation downloads every listed artifact into temporary files. It
checks hashes, catalog records, document derivation, stored vectors, native
indexes, and exports. Embedding providers and their credentials are not needed
for these checks.

Verify the reader endpoint and build the site against that exact release:

```bash
RELEASE_URL="$PUBLIC_BASE/catalog/releases/$RELEASE_DIGEST/release.json"
uv run --locked --package chartcoach \
  chartcoach catalog describe --source "$RELEASE_URL"
CHARTCOACH_SITE_CATALOG="$RELEASE_URL" pnpm --dir apps/site build
```

For every profile listed by `catalog describe`, inspect its metadata and run
provider-free FTS through the public release before selection:

```bash
PROFILE="minilm-normalized"
uv run --locked --package chartcoach --extra index \
  chartcoach catalog describe \
  --source "$RELEASE_URL" \
  --profile "$PROFILE"
uv run --locked --package chartcoach --extra index \
  chartcoach catalog search \
  --source "$RELEASE_URL" \
  --profile "$PROFILE" \
  --mode fts \
  "direct labels"
```

Provider-backed vector or hybrid smoke checks are explicit release actions.
Run them with the declared Python requirements and authorized credentials.

Preview the public selection, then update `catalog.json`:

```bash
uv run --locked --package chartcoach --extra curation \
  chartcoach catalog release select "$RELEASE_DIGEST" \
  --store "$CATALOG_STORE" \
  --dry-run

uv run --locked --package chartcoach --extra curation \
  chartcoach catalog release select "$RELEASE_DIGEST" \
  --store "$CATALOG_STORE"
```

Selection validates the candidate's fresh published bytes before writing
`catalog.json`. Its dry run performs the same validation. The files under the
digest path remain unchanged.

Confirm that the stored selection matches the intended digest and its
published descriptor, then check the public reader endpoint:

```bash
uv run --locked --package chartcoach --extra curation \
  chartcoach catalog release validate \
  --store "$CATALOG_STORE" \
  --expect-digest "$RELEASE_DIGEST"

uv run --locked --package chartcoach \
  chartcoach catalog describe --source "$PUBLIC_BASE/catalog.json"
```

Python calls that omit `location` and commands that omit `--source` read the
official catalog selection.
