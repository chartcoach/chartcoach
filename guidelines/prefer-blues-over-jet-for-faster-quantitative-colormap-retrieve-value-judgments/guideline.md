---
id: prefer-blues-over-jet-for-faster-quantitative-colormap-retrieve-value-judgments
title: Prefer blues over jet when you need faster quantitative retrieve-value judgments
bibliography: references.bib
description: For retrieve-value judgments using quantitative colormaps, prefer blues
  over jet to reduce response time.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:speed
- data:quantitative
- audience:general
- palette:blues
- palette:jet
---

## Prefer blues over jet when speed matters in retrieve-value judgments <!-- role: advice -->

Use a blues quantitative colormap instead of jet when viewers must quickly make retrieve-value comparisons from color. Keep the scale continuous and show a legend.

## Single-hue blues can reduce time compared to jet in the tested judgment task <!-- role: reason -->

This works because a simpler, more uniform progression can reduce the time needed to decide which color is closer to a reference value.

**Mechanism:** Easier-to-parse color progressions can reduce deliberation time during forced-choice comparisons.

**Evidence:** In the extracted retrieve-value timing results, blues ranked faster than jet, with statistically supported differences indicating blues faster than jet for response time in the tested condition. [@liuSomewhereRainbowEmpirical2018; @zengReviewCollationGraphical2023]

**Notes:** This is a speed-focused guideline; it does not claim higher accuracy than other palettes beyond what is reported in the extracted rankings.

## When this applies to quantitative colormap selection <!-- role: context -->

- **User Goal:** Make quick relative comparisons using a quantitative color legend.
- **Task:** retrieve-value (relative “closer” judgments).
- **Data:** One quantitative variable mapped to color.
- **Chart Setting:** Static display; time pressure or high-throughput comparisons.
- **Audience:** General audiences.
- **Success Criterion:** Lower response time without relying on precise numeric reading.

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** Accuracy is the dominant requirement and you can use a palette shown to be more accurate in the same task context. **Why:** A speed-optimized choice may not be the accuracy-optimal choice.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce apparent color variety compared to jet. **Risk:** If the task involves very fine discriminations, a single-hue scheme may not provide enough resolution in all situations. **Mitigation:** Validate with a small sample of representative comparisons before standardizing.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using jet to “make differences pop” when the goal is fast value retrieval. **Why it fails:** The extracted timing results show slower performance with jet than with blues in the tested task.

## Quick tests <!-- role: check -->

**Failure Sign:** People hesitate longer than expected on simple “which is closer?” comparisons. **Quick Check:** Time a small set of representative judgments with blues vs jet while keeping the legend identical. **Stronger Test:** Run an A/B timing study on a realistic set of retrieve-value questions.

## What to do instead <!-- role: fix -->

- Replace jet with a blues quantitative scale for the same data range.
- Keep a consistent, readable legend and value ticks to support fast comparisons.
- If speed remains an issue, reduce the number of comparisons required by adding callouts for key reference values.
