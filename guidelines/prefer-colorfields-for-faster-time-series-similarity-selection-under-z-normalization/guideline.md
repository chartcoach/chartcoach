---
id: prefer-colorfields-for-faster-time-series-similarity-selection-under-z-normalization
title: Use Colorfields for Faster Similarity Choices When Amplitude/Offset Invariance
  Matters
bibliography: references.bib
description: When users must visually choose the most similar time series and amplitude/offset
  should be treated as invariant, colorfields yield faster decisions than horizon
  graphs.
labels:
- chart:colorfield
- task:cluster
- visual:color
- impact:efficiency
- data:temporal
- audience:general
- invariance:amplitude-offset
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a colorfield (color-hue over time) instead of a horizon graph when people must quickly pick the most similar time series and amplitude/offset differences should not dominate the judgment.

## The Logic <!-- role: reason -->

Colorfields led to faster task completion than horizon graphs when participants performed similarity selection under the experiment condition contrasting Euclidean distance with z-normalized Euclidean distance; this is collated as a time ranking where the best-performing designs were line chart and colorfield (tied) ahead of horizon graph [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

- **The Principle:** Reduce decision time by avoiding the slower encoding for this similarity-selection task.
- **The Evidence:** Completion-time ranking places line chart and colorfield ahead of horizon graph for the second clustering/similarity condition [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Select the most similar time series from a small set of candidates.
- **Data Type:** Temporal (time series) with quantitative values over an ordinal time axis.
- **Audience:** General users (non-expert participants).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need the fastest possible option relative to a line chart specifically.
- **Reason:** In the same experiment condition, line chart and colorfield were grouped as equivalent in time (no observed ordering between them), so this rule does not justify choosing colorfield over line chart on speed alone [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the horizon graph’s combined encoding (area + color-hue bands) that may be desirable for other considerations not covered by this extracted result.
- **The Risk:** If your goal is not decision speed, you may optimize the wrong metric, because this guideline is only supported by time rankings for this task setup [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing a horizon graph by default for compactness even when speed is the primary goal.
- **Why it fails:** Horizon graphs ranked slower than the alternatives in the relevant time-based result [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users visibly hesitate longer before committing to a choice when viewing horizon graphs, compared to colorfields for the same candidate set.
- **The Test:** A/B test completion time for the same similarity-choice trials using colorfields vs. horizon graphs; if horizon graphs are slower, you’ve violated the rule [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the horizon graph view for a colorfield view while keeping the same ordering and number of candidates.
- **Best Fix:** Offer colorfields (or line charts) as the default view for this similarity-choice step, and reserve horizon graphs for other steps or views not governed by time-to-decision [@zengReviewCollationGraphical2023; @gogolouComparingSimilarityPerception2019].
