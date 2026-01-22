---
id: prefer-overlaid-slope-charts-for-biggest-mover
title: Prefer overlaid slope charts over animation for biggest-mover comparisons
bibliography: references.bib
description: For slope-chart style encodings, overlaying the two series supports more
  precise detection of the largest change than animation.
labels:
- chart:slope
- task:compare
- task:detect-change
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- comparison:two-series
---

## Overlaid slopes for maximum-delta judgments <!-- role: advice -->

Use an overlaid slope chart (both series in the same coordinate space) when the task is to pick which item changed the most between two series. Avoid relying on animation as the primary comparison aid for this slope-based biggest-mover task.

## Co-location helps slope-based delta discrimination <!-- role: reason -->

When both series are drawn in the same space, viewers can compare deltas with minimal eye movement and less need to remember values across views. For slope-style encodings, this co-location appears to provide a stronger advantage than motion cues.

**Mechanism:** Overlay puts corresponding items in the same spatial frame, enabling direct perceptual comparison of differences without cross-view matching.

**Evidence:** In the maximum-delta task using slope charts, the overlaid arrangement achieved more precise titers than the animated arrangement and outperformed the other tested layouts [@ondovFaceFaceEvaluating2019a].

**Notes:** In the same slope-chart experiment, mirroring did not show a benefit over standard small multiples.

## Context for choosing overlaid slope charts <!-- role: context -->

- **User Goal:** Identify the single item with the largest absolute change between two snapshots.
- **Task:** MAXDELTA on slope-style marks.
- **Data:** Exactly two series with a small number of items represented as slopes.
- **Chart Setting:** Static display or a setting where overlay is feasible and legible.
- **Audience:** Non-expert viewers making quick perceptual judgments.
- **Success Criterion:** Accurate selection at small differences between the largest change and distractor changes.

## Exceptions for overlaid slope charts <!-- role: exceptions -->

- **Break it when:** Overlap makes items indistinguishable (e.g., excessive occlusion or ambiguity). **Why:** If viewers cannot reliably separate the two series, co-location no longer aids comparison.
- **Break it when:** The task is overall correlation judgment rather than biggest-mover detection. **Why:** This guideline is specific to MAXDELTA and not evaluated for correlation with slope charts in this study [@ondovFaceFaceEvaluating2019a].

## Costs of overlay in slope charts <!-- role: costs -->

**Sacrifice:** Overlays can reduce clarity if marks overlap heavily. **Risk:** Viewers may confuse which series a mark belongs to if styling is too similar. **Mitigation:** Use consistent, distinguishable styling for the two series.

## Mistakes with overlaid slope comparisons <!-- role: mistakes -->

**Mistake:** Treating animation as a universal upgrade over overlay for slope comparisons. **Why it fails:** Animation underperformed overlay for slope-chart biggest-mover detection in this study [@ondovFaceFaceEvaluating2019a].

## Check for whether overlay is working in slope charts <!-- role: check -->

**Failure Sign:** Viewers hesitate or misidentify the biggest mover despite large apparent changes. **Quick Check:** Ask a few users to point to the biggest mover without explanation; they should succeed quickly. **Stronger Test:** Compare accuracy against an animated version using matched exposure time to ensure overlay remains superior for your data.

## Fixes when overlay becomes too cluttered <!-- role: fix -->

- Reduce the number of items shown simultaneously (filter, facet, or focus on a subset).
- Switch to a mirrored small-multiples layout if overlay creates too much ambiguity.
- Add interaction to highlight one item across both series on hover/selection.
- Use a different encoding that supports clearer co-location for the same task (e.g., directly visualizing deltas).
