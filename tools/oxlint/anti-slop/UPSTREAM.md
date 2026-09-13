# Anti-slop provenance

Source: https://github.com/dmmulroy/anti-slop

Additions imported from `c44ef22ca116d0ba62a3ff663a0bd13a3f3fa40b`:

- `no-array-filter-map`, `no-reduce-accumulator-copy`, `no-shape-in-symbol-names`, and `require-readable-spacing`.
- All five rules in the separate Effect plugin, including `effect/shared/tagged-values.ts`.
- The array-method helper and the licensed ESLint Stylistic spacing engine.
- Their upstream RuleTester cases and the spacing CLI integration test.

Production rule implementations are retained from this revision. Local entry points
export rule catalogs so the preset and tests can verify complete error-level coverage.
Tests live under `test/` and import the existing Node test bootstrap. Effect policy
is enabled for `apps/chat`, the workspace that depends directly on Effect.
Knip retains the upstream-generated padding options declaration surface through
a file-scoped exported-type exemption. Production rule exports remain checked.

The existing fourteen generic rules and their lexical type-flow helpers retain
ChartCoach's local behavior and compatibility tests. They were not overwritten by
this import. Future updates must compare these local implementations before merging
upstream changes.

Keep this directory's MIT `LICENSE` and `vendor/eslint-stylistic/LICENSE` with redistributed
copies. The spacing engine has its own upstream revision and adaptation notes in
`vendor/eslint-stylistic/UPSTREAM.md`.

Run `pnpm check:anti-slop` for rule tests and plugin typechecking. Run `pnpm ready`
and `make check` to validate the configured rules against their consumers.
