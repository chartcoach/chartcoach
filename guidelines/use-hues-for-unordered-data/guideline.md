---
id: use-hues-for-unordered-data
title: Use Hues for Unordered Categories
bibliography: references.bib
description: Use qualitative color scales (hues) for nominal data to avoid implying
  rank.
labels:
- visual:color
- data:categorical
- data:nominal
- impact:clarity
- task:distinguish
---

## The Rule <!-- role: advice -->
Use qualitative color scales (hues) when your values do not have an inherent order. Conversely, use quantitative scales (shades/gradients) if the data has a natural order.

## The Logic <!-- role: reason -->
When data categories have no intrinsic ranking (e.g., countries like Iran, Morocco, Pakistan), no single category is "better" or "higher" than another. Using distinct hues treats them as equals. However, if values represent ordered concepts—like unemployment rates, Likert scales (strongly agree to strongly disagree), or clothing sizes (XS to XXL)—quantitative scales are required because these possess an inherent hierarchy [@muth_quantitative_vs_qualitative_2021].

## Where to Apply <!-- role: context -->
*   **Data Type:** Nominal data (industries, countries, names).
*   **User Goal:** Distinguishing between items without comparing their magnitude.
*   **Audience:** General audiences interpreting categorical differences.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The categories have an underlying value you wish to emphasize (e.g., ranking countries by GDP).
*   **Reason:** In this case, you are encoding a quantitative variable (the rank or value) rather than just the category identity [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to encode a secondary variable (like rank) through color brightness.
*   **The Risk:** If you use hues for ordered data (like "Low, Medium, High"), the user must constantly consult the legend to understand the sequence.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a gradient (light blue to dark blue) for unordered countries.
*   **Why it fails:** Readers will subconsciously assume the dark blue country is "more" or "better" than the light blue country.

## How to Check <!-- role: check -->
*   **The Test:** Ask yourself, "Is category A inherently larger, faster, or better than category B?"
*   **Visual Sign:** If the answer is "No," but your chart uses light-to-dark colors, you have broken the rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the palette to a qualitative scheme (e.g., red, yellow, blue).
*   **Best Fix:** Ensure the colors are distinct in hue but relatively similar in saturation and brightness to avoid implied hierarchy.
