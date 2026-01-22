---
id: choose-color-scale-interpolation-based-on-data-distribution
title: Choose your color-scale interpolation based on the distribution of your data
bibliography: references.bib
description: Pick linear, quantile, natural breaks, or custom cut points based on
  how evenly your values are distributed and what patterns you need readers to see.
labels:
- chart:map-choropleth
- task:encode
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:intermediate
---

## Choose interpolation from the data distribution, not by default <!-- role: advice -->

Choose the interpolation for your color scale only after inspecting how your values are distributed (for example with a histogram or rug plot). Use the interpolation to match how you want differences and outliers to appear.

## Interpolation changes what differences look big or small <!-- role: reason -->

Interpolation determines how numeric differences are translated into color differences across the map, so it can either compress most areas into similar colors or spread them across the full palette. When distributions have strong outliers, an interpolation that ignores distribution can make most regions look the same, while distribution-aware choices can reveal geographic patterns among the non-outliers.

**Mechanism:** Changing interpolation changes how much of the color range is allocated to dense versus sparse parts of the value range, which changes perceived contrast and which regions look meaningfully different.

**Evidence:** Linear interpolation can cause most regions to share similar light colors when values are clustered with a few high outliers, while quantile- and natural-style interpolations redistribute the gradient so more regions receive mid/dark colors and patterns become easier to see [@muth_interpolation_2022]. Different interpolations can also invert perceived magnitude, making some moderate differences look larger than very large differences when the gradient is stretched unevenly across the data range [@muth_interpolation_2022].

**Notes:** Inspecting distribution first helps you predict whether an interpolation will emphasize outliers, emphasize within-cluster variation, or balance both.

## Use this when mapping values to a gradient on regions <!-- role: context -->

- **User Goal:** Understand how a quantitative variable varies across geographic areas, including outliers and/or regional patterns.
- **Task:** Interpret relative intensity and compare areas by color.
- **Data:** Quantitative values per region; often skewed with clusters and outliers.
- **Chart Setting:** Choropleth maps (also applicable to other color-encoded charts like symbol maps or heat maps).
- **Audience:** Readers who infer magnitude from color contrast and legend cut points.
- **Success Criterion:** Regions that should look different actually look different, without implying false uniformity or false extremeness.

## When not to use distribution-driven interpolation <!-- role: exceptions -->

**Break it when:** You need the colors to represent equal steps in the original numeric scale above all else. **Why:** Distribution-driven interpolations can intentionally distort how much color change corresponds to a given numeric change, changing how “big” differences look [@muth_interpolation_2022].

## What you trade off by changing interpolation <!-- role: costs -->

**Sacrifice:** You may lose the most straightforward “equal steps in value = equal steps in color” interpretation. **Risk:** Readers may infer that high values are common (with quantiles) or may underestimate how extreme the top outliers are (with heavily redistributed gradients). **Mitigation:** Make the legend explicit and ensure the interpolation matches the story goal (outliers vs. regional variation) [@muth_interpolation_2022].

## Common ways interpolation goes wrong <!-- role: mistakes -->

- **Mistake:** Using linear interpolation on heavily skewed data and accepting a map where most regions fall into the lightest color. **Why it fails:** Dense parts of the distribution get too little color range, hiding geographic structure among most regions [@muth_interpolation_2022].
- **Mistake:** Using strong equal-count interpolations (e.g., many quantile cuts) just to make the map look dramatic. **Why it fails:** It can imply widespread high values and exaggerate small differences near dense parts while compressing large differences among outliers [@muth_interpolation_2022].

## Quick ways to sanity-check the interpolation choice <!-- role: check -->

**Failure Sign:** Most regions share nearly the same shade, or the darkest shades appear so widely that the map suggests “many extremes.” **Quick Check:** Look at a histogram/rug plot and ask whether large parts of the distribution are being squeezed into a tiny part of the gradient. **Stronger Test:** Compare two or three interpolations side by side and check whether the implied story (outliers vs. patterns) matches the data distribution you see in the histogram [@muth_interpolation_2022].

## Alternatives when the current interpolation misleads <!-- role: fix -->

- Switch from linear to a distribution-aware interpolation (quantiles or natural-style) when outliers cause most regions to look the same [@muth_interpolation_2022].
- Switch from equal-count interpolation to a more distribution-respecting option (natural-style) when equal-count makes outliers look common [@muth_interpolation_2022].
- If you must keep distribution-aware cuts but want readability, round or manually adjust cut values to create a clearer legend while preserving the overall grouping [@muth_interpolation_2022].
- If neither outlier emphasis nor pattern emphasis is acceptable with one interpolation, annotate the map to call out outliers explicitly and choose an interpolation that supports the primary message [@muth_interpolation_2022].
