---
version: alpha
name: ChartCoach Visual System
description: Visual system for the ChartCoach Guideline Catalog experience.
colors:
  light:
    canvas: "#FCFBF8"
    ink: "#001011"
    veil: "#172323"
    mutedInk: "#5C6764"
    layer: "#EDEDEA"
    layerStrong: "#E2E1DB"
    line: "#C4C5BD"
    ember: "#FD5321"
  dark:
    canvas: "#101312"
    ink: "#F6F1E7"
    veil: "#D6D0C3"
    mutedInk: "#A6AAA2"
    layer: "#191D1B"
    layerStrong: "#242A27"
    line: "#3F4741"
    ember: "#FF7A45"
typography:
  display:
    fontFamily: Bricolage Grotesque
    fontSize: 54px
    fontWeight: 760
    lineHeight: 0.98
    letterSpacing: "0"
  heading:
    fontFamily: Bricolage Grotesque
    fontSize: 35px
    fontWeight: 650
    lineHeight: 1.08
    letterSpacing: "0"
  body:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0"
rounded:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  pill: 999px
spacing:
  1: 4px
  2: 8px
  3: 12px
  4: 16px
  5: 24px
  6: 32px
  7: 48px
  8: 64px
components:
  header:
    background: "{colors.*.canvas}"
    border: "{colors.*.line}"
    activeNav: "{colors.*.ink}"
  guidelineCard:
    background: "{colors.*.layer}"
    border: "{colors.*.line}"
    radius: "{rounded.md}"
  labelChip:
    background: "{colors.*.canvas}"
    border: "{colors.*.line}"
    radius: "{rounded.xs}"
  primaryAction:
    background: "{colors.*.ink}"
    foreground: "{colors.*.canvas}"
    accent: "{colors.*.ember}"
---

# ChartCoach Design System

## Experience Boundary

ChartCoach uses one visual language for a focused public experience: orient a visitor, let them browse guideline records, filter by labels, open a guideline, inspect sections, and follow references.

Keep this document about the visual system, interaction rhythm, and content hierarchy. Do not record repository layout, release ownership, or deployment topology here.

## Source Adaptation

The original design reference is `https://dotconnect.vc/`. A browser audit captured the warm canvas, near-black ink, orange action accent, compact navigation, numbered section rails, direct headlines, repeated cards, and dark closing band.

Adapt those moves to ChartCoach:

- Use numbered section labels for cataloging and source sections.
- Keep cards compact and action-oriented.
- Pair direct headlines with short explanatory copy.
- Use ember for one action or evidence accent at a time.
- Use a dark closing band as a final catalog entry point.

Do not copy dotconnect content, business sections, imagery, font files, icons, or interaction patterns that do not fit a Guideline Catalog.

## Modes

Light and dark modes are supported contracts. The document root may use `data-theme="light"` or `data-theme="dark"`. ChartCoach tokens respond to those attributes wherever the experience renders.

Every visible page and component must be checked in both modes:

- Header, navigation, theme toggle, and mobile menu.
- Home hero, feature cards, and catalog sections.
- Guideline index count, filter input, suggestions, active filters, and cards.
- Guideline detail title, labels, sections, bibliography, BibTeX block, and copy control.
- Inline code, code blocks, tables, focus rings, and selection color.

Do not create a separate theme system, duplicate mode props, or mode-specific component variants. Use CSS variables as the shared contract.

## Colors

The light palette uses a warm canvas, near-black ink, neutral layers, disciplined borders, and one ember accent. The dark palette keeps the same relationships with low-saturation near-black backgrounds and warm text.

Implementation variables:

```css
:root,
:root[data-theme="light"] {
  --canvas: #fcfbf8;
  --ink: #001011;
  --veil: #172323;
  --muted-ink: #5c6764;
  --layer: #ededea;
  --layer-strong: #e2e1db;
  --line: #c4c5bd;
  --ember: #fd5321;
}

:root[data-theme="dark"] {
  --canvas: #101312;
  --ink: #f6f1e7;
  --veil: #d6d0c3;
  --muted-ink: #a6aaa2;
  --layer: #191d1b;
  --layer-strong: #242a27;
  --line: #3f4741;
  --ember: #ff7a45;
}
```

Tailwind 4 exposes these through CSS-first `@theme` tokens. Application styles, syntax highlighting variables, Pagefind variables, and shared React components must all reference the same variables.

## Typography

Use Fontsource packages imported by `@chartcoach/ui`.

- **Manrope:** Body text, navigation, controls, labels, cards, and dense catalog copy.
- **Bricolage Grotesque:** Hero headline, section headings, guideline titles, and major record titles.
- **System mono:** Label families, copied markdown controls, BibTeX, and compact metadata.

Letter spacing is `0`. Use fixed type sizes with breakpoints instead of viewport-scaled type. Long headings should wrap naturally without clipping or overlapping nearby controls.

## Layout

The opening page should feel close to the restraint of a technical open-source project page: short hero, direct actions, compact cards, and clear navigation. The brand signal comes from the ChartCoach name, catalog nouns, and source-backed guidance rather than decorative backgrounds or a standalone logo.

- Keep prose near `52rem`.
- Keep catalog lists near `72rem`.
- Use repeated cards only for feature cards and guideline records.
- Avoid nested cards, gradient ornaments, glass effects, and decorative blobs.
- Keep the next section visible below the hero on common desktop and mobile viewports.

## Components

### Header

The header contains a text-only ChartCoach wordmark, primary navigation, social link, and local theme toggle. Active navigation should be visible without dominating the page. The mobile menu must include the same navigation.

### Home Hero

The hero states what the catalog provides in one headline and one paragraph. Keep it text-only until a real visual identity earns its place. The next section makes the catalog concrete through compact cards that name review, label browsing, and source-backed records.

### Catalog Cards

Cards explain what visitors can inspect: guideline records, label filters, section roles, source references, search, and agent context. Each card should name one concrete action and link into the catalog path.

### Guideline Index

The index is the main browser. The count, hint, filter input, suggestions, active filters, and cards should read as one catalog task. Filtering must remain client-side and visibly update the count and card list.

### Guideline Detail

The detail page is for reading one record. It prioritizes title, summary, copy markdown, labels, role-annotated sections, bibliography, and BibTeX. Code and references must pass contrast in both modes.

### Shared UI

Shared React components expose their public API from `@chartcoach/ui`. Application code must not import UI internals through `@chartcoach/ui/lib/*` or `@chartcoach/ui/components/*`. CSS remains available through `@chartcoach/ui/styles/*`.

## Copy Rules

- Start with what the visitor can inspect or do.
- Use ChartCoach nouns from `CONTEXT.md`.
- Keep claims tied to the Guideline Catalog, labels, sections, and sources.
- Avoid package reference prose in the primary experience.
- Avoid broad adjectives that do not name a mechanism.

## Verification

Before handoff, run local build checks and use browser screenshots at desktop and mobile widths. Capture both light and dark modes for the opening page, guideline index, guideline details, quick start, mobile menus, and routes with code. Use an independent aesthetic judge and Agentation annotations before declaring the redesign complete when those tools are practical.
