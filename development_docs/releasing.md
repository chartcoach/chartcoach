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

Set `RELEASE_TAG` to the proposed stable version and check both package identities
and versions:

```bash
./scripts/release.sh check-version "$RELEASE_TAG"
```

A matching `X.Y.Z` or `vX.Y.Z` tag starts `.github/workflows/publish.yml`.
Merge the release commit and wait for its successful main CI run before pushing
the tag. Main CI builds and verifies the distributions, then retains them as
`python-package` and `npm-package` artifacts for 30 days. For local checks before
pushing the version change, run `make check`.

CI verifies the wheel in an isolated environment and the npm tarball through
Node.js, TypeScript, Chromium, DuckDB, and LanceDB consumers. The minimum Node.js
version comes from the SDK's `engines.node`. Minimum direct dependency checks
also run in CI. Package versions come from their manifests and built artifacts.

Publishing downloads the artifacts from the successful main CI run for the exact
tagged commit. It checks that both packages match the tag and rejects conflicting
registry bytes. The publisher jobs reuse this retained `release-packages` bundle.
A final job verifies registry metadata and downloadable bytes before creating
the GitHub release notes. Publication does not rebuild or rerun consumer tests.

### Registry setup

[PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/) and
[npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) exchange
GitHub Actions identity tokens for short-lived publication credentials.
Configure each package's publisher for this repository and `publish.yml`.
The workflow's publishing jobs request `id-token: write` and use no GitHub
environment. If environment protection is required, configure the same
environment in the workflow and both registry publishers.

Confirm publisher settings before tagging. npm generates provenance for public
repositories. Repository visibility and trusted-publisher authorization are
separate settings.

### Recover a partial publication

PyPI and npm publish independently. If a job fails, rerun the failed jobs from
the same workflow run so they reuse the retained `release-packages` artifact.
The artifact is retained for 30 days. Keep the original tag and build intact.

The npm job skips a version whose registry integrity matches the verified
tarball. A different digest fails publication. uv accepts identical Python
files that have already been uploaded. Registry verification and release notes
resume after both publishers succeed. Verification retries pending registry
files and transient network failures for up to two minutes, five seconds apart.
Missing download URLs are treated as propagation delays. Digest conflicts and
authorization errors fail immediately. Local checks can set `--wait-seconds 0`
to return immediately.

If preparation fails before publication and a workflow correction is needed, merge
the correction and wait for main CI. Then dispatch the corrected workflow for
the existing tag:

```bash
gh workflow run publish.yml --ref main -f tag="$RELEASE_TAG"
```

The workflow resolves the tag to its successful main CI run and promotes that
run's packages. Its tooling comes from the workflow revision, so workflow fixes
can recover publication while the release tag and package bytes stay unchanged.
For partial publication, rerun the original failed jobs. They retain the original
workflow revision and artifact bundle.

To inspect retained artifacts locally:

```bash
gh run download "$RUN_ID" --name release-packages --dir ./release-packages
python3 scripts/release_registry.py check ./release-packages --allow-missing
```

`--allow-missing` permits files awaiting publication while rejecting digest
conflicts. Run the command without that flag to require every published file
and verify its downloaded bytes. If an artifact has expired or a digest differs,
stop and recover the original build before attempting another upload.

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
