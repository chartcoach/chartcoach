---
id: use-area-charts-for-changing-composition-over-time
title: Use Area Charts to Show How Composition Changes Over Time
bibliography: references.bib
description: Choose area charts when your message is how parts-of-a-whole evolve across
  time.
labels:
- chart:area
- task:show-composition
- visual:area
- impact:clarity
- data:temporal
- audience:mainstream
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use an area chart to show how the internal breakdown of a total changes over time.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Stacked filled areas make part-to-whole structure over time visually salient.
- **The Evidence:** The post recommends area charts for intuitively showing how an internal breakdown (e.g., energy mix) changes over time [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Understanding changing composition (shares) across time.
- **Data Type:** Time series with categories that sum to a whole at each time point.
- **Audience:** Mainstream/general readers [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The task is to compare small differences between categories precisely.
- **Reason:** The post repeatedly favors bar/column encodings for easier precise comparison (especially for shares) over harder-to-compare shapes [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Exact values can be harder to read than in bars/lines.
- **The Risk:** Smaller categories can become visually minimized or hard to compare (especially away from the baseline) [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using an area chart when the real question is ranking categories at one point in time.
- **Why it fails:** Area emphasizes evolution and composition; ranking is usually clearer with bars [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers would need to estimate thin layers to answer the main question.
- **The Test:** Ask, “Is my headline about changing shares over time?” If not, an area chart is likely the wrong fit [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If you only need a few time points, switch to stacked columns.
- **Best Fix:** If the main task is comparing category sizes (not composition over time), switch to bars/columns that support that comparison [@muth_chart_types_guide_2025].
