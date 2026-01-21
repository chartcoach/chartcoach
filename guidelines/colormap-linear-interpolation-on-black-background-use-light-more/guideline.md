---
id: colormap-linear-interpolation-on-black-background-use-light-more
title: Use Light-More Encoding on Dark Backgrounds When Colors Appear to Vary in Opacity
bibliography: references.bib
description: On dark (black) backgrounds, light-more can be faster than dark-more
  for certain sequential colormaps, reversing the usual expectation.
labels:
- chart:heatmap
- task:aggregate
- visual:color
- impact:speed
- data:matrix
- audience:general
- encoding:sequential-colormap
- background:dark
---

## The Rule <!-- role: advice -->

When showing a sequential colormap on a dark (black) background and you observe that the condition is one where light-more is faster than dark-more, choose light-more (map larger quantities to lighter colors).

## The Logic <!-- role: reason -->

The fastest mapping can flip on dark backgrounds for some colormap/background combinations in the reported experiments.

- **The Principle:** Background-dependent reversal in fastest encoded mapping for colormaps (time performance depends on background/scale combination).
- **The Evidence:** In the reported rankings, for at least one tested set of conditions on a black background, light-more is faster than dark-more (E-15 ≻ E-16 in aggregate-4; also E-11 ≻ E-9 in aggregate-3’s ordering, where a black-background light-more condition outranks a white-background light-more condition within that rank list) [@schlossMappingColorMeaning2019]. This kind of conditional rule extraction is the purpose of the collation workflow described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Fast aggregate judgments from a color-encoded grid on a dark UI theme.
- **Data Type:** Quantitative values encoded by color saturation in a grid/matrix.
- **Audience:** General users in dark-mode dashboards where speed matters.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your specific dark-background condition does not match one of the cases where light-more was faster in the evidence.
- **Reason:** Dark-background results were not uniform across all designs; for some black-background cases, dark-more remained faster (e.g., E-4 ≻ E-3; E-8 ≻ E-7; E-12 ≻ E-11) [@schlossMappingColorMeaning2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Inconsistent mapping across themes (light-mode vs dark-mode) if you switch mapping direction.
- **The Risk:** Users comparing across reports may misread values if they assume “dark always means more.”

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always forcing dark-more even in dark-mode themes to keep consistency.
- **Why it fails:** The experimental rankings include cases where that choice is slower than light-more on black backgrounds [@schlossMappingColorMeaning2019].

## How to Check <!-- role: check -->

- **Visual Sign:** On a black background, the mapping direction produces hesitation or repeated legend checking during quick “more vs fewer” judgments.
- **The Test:** Run a quick A/B with the same data: dark-more vs light-more, and measure time-to-answer for an aggregate question; prefer the faster mapping in your specific context, consistent with the approach advocated in [@zengReviewCollationGraphical2023] and supported by [@schlossMappingColorMeaning2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reverse the colormap direction for the dark-theme version only.
- **Best Fix:** Make mapping direction theme-aware (light vs dark background) and validate with a short timing test aligned to the aggregate task, mirroring the evidence-driven approach in [@zengReviewCollationGraphical2023] using results from [@schlossMappingColorMeaning2019].
