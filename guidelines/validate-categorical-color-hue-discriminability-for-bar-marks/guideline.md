---
id: validate-categorical-color-hue-discriminability-for-bar-marks
title: Validate Categorical Color Hue Discriminability for Bar Marks
bibliography: references.bib
description: Ensure categorical colors are distinguishable when applied to rectangular
  bar marks, considering bar thickness and length.
labels:
- chart:bar
- task:cluster
- visual:color
- visual:length
- visual:position
- impact:clarity
- data:categorical
- data:quantitative
- audience:general
- source:szafir2018
---

## The Rule <!-- role: advice -->

When encoding categories with color hue on rectangular bar marks, validate color distinguishability at your smallest bar thickness (and shortest bars if those occur).

## The Logic <!-- role: reason -->

- **The Principle:** Color discriminability varies with mark geometry; elongated rectangular marks can yield different discriminability behavior than point marks, and thickness/length changes can affect perceived color differences.
- **The Evidence:** The graphical perception collation includes this work as evidence about color-hue perception as used in bar-chart marks for clustering-style judgments [@zengReviewCollationGraphical2023]. Szafir empirically measures color-difference perception for bar-like marks and models how discriminability changes with bar size parameters [@szafirModelingColorDifference2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster—distinguish categories/groups using bar mark color hue.
- **Data Type:** Quantitative values encoded by bar length plus nominal category encoded by color hue (bar-chart design).
- **Audience:** General audiences on typical displays.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Bars are never thin (e.g., the design guarantees large bar thickness) and color hues are not doing any categorical separation work.
- **Reason:** The need to validate discriminability is driven by the presence of small marks and reliance on hue for cluster judgments.

## The Price <!-- role: costs -->

- **The Sacrifice:** Might constrain layout (e.g., requiring thicker bars or fewer categories).
- **The Risk:** Optimizing for discriminability at small thickness may reduce palette flexibility or increase visual intensity.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Validating the palette only on a sample chart where bars are wide and long.
- **Why it fails:** If real cases include thinner or shorter bars, the perceived separability of hues can change with mark geometry [@szafirModelingColorDifference2018], which is exactly the kind of condition-sensitive result the collation warns recommendation systems/designers must account for [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Some bar categories become hard to tell apart when bars are thin or short, causing category “collisions.”
- **The Test:** Render worst-case geometry (minimum thickness; include short bars if present) and verify categorical colors remain distinguishable.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase minimum bar thickness (or adjust layout to reduce thinning).
- **Best Fix:** Adjust the categorical hues (or their spacing) to remain distinguishable for the minimum thickness/length conditions, using mark-aware color-difference considerations from [@szafirModelingColorDifference2018] as cataloged in [@zengReviewCollationGraphical2023].
