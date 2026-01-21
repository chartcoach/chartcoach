# Proposed monorepo structure (working draft)

## Top-level folders
- `apps/` — runnable products (servers, UIs, sites)
- `packages/` — reusable libraries (Python and/or TS packages)
- `guidelines/` — source-of-truth guideline catalog dataset (markdown + bib + assets)
- `evaluations/` — evaluation *code + data* (scenarios, judgments, runs, drivers)
- `docs/` — repo-level documentation (architecture, formats, how-tos)
- `scripts/` (optional) — repo utilities not worth packaging

## Naming conventions
- Folder names: short, domain-based (`catalog`, `retrieval`, `cataloging`, `mcp`, `site`, `eval-ui`)
- Avoid `packages/examples/*` for anything you rely on.

## Packages (libraries)
- `packages/chartcoach/` (Python): single distribution (`chartcoach`) with modules like `chartcoach.catalog`, `chartcoach.cataloging`, `chartcoach.retrieval`, `chartcoach.eval`.
  - Use Python extras for optional features (e.g. embeddings/indexing, notebooks, cataloging pipelines).

## Apps (products)
- `apps/retrieval-api/` (Python): HTTP API for retrieval + evaluation storage (FastAPI is a typical fit)
- `apps/mcp-server/` (Python): MCP server exposing retrieval tools (either calls `packages/retrieval` directly or calls `apps/retrieval-api`)
- `apps/eval-ui/` (Node): annotation UI that talks to retrieval-api (Revisit/Next/etc.)
- `apps/guidelines-site/` (Node): Astro site to browse guidelines (static-first; search can be static index or API-backed later)

## Evaluations (code + data in one place)
Structure the `evaluations/` directory as its own “workspace area”:
- `evaluations/scenarios/` — scenario specs + assets (chart images, prompts, constraints, provenance)
- `evaluations/judgments/` — exported annotations (or SQLite snapshots)
- `evaluations/runs/` — run manifests + metrics outputs
- `evaluations/drivers/` — scripts/CLIs to run experiments, seed pooling sets, compute metrics
- `evaluations/README.md` — how to add scenarios, run a benchmark, export/import judgments

This satisfies your desire for a dedicated place that contains both the evaluation datasets and the driver code, without forcing evaluation data into a publishable Python wheel.

## Curation ownership (what replaces `packages/examples/guideline-cataloging`)
Promote it to a first-class “cataloging” area:
- Library: `chartcoach.cataloging` (Python) — ingestion, extraction, dedup, labeling, validation; writes to `guidelines/`
- App/notebooks: `apps/cataloging-notebook/` (optional) — marimo UI for semi-automatic cataloging workflows

Rule of thumb:
- If it’s reusable logic (parse Zotero, normalize labels, dedup merge), it belongs in `chartcoach.cataloging`.
- If it’s interactive workflow (review, triage, manual edits), it belongs in an app/notebook.

## Repo-level docs location
- Keep monorepo “meta docs” in `docs/`:
  - `docs/architecture.md` (high-level)
  - `docs/data-formats/guidelines.md`
  - `docs/data-formats/evaluations.md`
  - `docs/dev/` (how to run API, UI, MCP, site)
  - `docs/adr/` (architecture decision records)
- Keep the root `README.md` short: what this repo is + quickstart + pointers into `docs/`.
- Each app/package also has its own `README.md` for local usage.

## Migration sketch (minimal steps)
1. Create `packages/chartcoach` and move the catalog code to `chartcoach.catalog`.
2. Promote notebook helper logic into `chartcoach.cataloging` / `chartcoach.utils` so notebooks are glue, not implementations.
3. Add `chartcoach` Python extras for optional dependencies (embeddings, notebooks, cataloging, application).
4. Create `evaluations/` tree and start putting scenario + judgments there (even if empty initially).
5. Populate `apps/` with `retrieval-api`, `mcp-server`, `eval-ui`, `guidelines-site` as you build them.
