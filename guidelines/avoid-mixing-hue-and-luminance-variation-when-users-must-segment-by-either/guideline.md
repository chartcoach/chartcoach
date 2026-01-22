---
id: avoid-mixing-hue-and-luminance-variation-when-users-must-segment-by-either
title: Avoid simultaneously varying hue and luminance (when viewers must segment clusters
  by color)
bibliography: references.bib
description: Concurrent variation in hue and luminance can interfere with featural
  segmentation, making clusters harder to see.
labels:
- chart:scatter
- task:segment
- visual:color
- impact:clarity
- data:multivariate
- audience:general
- complexity:intermediate
---

## Keep color dimensions simple when color-based clustering matters <!-- role: advice -->

Do not encode one variable with hue and another with luminance if viewers need to visually cluster points by color. Use a single dominant color dimension for the segmentation-relevant variable.

## Why hue–luminance interactions disrupt segmentation <!-- role: reason -->

Featural segmentation relies on grouping by similarity along a feature dimension; adding variation in a second, interacting color dimension can make similarity less perceptually stable.

**Mechanism:** Variation in one color dimension can interfere with grouping along another, reducing the salience of clusters defined by hue or by luminance.

**Evidence:** Luminance variation can inhibit segmentation by hue, and large hue differences can make it difficult to segment by luminance in texture/feature segregation contexts, implying risks for color-based clustering in visualizations [@szafirFourTypesEnsemble2016a].

**Notes:** This targets tasks where the viewer must perceive discrete clusters, not continuous gradients.

## When you should apply this guideline <!-- role: context -->

- **User Goal:** Identify clusters or categories by color at a glance.
- **Task:** Segment elements into groups based on color similarity.
- **Data:** Multi-dimensional data where multiple fields compete for the color channel.
- **Chart Setting:** Dense mark displays (scatterplots, maps, glyph fields) where clustering is part of interpretation.
- **Audience:** General or mixed audiences; quick visual parsing.
- **Success Criterion:** Clear, stable perceived grouping by the intended color dimension.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Color-based segmentation is not a required task (for example, color is decorative or only used for annotation). **Why:** Interference matters most when clustering by color drives analysis.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the ability to encode two variables simultaneously with color. **Risk:** Using fewer encodings can reduce data density. **Mitigation:** Move the extra variable to another channel or another coordinated view.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding category with hue while encoding magnitude with luminance on the same marks when the user must cluster by category. **Why it fails:** Luminance variation can make same-hue items look less like a group, weakening segmentation.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers cannot quickly tell how many color groups exist or which items belong together without scanning item-by-item. **Quick Check:** Ask someone to describe the number of color groups and point to them within a brief glance. **Stronger Test:** Compare cluster identification accuracy between a single-dimension color design and a hue+luminance combined design.

## What to do instead when this fails <!-- role: fix -->

- Encode the segmentation-critical grouping using hue alone or luminance alone, not both.
- Move the secondary variable to a non-color channel (e.g., position or size) if available.
- Split the view into small multiples so each panel uses color for only one purpose.
