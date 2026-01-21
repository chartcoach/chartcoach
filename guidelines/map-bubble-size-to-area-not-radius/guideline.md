---
id: map-bubble-size-to-area-not-radius
title: Map Bubble Size to Area, Not Radius
bibliography: references.bib
description: Prevent exaggerated magnitude impressions by ensuring bubble sizes scale
  with area, not radius.
labels:
- chart:bubble
- task:compare
- visual:area
- impact:integrity
- data:quantitative
- audience:general
- distortion:area-as-quantity
---

## The Rule <!-- role: advice -->

When using bubble charts, scale bubbles so the *area* corresponds to the data value; do not map values to the radius (or diameter).

## The Logic <!-- role: reason -->

If values are mapped to radius/diameter, the resulting area grows nonlinearly, making one value look much larger than it is and pushing viewers toward exaggerated “how much bigger” judgments.

- **The Principle:** Nonlinear size encoding inflates perceived differences
- **The Evidence:** Pandey et al. found that the “area as quantity” distortion significantly increased “how much” responses versus a correctly scaled control (Mann–Whitney U, p = 0.0007), demonstrating message exaggeration even with correct numbers shown [@pandeyHowDeceptiveAre2015].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare magnitudes between entities using bubble size.
- **Data Type:** A small set of quantitative values represented by circles.
- **Audience:** Mixed-literacy audiences interpreting infographic-style charts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not encoding quantity with bubble size (size is decorative or encodes a non-quantitative attribute).
- **Reason:** The paper’s finding concerns deception when size is used as the quantitative channel [@pandeyHowDeceptiveAre2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** Correct area scaling can make moderate differences look less dramatic.
- **The Risk:** Stakeholders seeking “impactful” visuals may resist because the chart appears less persuasive.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding value labels but leaving bubbles scaled by radius/diameter.
- **Why it fails:** The study’s charts included accurate numbers, yet distorted size mapping still shifted message-level judgments [@pandeyHowDeceptiveAre2015].

## How to Check <!-- role: check -->

- **Visual Sign:** Doubling a value makes the bubble look more than twice as big in area.
- **The Test:** Pick two values where one is 2× the other; verify that the bubble’s *area* (not radius) appears roughly 2×.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change the size scale so the plotted circle area is proportional to the value.
- **Best Fix:** If precise comparison is important, switch to an axis-based chart (e.g., bars) rather than relying on area judgments, which the paper highlights as deception-prone when mis-scaled [@pandeyHowDeceptiveAre2015].
