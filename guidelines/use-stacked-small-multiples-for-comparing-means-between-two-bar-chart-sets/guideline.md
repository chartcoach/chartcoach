---
id: use-stacked-small-multiples-for-comparing-means-between-two-bar-chart-sets
title: Stack Bar Charts Vertically to Compare Means Between Two Sets
bibliography: references.bib
description: Use vertically stacked bar-chart small multiples to support precise set-to-set
  mean comparisons.
labels:
- chart:bar
- task:compare
- task:rank
- visual:position
- visual:length
- impact:accuracy
- impact:clarity
- data:categorical
- audience:novice
- comparison:set-to-set
- source:jardine-2020
---

## The Rule <!-- role: advice -->

When users must judge which of two bar-chart sets has the larger mean, show the two charts as **vertically stacked** small multiples.

## The Logic <!-- role: reason -->

Stacking aligns bars so viewers can “slice” their gaze down the page and compare lengths with minimal spatial transformation, which improved discrimination precision for the **MAXMEAN** task in this paper’s staircase-threshold experiments [@jardinePerceptualProxiesVisual2020a].

- **The Principle:** Arrangement-dependent perceptual precision for set-to-set comparison
- **The Evidence:** Vertically stacked was the most precise arrangement for MAXMEAN, while superposed was least precise [@jardinePerceptualProxiesVisual2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which group has the higher overall average (mean) across corresponding categories
- **Data Type:** Two comparable sets of values shown as horizontal bars (same categories/order)
- **Audience:** Non-experts and general audiences making quick judgments under time limits

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is to find the **single biggest item change** between two sets.
- **Reason:** Item-to-item “biggest delta” comparisons were previously best supported by superposition/animation rather than separated arrangements; stacking is not the best general-purpose comparison layout across tasks [@jardinePerceptualProxiesVisual2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses more vertical space than adjacent layouts.
- **The Risk:** If many groups must be compared at once, stacking can reduce the number of panels visible and encourage scrolling.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Overlaying the two bar sets (superposed) to “reduce eye movement.”
- **Why it fails:** For mean comparisons, superposed charts produced the lowest precision in this study [@jardinePerceptualProxiesVisual2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** People hesitate or disagree on which set “looks higher overall,” especially when the bars interleave visually.
- **The Test:** Run a quick internal check: can a viewer compare corresponding bars by moving only up/down (not diagonally/across)?

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-layout the two series into a top/bottom stacked pair with consistent ordering.
- **Best Fix:** Keep stacked layout and ensure the two sets share identical category order so the vertical scan maps bar-to-bar cleanly [@jardinePerceptualProxiesVisual2020a].
