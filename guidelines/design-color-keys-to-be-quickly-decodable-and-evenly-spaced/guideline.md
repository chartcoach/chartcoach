---
id: design-color-keys-to-be-quickly-decodable-and-evenly-spaced
title: Make the Color Key Quickly Decodable
bibliography: references.bib
description: Build choropleth legends that show the full scale, include the midpoint
  for diverging schemes, and use evenly spaced numeric labels.
labels:
- chart:choropleth
- task:interpret
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- custom:legend
---

## The Rule <!-- role: advice -->

Design the color key to be instantly readable: show low and high (plus 2–4 intermediates) for sequential schemes, include the center value for diverging schemes, and label values in equal intervals.

## The Logic <!-- role: reason -->

The legend is the decoding bridge between color and meaning; uneven or incomplete labeling increases cognitive work and slows comprehension. Muth stresses that color keys are crucial, recommends showing endpoints plus a few intermediates, using equal-interval labels (e.g., 0/25/50), and including the center value for diverging scales [@muth_choroplethmaps_2018].

- **The Principle:** Reduce decoding friction in legends
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand what colors mean and estimate values/ranges
- **Data Type:** Sequential or diverging choropleth scales
- **Audience:** General readers who will glance between map and key

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the post
- **Reason:** The post frames these legend features as necessary for comprehension [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** A larger or more prominent legend may take space.
- **The Risk:** Overstuffing the key with too many ticks/colors can itself become confusing [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using irregular numeric labels in the key (e.g., 0, 15, 50)
- **Why it fails:** Readers can’t quickly infer the mapping or interpolate consistently [@muth_choroplethmaps_2018].
- **The Wrong Fix:** Omitting the midpoint on diverging scales
- **Why it fails:** Readers can’t tell what “neutral” corresponds to [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must reread the legend to interpret colors; the key feels “mathy.”
- **The Test:** Can you explain the scale in one glance (endpoints, spacing, and—if diverging—the center)? If not, redesign the key [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce to endpoints + a few evenly spaced intermediate labels; add the center label for diverging scales [@muth_choroplethmaps_2018].
- **Best Fix:** Rework the scale (including stops) so the legend can use clean, equal-interval labeling without confusion [@muth_choroplethmaps_2018].
