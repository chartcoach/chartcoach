---
id: prefer-blues-over-blueorange-for-faster-quantitative-colormap-retrieve-value-judgments
title: Prefer blues over blueorange when you need faster quantitative retrieve-value
  judgments
bibliography: references.bib
description: For retrieve-value judgments using quantitative colormaps, prefer blues
  over blueorange to reduce response time.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:speed
- data:quantitative
- audience:general
- palette:blues
- palette:blueorange
---

## Prefer blues over blueorange when speed matters in retrieve-value judgments <!-- role: advice -->

Use a blues quantitative colormap instead of blueorange when viewers must quickly make retrieve-value comparisons from color. Keep the legend visible during reading.

## Blues can be faster than blueorange in the tested retrieve-value judgment task <!-- role: reason -->

This works because a simpler sequential progression can reduce decision time relative to a palette that introduces stronger cross-scale changes.

**Mechanism:** Reduced complexity in the perceived progression can lower the time needed to compare relative distances between colors.

**Evidence:** In the extracted retrieve-value timing results, blues ranked faster than blueorange, with statistically supported differences indicating blues faster than blueorange for response time in the tested condition. [@liuSomewhereRainbowEmpirical2018; @zengReviewCollationGraphical2023]

**Notes:** This guideline is limited to the timing outcome for the tested task and conditions.

## When this applies to quantitative colormap selection <!-- role: context -->

- **User Goal:** Make rapid relative comparisons using color plus a legend.
- **Task:** retrieve-value (relative “closer” judgments).
- **Data:** Single quantitative attribute encoded by color.
- **Chart Setting:** Static chart where speed matters.
- **Audience:** General audiences.
- **Success Criterion:** Faster responses on retrieve-value comparisons.

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** You need a palette form that matches an established presentation standard already using blueorange. **Why:** Organizational constraints can outweigh performance considerations.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up a familiar “two-sided” look. **Risk:** A palette change can create inconsistency across a dashboard suite if other charts use blueorange. **Mitigation:** Standardize palette choices across the product rather than changing only one view.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing blueorange for general quantitative value retrieval without checking whether it slows down comparisons. **Why it fails:** The extracted timing results show slower performance relative to blues in the tested retrieve-value setting.

## Quick tests <!-- role: check -->

**Failure Sign:** Users take longer on “which value is closer?” questions than expected. **Quick Check:** Swap only the palette (blues vs blueorange) and compare median completion time across a small set of tasks. **Stronger Test:** Run a small controlled timing study with randomized palette order.

## What to do instead <!-- role: fix -->

- Use a blues sequential palette for the quantitative color encoding.
- Maintain the same legend scale and tick marks to keep comparisons fair.
- If you must keep blueorange, reduce dependence on rapid color reading by annotating key values directly.
