---
id: keep-axis-scales-consistent-across-comparable-plots
title: Keep Axis Scales Consistent Across Comparable Plots
bibliography: references.bib
description: Use the same axis ranges when showing the same variables across multiple
  plots to avoid shape-based misinterpretation.
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

When multiple plots show the same variables for comparison, use identical axis ranges and scaling across all plots.

## The Logic <!-- role: reason -->

Viewers unconsciously extract the “shape” and gist of a plot; changing scales changes apparent shape and can create false visual features (e.g., crossings) that drive incorrect conclusions, as explained in [@szafirGoodBadBiased2018].

- **The Principle:** Gist-based shape perception
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare trends or levels across panels/conditions/time
- **Data Type:** Small multiples, faceted charts, before/after comparisons
- **Audience:** Any audience relying on visual comparison

## When to Break It <!-- role: exceptions -->

- **Scenario:** Panels intentionally show different variables or fundamentally different units
- **Reason:** Identical scales would be meaningless or misleading when the quantities differ (the rule is specifically for “same variables” comparisons in [@szafirGoodBadBiased2018]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Some panels may look sparse if their data uses only a small part of the shared range
- **The Risk:** Small variations can become harder to see

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Auto-scaling each panel to its own min/max to “maximize detail”
- **Why it fails:** It changes apparent shapes and can fabricate salient features, consistent with [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Two panels suggest different trend relationships (like a crossover) that disappear when rescaled
- **The Test:** Temporarily enforce a shared range; if the story changes materially, inconsistent scaling was misleading (as discussed in [@szafirGoodBadBiased2018])

## How to Fix <!-- role: fix -->

- **Quick Fix:** Lock axes to the same min/max across panels
- **Best Fix:** Re-express the analysis target (e.g., show relative change from a baseline) so the shared scale supports the actual question, per [@szafirGoodBadBiased2018]
