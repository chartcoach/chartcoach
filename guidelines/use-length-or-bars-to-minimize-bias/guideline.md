---
id: use-length-or-bars-to-minimize-bias
title: Use Length or Bars to Minimize Systematic Bias
bibliography: references.bib
description: To ensure users do not systematically over- or under-estimate values,
  prefer length or bar encodings over area or angle.
labels:
- chart:bar
- visual:length
- visual:position
- task:estimate
- impact:truthfulness
- data:quantitative
---

## The Rule <!-- role: advice -->
To minimize **systematic bias** (the tendency to consistently over- or under-estimate values), use **Length** (e.g., misaligned bars) or **Position-Bar** encodings. Avoid Angle or Area when unbiased estimation is critical.

## The Logic <!-- role: reason -->
While Area charts may be precise (consistent), they suffer from perceptual scaling issues. Length and aligned Position are the most robust against systematic error.
*   **The Evidence:** In bias rankings for datasets with 4 and 8 marks, **Length** and **Position-Bar** encodings were significantly less biased than Angle or Area encodings [@mccoleman_rethinking_2022].
*   **The Principle:** Humans perceive linear length more accurately than 2D area or radial angles, which are subject to psychophysical distortions (e.g., Stevens' Power Law) noted in foundational reviews [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate estimation of magnitude where "truthfulness" is more important than "gist."
*   **Data Type:** Quantitative comparisons where fair comparison is legally or analytically required (e.g., financial reporting).
*   **Audience:** Auditors, scientists, or decision-makers requiring objective accuracy.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is extremely sparse (e.g., 2 items) and memory precision is preferred over bias accuracy.
*   **Reason:** For very small N (2 marks), Angle and Area can be extremely precise and memorable, even if slightly biased [@mccoleman_rethinking_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the compactness of a Bubble chart or the "part-to-whole" metaphor of a Pie chart.
*   **The Risk:** Bar charts can become visually heavy or cluttered with many categories.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Donut chart to "clean up" a Pie chart.
*   **Why it fails:** Angles and Areas (even in donuts) induce higher systematic bias than linear bars.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using circles, squares, or wedges to represent linear data?
*   **The Test:** Ask users to estimate the ratio between two values (e.g., "Is A twice as big as B?"). If they consistently get it wrong in the same direction, the encoding is biased.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Unwrap the radial chart into a **Bar Chart**.
*   **Best Fix:** Use a **Bar Chart** or **Dot Plot** (using position on a common scale) to ensure linear mapping of values.
