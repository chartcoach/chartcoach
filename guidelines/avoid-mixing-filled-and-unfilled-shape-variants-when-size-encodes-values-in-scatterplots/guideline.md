---
id: avoid-mixing-filled-and-unfilled-shape-variants-when-size-encodes-values-in-scatterplots
title: Avoid mixing filled and unfilled shape variants when size encodes values in
  scatterplots
bibliography: references.bib
description: Shape differences can bias perceived point size in scatterplots, so mixing
  shape variants can distort size comparisons.
labels:
- chart:scatter
- task:rank
- visual:size
- impact:accuracy
- data:quantitative
- audience:general
- complexity:advanced
---

## Keep point shape consistent when viewers must compare sizes <!-- role: advice -->

When point size encodes a quantitative variable in a scatterplot, keep the point shape consistent across categories to reduce shape-driven size bias.

## Shape can bias perceived size (size is not fully separable from shape) <!-- role: reason -->

If shape changes the apparent size of a mark, then viewers may misread the underlying quantitative values encoded by size.

**Mechanism:** Some shapes appear larger or smaller than other shapes even when rendered at the same nominal size, which distorts size-based comparisons.

**Evidence:** Size difference perception depended strongly on mark shape, including systematic biases where some shapes were perceived as larger than others at comparable sizes; the interference was asymmetric, with shape affecting size perception more strongly than size affected shape perception within the tested ranges [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].

**Notes:** The evidence concerns point marks in scatterplot-like displays, not area marks in other chart types.

## Context where size comparisons must be trustworthy <!-- role: context -->

- **User Goal:** Compare or rank magnitudes encoded by point size.
- **Task:** Sort/rank (relative magnitude judgments).
- **Data:** Two quantitative variables on position; one quantitative variable mapped to size; optional nominal grouping by shape.
- **Chart Setting:** Static scatterplot with many marks where category styling may vary.
- **Audience:** Any audience making value judgments from size.
- **Success Criterion:** Size comparisons reflect the encoded values rather than shape artifacts.

## When mixing shapes may be acceptable <!-- role: exceptions -->

**Break it when:** Size is not intended to be read precisely (e.g., purely decorative emphasis) and the primary analysis does not depend on size comparison. **Why:** The cost of bias is lower when size is not part of the analytical judgment.

## Costs of keeping shape consistent <!-- role: costs -->

**Sacrifice:** You lose an extra categorical channel (shape) for encoding group identity. **Risk:** Removing shape can reduce category distinguishability if color alone is insufficient. **Mitigation:** Use fewer categorical encodings so the remaining channel is clearer.

## Mistakes that create size-reading bias <!-- role: mistakes -->

**Mistake:** Encoding category with different shapes while also expecting viewers to compare point sizes across categories. **Why it fails:** Shape can systematically shift perceived size, distorting cross-category size comparisons [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].

## Quick checks for size bias from shape <!-- role: check -->

**Failure Sign:** Two categories appear to have different magnitudes even when their size scale is the same. **Quick Check:** Render the same size value using each shape and see whether any shape “looks bigger” at a glance. **Stronger Test:** Ask a small set of users to pick the larger of two equal-sized but differently shaped marks and see if responses deviate from 50/50.

## Fixes when you need both category and size <!-- role: fix -->

- Use one shape for all points and encode category using another channel instead of shape.
- If shape must encode category, avoid using size to encode values that require cross-category comparison.
- Validate size perception with quick same-size trials using your exact shapes and rendering settings before finalizing the design.
