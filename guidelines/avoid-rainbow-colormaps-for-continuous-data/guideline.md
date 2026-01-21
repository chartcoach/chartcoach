---
id: avoid-rainbow-colormaps-for-continuous-data
title: Avoid Rainbow Colormaps for Continuous Data
bibliography: references.bib
description: Use perceptually appropriate sequential or diverging colormaps instead
  of rainbow schemes for ordered or continuous values.
labels:
- chart:heatmap
- task:interpret
- visual:color
- impact:accuracy
- data:continuous
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Do not use rainbow (red–yellow–green–blue) colormaps to encode ordered or continuous data.

## The Logic <!-- role: reason -->

Rainbow colormaps create non-uniform and non-monotonic perceived color differences, which distorts perceived value differences and introduces false banding/grouping that can imply discontinuities in smooth data, as described in [@szafirGoodBadBiased2018].

- **The Principle:** Perceptual non-uniformity and categorical grouping in hue
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurately see relative magnitudes and smooth gradients
- **Data Type:** Ordered/continuous scalar fields (e.g., density maps, choropleths, heatmaps)
- **Audience:** General audiences and experts alike

## When to Break It <!-- role: exceptions -->

- **Scenario:** The data is categorical (unordered groups)
- **Reason:** The grouping effect of distinct hues can be acceptable for categories, per [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less “flashy” or familiar aesthetics compared to a rainbow default
- **The Risk:** If the replacement palette is chosen poorly, it may reduce contrast in key ranges

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the rainbow but adding a legend or claiming users “learn it”
- **Why it fails:** The perceptual distortions occur at a glance and persist even for experienced users, according to [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Apparent bands/regions in what should be smooth variation; unequal “jumps” between neighboring colors
- **The Test:** Look for whether equal data steps appear as unequal color steps across the scale

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the rainbow with a single-hue sequential colormap
- **Best Fix:** Choose a sequential colormap for magnitude-only data or a diverging colormap when there is a meaningful midpoint (e.g., baseline/zero), as recommended in [@szafirGoodBadBiased2018]
