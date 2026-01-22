---
id: use-small-multiple-line-charts-with-independent-y-axes-only-to-compare-shapes
title: Use independent y-axes in small multiple line charts only to compare trend
  shapes across magnitudes
bibliography: references.bib
description: Allow different y-axis scales across panels only when the goal is to
  compare shapes and direction despite vastly different magnitudes.
labels:
- chart:line
- task:trend
- visual:scale
- impact:clarity
- data:temporal
- audience:novice
- complexity:advanced
---

## Use independent y-axes in small multiple line charts only to compare trend shapes across magnitudes <!-- role: advice -->

Use independent y-axis scales across panels only when category magnitudes differ so much that a shared scale hides important up/down patterns. Treat the result as a shape-comparison view rather than a value-comparison view.

## Different scales restore visibility but change what “equal height” means <!-- role: reason -->

A shared y-axis lets readers compare absolute values across categories, but it can compress smaller-magnitude series into near-flat lines when one category dominates the range. Independent y-axes re-expand each series to a similar visual height so direction and pattern become visible, but this also breaks cross-panel value comparability because the same vertical distance no longer represents the same numeric change everywhere.

**Mechanism:** Rescaling increases perceptual resolution for each series’ variation while removing a common quantitative reference across panels.

**Evidence:** Small multiple line charts can reveal strong trends that are invisible in a normal line chart when magnitudes differ greatly by allowing different y-axes per panel, giving each line similar visual height [@muth_small_multiple_line_charts_2024].

**Notes:** Independent scales are powerful but easy to misread if viewers assume all panels share one scale.

## When magnitude differences hide trends on a shared scale <!-- role: context -->

- **User Goal:** See whether each category rises or falls and how sharply, even when sizes differ greatly.
- **Task:** Compare direction, timing of peaks, and pattern similarity across categories.
- **Data:** Temporal series with widely different ranges (orders of magnitude or dominant outliers).
- **Chart Setting:** Small multiple line charts where each panel can display its own axis markings.
- **Audience:** Readers who may default to assuming consistent axes unless clearly signaled.
- **Success Criterion:** Previously “flat” lines become interpretable without implying false equality of values.

## When not to use independent y-axes <!-- role: exceptions -->

**Break it when:** Readers need to compare absolute levels or differences between categories. **Why:** Independent y-axes can produce false insights if viewers assume a shared scale and read heights as comparable across panels [@muth_small_multiple_line_charts_2024].

## Tradeoffs of independent scales <!-- role: costs -->

**Sacrifice:** You give up direct comparability of levels and changes across panels. **Risk:** Readers may overlook that scales differ and infer incorrect rankings or magnitudes. **Mitigation:** Treat the visualization as pattern-focused and make the scaling difference hard to miss through clear signaling [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using independent y-axes without making the differing scales obvious. **Why it fails:** Readers may assume a common scale and draw incorrect conclusions about relative size or change [@muth_small_multiple_line_charts_2024].
- **Mistake:** Using independent y-axes to support claims about which category is “higher.” **Why it fails:** Height is no longer directly comparable across panels [@muth_small_multiple_line_charts_2024].

## Quick tests for safety <!-- role: check -->

**Failure Sign:** A reader could reasonably interpret a taller line in one panel as “bigger” than a shorter line in another panel. **Quick Check:** If you removed the y-axis labels, would the chart become misleading? If yes, independent scales are risky. **Stronger Test:** Ask a reader what they can compare across panels; if they mention absolute levels, the design is likely being misread [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Keep a shared y-axis across panels when cross-category level comparisons are important.
- Reduce the influence of extreme categories by separating them into their own view rather than rescaling all panels independently.
- Add explicit language in the chart description that y-axis scalings differ among panels when you must use independent scales [@muth_small_multiple_line_charts_2024].
- Use visual cues (such as unusual-looking gridlines per panel) that prompt readers to notice different axes [@muth_small_multiple_line_charts_2024].
