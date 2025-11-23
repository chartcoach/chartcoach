---
id: add-shadow-lines-for-context
title: Add Shadow Lines to Enable Comparison
bibliography: references.bib
description: Repeat all lines as a faint background in every panel to allow comparison
  across small multiples.
labels:
- chart:small-multiples
- visual:context
- task:compare
- impact:context
---

## The Rule <!-- role: advice -->
Repeat all lines from the dataset in the "background" of every single panel using a neutral, faint color (e.g., light gray), while highlighting only the panel's specific subject line.

## The Logic <!-- role: reason -->
*   **The Principle:** Contextual Comparison.
*   **The Evidence:** Small multiples inherently make it difficult to compare data points at specific times across different panels. [@muth_small_multiple_line_charts_2024] suggests that repeating all lines in the background enables readers to see how the focal category ranks against the others (higher or lower) at any given point, bridging the gap between a single chart and isolated panels.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the performance of one category against the group average or the rest of the cohort.
*   **Data Type:** Small multiple line charts where the Y-axis scales are identical (shared scales).
*   **Audience:** Readers looking for outliers or ranking context.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset contains hundreds of lines.
*   **Reason:** The background will become a solid block of color (ink), providing no useful definition.
*   **Scenario:** Panels use independent Y-axis scales.
*   **Reason:** Shadow lines from other panels would be misleading if plotted on different scales.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increases the visual density (ink-to-data ratio) of each panel.
*   **The Risk:** If the background lines are too dark, they distract from the main data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Leaving panels empty of context.
*   **Why it fails:** The reader sees a trend going "up" but doesn't know if it went up *more* or *less* than the others.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the highlighted line exist in a void, or can you see the "cloud" of other data behind it?
*   **The Test:** Ask, "Is this category performing better than average?" If you can't answer immediately, add shadow lines.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the full dataset to every panel in light grey (#dddddd).
*   **Best Fix:** Add the full dataset in grey and ensure the main line is a high-contrast color (e.g., blue or red).
