---
id: choose-independent-scales-when-comparing-trends-within-regions
title: Use Independent Scales When the Task Is Trend Comparison Within Each Region
bibliography: references.bib
description: When comparing temporal trends across regions, allow per-region y-axis
  scaling to preserve within-region change visibility.
labels:
- chart:area
- task:compare
- visual:scale
- impact:trend-detection
- data:temporal
- audience:expert
- custom:small-multiples
---

## The Rule <!-- role: advice -->

If users need to see trends within each geographic region over time, allow each region’s chart to use its own y-axis scale rather than forcing one global scale.

## The Logic <!-- role: reason -->

The paper’s chronology geography-by-region area charts use separate y-axes so users can perceive local temporal variation; a shared global scale can flatten smaller-range regions and make changes hard to see (e.g., 146→181 becomes imperceptible against a 0→969 scale). [@olaSimpleChartsDesign2016]

- **The Principle:** Preserve within-group variation when the analytic goal is within-group trend perception
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify whether mortality is rising/falling within each region across years
- **Data Type:** Time series by multiple regions with very different magnitudes
- **Audience:** Analysts comparing regional trend shapes rather than exact cross-region magnitudes

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary task is direct magnitude comparison between regions at the same time point.
- **Reason:** Independent scales make absolute cross-region comparisons harder. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduces comparability of absolute levels across regions.
- **The Risk:** Users may mistakenly compare heights across panels as if scales were shared. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using one global scale because it “seems more honest,” even when it hides meaningful local change.
- **Why it fails:** Regions with smaller ranges look constant and trends are missed. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple region lines/areas appear flat despite known variation, or small changes vanish.
- **The Test:** For a low-magnitude region, compute min–max across time; if the visual shows near-zero variation, a global scale is masking trends. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to per-panel scaling and label axes clearly for each panel.
- **Best Fix:** Provide interaction to toggle between “within-region trend mode” (independent scales) and “between-region magnitude mode” (shared scale), matching the user’s task. [@olaSimpleChartsDesign2016]
