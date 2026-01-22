---
id: add-decile-ticks-to-stacked-bars-to-improve-part-to-whole-estimation-accuracy
title: Add decile ticks to stacked bar charts to improve part-to-whole estimation
  accuracy
bibliography: references.bib
description: Adding decile reference ticks inside stacked bars reduced estimation
  error versus both a baseline bar and a bar with quartile ticks in one experiment.
labels:
- chart:bar
- task:estimate
- visual:length
- visual:annotation
- impact:accuracy
- data:categorical
- data:quantitative
- audience:general
- study:experiment
---

## Add decile ticks to stacked bars for part-to-whole percent estimation <!-- role: advice -->

When using a stacked bar for part-to-whole estimation, add internal decile reference ticks rather than relying on a plain bar or quartile ticks.

## Why denser internal anchors can reduce estimation error in stacked bars <!-- role: reason -->

Estimating a segment as a percent of a whole improves when the display provides more evenly spaced visual reference points that help calibrate judgments. In the tested variants, a bar with decile ticks outperformed both the bar with quartile ticks and the baseline bar, indicating that additional internal anchors improved accuracy for this estimation task.

**Mechanism:** More frequent internal reference points reduce uncertainty about the segment’s relative length, lowering absolute estimation error.

**Evidence:** For a part-to-whole estimation task, the bar with decile ticks ranked higher (lower error) than the bar with quartile ticks and higher than the baseline bar, with significant differences recorded for decile vs quartile and decile vs baseline comparisons [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

**Notes:** The extracted record does not indicate a significant difference between quartile ticks and the baseline bar.

## When you must keep a bar but need better percent estimates <!-- role: context -->

- **User Goal:** Estimate a highlighted segment’s share of a stacked bar as an integer percentage.
- **Task:** Characterize distribution (part-to-whole segment estimation).
- **Data:** One quantitative proportion per segment (sums to 100%); two segments shown (highlighted segment vs remainder).
- **Chart Setting:** Static bar; segment distinguished via color saturation; ticks used as internal reference cues.
- **Audience:** General audience (crowdsourced participants).
- **Success Criterion:** Lower estimation error (higher accuracy).

## When not to add decile ticks <!-- role: exceptions -->

**Break it when:** The bar is already paired with a different mechanism that directly supports precise percent reading (for example, a full external scale) and adding many internal ticks would overly clutter the mark. **Why:** The rule targets improving estimation from the bar itself; extra internal cues may be redundant or distracting in other layouts.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Extra visual elements inside the bar increase visual complexity and take design time.
**Risk:** Over-ticking can make bars look busy and may distract from the overall message.
**Mitigation:** Use decile ticks only on bars meant for estimation, and keep tick styling visually subordinate to the data segment.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding only quartile ticks and assuming they will meaningfully improve estimation. **Why it fails:** In the extracted results, decile ticks improved accuracy relative to quartile ticks, while quartile ticks did not clearly outperform the baseline bar.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers disagree widely on whether the segment is closer to (for example) 20% vs 30%.
**Quick Check:** Ask a few readers to estimate the same segment with and without decile ticks and compare absolute error.
**Stronger Test:** Run a small randomized comparison measuring mean absolute error across a set of target percentages.

## What to do instead if decile ticks are too visually heavy <!-- role: fix -->

- Use fewer but more targeted internal reference cues that match the specific estimation ranges you expect viewers to judge.
- Add a direct numeric label for the highlighted segment if the task is to read the value rather than estimate it from the mark.
- Switch to a different part-to-whole chart form that performs well for estimation in your context and validate with a quick accuracy check.
