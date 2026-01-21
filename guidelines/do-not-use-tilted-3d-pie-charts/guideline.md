---
id: do-not-use-tilted-3d-pie-charts
title: Do Not Use Tilted 3D Pie Charts
bibliography: references.bib
description: Avoid 3D pie charts because perspective distorts slice angles and perceived
  proportions, leading to incorrect comparisons.
labels:
- chart:pie
- task:compare
- visual:angle
- impact:honesty
- data:part-to-whole
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Do not use 3D or tilted pie charts to show part-to-whole proportions.

## The Logic <!-- role: reason -->

Projecting a 3D pie onto 2D distorts slice angles and areas based on depth, which can make some categories appear larger than the data supports, as demonstrated in [@szafirGoodBadBiased2018].

- **The Principle:** Perspective projection distorts angle/area judgments
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare market shares or part-to-whole quantities
- **Data Type:** Categorical shares summing to a whole
- **Audience:** General public and decision-makers who read quickly

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the paper for tilted 3D pies
- **Reason:** The described distortion mechanism directly undermines the intended reading in [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Decorative 3D styling
- **The Risk:** A 2D alternative may take more space if you choose a bar-based display

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the 3D pie but rotating it so “no slice is in front”
- **Why it fails:** Any perspective can still distort perceived angles and sizes, consistent with [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Front slices look inflated; back slices look compressed
- **The Test:** Compare the same data in 2D; if the apparent ranking or dominance changes, the 3D pie was distorting perception as in [@szafirGoodBadBiased2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the chart to a flat 2D pie
- **Best Fix:** Use a 2D bar-style comparison to support more reliable proportion judgments (the paper’s example replaces the 3D pie with a clearer alternative), per [@szafirGoodBadBiased2018]
