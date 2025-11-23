---
id: explicitly-encode-data-differences
title: Explicitly Encode Differences Between Data Pairs
bibliography: references.bib
description: When comparing data pairs, plotting the calculated difference (delta)
  is significantly faster and more accurate than plotting the absolute values.
labels:
- chart:delta-chart
- chart:dot-plot
- task:compare
- task:filter
- task:sort
- task:aggregate
- visual:position
- visual:length
- impact:efficiency
- impact:accuracy
---

## The Rule <!-- role: advice -->
When the user's primary task is to compare two values (e.g., "Pre vs. Post" or "Group A vs. Group B"), explicit visualize the difference (the delta) as its own mark. Do not rely on the user to visually estimate the difference between two absolute value marks.

## The Logic <!-- role: reason -->
Visualizing the delta directly removes the cognitive step of mentally subtracting one value from another.
*   **The Principle:** Direct Encoding of Relations.
*   **The Evidence:** Experiments collated by [@zeng_review_2023] and conducted by [@nothelfer_measures_2020] show massive performance gains when using delta charts. For "filter" tasks (searching for specific differences), delta encodings were significantly faster. For "sort" and "aggregate" tasks, delta encodings yielded significantly higher accuracy compared to standard charts showing absolute values (like paired bars or slope graphs).

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying magnitude of change, sorting by difference, or estimating the average change across a group.
*   **Data Type:** Paired quantitative data (e.g., 2022 vs. 2023 sales, Treatment vs. Control).
*   **Audience:** Analytical users needing to make rapid decisions based on change or disparity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The absolute baseline values are critical for context (e.g., a 5% increase on \$1 is different than on \$1,000,000).
*   **Reason:** Delta charts often hide the "starting line." In these cases, consider a "difference overlay" or showing the delta adjacent to the absolute values, rather than replacing them entirely.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Context of the original scale. You lose the ability to see the raw magnitude of the individual data points.
*   **The Risk:** Users may misinterpret a small delta as significant without knowing the total volume (e.g., "small n" problems).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard grouped bar chart or a slope graph (line chart connecting two points).
*   **Why it fails:** [@nothelfer_measures_2020] demonstrated that even though slope graphs connect the points, users are still significantly slower and less accurate at perceiving the relationship compared to a simple mark representing the difference.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you asking the user to look at two points and estimate the gap size?
*   **The Test:** Ask a user, "Which pair has the largest increase?" If they have to scan back and forth between two bars or points to answer, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a data label explicitly stating the numeric difference next to the pair.
*   **Best Fix:** Switch to a "Delta Chart" (e.g., a dot plot or floating bar) where the mark's position or length represents the difference itself (Results E-2, E-4 in the study).
