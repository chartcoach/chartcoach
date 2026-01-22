---
id: use-filled-shapes-to-improve-categorical-color-separability-in-scatterplots
title: Use filled point shapes to maximize categorical color-hue separability in scatterplots
bibliography: references.bib
description: "Filled point shapes improve viewers\u2019 ability to discriminate color\
  \ differences compared to unfilled shapes in scatterplots."
labels:
- chart:scatter
- task:rank
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
---

## Prefer filled point shapes when color encodes categories <!-- role: advice -->

Use filled point shapes instead of unfilled point shapes when color hue is the primary cue for distinguishing categories in a scatterplot.

## Shape–color interference makes some shapes harder to tell apart by color <!-- role: reason -->

In multichannel scatterplots, the mark’s shape changes how easily viewers can tell whether two colors are different, so color is not fully separable from shape.

**Mechanism:** Filled shapes provide more visible colored area, which increases discriminability for color differences compared to outlines, making category colors easier to separate.

**Evidence:** Color difference discriminability varied significantly by mark shape, with filled shapes generally yielding higher discriminability than unfilled counterparts in scatterplot-like stimuli [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].

**Notes:** The observed interference was asymmetric: shape affected color perception more strongly than color affected shape perception within the tested ranges [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].

## Context for choosing filled shapes with color categories <!-- role: context -->

- **User Goal:** Distinguish or rank categories by their color-coded points.
- **Task:** Sort/rank (categorical differentiation while reading a scatterplot).
- **Data:** Two quantitative fields on position; one nominal field mapped to color hue.
- **Chart Setting:** Static scatterplot with point marks using different shapes.
- **Audience:** General audiences relying on color to separate groups.
- **Success Criterion:** Higher accuracy in distinguishing category colors.

## When not to rely on filled shapes for color separability <!-- role: exceptions -->

**Break it when:** Shape is the only (or primary) channel users will use to distinguish categories and color is secondary. **Why:** The guideline targets improving color discrimination, not improving shape discrimination.

## Costs of using filled shapes <!-- role: costs -->

**Sacrifice:** Filled shapes can reduce the distinctiveness of shape outlines as a cue. **Risk:** If multiple channels compete, viewers may overweight the more salient filled areas and underuse other encodings. **Mitigation:** Treat shape as a secondary cue when using filled shapes with color categories.

## Mistakes when combining shape and color in scatterplots <!-- role: mistakes -->

**Mistake:** Mixing filled and unfilled shapes while expecting color categories to be equally discriminable across all groups. **Why it fails:** Shape alters color discriminability, creating uneven category separability by color [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].

## Quick checks for color separability problems <!-- role: check -->

**Failure Sign:** Some categories feel “harder to see” even when their hues are intended to be equally distinct. **Quick Check:** Compare a few pairs of similarly separated hues using both filled and unfilled shapes; if unfilled shapes feel less distinct, switch to filled. **Stronger Test:** Run a small forced-choice “same vs different color” check with representative mark shapes and sizes.

## Fixes if filled shapes are not feasible <!-- role: fix -->

- Use a single shape family (all filled or all unfilled) to avoid uneven color discriminability across categories.
- Reduce reliance on color by removing shape variation if category separation must be primarily color-driven.
- If shape must vary, validate separability with a small user check focused on “same vs different color” judgments.
