---
id: prefer-viridis-over-blueorange-for-quantitative-colormaps-in-retrieve-value-judgments
title: Prefer viridis over blueorange for quantitative color scales in retrieve-value
  judgments
bibliography: references.bib
description: For retrieve-value judgments using quantitative colormaps, prefer viridis
  over blueorange to improve accuracy.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- palette:viridis
- palette:blueorange
---

## Prefer viridis over blueorange for quantitative retrieve-value judgments <!-- role: advice -->

Use a viridis-style quantitative colormap instead of a blueorange colormap when people must retrieve values by comparing colors. Keep the mapping continuous and ordered.

## Viridis yields fewer errors than blueorange in relative-distance judgments <!-- role: reason -->

This works because a colormap that maintains consistent perceptual progression across the scale supports more reliable relative-distance comparisons between colors.

**Mechanism:** More consistent perceived differences reduce ambiguity when choosing which of two colors is closer to a reference on a quantitative scale.

**Evidence:** In triplet-based retrieve-value judgments, viridis had higher accuracy than blueorange, with the collated results marking viridis as significantly better than blueorange for accuracy. [@liuSomewhereRainbowEmpirical2018; @zengReviewCollationGraphical2023]

**Notes:** This guideline reflects the extracted accuracy ranking and does not generalize beyond the tested palettes and task.

## When this applies to quantitative colormap selection <!-- role: context -->

- **User Goal:** Retrieve or compare a quantitative value by interpreting colors with a legend.
- **Task:** retrieve-value (relative distance comparisons).
- **Data:** Single quantitative attribute on a continuous scale.
- **Chart Setting:** Static chart; color is the primary quantitative encoding.
- **Audience:** General audiences.
- **Success Criterion:** Higher judgment accuracy.

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** You must emphasize a meaningful mid-point using an existing blueorange convention. **Why:** This guideline only addresses performance for retrieve-value comparisons, not semantic conventions around mid-points.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose a familiar “two-sided” aesthetic associated with blueorange. **Risk:** If stakeholders expect a specific palette, changing it can reduce trust even if accuracy improves. **Mitigation:** Communicate the palette change and keep the legend prominently visible.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating viridis and blueorange as interchangeable “good” defaults for quantitative value retrieval. **Why it fails:** The extracted results show a measurable accuracy advantage for viridis in the tested retrieve-value task.

## Quick tests <!-- role: check -->

**Failure Sign:** Users misjudge which of two colors is closer to a reference even when the legend is visible. **Quick Check:** Run a handful of “which is closer?” checks on typical value ranges using both palettes and compare error frequency informally. **Stronger Test:** Conduct a small within-subjects comparison on representative questions.

## What to do instead <!-- role: fix -->

- Switch the quantitative color scale from blueorange to a viridis-style palette.
- Keep legend ticks and value sampling consistent so users can reliably compare.
- If palette switching is constrained, add a second encoding (e.g., numeric annotations for key values) to reduce reliance on fine-grained color distance judgments.
