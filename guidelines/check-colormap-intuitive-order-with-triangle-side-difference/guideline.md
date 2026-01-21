---
id: check-colormap-intuitive-order-with-triangle-side-difference
title: Check Intuitive Colormap Order with Triangle Side Difference
bibliography: references.bib
description: Evaluate whether a continuous colormap can be intuitively ordered by
  testing triangle side differences for local and global triplets of colors.
labels:
- chart:colormap
- task:validate
- visual:color
- impact:interpretability
- data:quantitative
- audience:expert
- scope:continuous-colormap
---

## The Rule <!-- role: advice -->

Assess intuitive order in a continuous colormap using the **triangle side difference**: require **minimum local triangle side difference > 0** for local intuitive order and **minimum global triangle side difference > 0** for global intuitive order.

## The Logic <!-- role: reason -->

- **The Principle:** For three colors sampled in increasing value order, the “middle” color should be perceptually between the two outer colors. This is tested by whether the distance between the outer colors exceeds the distances from each outer color to the middle one; triangle side difference quantifies violations.
- **The Evidence:** The framework defines local/global intuitive order via triangle inequalities over colormap triplets and proposes triangle side difference (and its minimum) as an evaluation measure [@bujackGoodBadUgly2018]. This theoretical knowledge is included in the broader collation used to inform recommendation constraints [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Ordering colors “naturally” (without relying on the legend) when interpreting a continuous color scale.
- **Data Type:** Quantitative data encoded with a continuous colormap.
- **Audience:** Designers or systems that need to reject colormaps that mislead intuitive ordering (even if they are legend-invertible).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only require legend-based readability and do not care about intuitive ordering without a legend.
- **Reason:** The paper distinguishes legend-based order (invertibility) from intuitive order; a map may be legend-orderable but not intuitively orderable [@bujackGoodBadUgly2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some high-discriminative-power colormaps may be rejected if they do not preserve intuitive ordering globally.
- **The Risk:** The triangle side difference value is not meant to be interpreted as “how close to linear” a colormap is; it depends on resolution and can be hard to compare across different samplings [@bujackGoodBadUgly2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “no repeated colors” (invertibility) as sufficient for intuitive order.
- **Why it fails:** The framework shows a colormap can be globally legend-orderable (minimum global speed > 0) but still fail global intuitive order (negative triangle side differences) [@bujackGoodBadUgly2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Some colors (e.g., a region of the gradient) feel “out of sequence,” where a mid-range color appears more extreme than neighboring ranges.
- **The Test:** Compute minimum local and global triangle side differences; negative minima indicate intuitive order violations [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Choose a different continuous colormap whose minimum triangle side differences are positive under the same metric and sampling.
- **Best Fix:** Encode intuitive-order constraints directly into automated colormap assessment/selection pipelines so colormaps that fail intuitive ordering are filtered out for tasks requiring intuitive ordering [@zengReviewCollationGraphical2023; @bujackGoodBadUgly2018].
