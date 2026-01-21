---
id: prefer-rainbow-isarithmic-over-sequential-for-determining-range-on-quantitative-maps
title: Use Rainbow Hue on Isarithmic Maps to Determine Ranges
bibliography: references.bib
description: For determining range on quantitative maps, the rainbow isarithmic condition
  ranked best in accuracy.
labels:
- chart:map
- task:determine-range
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- map-type:isarithmic
- color-scheme:rainbow
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

For determine-range tasks on quantitative maps, prefer an isarithmic map with a rainbow (hue-based) scheme over the sequential (saturation-based) alternatives.

## The Logic <!-- role: reason -->

In the reported comparison, the isarithmic rainbow condition achieved the highest accuracy rank for determine-range, with multiple significant pairwise differences against the other conditions.

- **The Principle:** For some range-judgment tasks, hue variation in a continuous-field representation can be competitive
- **The Evidence:** For **determine-range (accuracy)**, the rank order is **E-2 (RC-Isa)** > **E-4 (SC-Isa)** > **E-1 (RC-Choro)** > **E-3 (SC-Choro)**, with significant pairwise differences including E-2 outperforming E-4, E-1, and E-3 [@golbiowskaRainbowDashIntuitiveness2022]. This task-conditioned ranking is captured in the collation for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine the span/range of values depicted on the map (determine-range)
- **Data Type:** Quantitative values displayed as an isarithmic field with ordered classes
- **Audience:** General audiences reading quantitative maps

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s task is finding extremes (find-extremum).
- **Reason:** The same study ranks sequential schemes above rainbow schemes for find-extremum in both accuracy and time; optimize for the actual task [@golbiowskaRainbowDashIntuitiveness2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potential loss of intuitive global ordering of colors compared to sequential schemes.
- **The Risk:** Users may disagree on the implied order of rainbow hues, which can hurt other tasks not targeted here.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using rainbow on a choropleth map and expecting the same determine-range benefit.
- **Why it fails:** The top-performing condition for determine-range accuracy is specifically **rainbow + isarithmic** (E-2), not rainbow choropleth (E-1) [@golbiowskaRainbowDashIntuitiveness2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Users misjudge the overall span (e.g., systematically underestimate or overestimate the range).
- **The Test:** Give users a quick “what is the approximate range shown?” task on both (RC-Isa) and (SC-Isa); compare accuracy, mirroring the reported metric [@golbiowskaRainbowDashIntuitiveness2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If you already use an isarithmic map, switch the sequential palette to the rainbow palette for determine-range views.
- **Best Fix:** In a recommendation system, condition palette+map-type selection on task: for determine-range, prioritize the **RC-Isa** design, consistent with the collated ranking [@zengReviewCollationGraphical2023; @golbiowskaRainbowDashIntuitiveness2022].
