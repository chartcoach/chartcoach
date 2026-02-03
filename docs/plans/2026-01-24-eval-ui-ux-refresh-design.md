# Design: Eval UI UX refresh

## Objectives
1. Keep scenario context visible while rating guideline relevance (sticky chart + title).
2. Reduce control clutter (remove keyboard shortcut messaging, compact mode, auto-advance, next-unrated, download/export).
3. Improve comprehension and mobile usability (strategy selection, guideline card rating controls).
4. Ensure ratings sync is enabled when S3 env vars are present (even without `S3_REGION` if a custom endpoint is used).

## Information architecture (Iteration 6)
- Landing index (`/`): lists all scenarios with brief context (intent/query) + chart thumbnail.
- Scenario page (`/scenarios/:scenarioId`): dedicated page per scenario with:
  - **Top-level Tabs:** scenarios (quick switching)
  - **Second-level Tabs:** retrieval strategies (line style; changes guideline list)

## Proposed layout

### Desktop (`lg+`)
- Use a **sticky scenario header** (anchored under the app header) so the chart stays visible while rating.
- Within the sticky header:
  - Scenario Tabs, then Strategy Tabs + helper text.
  - Two-column grid:
    - Left: title + provenance + explicit task instruction, progress bar, designer intent, query.
    - Right: large chart image (click opens full-size).
- Below the sticky header: full-width guideline cards with always-visible Likert rating controls.

### Mobile
- Keep the same hierarchy (Scenario Tabs → Strategy Tabs) but allow horizontal scrolling.
- Ensure guideline cards remain full width and rating controls are easy to tap.
- Keep the chart prominent, but watch sticky header height (avoid consuming too much vertical space).

## Behavioral changes
- Remove compact mode toggle and always show scenario context.
- Remove auto-advance and next-unrated button (and associated shortcuts/logic).
- Remove keyboard shortcut help text from the UI (and drop keyboard handlers to avoid hidden affordances).
- Remove Download/export button. Keep Clear ratings.

## UI affordances for rating
- Keep the 1-5 Likert buttons but ensure they lay out well on narrow widths:
  - Allow the guideline card header/actions to wrap on small screens.
  - Make the rating control clearly labeled (“Relevance”) and easy to tap.

## Sync enablement
- Treat missing `S3_REGION` as non-fatal when `S3_ENDPOINT` is set (default region to `us-east-1`).
- Preserve existing “Syncing / queued / failed” states; avoid “disabled” when config is effectively usable.
