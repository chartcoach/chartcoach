---
id: treat-interpolation-as-a-tradeoff-between-truthfulness-and-usefulness
title: Choose interpolation as an explicit tradeoff between outlier truthfulness and
  pattern usefulness
bibliography: references.bib
description: Select color interpolation based on whether you want to emphasize absolute
  extremes or reveal mid-range geographic structure, and acknowledge the perceptual
  tradeoff.
labels:
- chart:map-choropleth
- task:communicate
- visual:color
- impact:trust
- data:quantitative
- audience:general
- complexity:intermediate
---

## Decide whether your map should emphasize outliers or emphasize mid-range patterns <!-- role: advice -->

Choose an interpolation by first deciding whether the primary message is about extreme outliers or about regional patterns among typical values, then select the interpolation that supports that message. Ensure the chosen interpolation does not accidentally imply a different story about rarity or magnitude than the one your data supports.

## Different interpolations reshape perceived differences and implied prevalence <!-- role: reason -->

Interpolation does not just “color the map”; it changes the implied distribution by allocating more or less of the palette to certain ranges. As you move from linear toward equal-count approaches, the map generally becomes higher-contrast and more varied, but it can also make high values appear more common and make very large numeric gaps look visually small.

**Mechanism:** Stretching the gradient unevenly changes the mapping from numeric distance to perceptual distance, so some differences are visually amplified while others are visually compressed.

**Evidence:** Linear interpolation was described as the most honest for uneven data when the goal is to keep a linear scale and draw attention to rare outliers, while quantile-style interpolations reveal more geographic patterns among typical values but can imply that extreme values are widespread [@muth_interpolation_2022]. In a decile-style continuous interpolation, very high and moderately high values can appear in very similar dark shades while moderate-to-low differences can look much larger than their numeric gap, altering perceived importance [@muth_interpolation_2022].

**Notes:** This is a design choice that should be made intentionally rather than by aesthetic preference for higher contrast.

## Situations where the “truthfulness vs usefulness” choice matters most <!-- role: context -->

- **User Goal:** Use a choropleth map to support a narrative or analytical takeaway.
- **Task:** Balance accurate magnitude perception with discoverable geographic structure.
- **Data:** Skewed quantitative data where outliers exist and most values cluster.
- **Chart Setting:** Published map with a legend that readers use to infer prevalence and intensity.
- **Audience:** Mixed audiences who may not inspect the legend carefully.
- **Success Criterion:** The visual emphasis matches the intended takeaway and does not mislead about rarity or magnitude.

## When not to treat this as a flexible tradeoff <!-- role: exceptions -->

**Break it when:** You are required to keep a strict linear mapping between value and color for comparability across maps or reports. **Why:** Distribution-altering interpolations can undermine comparability by changing what the same color means across different views [@muth_interpolation_2022].

## Risks and tradeoffs of prioritizing one side <!-- role: costs -->

**Sacrifice:** Emphasizing outlier truthfulness can hide meaningful mid-range structure, while emphasizing pattern usefulness can downplay how exceptional the outliers are. **Risk:** Viewers may overestimate or underestimate differences based on contrast rather than values. **Mitigation:** Align interpolation with the map’s stated purpose and make thresholds and interpretation explicit in the legend and accompanying text [@muth_interpolation_2022].

## Common ways this tradeoff gets mishandled <!-- role: mistakes -->

**Mistake:** Selecting the interpolation that “looks best” (most contrast) without checking what it implies about prevalence and magnitude. **Why it fails:** The map can become more dramatic while becoming less faithful to the distribution and relative gaps in the data [@muth_interpolation_2022].

## Quick tests that your emphasis matches your intent <!-- role: check -->

**Failure Sign:** Readers could reasonably infer “many extreme areas” or “almost no differences” from the colors, despite the distribution showing the opposite. **Quick Check:** Identify two pairs of regions—one pair with a large numeric gap and one with a small gap—and verify the color differences do not invert their apparent importance unintentionally. **Stronger Test:** Compare linear, quantile-style, and natural-style outputs and choose the one whose implied story matches both the histogram and the narrative goal [@muth_interpolation_2022].

## What to do instead if the map’s emphasis is wrong <!-- role: fix -->

- Switch to linear interpolation if you need to preserve absolute scale and spotlight rare extremes [@muth_interpolation_2022].
- Switch to quantile-style interpolation if revealing differences among typical regions is more important than preserving absolute distances [@muth_interpolation_2022].
- Switch to natural-style interpolation if you need a middle ground that reflects clustering while keeping outliers rare [@muth_interpolation_2022].
- Adjust class thresholds (custom breaks) to improve readability without materially changing the intended emphasis [@muth_interpolation_2022].
