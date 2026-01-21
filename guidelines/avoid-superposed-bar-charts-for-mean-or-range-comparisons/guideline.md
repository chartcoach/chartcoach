---
id: avoid-superposed-bar-charts-for-mean-or-range-comparisons
title: Avoid Superposing Bar Sets When Comparing Means or Ranges
bibliography: references.bib
description: Do not overlay two bar-chart series when the task is set-to-set mean
  or range comparison; it reduces precision.
labels:
- chart:bar
- task:compare
- task:rank
- visual:color
- visual:position
- impact:accuracy
- impact:clarity
- data:categorical
- audience:novice
- layout:superposed
- source:jardine-2020
---

## The Rule <!-- role: advice -->

Do **not** use a superposed/overlaid bar chart when the user task is to compare **which set has the larger mean** or **larger range**.

## The Logic <!-- role: reason -->

Overlaying forces separation by color rather than by space and degrades the perceptual cues that support set-level judgments; in both experiments, superposed charts produced the **lowest precision** [@jardinePerceptualProxiesVisual2020a].

- **The Principle:** Perceptual proxies depend on available spatial separation cues
- **The Evidence:** Superposed was least precise for both MAXMEAN and MAXRANGE [@jardinePerceptualProxiesVisual2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Choose which of two groups has higher average or greater spread
- **Data Type:** Two comparable sets of bars (same categories)
- **Audience:** Non-experts making fast judgments (e.g., brief “glance” comparisons)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is an **item-to-item** comparison like “which category changed the most?”
- **Reason:** The paper contrasts its results with prior work where superposition/animation supported biggest-delta judgments; superposition is not universally bad—only task-dependent [@jardinePerceptualProxiesVisual2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the compactness of fitting both series into a single coordinate space.
- **The Risk:** Switching away from overlay can increase required screen real estate.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the overlay and increasing opacity/contrast to “make both readable.”
- **Why it fails:** The core issue is the arrangement’s reduced precision for these tasks, not merely legibility [@jardinePerceptualProxiesVisual2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars overlap heavily and viewers rely on color filtering to parse sets.
- **The Test:** Temporarily desaturate the chart (or imagine it without color). If the sets become hard to separate, the layout is likely harming mean/range comparison.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the overlay to stacked small multiples (top/bottom).
- **Best Fix:** Use vertically stacked small multiples, which the paper found most supportive for both mean and range comparisons [@jardinePerceptualProxiesVisual2020a].
