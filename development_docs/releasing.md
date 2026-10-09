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
`packages/catalog` publishes `@chartcoach/catalog` to npm. `apps/chat` assembles the
`chartcoach` npm application in `apps/chat/dist`. All three software manifests must
contain the same version.

Set `RELEASE_TAG` to the proposed stable version and check all package identities
and versions:

```bash
./scripts/release.sh check-version "$RELEASE_TAG"
```

A matching `X.Y.Z` or `vX.Y.Z` tag starts `.github/workflows/publish.yml`.
Merge the release commit and wait for its successful main CI run before pushing
the tag. Main CI builds and verifies the distributions, then retains them as
`python-package` and `npm-package` artifacts for 30 days. For local checks before
pushing the version change, run `make check`.

Pull requests select Python checks and JavaScript packages through
`.github/filters.yml`. Shared catalog fixtures select both language contracts.
The JavaScript workspace builds the npm tarballs once, then Node.js, Bun, and
Deno consumer jobs verify those same artifacts in parallel. Package jobs run
typed linting after their generated types are ready. Formatting, repository
linting, architecture, unused-code checks, and lint-rule tests run in a separate
quality job. The `CI gate` requires each selected job to succeed and accepts skipped
jobs when their inputs are unchanged.

Main CI runs every check and retains a complete artifact set for the exact
commit that a release tag will identify. Main runs finish independently while
new pushes replace earlier checks on the same pull request.
[Vite Task caching](https://viteplus.dev/guide/github-actions-cache) restores
task results after dependency installation. Successful main jobs save separate
quality and workspace caches. Vite Task fingerprints determine which results
can be replayed. uv caches the locked Python dependencies, including the minimum
dependency job. Container publication caches BuildKit layers through GitHub Actions.

CI verifies the wheel in an isolated environment and the npm tarball through
Node.js, TypeScript, Chromium, DuckDB, and LanceDB consumers. The minimum Node.js
version comes from the SDK's `engines.node`. Minimum direct dependency checks
also run in CI. The chat consumer installs with lifecycle scripts disabled and verifies
the packed CLI against both the shared fixture and a pinned full catalog release.
The same consumer check runs through `bunx`, native Bun, and native Deno against
the shared fixture. Use `verify:chat --runner npx|bunx|bun|deno` to select a runner
when checking local tarballs.
It exercises browser catalog loading and retry, author/year/source filters,
pagination, empty-scope recovery, chart and draft preservation, grounded chat,
local citations, mobile layout, and restart persistence. All consumer jobs must
succeed before packages become eligible for publication. Package versions come
from their manifests and built artifacts.

Publishing downloads the artifacts from the successful main CI run for the exact
tagged commit. It checks that all packages match the tag and rejects conflicting
registry bytes. The publisher jobs reuse this retained `release-packages` bundle.
A final job verifies registry metadata and downloadable bytes before publishing the versioned `ghcr.io/chartcoach/chartcoach` container image and
creating the GitHub release notes. Container builds consume the retained npm
artifacts through `infra/Dockerfile`'s `packages` build context for Linux amd64 and arm64. A separate job pulls the public image from GHCR without registry credentials and checks native dependencies, health, and authenticated UI/API access before creating release notes. Retrying that check does not rebuild the image. Publication does not rebuild or rerun consumer tests.

### Registry setup

[PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/) and
[npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) exchange
GitHub Actions identity tokens for short-lived publication credentials.
Configure each package's publisher for this repository and `publish.yml`.
The publishing jobs request `id-token: write`. Python publishing uses the GitHub
environment `pypi`; both npm packages publish through `npm`. Configure the matching
environment name in each registry's trusted publisher. Any environment protection
rules must permit the release tag.

After the first container push, set the GHCR package visibility to **Public**.
The container verification job deliberately pulls without registry credentials.

Confirm publisher settings before tagging. npm generates provenance for public
repositories. Repository visibility and trusted-publisher authorization are
separate settings.

### Recover a partial publication

PyPI and npm publish independently. If a job fails, rerun the failed jobs from
the same workflow run so they reuse the retained `release-packages` artifact.
The artifact is retained for 30 days. Keep the original tag and build intact.

The npm job publishes the catalog SDK before the chat application and checks each
package independently. It skips a version whose registry integrity matches the verified
tarball. A different digest fails publication. uv accepts identical Python
files that have already been uploaded. Registry verification and release notes
resume after all packages publish successfully. Verification retries pending registry
files and transient network failures for up to ten minutes, five seconds apart,
including packages npm has accepted but is still processing. Missing download
URLs are treated as propagation delays. Digest conflicts and authorization errors
fail immediately. Local checks default to two minutes and can set
`--wait-seconds 0` to return immediately.

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

## Rolling previews

After the latest push-event `CI` workflow succeeds for an exact `main` commit,
`publish.yml` builds matching Python, catalog SDK, and chat previews on the rolling
[`previews` GitHub prerelease](https://github.com/chartcoach/chartcoach/releases/tag/previews).
PR runs, forks, failed runs, and cancelled runs cannot publish. CI already builds
and checks the site and docs, so chartcoach requires only that workflow. Stable
registry publication and container publication continue to use retained main CI
artifacts for a matching release tag.

The highest reachable stable `X.Y.Z` or `vX.Y.Z` tag preceding the source commit
supplies the base. The next patch version and commit count since that tag produce
Python `X.Y.(Z+1).devN` and npm `X.Y.(Z+1)-dev.N`. Suffixed and unrelated tags are
excluded. Tagging the source commit later cannot change its preview identity.
Full Git history and release tags are required to resolve a version.

Only the build checkout is stamped. The Python lockfile is refreshed for that
version; source versions and repository lockfiles stay on the stable development
version. Python wheel/source verification and isolated CLI/MCP checks run on the
stamped build. The catalog SDK and chat tarballs pass Node.js, Bun, and Deno
consumer checks before attestation and upload. Preview chat packages depend on
the exact matching SDK tarball URL, so installing chat alone resolves its SDK.

Merged-PR announcements include exact URLs for:

```bash
uv pip install "chartcoach @ https://github.com/chartcoach/chartcoach/releases/download/previews/chartcoach-X.Y.Z.devN-py3-none-any.whl"
pnpm add "https://github.com/chartcoach/chartcoach/releases/download/previews/chartcoach-catalog-X.Y.Z-dev.N.tgz"
npx --yes https://github.com/chartcoach/chartcoach/releases/download/previews/chartcoach-X.Y.Z-dev.N.tgz
```

Replace the example versions with those in the merged-PR announcement or a
retained checksum asset's filename. For the Python CLI,
use `uv tool install --force "chartcoach @ <wheel-url>"`. To run the MCP server,
install `chartcoach[mcp] @ <wheel-url>`. These previews are distributed through
GitHub rather than PyPI or npm. Use the registries for stable versions.

Uploads are immutable: retries compare existing bytes and reject conflicts.
Empty starter assets left by failed uploads are removed before retrying. A
versioned `chartcoach-X.Y.Z.devN-SHA256SUMS` completion marker is uploaded last,
after a deduplicated merged-PR announcement and retention.
Publication jobs serialize asset mutations of the shared release. Release notes
stay static; each announcement records its build's commit, installation commands,
and provenance status. Select a completed version from the versioned checksum
assets. The newest 30 completed publications remain;
older complete or interrupted builds are pruned as whole sets. Older builds that
finish outside that window are pruned without announcing unavailable URLs.
The `previews` tag stays on its initial commit; it is not a moving source
pointer. Pin the versioned asset URLs for downstream CI while within retention.

### Provision the preview channel

The publisher requires an existing, published, mutable `previews` release.
It checks this before building and again before uploading. GitHub's immutable
release setting remains enabled for stable releases. Rolling previews need a
mutable release so later builds can add assets and retention can remove old ones;
the publisher protects each retained build by comparing existing bytes.

For initial setup, a repository administrator must:

1. Confirm no other release will publish during this brief setup window.
2. Temporarily disable repository release immutability in **Settings > General > Releases**.
3. Create the `previews` prerelease targeting the current `main` commit,
   without marking it latest. Set its title and static notes during creation;
   describe the versioned assets, completion markers, and installation docs.
4. Immediately restore release immutability, even if creation fails. Verify
   `GET /repos/chartcoach/chartcoach/immutable-releases` reports `enabled: true`
   and the new release reports `draft: false` and `immutable: false`.

Previously published immutable releases retain their protection when the setting
changes. The Actions token cannot change this administrator setting, and CI
never attempts to disable it. See [GitHub's immutable release rules](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).

Never edit the rolling release's metadata while repository immutability is
enabled. GitHub seals an existing mutable release when its notes are updated,
including a body-only REST update. Uploading and deleting assets preserve
mutability; the publisher performs only those release mutations.

The earlier `preview` and `preview-builds` channels became immutable during
failed publications and link here in their notes. The latter contains an
incomplete build without its checksum completion marker. An immutable release
cannot be unlocked; deleting it also prevents reuse of its tag name. If the
rolling channel itself becomes immutable, provision a fresh tag and update the
publisher, chat SDK dependency URL, release validator, tests, and installation
docs together.

### Preview provenance v1

Each build retains an immutable `chartcoach-X.Y.Z.devN-provenance.json` record
using chartcoach's custom predicate type
`https://github.com/chartcoach/chartcoach/blob/main/development_docs/releasing.md#preview-provenance-v1`.
Its checksum is included
alongside the four distributions in the completion manifest.
`workflow_run` can use a newer workflow revision than its validated source.
The `buildDefinition.externalParameters.checkoutCommit` field records the
packaged commit, and `resolvedDependencies` records both source and signing
workflow revisions. The record is generated in the build job and reused across
publication retries, including its original run attempt.

The publisher creates a [GitHub artifact attestation](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations)
for every distribution, provenance record, and checksum manifest. Each signed
record binds artifact bytes to the publication workflow and packaged source.
Verify a downloaded artifact with:

```bash
gh attestation download chartcoach-X.Y.Z.devN-py3-none-any.whl -R chartcoach/chartcoach
gh attestation verify chartcoach-X.Y.Z.devN-py3-none-any.whl -R chartcoach/chartcoach \
  --bundle BUNDLE_FILE \
  --predicate-type "https://github.com/chartcoach/chartcoach/blob/main/development_docs/releasing.md#preview-provenance-v1" \
  --signer-workflow "chartcoach/chartcoach/.github/workflows/publish.yml"
```

Replace `BUNDLE_FILE` with the `.jsonl` filename printed by the download.
GitHub restricts custom build types under the standard SLSA predicate.
Download without a predicate filter;
bundle verification enforces the predicate type, signer, and artifact digest.
The publisher downloads the persisted attestation with five
attempts, two seconds apart, then verifies it once and checks the packaged source
commit before uploading release assets.

### Recover publication

| First failed job                  | Response                                                                                                                                                          |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable `prepare`                  | Wait for main CI for the exact tag, or correct the workflow and dispatch for the same immutable tag as described above.                                           |
| Stable registry or container jobs | Rerun failed jobs using the retained `release-packages` bundle; inspect conflicts before retrying.                                                                |
| `resolve-preview`                 | Resolve GitHub API access, missing history/tags, or an unprovisioned mutable channel, then rerun. The latest exact-commit main CI must succeed.                   |
| `build-preview`                   | Fix source/build inputs in a new main commit and let CI trigger a new preview.                                                                                    |
| `verify-preview`                  | Inspect the consumer failure; rerun transient failures or fix package behavior in a new main commit.                                                              |
| `publish-preview`                 | Rerun failed jobs on the same run to reuse its 30-day `preview-packages` artifact. Announcement and retention failures resume without overwriting uploaded bytes. |

Rerunning all jobs after partial publication rebuilds packages and can produce
byte conflicts; rerun failed jobs instead. When the checksum marker is present,
resolution skips a completed preview. Expired artifacts or conflicting bytes
require recovering the original build before any further upload.

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
