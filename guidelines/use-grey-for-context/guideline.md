---
id: use-grey-for-context
title: Use Grey for Comparison Data
bibliography: references.bib
description: Highlight the main data in a bold color and relegate all comparison data
  to grey to focus attention.
labels:
- visual:color
- impact:focus
- task:compare
- data:multivariate
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Color the single most critical element (the "star" of the show) in a distinct hue, and color all contextual or comparison data in grey.

## The Logic <!-- role: reason -->
Color is a spotlight that tells the reader "Look there." When a chart contains significant comparison data, using multiple bright colors creates clutter.
*   **The Principle:** Selective Attention.
*   **The Evidence:** [@muth_better_charts_2017] argues that "Grey is the most important color in data vis" because it allows secondary data to exist in the background of the reader's attention while pushing the main story to the foreground.

## Where to Apply <!-- role: context -->
*   **User Goal:** Emphasizing one specific trend or category within a larger dataset.
*   **Data Type:** Charts with multiple series (e.g., spaghetti plots, multi-bar charts) where one series is the focus.
*   **Audience:** General audiences who need guidance on where to look.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** All data points are equally important.
*   **Reason:** If the user needs to distinguish between 10 equally valid competitors, highlighting only one introduces bias and obscures the others.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The specific identities of the "grey" data points become harder to distinguish from one another.
*   **The Risk:** The reader may ignore the context entirely if the contrast is too high.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Giving every line or bar a different distinct color.
*   **Why it fails:** It creates visual noise and fails to guide the eye to the critical element [@muth_better_charts_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there more than 2-3 distinct hues (excluding grey) on the chart?
*   **The Test:** squint at the chart. Does the main data point pop out, while the rest recedes?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Select all data series except the main one and change their color to light grey.
*   **Best Fix:** Use a bright color (like red) for the main series and a neutral grey for all comparison series to establish a clear visual hierarchy [@muth_better_charts_2017].
