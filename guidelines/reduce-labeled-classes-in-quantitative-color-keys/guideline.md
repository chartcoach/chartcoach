---
id: reduce-labeled-classes-in-quantitative-color-keys
title: Label Only Visibly Distinct Values in Quantitative Color Keys
bibliography: references.bib
description: "Avoid overcrowded numeric legends by labeling fewer classes\u2014only\
  \ where colors and boundaries are clearly distinguishable."
labels:
- chart:map
- task:estimate
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- complexity:intermediate
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

In sequential or diverging color keys, don’t label every class by default; label fewer values (e.g., every other class or just key points) and only label colors that are visibly distinct.

## The Logic <!-- role: reason -->

Too many labels create overlap and visual busyness, making the legend harder to read and less inviting. Labeling only distinct steps preserves readability while still communicating the scale, as Muth recommends for both classed and unclassed scales [@muth_color_keys_2023].

- **The Principle:** Prevent label crowding; prioritize discriminable steps
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding approximate magnitude and direction from color
- **Data Type:** Quantitative color scales with many classes or smooth interpolation
- **Audience:** Readers who need a quick sense of “more/less” rather than exact numbers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is static and readers must read exact values from the key (no tooltips), or classes/boundaries are subtle
- **Reason:** Too few labels can make the scale feel underspecified; Muth notes static charts should err toward showing more values when exact reading is needed [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Precision in reading exact numeric values from the legend
- **The Risk:** Readers may overgeneralize or misestimate if intermediate values aren’t labeled [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Labeling every class even when labels overlap or the colors are nearly indistinguishable
- **Why it fails:** The legend becomes cluttered, and extra labels don’t add usable information because readers can’t reliably tell adjacent shades apart [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Numbers collide, appear cramped, or the gradient looks “busy.”
- **The Test:** Look at adjacent labeled colors—if you can’t clearly see the difference, the extra label isn’t helping and should be removed [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove every other label (or keep only min/max and center for diverging scales).
- **Best Fix:** Choose label positions based on what you want readers to learn (trend vs precision) and ensure labels correspond only to clearly distinguishable color steps [@muth_color_keys_2023].
