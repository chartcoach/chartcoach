---
id: use-diverging-palettes-for-deviation-from-a-baseline
title: Use a Diverging Palette for Deviations from a Baseline
bibliography: references.bib
description: When values diverge around a meaningful midpoint, use a diverging gradient
  with distinct hues on each side and a light grey center.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- scale:diverging
---

## The Rule <!-- role: advice -->

When showing deviation from a baseline, use a diverging color gradient with clearly distinguishable hues on both sides and a light grey center.

## The Logic <!-- role: reason -->

Muth recommends diverging palettes to emphasize how a variable differs from a baseline (e.g., national average). Distinct hues clarify direction (above/below), and a light grey midpoint avoids an overly stark center [@muth_colors_2018].

- **The Principle:** Encode direction around a meaningful midpoint with symmetric contrast.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** See both magnitude and direction of difference relative to a reference value.
- **Data Type:** Quantitative values centered on a meaningful midpoint (0, average, target).
- **Audience:** General readers interpreting “above vs. below” quickly.

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is no meaningful midpoint/baseline (only “more” vs. “less”).
- **Reason:** A sequential gradient better matches a one-direction magnitude story [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires choosing and balancing two hue families and defining a defensible midpoint.
- **The Risk:** If hues aren’t clearly distinguishable, viewers may miss the direction of deviation [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a diverging palette with a white center.
- **Why it fails:** Muth suggests the center should ideally be light grey, not white, to avoid an overly bright midpoint impression [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** It’s unclear which areas are above vs. below the baseline at a glance.
- **The Test:** Identify a few known above/below examples and confirm the palette makes their direction immediately obvious [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the midpoint color with a light grey and increase hue separation between sides.
- **Best Fix:** Redesign the diverging palette so both sides have clearly distinguishable hues and balanced lightness progression away from the center [@muth_colors_2018].
