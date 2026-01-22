---
id: prefer-baseline-pie-over-baseline-stacked-bar-for-part-to-whole-estimation
title: Prefer a baseline pie chart over a baseline stacked bar chart for part-to-whole
  estimation
bibliography: references.bib
description: For estimating a highlighted part as a percentage of a whole, baseline
  pie charts produced lower error than baseline stacked bars in one controlled comparison.
labels:
- chart:pie
- chart:bar
- task:estimate
- visual:angle
- visual:length
- impact:accuracy
- data:categorical
- data:quantitative
- audience:general
- study:experiment
---

## Prefer baseline pie over baseline stacked bar for part-to-whole estimation <!-- role: advice -->

Use a pie chart rather than a plain stacked bar chart when people must estimate the size of a highlighted part as a percentage of the whole.

## Why pie can outperform a plain stacked bar in this estimation task <!-- role: reason -->

Part-to-whole estimation accuracy depends on how consistently viewers can map a displayed segment to a percent judgment. In the tested designs, the pie (angle-based segment) yielded lower mean absolute error than the baseline stacked bar (length-based segment), indicating a more accurate perceptual-to-numeric mapping for this specific task and setup.

**Mechanism:** A more stable perceptual cue for estimating the highlighted fraction reduces absolute estimation error.

**Evidence:** In a part-to-whole estimation task, the baseline pie chart (angle + color saturation) had lower mean absolute error than the baseline stacked bar (length + color saturation), and the comparison was treated as significant in the extracted results [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline is limited to the specific “baseline” designs and the estimation-style task represented in the extracted record.

## When you are doing part-to-whole percent estimation <!-- role: context -->

- **User Goal:** Estimate a highlighted segment’s share of a whole as an integer percentage.
- **Task:** Characterize distribution (part-to-whole segment estimation).
- **Data:** One quantitative proportion per segment (sums to 100%); two segments shown (highlighted segment vs remainder).
- **Chart Setting:** Static chart; segment distinguished via color saturation.
- **Audience:** General audience (crowdsourced participants).
- **Success Criterion:** Lower estimation error (higher accuracy).

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** You are not asking viewers to estimate a part-to-whole percentage from the mark, but instead need precise read-off values from an explicit scale. **Why:** This rule only covers estimation performance for the tested baseline designs and does not establish superiority for other reading tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Using pies may constrain how easily you can add axis-based scaffolding and may limit alignment with other quantitative charts in a dashboard.
**Risk:** Overgeneralizing this result to other pie/bar variants, different numbers of segments, or different tasks can lead to the wrong design choice.
**Mitigation:** Treat this as a task- and design-specific preference and validate with a quick pilot if the context differs.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Applying “pie beats bar” as a universal rule for all comparison tasks. **Why it fails:** The evidence here is specific to part-to-whole estimation for particular baseline designs and does not cover broader comparison tasks.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers’ estimates for the highlighted segment show large absolute deviations from the true percent.
**Quick Check:** Give 5–10 readers a few sample questions (e.g., “What percent is the darker segment?”) and compare typical absolute errors across the two chart options.
**Stronger Test:** Run a small A/B test measuring mean absolute error for the same set of values in both designs.

## What to do instead if a pie is not acceptable <!-- role: fix -->

- Switch to a bar variant that provides stronger internal or external reference cues for estimating the segment.
- Provide an explicit numeric readout adjacent to the segment when estimation from the mark is not required.
- Use a different part-to-whole display only after testing estimation error for your specific design and audience.
