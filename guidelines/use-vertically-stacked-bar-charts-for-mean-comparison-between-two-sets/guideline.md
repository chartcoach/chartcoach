---
id: use-vertically-stacked-bar-charts-for-mean-comparison-between-two-sets
title: Use vertically stacked bar charts to compare which of two sets has the larger
  mean
bibliography: references.bib
description: Vertically stacked bar charts support more precise judgments of which
  set has the larger mean than other arrangements.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- comparison:set-to-set
---

## Use vertical stacking for set-to-set mean comparisons <!-- role: advice -->

Use two vertically stacked bar charts when the user must decide which of two bar-chart datasets has the larger mean. Keep the two sets in separate chart areas rather than overlapping them.

## Why vertical stacking improves mean comparison precision <!-- role: reason -->

Separating the two sets into a clean vertical stack helps the visual system treat each set as its own unit and compare set-level proxies (such as ensemble bar lengths or the centroid of bar areas) without needing to untangle overlapping marks. When marks are horizontally extending bars, vertical stacking also supports fast “slicing” comparisons of lengths between corresponding bars across the two sets.

**Mechanism:** Vertical separation reduces interference between the two sets, making global, set-based perceptual proxies easier to apply when judging overall average level.

**Evidence:** In timed comparisons of “which set has the biggest mean” for two horizontal bar-chart sets, precision (smaller titers at threshold) was best with vertically stacked charts and worst with superposed charts [@jardinePerceptualProxiesVisual2020a].

**Notes:** The same arrangement pattern held for both mean and range tasks in this study, even though different perceptual proxies best matched each task.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Decide which of two groups is higher on average.
- **Task:** Biggest mean (average) comparison between two sets of values shown as bars.
- **Data:** Two series with multiple items each (the study used 7 items per set).
- **Chart Setting:** Brief viewing time (about 1.5 seconds) with a forced response after the chart disappears.
- **Audience:** Non-expert viewers making perceptual judgments.
- **Success Criterion:** High precision in discriminating small mean differences.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary task is an item-to-item change comparison (e.g., “which item changed the most between two states”). **Why:** This study’s mean-comparison result contrasts with earlier evidence summarized in the same paper that item-focused comparisons can benefit from overlap/animation rather than separation [@jardinePerceptualProxiesVisual2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Vertically stacked small multiples use more vertical space than superposed charts. **Risk:** If space constraints force very small charts, the benefit of stacking may be reduced by legibility limits. **Mitigation:** Treat stacking as the default arrangement choice for mean comparisons when you can afford the vertical space.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Overlapping (superposing) the two bar-chart sets to “reduce eye movements” for a mean judgment. **Why it fails:** Mean comparisons were least precise in the superposed arrangement in the study [@jardinePerceptualProxiesVisual2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers frequently disagree on which set is higher on average unless the difference is visually large. **Quick Check:** Compare a stacked version to a superposed version and see whether the decision becomes obvious without extended scrutiny. **Stronger Test:** Run a small timed pilot where you shrink the difference in means until accuracy drops; prefer the arrangement that still supports correct choices at smaller differences.

## What to do instead if stacking is not possible <!-- role: fix -->

- Use a horizontally adjacent small-multiple layout rather than overlapping the two sets.
- Use a mirrored variant only if it does not reduce readability for your audience.
- Reduce reliance on overlap by separating sets into distinct chart regions even within the same figure.
- If overlap is required, consider changing the task framing away from mean judgment to something overlap better supports.
