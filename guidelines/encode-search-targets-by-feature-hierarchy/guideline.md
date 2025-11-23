---
id: encode-search-targets-by-feature-hierarchy
title: Prioritize Basic Features Over Spatial Arrangements
bibliography: references.bib
description: Use basic features like color or orientation for search targets, as they
  are processed significantly faster than spatial configurations.
labels:
- visual:color
- visual:shape
- task:search
- impact:efficiency
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->
To ensure users can find specific data points quickly, define the target using a single basic feature (like color or orientation). Avoid defining targets based on spatial configurations (like the arrangement of lines) or complex shapes.

## The Logic <!-- role: reason -->
Search tasks are not all created equal. Evidence from 1 million trials shows a distinct hierarchy of efficiency based on the visual properties of the target.
*   **The Principle:** Search Asymmetry. "Feature searches" (defined by unique color or orientation) yield the shallowest search slopes (fastest). "Conjunction searches" (combining two features) are slower. "Spatial-configuration searches" (e.g., finding a T among Ls) are the slowest and most inefficient [@wolfe_what_1998].
*   **The Evidence:** Wolfe's meta-analysis shows that spatial-configuration searches produce significantly steeper reaction time slopes than feature searches, indicating that spatial relationships are not processed in parallel across items [@wolfe_what_1998].

## Where to Apply <!-- role: context -->
This advice applies whenever a user must scan a dense display to find specific items.
*   **User Goal:** Rapid identification of outliers, alerts, or specific categories.
*   **Data Type:** Scatterplots, dense maps, or grids of icons.
*   **Audience:** Users monitoring real-time data or performing time-sensitive analysis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The target requires high precision in value reading rather than detection.
*   **Reason:** While spatial position is slow for *search* (finding the item), it is the most accurate channel for *estimation* (reading the value). If the user knows where to look, spatial configuration is fine.
*   **Scenario:** "Hard" feature searches.
*   **Reason:** Not all features "pop out." Searching for a specific orientation (e.g., 15 degrees) among similar distractors (e.g., 10 degrees) can be as slow as spatial search if the target is not categorically different (e.g., steep vs. shallow) [@wolfe_what_1998].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You have a limited number of distinguishable colors and orientations (usually 5-8) before the display becomes cluttered.
*   **The Risk:** Overusing color for search targets can create a "fruit salad" effect, reducing the salience of the actual target.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using rotation (orientation) to encode categorical data in a way that requires distinguishing a "T" from an "L" or a "d" from a "b".
*   **Why it fails:** This forces the user into a "spatial-configuration search," which forces a slow, serial scan of the display [@wolfe_what_1998].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to look at each item individually to tell if it is the target?
*   **The Test:** Flash the visualization for 200ms. Can the user report the presence of the target? If not, the search slope is likely too steep.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Map the most critical search target to a high-contrast color (e.g., Red among Grey).
*   **Best Fix:** Redesign the markers so the target is distinct by a basic feature (unique color) rather than a conjunction of features (red AND square) or spatial arrangement.
