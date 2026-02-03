# Codereview Fixes (2026-01-27)

This document tracks the changes made to address `.artifacts/codereview-active.md` end-to-end, including verifiable checks.

## Decisions

- Canonical eval-ui data mode: **artifact-first** (precomputed `index.json` + `bundles/*.json`).
- Eval-ui now supports artifact roots via `EVAL_ARTIFACTS_URL` (`file://`, `https://`, `s3://`) and falls back to a small in-repo fixture artifact set when nothing is configured.
- Bibliography rendering is treated as **untrusted HTML** and sanitized at build time.

## Changes by review item

### P0.1 — Site Dockerfile missing `@chartcoach/ui`

- Fixed `apps/site/Dockerfile` to copy `packages/chartcoach-ui` manifests + sources so workspace installs/builds succeed.
- Updated `.github/workflows/site-docker-build.yml` trigger paths to include `packages/chartcoach-ui/**`.
- Trimmed Docker build context further by ignoring `packages/chartcoach-ui/dist/**` in `.dockerignore`.

### P0.2 — Eval UI README stale vs runtime behavior

- Updated `apps/eval-ui/README.md` to describe artifact-first reality (and remove claims about local YAML/parquet loading + scenario/bundle caching).
- Implemented `EVAL_ARTIFACTS_URL` support (local folder / HTTPS / S3) in `apps/eval-ui/src/eval/server/eval.server.ts`.
- Added small fixture artifacts under `apps/eval-ui/fixtures/eval-artifacts/v1/` so `pnpm dev:eval` works without S3.
- Updated `apps/eval-ui/Dockerfile` to copy fixture artifacts into the runtime image.

### P0.3 — Retrieval optional deps not truly optional

- Added `packages/chartcoach-py/src/chartcoach/retrieval/strategy/optional.py` (`require_dspy()` + `is_dspy_available()`).
- Updated DSPy-dependent modules to use `require_dspy()` and changed `chartcoach.retrieval.strategy.__init__` to gate DSPy exports behind `is_dspy_available()`.
- Added tests to ensure the error message is controlled and helpful.

### P1.1 — `k=None` semantics inconsistent in `GuidelineBrowserStrategy`

- Fixed early termination: unbounded `k=None` no longer stops after extracting 1 id; it evaluates both attempts and returns the best output.
- Added a unit test that fails under the previous behavior.

### P1.2 — Ratings sync signature too large

- Replaced JSON-string signature with a constant-size FNV‑1a 64-bit digest (`apps/eval-ui/src/eval/relevance-ratings-sync-metadata.ts`).
- Added a vitest that stress-tests signature length with 10k ratings.

### P1.3 — Duplicate wire→CatalogEntry mapping + weak artifact validation

- Centralized conversion in `@chartcoach/catalog` (`packages/chartcoach-js/src/catalog/wire.ts`).
- Updated parquet loader to use the shared converter.
- Tightened eval-ui artifact parsing: entries are validated with `isCatalogEntryWire`, and invalid artifacts now fail loudly instead of silently dropping guidelines.
- Added vitest coverage for the new wire helpers.

### P2.1 — Strict catalog validation

- Added `python -m chartcoach.catalog.validate` (`packages/chartcoach-py/src/chartcoach/catalog/validate.py`) and tests.
- Added `pnpm validate:catalog` script for convenience.

### P2.2 — Bibliography HTML injection risk

- Sanitized citation/bibliography HTML at build time using `sanitize-html` (`apps/site/src/loaders/guidelines-loader.ts`).

### P2.3 — Artifact “score” is a placeholder

- Labeled scores as rank-normalized placeholders by injecting `meta.score_kind = "rank_normalized"` in artifact generation.

### P3.1 — Unused eval-ui components

- Deleted `apps/eval-ui/src/components/scenario-sidebar.tsx` and `apps/eval-ui/src/components/strategy-picker.tsx`.

## Additional fixes found during E2E

- RxDB DB9 prevented ratings persistence in eval-ui (caused by `ignoreDuplicate` without dev-mode). Fixed in `apps/eval-ui/src/db/rxdb.ts` by removing `ignoreDuplicate` and storing the database promise on `globalThis` for HMR safety.

## Verification (commands run)

JS:

- `pnpm install`
- `pnpm lint:js`
- `pnpm --filter @chartcoach/catalog test`
- `pnpm test:eval`
- `pnpm build:site`
- `pnpm build:eval`

Python:

- `uv run ruff check`
- `uv run ty check`
- `uv run pytest` (100% coverage gate)
- `pnpm validate:catalog` (wraps `uv run python -m chartcoach.catalog.validate`)

Docker:

- `docker build -f apps/site/Dockerfile .`
- `docker build -f apps/eval-ui/Dockerfile .`

E2E (agent-browser):

- Site: loaded `http://localhost:4321/`, browsed `/guidelines`, opened a guideline detail page, confirmed bibliography container renders.
- Eval UI: loaded `http://127.0.0.1:3000/` with S3 env blanked, opened a scenario, set a rating, confirmed RxDB persistence across reload.

