---
id: use-quantile-interpolation-to-distribute-colors-evenly-across-regions
title: Use quantile interpolation when you need each color to represent an equal share
  of regions
bibliography: references.bib
description: Apply equal-count cuts (e.g., quintiles) to increase color variety across
  the map when linear mapping leaves most regions in the same shade.
labels:
- chart:map-choropleth
- task:compare
- visual:color
- impact:pattern-detection
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use quantiles to force a fuller use of the palette across areas <!-- role: advice -->

Use quantile (equal-count) interpolation when a linear mapping leaves most regions in one or two light shades and you need the map to show more variation across typical regions. Choose the number of quantiles to match the number of colors or gradient segments you intend to show.

## Equal-count grouping reallocates contrast to where most regions are <!-- role: reason -->

Quantiles cut the data so each class (or each gradient segment anchor) contains the same number of regions, which spreads colors evenly across geography even when the numeric range is skewed. This increases visible differences among the dense part of the distribution but also changes what the colors imply about how common high values are.

**Mechanism:** By assigning equal portions of the palette to equal portions of the ranked data, quantiles amplify differences in dense ranges and compress differences in sparse ranges.

**Evidence:** In skewed unemployment-rate data, quantile classing (quintiles) made each color appear in the same number of counties and revealed variance that linear classing largely hid [@muth_interpolation_2022]. In continuous scales, median/quartile/quintile/decile interpolations stretch the gradient within each quantile chunk, increasing overall contrast but potentially making outliers appear less exceptional [@muth_interpolation_2022].

**Notes:** Quantiles are especially useful when the map’s purpose is to compare relative standing (who is higher/lower) rather than absolute distances.

## When quantile interpolation fits the situation <!-- role: context -->

- **User Goal:** See more geographic differentiation and relative ranking across regions.
- **Task:** Compare regions by relative position in the distribution (top 20%, bottom 25%, etc.).
- **Data:** Quantitative values with clustering that makes linear mapping visually flat.
- **Chart Setting:** Choropleth maps with classed palettes (e.g., five steps) or continuous gradients segmented by quantile anchors.
- **Audience:** Readers comfortable interpreting percentiles and relative categories.
- **Success Criterion:** All (or most) colors appear meaningfully on the map and help readers distinguish regions.

## When not to use quantiles <!-- role: exceptions -->

**Break it when:** You must communicate how rare extreme values are. **Why:** Quantiles guarantee equal representation per color band, which can make it look like high values are common even when they are outliers [@muth_interpolation_2022].

## Tradeoffs and risks of quantiles <!-- role: costs -->

**Sacrifice:** The legend becomes less about equal numeric steps and more about rank positions. **Risk:** Readers can infer an exaggerated prevalence of high (or low) values because each band covers the same number of regions. **Mitigation:** Make the legend thresholds explicit and ensure the map text frames interpretation in terms of relative standing [@muth_interpolation_2022].

## Common quantile pitfalls <!-- role: mistakes -->

- **Mistake:** Using many cuts (e.g., deciles) primarily to increase drama. **Why it fails:** It can overemphasize small differences near dense ranges and downplay large differences among high-end outliers [@muth_interpolation_2022].
- **Mistake:** Interpreting quantile-colored regions as if each color represents equal numeric distance. **Why it fails:** Quantile bands can cover very different numeric ranges across the distribution [@muth_interpolation_2022].

## Quick checks for quantile suitability <!-- role: check -->

**Failure Sign:** The map implies “lots of extremes” even though the histogram shows only a few outliers. **Quick Check:** Compare the numeric width of the top band to middle bands; if the top band spans a huge numeric range, you are compressing outliers strongly [@muth_interpolation_2022]. **Stronger Test:** Place two labeled example regions from different ends (e.g., very high vs moderately high) and see whether their colors look too similar given the numeric gap [@muth_interpolation_2022].

## What to do instead when quantiles misrepresent outliers <!-- role: fix -->

- Use a natural-style interpolation to keep outliers visually rare while still revealing differences around the center of the distribution [@muth_interpolation_2022].
- Use linear interpolation if the key message is absolute magnitude and outlier extremeness rather than rank [@muth_interpolation_2022].
- Use a classed custom interpolation to preserve a distribution-aware structure but adjust thresholds to more interpretable values (e.g., rounded cut points) [@muth_interpolation_2022].
- Add explanatory annotation that the colors represent percentiles (and show thresholds) if relative ranking is the intended takeaway [@muth_interpolation_2022].
