---
id: use-quantile-based-interpolation-for-continuous-scales-to-redistribute-gradient
title: Redistribute Continuous Gradients with Quantile Interpolation
bibliography: references.bib
description: For unclassed scales, use median/quartile/quintile/decile interpolation
  to stretch dense value ranges across more of the gradient and increase color variation.
labels:
- chart:choropleth
- task:reveal-patterns
- visual:color
- impact:contrast
- data:quantitative
- audience:general
- complexity:intermediate
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

On continuous (unclassed) color scales with skewed data, use median/quartile/quintile/decile interpolation to redistribute the gradient so dense value ranges occupy more of the color ramp. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Quantile-based continuous interpolation keeps every value unique but “stretches” the gradient segments between quantile cut points, causing more of the map to use mid/dark colors rather than clustering near the light end under linear mapping. [@muth_interpolation_2022]

- **The Principle:** Nonlinear gradient stretching via quantiles
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Increasing visible variation while retaining a continuous legend
- **Data Type:** Quantitative, skewed distributions where linear continuous mapping yields many similar light tones
- **Audience:** Readers who benefit from continuous shading but need more differentiation among typical values [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need color differences to correspond proportionally to numeric differences across the full range.
- **Reason:** Quantile stretching makes equal color steps correspond to unequal value steps, altering perceived magnitude differences. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Proportionality between value distance and color distance.
- **The Risk:** The map can suggest that mid-to-high values are more prevalent (or more different) than they are under linear mapping. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing the number of cuts (e.g., moving to deciles) just to make the map darker.
- **Why it fails:** It can compress color differences among true high outliers while exaggerating differences around common values. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Many more regions become mid/dark, and the gradient “reaches” dark colors earlier than in linear.
- **The Test:** Compare two specific value gaps: if a small numeric gap near the center produces a larger color jump than a much larger numeric gap near the high end, quantile stretching is strongly affecting perception. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Step back from deciles to quartiles/quintiles or try Natural interpolation to avoid over-compressing outliers. [@muth_interpolation_2022]
- **Best Fix:** Choose the quantile granularity that supports your story goal (pattern discovery vs. outlier emphasis) and sanity-check how representative the darkest colors are of actual rarity. [@muth_interpolation_2022]
