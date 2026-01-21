---
id: choose-diverging-scales-for-two-sided-values-with-meaningful-midpoint
title: Use Diverging Scales for Two-Direction Data Around a Midpoint
bibliography: references.bib
description: Apply a diverging color scale when values meaningfully split around a
  central point (e.g., negative/positive or neutral).
labels:
- chart:general
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:foundational
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a **diverging** color scale (bright/neutral middle, darker toward both ends in different hues) when your values have a **meaningful midpoint** and can move in **two directions** away from it (e.g., negative vs. positive, election results, Likert-style responses). [@muth_which_color_scale_2021]

## The Logic <!-- role: reason -->

A diverging scale encodes both magnitude and direction relative to a center: the midpoint reads as “neutral,” while hue indicates side and darkness indicates distance from the middle. That matches the semantics of bipolar data. [@muth_which_color_scale_2021]

- **The Principle:** Bipolar data needs a visual “center” plus two opposing directions.
- **The Evidence:** [@muth_which_color_scale_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish “above vs. below” a central reference and judge how far values are from that reference.
- **Data Type:** Quantitative values with a center (0, average, “neutral”). [@muth_which_color_scale_2021]
- **Audience:** General audiences interpreting directionality (gain/loss, agree/disagree). [@muth_which_color_scale_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your data only meaningfully ranges from low to high with no defensible midpoint.
- **Reason:** A diverging palette would suggest a center split that the data/story doesn’t support; use sequential instead. [@muth_which_color_scale_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** You must commit to (and explain) a midpoint; that can add cognitive overhead.
- **The Risk:** Choosing the wrong midpoint (or an unclear one) can mislead by implying “neutrality” where none exists. [@muth_which_color_scale_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a sequential gradient for data that readers interpret as negative vs. positive.
- **Why it fails:** Without two hues and a bright center, direction relative to the midpoint becomes harder to see. [@muth_which_color_scale_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can tell magnitude but not which side of the midpoint values fall on.
- **The Test:** Identify the midpoint category/value in the legend: if the chart’s message depends on that middle being obvious but it isn’t visually emphasized, you likely need (or need to improve) a diverging scale. [@muth_which_color_scale_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the sequential palette with a diverging one that has a clearly lighter midpoint and two distinct endpoint hues. [@muth_which_color_scale_2021]
- **Best Fix:** Define and label the midpoint explicitly (e.g., 0 or “neutral”) and align your diverging scale so colors change symmetrically away from it. [@muth_which_color_scale_2021]
