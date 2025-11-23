---
id: reduce-number-precision
title: Reduce Number Precision
bibliography: references.bib
description: Remove unnecessary decimal places and abbreviate large numbers to improve
  memorability.
labels:
- data:numerical
- impact:cognitive-load
- visual:text
---

## The Rule <!-- role: advice -->
Don't add unnecessary precision. Use formats that abbreviate high numbers (e.g., "12.8k" instead of "12,831") and remove trailing zeros or excessive decimals.

## The Logic <!-- role: reason -->
Very few readers remember numbers with lots of decimal places or specific thousands places. Excessive precision makes a visualization look complicated and unattractive. Abbreviated formats (20b, 20m, 20k) or removing decimals (27% vs 27.0%) makes data easier to read and remember [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** scanning for trends and general magnitudes.
*   **Data Type:** Financial data, population stats, percentages.
*   **Audience:** General audience.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Financial auditing or engineering specs.
*   **Reason:** When the exact integer value is critical for reconciliation or safety.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Exactness in the visual layer.
*   **The Risk:** A reader might assume a rounded number is the exact number.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing 2 decimal places by default (e.g., "22.00%") just because the software allows it.
*   **Why it fails:** It adds visual noise without adding information.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do your axis labels or data labels have more than 3-4 digits/characters?
*   **The Test:** Read the number out loud. If it takes a long time to say (e.g., "twelve thousand eight hundred and thirty-one"), it should be abbreviated.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change number formatting settings to "0.[0]a" (or equivalent) to auto-abbreviate (k, m, b).
*   **Best Fix:** Use abbreviated numbers in the chart, but allow the exact number to appear in a tooltip or a downloadable dataset for those who need it.
