---
id: accept-scrolling-for-precision
title: Accept Scrolling for High-Precision Comparison
bibliography: references.bib
description: While slow, standard scrolled bar charts provide the highest accuracy
  for comparing specific values in long lists.
labels:
- chart:bar
- task:compare
- impact:accuracy
- visual:length
- interaction:scrolling
---

## The Rule <!-- role: advice -->
If the user's critical requirement is high-precision comparison between items or estimating exact values, use a standard linear bar chart and allow the user to scroll. Do not use compact alternatives like packed or piled bars.

## The Logic <!-- role: reason -->
The standard bar chart provides a single common baseline and linear scaling, which are the most robust perceptual cues for comparison. Novel compact visualizations often compromise these cues.
*   **The Principle:** Distorting the layout to fit one screen (e.g., packing or piling) destroys the shared baseline or introduces visual noise, degrading performance in comparison tasks.
*   **The Evidence:** Scrolled bar charts (E-1) consistently ranked in the top tier for accuracy across comparison and aggregation tasks. While they were the slowest due to interaction costs, they minimized error better than packed (E-4) or piled (E-5) alternatives [@mylavarapu_ranked-list_2019; @zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise extraction of values or comparing two items (e.g., "Who sold more, person A or person B?").
*   **Data Type:** Long lists where fidelity is more important than overview.
*   **Audience:** Users who need to trust the exact visual representation of the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to make a decision in under a few seconds.
*   **Reason:** The interaction cost of scrolling makes this design the slowest among all tested variations [@mylavarapu_ranked-list_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Speed. Users must perform physical actions (scrolling) to see the data.
*   **The Risk:** Users may miss data "below the fold" if they do not realize the chart scrolls.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "Packed Bars" to eliminate the scrollbar.
*   **Why it fails:** Packed bars (E-4) performed significantly worse in comparison accuracy because items do not share a common baseline [@mylavarapu_ranked-list_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the chart squeezing marks into a complex arrangement to avoid a scrollbar?
*   **The Test:** Select two random items. Is it instantly obvious which one is larger? If you have to decipher the layout first, the precision is lost.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Enable overflow scrolling on the chart container.
*   **Best Fix:** Use a standard list view with horizontal bars and a clear vertical scrollbar, ensuring the axis remains visible (sticky) while scrolling.
