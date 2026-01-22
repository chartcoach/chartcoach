---
id: use-linear-or-rounded-cuts-for-even-distributions-or-to-highlight-outliers
title: Use linear (or rounded) interpolation for even distributions or when you want
  outliers to stand out
bibliography: references.bib
description: Choose equal-distance steps (or rounded variants) when values are fairly
  evenly spread or when emphasizing extreme outliers is the point.
labels:
- chart:map-choropleth
- task:detect-outliers
- visual:color
- impact:truthfulness
- data:quantitative
- audience:general
- complexity:basic
---

## Use linear or rounded interpolation when values are fairly even (or outliers are the story) <!-- role: advice -->

Use linear interpolation for classed or unclassed color scales when the data range is not dominated by extreme outliers, or when you intentionally want the few extremes to pop strongly against the rest. If you need more legible legend thresholds in a classed scale, use a rounded-values variant that keeps roughly equal distances but with simpler numbers.

## Equal-distance steps preserve the numeric scale and amplify extremes in skewed data <!-- role: reason -->

Linear interpolation maps equal numeric changes to equal color changes across the full min-to-max range, which preserves a straightforward relationship between value and shade. In skewed distributions with large outliers, this allocates much of the gradient to the sparse high end, so the dense low end gets compressed into similar light shades and the few extremes gain strong contrast.

**Mechanism:** A linear mapping spends color range proportional to numeric range rather than proportional to how many data points occupy that range, so sparse extremes can consume much of the palette.

**Evidence:** With skewed county unemployment data, linear interpolation caused a large majority of regions to share the lightest color while the few high-outlier regions appeared in much darker shades, strongly drawing attention to those outliers [@muth_interpolation_2022]. Rounded class breaks can improve legend readability while staying close to equal-distance segmentation, but still behave similarly to linear segmentation with outliers [@muth_interpolation_2022].

**Notes:** This approach is intuitive for readers because cut points or gradient progression follow the raw numeric scale directly.

## Where linear/rounded interpolation is the right fit <!-- role: context -->

- **User Goal:** See values on an “as-measured” scale and/or quickly spot extreme regions.
- **Task:** Identify outliers; interpret magnitude in absolute terms.
- **Data:** Quantitative data with a fairly even spread, or skewed data where highlighting extremes is desired.
- **Chart Setting:** Choropleth maps using classed (stepped) or unclassed (continuous) color scales.
- **Audience:** Readers who expect equal numeric steps to look like equal color steps.
- **Success Criterion:** Outliers are immediately visible, and the legend thresholds are easy to interpret.

## When linear/rounded interpolation is a poor choice <!-- role: exceptions -->

**Break it when:** Most values cluster tightly and a few outliers stretch the maximum far to the right. **Why:** The cluster can collapse into near-identical light shades, obscuring geographic variation among the majority of regions [@muth_interpolation_2022].

## Tradeoffs of linear/rounded interpolation <!-- role: costs -->

**Sacrifice:** You may lose within-cluster detail when the distribution is skewed. **Risk:** Readers may conclude “almost everywhere is the same” when meaningful differences exist among the dense majority. **Mitigation:** Pair the map with a distribution view (histogram/rug) or switch interpolation if pattern-reading is the primary goal [@muth_interpolation_2022].

## Frequent misuse patterns <!-- role: mistakes -->

**Mistake:** Keeping linear interpolation on skewed data when the intended message is geographic pattern among typical (non-outlier) regions. **Why it fails:** The map allocates too little color variation to the dense portion of the distribution, so patterns remain hidden [@muth_interpolation_2022].

## Checks for whether linear/rounded is working <!-- role: check -->

**Failure Sign:** A dominant “wash” of the lightest shade covers most regions. **Quick Check:** Count (or estimate) what share of regions fall into the first class or the lightest half of the gradient; if it’s overwhelmingly large, the map likely hides variation [@muth_interpolation_2022]. **Stronger Test:** Compare a linear map against a distribution-aware alternative and see whether meaningful regional differences among typical values appear only in the alternative [@muth_interpolation_2022].

## What to do instead if linear/rounded hides patterns <!-- role: fix -->

- Use a quantile-based interpolation to force more regions into mid/dark shades when you need to reveal variation among the majority [@muth_interpolation_2022].
- Use a natural-style interpolation to balance pattern visibility with preserving the sense that outliers are rare [@muth_interpolation_2022].
- For classed scales, keep the overall grouping but adopt custom cut points (including rounding) to improve legend readability without changing the map’s message dramatically [@muth_interpolation_2022].
- If outliers matter but also distort the map, call them out explicitly in text and choose an interpolation that supports the main comparison task [@muth_interpolation_2022].
