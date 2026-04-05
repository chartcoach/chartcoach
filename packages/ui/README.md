# `@chartcoach/ui`

Shared generic UI package for the ChartCoach monorepo.

## Boundary

- Put **generic shadcn/Tailwind primitives** under `src/components` and `src/lib`.
- Import generic primitives from `@chartcoach/ui`.
- Import shared styles from `@chartcoach/ui/styles/{globals,fonts,tokens}.css`.
- Keep primitive/shared semantic tokens generic in `packages/ui`.
- App/editorial extension tokens (for example site-specific brand accents) stay app-local and should layer on top of shared semantics rather than leaking back into `packages/ui`.

## Workflow

- Add new primitives with the shadcn CLI from the consuming workspace:
  - `pnpm dlx shadcn@latest add <component> -c apps/site`
  - `pnpm dlx shadcn@latest add <component> -c apps/visground-viewer`
- The monorepo aliases route generated primitives back into `packages/ui`.
- Review generated files, export them from `src/index.ts`, and keep this package generic-only.
- This package emits JS + declarations to `dist/`. Shared CSS stays as source assets under `src/styles/`.
- Workspace apps resolve internal package source via the package `chartcoach-source` export condition during local dev/build.
- Dist outputs remain the explicit artifact path for package builds and CI-like flows.
- If you want prebuilt package artifacts or watch mode explicitly, use:
  - `pnpm build:packages`
  - `pnpm dev:watch:packages`
- Source scanning must use workspace-owned repo paths, not `node_modules` installation paths.
- Package styles own their cross-package Tailwind source registration. Consumers should import `@chartcoach/ui/styles/globals.css` instead of adding cross-package `@source` globs themselves.
- Alias policy:
  - cross-package imports use package names only
  - app-local aliases are optional and allowed only within one app when they solve repeated deep local imports
  - short relative imports are preferred when already obvious

## Verification

- Use real product surfaces, not committed smoke pages.
- Site verification: `/`, `/guidelines/`, `/guidelines/<detail>`, `/labels/`
- Viewer verification: `apps/visground/workbench/06_viewer.py`
