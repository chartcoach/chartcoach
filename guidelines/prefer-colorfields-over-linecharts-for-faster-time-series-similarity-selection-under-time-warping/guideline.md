---
id: prefer-colorfields-over-linecharts-for-faster-time-series-similarity-selection-under-time-warping
title: Use Colorfields Instead of Line Charts to Reduce Time in Time-Warping Similarity
  Choices
bibliography: references.bib
description: For time-series similarity selection in a time-warping context (ED vs
  DTW), colorfields enable faster completion than line charts.
labels:
- chart:colorfield
- chart:line
- task:cluster
- visual:color
- visual:position
- impact:efficiency
- data:temporal
- audience:general
- invariance:time-warping
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When users must choose the most similar time series in a time-warping similarity context, prefer a colorfield over a line chart to reduce completion time.

## The Logic <!-- role: reason -->

In the experiment condition contrasting Euclidean distance (ED) with dynamic time warping (DTW), the time-based result ranks colorfield as faster than line chart, with statistically significant pairwise differences reported for colorfield over line chart and over horizon graph [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

- **The Principle:** Choose the encoding that minimizes time-to-decision for similarity selection.
- **The Evidence:** Time ranking for the first clustering/similarity condition is colorfield (best), then line chart, then horizon graph; significance pairs include colorfield beating line chart [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Pick which candidate time series is most similar to a query series.
- **Data Type:** Temporal sequences with quantitative values; candidates compared without alignment aids.
- **Audience:** General users (non-expert participants).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary requirement is not speed, or you need a positional trace for other judgments not captured here.
- **Reason:** This guideline is supported only for completion time under the similarity-choice task; it does not assert superiority on other metrics or tasks beyond what was extracted [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up explicit positional shape encoding of the quantitative series that a line chart provides.
- **The Risk:** If users need positional cues for reasons outside this time-to-choice objective, speed gains may come at the expense of those unmeasured needs in this evidence slice [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using line charts as the default for similarity selection because they are conventional.
- **Why it fails:** In the extracted time ranking for this task condition, line charts are slower than colorfields, and the difference is reported as significant [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users complete similarity selection faster with colorfields than with line charts on the same trials.
- **The Test:** Run a timed task where users pick the closest match; if line charts yield longer completion times than colorfields, you are not following the rule [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a toggle that switches a line chart small-multiple list into a colorfield list for the same candidates.
- **Best Fix:** Make colorfields the default view for time-warping similarity selection steps, and only fall back to line charts when users explicitly request positional detail [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].
