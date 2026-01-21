---
id: explicitly-encode-extrema-when-users-compare-minima-maxima-or-range
title: Explicitly Encode Extrema for Extrema and Range Tasks
bibliography: references.bib
description: Add explicit monthly minima/maxima encodings when tasks require comparing
  extrema or ranges across time blocks.
labels:
- chart:box
- chart:stock
- task:compare
- task:locate
- visual:position
- visual:color
- impact:accuracy
- data:temporal
- audience:novice
- source:albers-2014
---

## The Rule <!-- role: advice -->

When the task is to compare monthly maxima, minima, or ranges, explicitly encode each month’s min and max (not just the raw series).

## The Logic <!-- role: reason -->

Showing the relevant statistic reduces the viewer’s need to visually search and mentally compute extrema (or their difference). In the study, encodings that explicitly showed monthly extrema improved performance within their visual-variable group (e.g., color stock charts among color encodings; box plots/modified stock charts among position encodings for certain extrema/range tasks).

- **The Principle:** Mapping task-relevant statistics into the display reduces mental computation burden.
- **The Evidence:** For minima and range, designs explicitly encoding local extrema outperformed comparable designs that did not; for maxima, explicit extrema helped within color encodings but not uniformly across all position encodings due to specific issues with box plots [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Pick the month with the highest day, lowest day, or largest (max–min) range.
- **Data Type:** Time series compared across discrete blocks (months).
- **Audience:** Viewers who must answer quickly without calculation tools.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot assume the comparison granularity (e.g., users may compare weeks, months, quarters interchangeably).
- **Reason:** Explicit extrema computed at one granularity can misalign with the user’s intended granularity, potentially harming flexibility [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computed overlays/glyphs can increase information density.
- **The Risk:** Added elements can create clutter or draw attention away from other patterns the user might need [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding only the average (mean) and assuming users can infer maxima/minima from it.
- **Why it fails:** Extrema tasks depend on specific points, and mean is not a reliable proxy; the paper notes deliberate decorrelation to prevent such confounds [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly “hunt” inside each month to estimate the top and bottom.
- **The Test:** Remove access to interaction/hover and see if users can still reliably identify the correct month for min/max/range; if not, extrema likely need explicit encoding [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add per-month min/max indicators (e.g., range bars) while keeping the underlying display.
- **Best Fix:** Use a design that natively encodes minima and maxima per block (e.g., modified stock chart ranges or box-plot whiskers) when those are the primary tasks [@albersTaskdrivenEvaluationAggregation2014a].
