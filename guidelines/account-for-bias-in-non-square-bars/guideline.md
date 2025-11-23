---
id: account-for-bias-in-non-square-bars
title: Account for Directional Bias in Non-Square Bars
bibliography: references.bib
description: Anticipate overestimation in wide bars and underestimation in tall bars
  when precise aspect ratios are impossible.
labels:
- chart:bar
- task:retrieve-value
- visual:bias
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
When using non-square bars, anticipate that users will overestimate values in wide bars and underestimate values in tall bars.

## The Logic <!-- role: reason -->
When a bar mark deviates from a square, memory reconstructs the shape by distorting the height to bring it closer to a square prototype.
*   **The Principle:** Systematic Recall Bias.
*   **The Evidence:** In experimental results summarized by Zeng and Battle [@zeng_review_2023], wide aspect ratios caused significant positive bias (overestimation), while tall aspect ratios caused significant negative bias (underestimation) [@ceja_truth_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Designing charts where space constraints prevent ideal aspect ratios.
*   **Data Type:** Quantitative comparisons using bar charts.
*   **Audience:** Analysts interpreting magnitude from visual memory.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The chart includes direct value labels on every bar.
*   **Reason:** Reading the number bypasses the visual estimation bias associated with the bar's shape.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Perceived Accuracy. Users relying on the visual signal alone will consistently misjudge the data.
*   **The Risk:** Decisions based on "tall" (thin) bars may be conservative because values are recalled as lower; decisions based on "wide" bars may be aggressive because values are recalled as higher.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Stretching a chart horizontally to fill a wide monitor without adding more data.
*   **Why it fails:** This creates wide aspect ratios for individual bars, inducing an overestimation bias where values appear "higher" in memory than reality.

## How to Check <!-- role: check -->
*   **Visual Sign:** Inspect the shape of the bars relative to a square.
*   **The Test:** If `Width > Height` significantly, expect overestimation. If `Height > Width` significantly, expect underestimation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add data labels to the bars to anchor the true value.
*   **Best Fix:** Re-scale the axes or resize the chart container to neutralize the extreme aspect ratio.
