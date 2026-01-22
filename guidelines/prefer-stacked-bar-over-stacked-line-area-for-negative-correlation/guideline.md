---
id: prefer-stacked-bar-over-stacked-line-area-for-negative-correlation
title: Prefer stacked bar over stacked area or stacked line for negative-correlation
  discrimination
bibliography: references.bib
description: For negative correlations, stacked bar charts yield lower JNDs than stacked
  area or stacked line in correlation discrimination.
labels:
- chart:stacked-bar
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:practitioner
- direction:negative-correlation
---

## Use stacked bar (not stacked line or stacked area) when discriminating negative correlations in stacked charts <!-- role: advice -->

When you must use a stacked chart to compare correlation strength for negatively correlated data, choose stacked bars rather than stacked lines or stacked areas.

## Why stacked-bar encodings can yield lower JND than stacked line/area in this task <!-- role: reason -->

Even when visual forms look similar, viewers may rely on different perceptual cues across chart variants, leading to different discrimination thresholds. In the tested setting, stacked bars supported more precise correlation discrimination for negative correlations than stacked lines or stacked areas.

**Mechanism:** A chart that supports a more stable, consistently readable cue for the relationship yields smaller JND, meaning viewers can detect finer differences in correlation.

**Evidence:** For negative correlations, stacked bar charts significantly outperformed both stacked area and stacked line charts in JND-based correlation discrimination (both comparisons significant under corrected thresholds) [@harrisonRankingVisualizationsCorrelation2014a]. Stacked area and stacked line did not show a significant difference from each other under the paper’s corrected criterion [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** The paper excluded the positive-correlation versions of these stacked charts due to unreliable (near-chance) JNDs, so this guideline is limited to negative correlations.

## When this stacked-bar preference applies <!-- role: context -->

- **User Goal:** Compare correlation strength using a stacked-chart style.
- **Task:** Decide which of two displays shows stronger negative correlation.
- **Data:** Two quantitative variables represented through stacked components; ordering is fixed as in the tested design.
- **Chart Setting:** Static panels of similar size and density to those tested.
- **Audience:** Mixed literacy; needs reliable discrimination.
- **Success Criterion:** Lower JND than alternative stacked variants for the negative-correlation condition.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Your correlations are positive (or you need both signs) and you cannot validate stacked-bar performance for that sign in your setting. **Why:** The paper found positive versions of stacked charts to be unreliable under the tested staircase/JND procedure.

## Tradeoffs of preferring stacked bars <!-- role: costs -->

**Sacrifice:** Stacked bars may be less aesthetically consistent with line/area-heavy dashboards. **Risk:** The benefit is established for a specific discrimination task and negative correlations; it may not transfer to other tasks. **Mitigation:** Use this choice specifically for correlation-comparison tasks and validate if you generalize beyond that.

## Common mistakes with stacked charts for correlation <!-- role: mistakes -->

- **Mistake:** Assuming stacked area, stacked line, and stacked bar are interchangeable because they look similar. **Why it fails:** The paper shows significant JND differences among these variants for negative correlations.
- **Mistake:** Using stacked chart variants for positive-correlation discrimination without checking for chance-level performance. **Why it fails:** Several positive stacked variants were excluded due to unreliable discrimination.

## Quick checks for choosing among stacked variants <!-- role: check -->

**Failure Sign:** Viewers’ choices look random when comparing two correlations using a stacked chart. **Quick Check:** Ensure the chosen stacked variant and correlation sign have JND predictions meaningfully below the chance boundary. **Stronger Test:** Run a small staircase-based JND study comparing stacked bar vs stacked area/line for your negative-correlation range.

## What to do instead if stacked bars are not available <!-- role: fix -->

- Switch to a scatterplot for the correlation discrimination task.
- Use the paper’s Weber-model ranking to pick a non-stacked alternative with lower predicted JND for the sign you need.
- Limit the task to coarse bins of correlation strength where discrimination is still feasible.
- Split the view so that correlation comparisons are made in a chart type with reliable JNDs, while stacked charts serve other purposes.
