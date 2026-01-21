---
id: use-quantiles-to-distribute-colors-evenly-across-regions
title: Use Quantiles to Equalize Color Usage Across Regions
bibliography: references.bib
description: Choose quantile interpolation when you need each color to appear on roughly
  the same number of regions and reveal variation among common values.
labels:
- chart:choropleth
- task:reveal-patterns
- visual:color
- impact:readability
- data:quantitative
- audience:general
- complexity:intermediate
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use quantile interpolation (e.g., quintiles for five classes) when you want each class color to cover the same number of regions and increase visible variation across the map. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Quantiles set breakpoints so each class contains an equal count of observations; this forces underused mid/dark colors to appear more often and makes differences among densely clustered values easier to see. [@muth_interpolation_2022]

- **The Principle:** Equal-count binning increases apparent contrast
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Finding geographic patterns among typical values when linear binning yields a mostly single-color map
- **Data Type:** Skewed quantitative distributions where many values cluster in a narrow range
- **Audience:** Readers who benefit from a more varied map, even if class widths become uneven [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must communicate absolute magnitude faithfully (e.g., how extreme the extremes are) and avoid implying that “many places are extreme.”
- **Reason:** Equal-count classes can make the highest class appear as common as the lowest, downplaying the rarity of true outliers. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Class ranges become uneven, reducing interpretability of absolute differences between classes.
- **The Risk:** Readers may infer that high values are widespread because the darkest color is assigned to as many regions as other colors. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using quantiles and then describing the top class as “extreme” without acknowledging it always contains a fixed share of regions.
- **Why it fails:** The class definition is count-based, not threshold-based; “top 20%” is not the same as “rare outliers.” [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Every class color appears in similar amounts, but the legend shows very uneven numeric ranges.
- **The Test:** Compare the size of the numeric intervals between class breaks; if they vary widely, you’re in quantile territory and should ensure the narrative matches that. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** If quantiles overstate how common “high” values are, switch to Natural breaks to keep outliers rarer while still adding variation. [@muth_interpolation_2022]
- **Best Fix:** Align binning with the message: quantiles for rank-like comparisons (“top 20%”), linear for magnitude, Natural breaks for distribution-shaped groupings. [@muth_interpolation_2022]
