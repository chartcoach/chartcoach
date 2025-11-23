---
id: superimpose-uncertainty
title: Superimpose Uncertainty Instead of Juxtaposing
bibliography: references.bib
description: Integrate uncertainty directly into the main chart rather than using
  side-by-side comparisons.
labels:
- chart:bivariate-map
- chart:choropleth
- task:information-fusion
- visual:layout
- impact:accuracy
- data:spatial
---

## The Rule <!-- role: advice -->
Encode uncertainty and data values simultaneously in a single chart (superposition), rather than placing a data map next to an uncertainty map (juxtaposition).

## The Logic <!-- role: reason -->
Juxtaposition turns an information fusion task into a search task. The user must look at a location on one map, hold the value in working memory, search for the corresponding location on the second map, and then synthesize the result. This introduces significant error.
*   **The Principle:** Perceptual Integrality and Cognitive Load.
*   **The Evidence:** In identification tasks, superimposed charts achieved 58% accuracy compared to 51% for juxtaposed charts. Juxtaposition forced participants to perform "error-prone correspondence" between two dense maps [@correll_value-suppressing_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Integrating two variables (Value + Uncertainty) to make a single judgment about a specific data point.
*   **Data Type:** Spatially co-located data (e.g., heatmaps, choropleth maps).
*   **Audience:** General audiences or analysts performing rapid assessments.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The variables are completely orthogonal and the user needs to analyze the distribution of uncertainty *independently* of value.
*   **Reason:** If the goal is to see "Where is our data generally poor?" regardless of the values, a separate map isolates that pattern more clearly.
*   **Scenario:** Extreme visual complexity.
*   **Reason:** If the bivariate map is illegible due to too many colors/textures, interaction (highlighting across linked views) might be a necessary compromise [@correll_value-suppressing_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity of the legend. Univariate legends (used in juxtaposition) are easier to memorize than bivariate legends.
*   **The Risk:** Inter-channel interference. Color dimensions (like saturation and lightness) interact, making it harder to perceive one variable completely independently of the other.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing two heatmaps side-by-side without interaction.
*   **Why it fails:** Users struggle to align specific grid cells or regions mentally between the two views.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have two separate charts for the same spatial area—one saying "Value" and one saying "Confidence"?
*   **The Test:** Ask a user to find a point with "High Value and Low Confidence." Watch their eyes. If they dart back and forth repeatedly, you are using juxtaposition.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use interaction to link the views (hovering one highlights the other).
*   **Best Fix:** Merge the variables into a single bivariate color map or glyph-based encoding.
