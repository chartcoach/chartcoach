# Catalog files and records

Python and JavaScript read the same guideline fields and four catalog files:
`MANIFEST.md`, `entries.parquet`, `release.json`, and `catalog.json`.

## Guideline record

Every `entries.parquet` row has six fields:

```text
id
title
description
labels
sections
references
```

`sections` preserves source order. Each section contains `role`, `title`, and
`content`. Python and JavaScript join those sections in order when they produce
the guideline body.

`labels` use `family:value` names. `MANIFEST.md` lists every accepted section
role and label family. Both readers reject a record that uses an undeclared
role or family.

When one of these fields changes, update the Python model, JavaScript model,
shared fixture, site, and public docs together.

## `release.json`

Current releases use `schema_version: 1`:

```json
{
  "schema_version": 1,
  "digest": "<sha256>",
  "artifacts": {
    "MANIFEST.md": { "sha256": "<sha256>", "bytes": 123 },
    "entries.parquet": { "sha256": "<sha256>", "bytes": 456 }
  }
}
```

The digest covers `schema_version` and the path-sorted `artifacts` entries.
Each `artifacts` key is a relative path. Both readers require `MANIFEST.md` and
`entries.parquet`, verify the release digest, then verify each required file's
byte count and SHA-256 hash before parsing it.

Optional search indexes add two files under a profile name:

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

`documents.parquet` contains document IDs, parent guideline IDs, section roles,
labels, text, vectors, projection coordinates, and neighbors. `index.tar.gz`
contains one LanceDB table named `documents`.

## `catalog.json`

`catalog.json` stores the record for the currently selected public release.
Selecting a new digest overwrites this file. Files under
`catalog/releases/<digest>/` keep the bytes named by that digest.

Readers fetch `catalog.json` on each open so they see the current selection. A
specific `release.json` keeps one digest across calls. Verified files can be
reused from the content-addressed cache.

## Shared fixture

`fixtures/catalog-release` supplies one small release to:

- Python catalog loading tests
- JavaScript release and Parquet tests
- local site builds and generated-file tests

When a guideline field, manifest rule, release field, or file path changes,
create a small authored catalog and rebuild all three fixture files. Set
`FIXTURE_SOURCE` to that authored directory:

```bash
FIXTURE_SOURCE="/absolute/path/to/authored-fixture"
FIXTURE_BUILD="$(mktemp -d)"

uv run --locked --package chartcoach --extra curation \
  chartcoach catalog build \
  --source "$FIXTURE_SOURCE" \
  --out "$FIXTURE_BUILD/catalog"

uv run --locked --package chartcoach --extra curation \
  python - "$FIXTURE_BUILD" <<'PY'
from pathlib import Path
import sys

from chartcoach import open_catalog
from chartcoach.catalog.curation import build_release

root = Path(sys.argv[1])
build_release(open_catalog(root / "catalog"), root / "release")
PY

cp "$FIXTURE_BUILD/release/MANIFEST.md" fixtures/catalog-release/
cp "$FIXTURE_BUILD/release/entries.parquet" fixtures/catalog-release/
cp "$FIXTURE_BUILD/release/release.json" fixtures/catalog-release/
rm -r "$FIXTURE_BUILD"
```

Inspect the three-file diff, then read the fixture through both public clients.

Run:

```bash
uv run --locked --package chartcoach --all-extras \
  pytest packages/chartcoach/tests/test_release_contract.py \
  packages/chartcoach/tests/test_catalog_runtime.py
pnpm --dir packages/catalog test
pnpm --dir apps/site build
```
