---
id: use-event-striping-to-make-outlier-counting-accurate
title: Use Event Striping to Make Outlier Counting Accurate
bibliography: references.bib
description: Highlight outliers explicitly (event striping) when users must compare
  how many unusual points occur across time blocks.
labels:
- chart:heatmap
- task:count
- task:compare
- visual:color
- impact:accuracy
- data:temporal
- audience:novice
- custom:technique-event-striping
- source:albers-2014
---

## The Rule <!-- role: advice -->

When the task is “which month has the most outliers,” explicitly mark outliers as salient events (event striping) instead of expecting users to infer them from raw traces or unboosted colorfields.

## The Logic <!-- role: reason -->

Outlier counting is a hybrid task: users must identify points that violate a context (summary) and then estimate numerosity. By devoting explicit visual emphasis to outliers (stripes), the display reduces the detection step and supports accurate counting/comparison across months.

- **The Principle:** Explicit outlier mapping (“visual boosting”) improves outlier detection and comparison.
- **The Evidence:** Event striping significantly outperformed all other evaluated encodings for the outlier-count task [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare months by number of unusual/outlier days.
- **Data Type:** Time series where outliers are meaningful events (e.g., anomalies).
- **Audience:** Users without specialized statistical training who need to spot/count anomalies.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is comparing other summaries (e.g., average, spread) rather than outliers.
- **Reason:** The paper notes event striping underperformed standard colorfields for summary tasks other than outlier detection, despite visual similarity [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual emphasis on outliers can distract from overall distribution patterns.
- **The Risk:** If outlier definition is wrong or not aligned to user expectations, the visualization can mislead by over-highlighting the “wrong” events [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using woven colorfields to make “interesting values pop” and then trying to count outliers.
- **Why it fails:** In the outlier experiment, woven colorfields underperformed other conditions; weaving disrupts point identification needed for counting specific events [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users disagree widely on which days are “outliers” and miss months with many unusual points.
- **The Test:** Create examples where the month with the most outliers does not have the largest single extreme; if users pick the extreme month, outliers aren’t being explicitly supported [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Overlay explicit outlier markers/stripes on the existing display.
- **Best Fix:** Use event striping: a context-preserving background (e.g., smoothed colorfield) plus explicit, high-salience outlier stripes to enable accurate month-by-month outlier counting [@albersTaskdrivenEvaluationAggregation2014a].
