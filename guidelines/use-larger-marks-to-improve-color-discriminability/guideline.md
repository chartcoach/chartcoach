---
id: use-larger-marks-to-improve-color-discriminability
title: Increase mark size when color-hue differences must be discriminable
bibliography: references.bib
description: Make marks larger so viewers can more reliably tell encoded colors apart.
labels:
- chart:scatter
- chart:bar
- chart:line
- task:cluster
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
---

## Make mark size large enough for reliable color-hue discrimination <!-- role: advice -->

Increase the size of the marks when you need viewers to distinguish categories by color hue (for example, in clustering judgments). Prefer the largest feasible mark size within your layout constraints.

## Why color discriminability improves with larger marks <!-- role: reason -->

Color differences are harder to see on small marks; enlarging marks increases the perceptual signal available for comparing colors, raising the probability that viewers notice differences.

**Mechanism:** Larger marks reduce the just-noticeable difference (JND) threshold required to perceive that two colors differ, so the same palette becomes easier to discriminate.

**Evidence:** In crowdsourced forced-choice comparisons embedded in common visualization contexts, color-difference thresholds decreased as mark size increased for point marks, bar marks, and line marks. [@szafirModelingColorDifference2018] This paper is included as empirical evidence in a broader collation intended for visualization recommendation rules. [@zengReviewCollationGraphical2023]

**Notes:** This guideline concerns discriminating colors (same vs different), not judging ordered magnitude from color.

## When mark-size tuning for color applies <!-- role: context -->

- **User Goal:** Distinguish groups or categories encoded by color.
- **Task:** Cluster.
- **Data:** Categorical (nominal) classes mapped to color hue.
- **Chart Setting:** Static scatterplots (points), bar charts (bars), or line charts (lines) using color hue to separate series/groups.
- **Audience:** General audiences, including viewers on typical consumer displays.
- **Success Criterion:** Viewers can correctly and confidently tell categories apart by color.

## When not to rely on mark size for color discriminability <!-- role: exceptions -->

**Break it when:** The visualization cannot increase mark sizes due to extreme overplotting or fixed-density constraints. **Why:** Larger marks can occlude each other and remove needed positional information, undermining the chart’s readability.

## Tradeoffs of increasing mark size <!-- role: costs -->

**Sacrifice:** You give up space and may reduce the number of marks that can be shown without overlap. **Risk:** Overplotting can increase, causing category mixing and hiding points/segments. **Mitigation:** Consider reducing mark count (sampling/aggregation) or changing layout density without assuming color alone will carry the grouping.

## Common mistakes when “fixing” color discriminability <!-- role: mistakes -->

**Mistake:** Keeping marks tiny and assuming a color palette alone will make clusters separable. **Why it fails:** Small marks require larger color differences to be reliably perceived, so categories can become indistinguishable in practice.

## Quick ways to check if marks are too small for color <!-- role: check -->

**Failure Sign:** Viewers confuse similarly colored categories or cannot segment the plot into colored groups at a glance. **Quick Check:** Shrink the chart to a typical “dashboard tile” size; if categories blur together, the marks are likely too small. **Stronger Test:** Run a simple “same vs different color” check with representative mark sizes and your intended palette on the target device class.

## What to do instead if you cannot increase mark size <!-- role: fix -->

- Use fewer categories per view by filtering or faceting so each group has more visual space.
- Reduce mark density by aggregating, binning, or sampling while preserving the clustering signal.
- Switch to an encoding that does not depend primarily on color discrimination (for example, separate groups spatially).
- Add redundant non-color cues for grouping only if the chart remains legible after doing so.
