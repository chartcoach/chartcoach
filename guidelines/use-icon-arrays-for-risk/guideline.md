---
id: use-icon-arrays-for-risk
title: Use Icon Arrays to Communicate Treatment Risk
bibliography: references.bib
description: Use icon arrays to prevent denominator neglect when communicating medical
  risk reductions.
labels:
- chart:icon-array
- task:compare
- impact:clarity
- data:categorical
- audience:novice
- audience:patient
- complexity:low
---

## The Rule <!-- role: advice -->
Represent medical risk and treatment effects using icon arrays (pictographs) that display the entire population, including those who are unaffected.

## The Logic <!-- role: reason -->
People suffer from "denominator neglect"—they focus on the absolute number of events (e.g., "80 deaths") while ignoring the total size of the group (e.g., "out of 800"). This leads to distorted risk perceptions, especially when comparing groups of different sizes. Icon arrays force the viewer to visually process the superordinate class (the denominator), reducing this bias.
*   **The Principle:** Denominator Neglect mitigation.
*   **The Evidence:** [@garcia-retamero_communicating_2009]

## Where to Apply <!-- role: context -->
Use this when presenting risk reductions or treatment efficacy, particularly in medical contexts.
*   **User Goal:** Accurately estimating whether a treatment reduces risk.
*   **Data Type:** Ratios or probabilities where the group sizes (denominators) might differ (e.g., 80/800 vs. 5/100).
*   **Audience:** General public, patients, and specifically individuals with low numeracy skills.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-numeracy audiences viewing data with strictly equal denominators.
*   **Reason:** The paper shows that when denominators are identical (e.g., 800 vs 800) and numeracy is high, text-based accuracy is comparable to visual accuracy. However, visuals remain safer for mixed audiences.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Displaying 100 or 1000 individual icons takes significantly more space than a single number or a bar.
*   **The Risk:** If the array is too dense or the icons are too small, readability may suffer (though the paper successfully used arrays of up to 800 dots).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing only the "events" (e.g., only the 5 dead patients) without the "non-events" (the 95 survivors).
*   **Why it fails:** This reinforces denominator neglect by hiding the context required to calculate the ratio [@garcia-retamero_communicating_2009].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can I see the people who *didn't* die (or didn't experience the event)?
*   **The Test:** If you remove the text labels, can you still roughly estimate the proportion of the group affected?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the total population number (N=100) in large text next to the event count.
*   **Best Fix:** Implement a grid-based icon array where every individual in the sample is represented by a dot or icon, with affected individuals clearly distinguished by color (e.g., black circles at the end of the array).
