---
id: use-square-aspect-ratios-for-bars
title: Use Square Aspect Ratios for Bar Marks
bibliography: references.bib
description: Minimize memory bias in value retrieval by designing bars with a 1:1
  width-to-height ratio.
labels:
- chart:bar
- task:retrieve-value
- visual:shape
- impact:accuracy
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->
Design individual bar marks so that their aspect ratio (width-to-height) approximates a 1:1 square.

## The Logic <!-- role: reason -->
Human memory for position is influenced by the shape of the mark. The brain tends to "pull" the memory of a shape toward a "categorical prototype," which in this context is a perfect square.
*   **The Principle:** Categorical Prototype Effect / Perception Bias.
*   **The Evidence:** Experiments collated by Zeng and Battle [@zeng_review_2023] and conducted by Ceja et al. [@ceja_truth_2021] show that users systematically overestimate the height of wide bars and underestimate the height of tall bars. Bars with a square aspect ratio demonstrated no systematic bias in value retrieval.

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately retrieving or recalling specific values from a chart after viewing it.
*   **Data Type:** Quantitative values represented by length/position (Bar Charts).
*   **Audience:** General users performing value retrieval tasks where precision matters.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density datasets (e.g., time-series with many data points).
*   **Reason:** Achieving a 1:1 aspect ratio for every bar would require excessive horizontal space, making the chart unreadable or forcing scrolling.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen Real Estate. Square bars are significantly wider than the thin bars typically used in default charting libraries.
*   **The Risk:** Using square bars reduces the number of data points that can be displayed in a single view.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using extremely thin (tall) bars to fit more data into a dashboard.
*   **Why it fails:** This triggers a systematic underestimation bias, causing users to recall values as lower than they actually are [@ceja_truth_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the bars look like thin lines (tall/skinny) or flattened bricks (wide/short)?
*   **The Test:** Measure the pixel width and height of the average bar. Divide width by height. The result should be close to 1.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the width of the bars in your chart settings (often `barWidth` or `padding` adjustments).
*   **Best Fix:** Adjust the aspect ratio of the entire chart container or the axis scales to ensure the geometric representation of the average data point approaches a square.
