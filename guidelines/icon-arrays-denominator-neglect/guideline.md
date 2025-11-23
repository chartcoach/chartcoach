---
id: icon-arrays-denominator-neglect
title: Use Icon Arrays to Fix Denominator Neglect
bibliography: references.bib
description: Use icon arrays to help audiences consider the total sample size, not
  just the event count.
labels:
- chart:icon-array
- task:compare
- impact:clarity
- audience:older-adults
- audience:general-public
- data:risk-ratios
---

## The Rule <!-- role: advice -->
Supplement numerical risk statistics with icon arrays that explicitly visualize the entire population (the denominator) alongside the affected individuals (the numerator).

## The Logic <!-- role: reason -->
People suffer from "denominator neglect": they focus on the absolute number of times an event occurs (the numerator) and ignore the overall number of opportunities for it to happen (the denominator). For example, people often perceive 50 deaths out of 500 as "worse" than 10 deaths out of 100 simply because 50 is larger than 10, even though the rates are identical.
*   **The Principle:** Visualizing the whole population helps people represent superordinate classes (the denominator). This forces the viewer to attend to the relationship between the part and the whole, rather than just the count of events [@garcia-retamero_icon_2010].
*   **The Evidence:** In experiments comparing drug effectiveness, adding icon arrays increased the percentage of participants estimating risk reduction correctly from 52% to 86% when sample sizes differed [@garcia-retamero_icon_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately communicating treatment risk reduction or medical probabilities.
*   **Data Type:** Ratios where the sample sizes (denominators) differ between groups (e.g., comparing a treated group of 100 to a non-treated group of 500).
*   **Audience:** General audiences, and specifically **older adults**. Research shows icon arrays are particularly effective for older populations (who may face cognitive declines or lower numeracy), helping them reach accuracy levels comparable to younger adults [@garcia-retamero_icon_2010].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the denominators of the groups being compared are identical (e.g., comparing 10/500 vs 50/500).
*   **Reason:** The study found that when sample sizes were equal, participants were generally accurate (approx. 90%) even with only numerical text. Denominator neglect is primarily triggered when base sizes differ [@garcia-retamero_icon_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space. Icon arrays require significantly more physical screen or page real estate compared to simple bar charts, pie charts, or numerical text [@garcia-retamero_icon_2010].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reporting only the relative risk reduction (e.g., "Reduces risk by 50%") or counts (e.g., "2 people died") without the denominator.
*   **Why it fails:** This obscures the base rate. If the denominator is not transparent, users will judge the risk based solely on the absolute number of events, leading to significant estimation errors [@garcia-retamero_icon_2010].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization show a grid of individual units?
*   **The Test:** Can you count (or clearly see) the unaffected individuals just as easily as the affected ones? If the "non-events" are hidden, you are susceptible to denominator neglect.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the total sample size clearly in the text (e.g., "2 out of 100" instead of just "2").
*   **Best Fix:** Create a grid (icon array) representing the total sample (e.g., 100 circles), with the affected individuals colored differently (e.g., 2 black circles at the end of the array) [@garcia-retamero_icon_2010].
