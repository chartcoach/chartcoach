# Releasing packages and catalog data

Python and JavaScript packages use version tags such as `v0.2.0`. Catalog data
uses a SHA-256 digest computed from the files in one release. Either can change
without changing the other.

## Publish the packages

`packages/chartcoach` publishes `chartcoach` to PyPI.
`packages/catalog` publishes `@chartcoach/catalog` to npm. Both manifests must
contain the same version.

Set the proposed tag and compare it with both manifests:

```bash
RELEASE_TAG="v0.2.0"
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

`./catalog-source` in the build command is a caller-provided authored catalog.
The commands also require `jq`. Both `dist/catalog` and `dist/release` must be
absent before the build begins.

Build the compiled catalog, then build a local release:

```bash
uv run --locked --package chartcoach --extra curation \
  chartcoach catalog build \
  --source ./catalog-source \
  --out ./dist/catalog
```

```bash
uv run --locked --package chartcoach --extra curation python - <<'PY'
from pathlib import Path

from chartcoach import open_catalog
from chartcoach.catalog.curation import build_release

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

Set the remote store and the HTTPS base URL that serves the same files:

```bash
CATALOG_STORE="s3://your-bucket/chartcoach"
PUBLIC_BASE="https://catalog.example.com/chartcoach"
```

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

Publication uploads the listed files and writes `release.json` last. Verify
the required files through their public URL and build the site against that
exact release:

```bash
RELEASE_URL="$PUBLIC_BASE/catalog/releases/$RELEASE_DIGEST/release.json"
uv run --locked --package chartcoach \
  chartcoach catalog overview --source "$RELEASE_URL"
CHARTCOACH_SITE_CATALOG_SOURCE="$RELEASE_URL" pnpm --dir apps/site build
```

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

The final command changes the release read from `$PUBLIC_BASE/catalog.json`.
The files under the digest path remain unchanged. Confirm the selection
through the public URL:

```bash
uv run --locked --package chartcoach \
  chartcoach catalog overview --source "$PUBLIC_BASE/catalog.json"
```

Calls and commands that omit `source` continue to read the official
`files.peter.gy` catalog selection.
