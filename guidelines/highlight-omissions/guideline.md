---
id: highlight-omissions
title: Acknowledge Data Omissions and Filtering
bibliography: references.bib
description: Prevent misleading interpretations by explicitly stating what data has
  been excluded or filtered out.
labels:
- data:filtering
- impact:integrity
- visual:annotation
- task:inform
---

## The Rule <!-- role: advice -->
Explicitly indicate when data has been filtered, thresholded, or aggregated to prevent users from assuming the visualization represents the complete phenomenon.

## The Logic <!-- role: reason -->
Omission is a powerful rhetorical technique because it is difficult for users to detect. Users typically assume "Metonymy"—that the visible selection of variables or data points represents the whole. If you omit outliers, threshold axes, or filter categories (e.g., showing only "traditional families" and omitting others), users will infer general patterns that may not exist in the full dataset. Explicitly noting these "information access" choices prevents misleading framing [@hullman_visualization_2011].

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the scope of the data.
*   **Data Type:** Large datasets where aggregation or subsetting is necessary for clarity.
*   **Audience:** Users who might not know the full scope of the domain (e.g., census data).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly simplified, "glanceable" indicators (e.g., a stock ticker).
*   **Reason:** Space constraints and immediacy requirements may preclude detailed notes on exclusions.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity.
*   **The Risk:** Highlighting what is *missing* might confuse users or make them doubt the utility of what is *present*.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Silently removing outliers or "bad" data points to make a trend line look cleaner.
*   **Why it fails:** This is "bias" in the negative sense; it manipulates the user's perception of reality without their knowledge [@hullman_visualization_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for axis breaks or categorical legends that don't sum to 100%.
*   **The Test:** Ask, "If I were a user, would I know that [X] was removed from this chart?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a footnote: "Excludes values below [X]."
*   **Best Fix:** Use "ghost" data or grayed-out elements to visually suggest the existence of the omitted data in the background.
