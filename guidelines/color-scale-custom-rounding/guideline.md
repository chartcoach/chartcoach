---
id: color-scale-custom-rounding
title: Round Custom Values for Readable Legends
bibliography: references.bib
description: Convert computed interpolation breaks into rounded numbers to make legends
  easier to digest.
labels:
- chart:map
- visual:legend
- visual:text
- impact:readability
- task:communicate
---

## The Rule <!-- role: advice -->
After calculating optimal breaks (like Natural Breaks), manually convert the scale to "Custom" and round the break values to clean, easy-to-read numbers.

## The Logic <!-- role: reason -->
Algorithms like Natural Breaks produce precise but cognitively burdensome numbers (e.g., 4.1, 5.7, 7.9). According to [@muth_interpolation_2022], slightly adjusting these cuts to whole or simple numbers (e.g., 4, 6, 8) creates a "far more readable color key." The visual difference on the map is usually negligible ("barely visible"), but the improvement in user experience and legibility is significant.

## Where to Apply <!-- role: context -->
*   **User Goal:** To produce a publication-ready map that is easy to scan.
*   **Data Type:** Any classed data where the calculated breaks result in decimals.
*   **Audience:** General public or busy stakeholders who need to parse the legend quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise scientific or regulatory reporting.
*   **Reason:** If the cut-off point has legal or strict scientific significance (e.g., a toxicity threshold of exactly 5.7), rounding it would be factually incorrect.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Mathematical precision of the "Natural Break."
*   **The Risk:** You might accidentally move a value from one bucket to another if a region lies exactly on the boundary (e.g., a region with 4.05 becomes "High" instead of "Low" if you round 4.1 down to 4.0).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Rounding values too aggressively (e.g., rounding 12.3 to 20).
*   **Why it fails:** This fundamentally changes the distribution and can misrepresent the data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the legend. Does it contain values like "14.78%"?
*   **The Test:** Read the legend out loud. If it sounds like a math problem, it needs rounding.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Round to the nearest whole number or single decimal place (e.g., 4.1 → 4).
*   **Best Fix:** Compare the map before and after rounding. If only a few insignificant regions change color, the rounding is safe to apply.
