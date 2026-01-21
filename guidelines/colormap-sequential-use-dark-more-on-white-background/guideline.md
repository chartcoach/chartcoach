---
id: colormap-sequential-use-dark-more-on-white-background
title: Encode Larger Values with Darker Colors on Light Backgrounds
bibliography: references.bib
description: On light (white) backgrounds, map higher quantitative values to darker
  colors to reduce response time in colormap interpretation.
labels:
- chart:heatmap
- task:aggregate
- visual:color
- impact:speed
- data:matrix
- audience:general
- encoding:sequential-colormap
- background:light
---

## The Rule <!-- role: advice -->

When showing quantitative values with a sequential colormap on a light (white) background, map larger quantities to darker colors (dark-more), not lighter colors (light-more).

## The Logic <!-- role: reason -->

People interpret these colormaps faster when the encoded mapping aligns with their inferred mapping for “more” on light backgrounds in this setup.

- **The Principle:** Faster interpretation when encoded mapping matches inferred mapping under the given background/colormap conditions.
- **The Evidence:** In the collated results, dark-more on a white background ranks faster than light-more on a white background for multiple tested color scales/conditions (e.g., E-2 ≻ E-1; E-6 ≻ E-5; E-10 ≻ E-9; E-14 ≻ E-13) [@schlossMappingColorMeaning2019]. This structured evidence is captured and organized for recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly aggregating/deciding which side/region has “more” in a color-encoded matrix.
- **Data Type:** Quantitative values shown as a grid/matrix (heatmap-like), with ordinal X and nominal Y.
- **Audience:** General audiences performing quick judgments (time-focused performance).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not on a light/white background (e.g., dark/black or other colored backgrounds).
- **Reason:** The ranking changes with background; “dark-more” is not always the fastest mapping outside the white background conditions [@schlossMappingColorMeaning2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose flexibility if your style guide prefers “light-more” mappings.
- **The Risk:** If the visualization is later placed on a dark background, the mapping may no longer be fastest to interpret [@schlossMappingColorMeaning2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping light-more encoding on white backgrounds because “the legend explains it anyway.”
- **Why it fails:** In these experiments, response time still favored dark-more on white backgrounds even though legends were present and varied to force legend reading [@schlossMappingColorMeaning2019].

## How to Check <!-- role: check -->

- **Visual Sign:** On a white background, the visually darker cells correspond to smaller values (light-more mapping).
- **The Test:** Show the chart briefly to a peer and ask “which side has more?”; if they hesitate or re-check the legend, you may be violating the faster mapping found here [@schlossMappingColorMeaning2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reverse the colormap direction so darker corresponds to larger values.
- **Best Fix:** Standardize a “dark-more on light background” default in your recommendation/rendering pipeline for this task context, as suggested by the collated guidance approach in [@zengReviewCollationGraphical2023] based on evidence from [@schlossMappingColorMeaning2019].
