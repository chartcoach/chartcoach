---
id: use-event-striping-to-identify-the-month-with-the-most-outliers
title: Use event striping to identify the month with the most outliers
bibliography: references.bib
description: When the task is to compare outlier counts across months, explicitly
  highlight outliers as stripes to improve accuracy.
labels:
- chart:heatmap
- task:find-anomalies
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- granularity:monthly
---

## Use outlier-highlighting stripes for month-level outlier-count tasks <!-- role: advice -->

Use an event-striping design that highlights outliers as visually salient stripes when viewers must decide which month contains the most unusual (outlier) days.

## Why explicit outlier highlighting supports outlier counting <!-- role: reason -->

Outlier-counting requires both detecting unusual values and estimating how many occur; making outliers visually prominent reduces missed detections and supports counting.

**Mechanism:** Salient outlier marks separate rare events from background variation, so viewers can focus on counting marked events rather than inferring outliers from subtle changes.

**Evidence:** For the outlier-count (find-anomalies) task, the event-striping design (E-7) ranked highest in accuracy and significantly outperformed all other evaluated designs in that task set. [@albersTaskdrivenEvaluationAggregation2014; @zengReviewCollationGraphical2023]

**Notes:** This guideline is specific to outlier counting across months, not to general pattern finding.

## When users must pick the month with the most unusual days <!-- role: context -->

- **User Goal:** Determine which month contains the most outliers.
- **Task:** Find anomalies (count outliers) across time windows.
- **Data:** Temporal quantitative series where “outlier” has been operationalized (e.g., unusually high/low relative to context).
- **Chart Setting:** Static; sufficient display resolution to make stripes distinct.
- **Audience:** General audiences performing detection-and-counting.
- **Success Criterion:** Higher accuracy in selecting the correct month.

## When not to use event striping as the primary view <!-- role: exceptions -->

**Break it when:** The task is to compare averages or spreads rather than count outliers. **Why:** An outlier-emphasizing design can pull attention toward rare events and away from the bulk of the distribution.

## Tradeoffs of outlier striping <!-- role: costs -->

**Sacrifice:** Additional design and computation to define and render outliers.\
**Risk:** Overemphasis can cause readers to overestimate the importance of rare events.\
**Mitigation:** Clearly label what is considered an outlier and keep contextual background visible.

## Common outlier-spotting mistakes <!-- role: mistakes -->

**Mistake:** Using a non-boosted, general-purpose time-series display for an outlier-count question. **Why it fails:** Accuracy was lower than with event striping for the outlier-count task.

## Quick checks for outlier-count support <!-- role: check -->

**Failure Sign:** Readers report “I can’t tell what counts as an outlier” or they miss visually obvious spikes/dips.\
**Quick Check:** Ask a few readers to count outliers in a month; if they cannot do it consistently, the outlier cues are not salient enough.\
**Stronger Test:** Run a small accuracy test comparing a standard display to event striping for the same outlier-count questions.

## What to do instead if event striping cannot be implemented <!-- role: fix -->

- Add explicit markers for outlier days on top of an existing time-series chart.
- Provide a separate per-month summary of outlier counts alongside the main time-series view.
- Reduce noise in the baseline display (e.g., show a smoothed context line) so outliers stand out more clearly.
