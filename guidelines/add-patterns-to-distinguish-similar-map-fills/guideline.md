---
id: add-patterns-to-distinguish-similar-map-fills
title: Add Patterns to Differentiate Area Fills
bibliography: references.bib
description: Use patterns on area fills (especially maps) to distinguish regions when
  colors alone are ambiguous for colorblind readers.
labels:
- chart:map
- task:distinguish
- visual:pattern
- visual:color
- impact:accessibility
- data:geospatial
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

When area fills (e.g., in maps) are hard to tell apart by color, add a pattern to at least one area so regions remain distinguishable without relying on hue.

## The Logic <!-- role: reason -->

Patterns provide a second visual variable that remains visible when hues converge under colorblindness; the post shows a map unreadable to red-blind readers becoming readable after adding a pattern, while cautioning that patterns can change perceived brightness [@muth_colorblindness_2020].

- **The Principle:** Redundant encoding for filled areas
- **The Evidence:** The article demonstrates a color-only map failing for red-blind readers and a pattern overlay fixing it, with a warning that pattern lines can alter perceived lightness [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which region belongs to which category
- **Data Type:** Choropleths or categorical region maps with adjacent areas
- **Audience:** General audiences, including colorblind readers [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Very small areas or dense boundaries where patterns would moiré or overwhelm
- **Reason:** Patterns can reduce legibility and make boundaries hard to see [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity and a clean aesthetic
- **The Risk:** Patterns can change perceived brightness and unintentionally shift emphasis [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Applying multiple different patterns everywhere
- **Why it fails:** Patterns are hard to use well and can quickly create clutter; the goal is selective disambiguation [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** In simulation, neighboring regions still look the same; or patterns make one region look much lighter/darker unintentionally
- **The Test:** Simulate colorblindness and also check perceived lightness after pattern application (e.g., grayscale) [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a simple, low-frequency hatch to one competing category and adjust stroke/spacing to maintain readability
- **Best Fix:** Combine pattern with improved lightness separation and, where possible, direct labeling or interactive tooltips for confirmation [@muth_colorblindness_2020].
