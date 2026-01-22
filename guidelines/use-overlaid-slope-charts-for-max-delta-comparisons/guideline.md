---
id: use-overlaid-slope-charts-for-max-delta-comparisons
title: Use overlaid slope charts to find the largest change between two slope-chart
  series
bibliography: references.bib
description: Overlaying two slope-chart series improves precision for identifying
  the biggest mover compared to animated transitions and small-multiple layouts.
labels:
- chart:line
- task:compare
- task:aggregate
- visual:position
- visual:orientation
- impact:accuracy
- data:categorical
- audience:novice
- comparison:two-series
---

## Prefer an overlaid slope chart for biggest-mover judgments <!-- role: advice -->

Use an overlaid slope-chart comparison (both series in the same plotting space) when the goal is to identify which item changed the most between two slope-chart series.

## Why overlaid slope charts help max-delta <!-- role: reason -->

Overlaying reduces the need to match corresponding items across separate views, keeping the comparison within a single coordinated frame.

**Mechanism:** Co-locating both series allows viewers to judge the largest change by directly comparing aligned visual features within one space, rather than relying on across-view correspondence or transient motion cues.

**Evidence:** For a max-delta (“biggest mover”) task using slope charts, the overlaid arrangement produced more precise thresholds than the animated arrangement, and small-multiple variants did not show improvements over each other. [@ondovFaceFaceEvaluating2019; @zengReviewCollationGraphical2023]

**Notes:** This guideline is specific to slope charts and the max-delta task; it does not imply the same ranking for bar charts.

## When you should apply overlaid slope charts for max-delta <!-- role: context -->

- **User Goal:** Identify which item’s change is largest between two series.
- **Task:** Aggregate (max-delta / “biggest mover”).
- **Data:** Two series with matched items (same categories/items in both).
- **Chart Setting:** Slope chart (two-point lines per item) with both series overlaid.
- **Audience:** Viewers doing quick comparison rather than detailed reading.
- **Success Criterion:** Better discrimination of small differences (higher precision).

## When not to use overlaid slope charts for max-delta <!-- role: exceptions -->

**Break it when:** Overlaying makes the display too visually ambiguous to tell which mark belongs to which series. **Why:** If viewers cannot reliably separate the two series, co-location no longer helps comparison.

## Tradeoffs of overlaid slope charts <!-- role: costs -->

**Sacrifice:** Overlaid displays can be harder to parse as the number of items increases.\
**Risk:** Visual overlap can obscure individual marks and reduce legibility.\
**Mitigation:** Keep the comparison to two series and a small set of items.

## Common mistakes with overlaid slope charts <!-- role: mistakes -->

**Mistake:** Expecting mirroring to improve slope-chart max-delta performance. **Why it fails:** Mirrored small multiples did not show improved thresholds over non-mirrored small multiples for slope charts in this task setting.

## Quick tests for whether overlay is working <!-- role: check -->

**Failure Sign:** Viewers hesitate because they cannot tell which series a line belongs to.\
**Quick Check:** Ask users to point to the biggest mover and explain which two values they compared; if they cannot articulate correspondence, overlay is too confusing.\
**Stronger Test:** Compare error rates on the same max-delta questions using overlaid versus animated slope charts.

## What to do instead if overlay is too confusing <!-- role: fix -->

- Use an animated transition for max-delta only if the overlaid view is too visually cluttered.
- Reduce the number of items shown in the slope chart so overlay remains readable.
- Use a small-multiple layout when viewers must keep both series visible and separable without overlap.
- Add a persistent highlight on hover/selection (if interaction is available) to isolate one item at a time.
