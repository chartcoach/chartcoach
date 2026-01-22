---
id: prefer-viridis-over-jet-for-quantitative-colormaps-in-retrieve-value-judgments
title: Prefer viridis over jet for quantitative color scales in retrieve-value judgments
bibliography: references.bib
description: For retrieve-value judgments using quantitative colormaps, prefer viridis
  over jet to improve accuracy.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- palette:viridis
- palette:jet
---

## Prefer viridis over jet for quantitative retrieve-value judgments <!-- role: advice -->

Use a viridis-style quantitative colormap instead of a jet (rainbow) colormap when people must retrieve values by comparing colors. Keep the encoding continuous and ordered.

## Viridis supports more accurate color-distance judgments than jet <!-- role: reason -->

This works because a well-ordered quantitative colormap makes perceived differences in color more reliably track differences in data values, reducing confusion during “which is closer?” judgments.

**Mechanism:** A colormap that yields clearer perceived ordering and separations reduces misjudgments when viewers compare the relative distance between values encoded by color.

**Evidence:** In a triplet-based retrieve-value judgment task, viridis had higher accuracy than jet, with a statistically supported advantage for viridis over jet in the collated results. [@liuSomewhereRainbowEmpirical2018; @zengReviewCollationGraphical2023]

**Notes:** This guideline only covers the colormaps and task captured in the extracted results.

## When this applies to quantitative colormap selection <!-- role: context -->

- **User Goal:** Retrieve or compare a quantitative value by reading color differences.
- **Task:** retrieve-value (relative “which value is closer?” style judgments).
- **Data:** One quantitative variable encoded on a continuous color scale.
- **Chart Setting:** Static chart; colors are the primary carrier of magnitude differences.
- **Audience:** General audiences (no assumption of expert calibration).
- **Success Criterion:** Higher accuracy of relative value judgments.

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** Jet is required to match a legacy standard in an existing workflow. **Why:** This guideline is scoped to perceptual performance, not compatibility constraints.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose continuity with existing defaults or established visual conventions that already use jet. **Risk:** Switching palettes without updating legends and documentation can confuse returning users. **Mitigation:** Keep the legend consistent and explicitly label the palette change.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Keeping jet as a default quantitative palette for value retrieval just because it is available in a tool. **Why it fails:** Accuracy can be worse than with viridis for the same retrieve-value judgment task.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers frequently pick the wrong “closer” value when colors come from the same quantitative scale. **Quick Check:** Ask a colleague to answer a few “which is closer?” comparisons using the legend; repeated errors are a warning. **Stronger Test:** Run a small internal A/B test comparing viridis vs jet on representative retrieve-value questions.

## What to do instead <!-- role: fix -->

- Replace the jet scale with a viridis-style quantitative scale for the same encoding.
- Keep the data range and legend ticks identical when comparing palette options.
- If a palette change is not possible, reduce reliance on color for value retrieval by adding an auxiliary cue (e.g., direct labels on key values).
