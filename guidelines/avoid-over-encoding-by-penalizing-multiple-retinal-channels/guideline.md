---
id: avoid-over-encoding-by-penalizing-multiple-retinal-channels
title: Penalize Over-Encoding with Multiple Retinal Channels
bibliography: references.bib
description: Prefer simpler encodings by discouraging unnecessary combinations like
  color+shape or color+size.
labels:
- chart:scatter
- task:explore
- visual:color
- impact:readability
- data:multivariate
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

Do not recommend encodings that stack multiple retinal channels (e.g., color+shape, color+size) unless necessary; rank them lower than simpler alternatives.

## The Logic <!-- role: reason -->

Compass explicitly penalizes over-encoding because it can impede interpretation, and it ranks candidates by an effectiveness score that accounts for these penalties [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Reduce perceptual load by avoiding unnecessary encodings
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Fast, low-effort comprehension while browsing many charts
- **Data Type:** Variable sets where one grouping variable is sufficient
- **Audience:** Analysts scanning recommended thumbnails

## When to Break It <!-- role: exceptions -->

- **Scenario:** Multiple distinct groupings must be shown simultaneously and can’t be expressed otherwise within the allowed channels.
- **Reason:** Avoiding multiple retinal channels may hide important structure.

## The Price <!-- role: costs -->

- **The Sacrifice:** Some richly annotated multivariate encodings won’t appear.
- **The Risk:** Users may need to expand/drill down or change variable selections to see additional dimensions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding both color and shape by default “to show more dimensions.”
- **Why it fails:** It increases cognitive effort and can reduce legibility, especially in thumbnail galleries [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Many recommended views use two or more retinal encodings for grouping.
- **The Test:** Remove one retinal channel and see if the chart’s intended message remains; if yes, you were over-encoding.

## How to Fix <!-- role: fix -->

- **Quick Fix:** In ranking, apply a penalty to candidates using multiple retinal channels.
- **Best Fix:** Offer alternative encodings in an expanded view so users can opt into additional channels when needed [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
