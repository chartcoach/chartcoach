---
id: increase-denominator-for-impact
title: Scale Up Denominators to Increase Perceived Treatment Helpfulness
bibliography: references.bib
description: Use larger denominators (e.g., 1,000 vs. 100) in icon arrays to make
  risks and treatment effects appear more significant.
labels:
- chart:icon-array
- visual:density
- impact:persuasion
- data:ratio
---

## The Rule <!-- role: advice -->
When designing icon arrays, use a larger total number of icons (e.g., 1,000) rather than a smaller number (e.g., 100) if you intend to highlight the seriousness of a risk or the helpfulness of a treatment.

## The Logic <!-- role: reason -->
People tend to put more weight on information obtained from larger samples. A larger overall number of icons suggests a higher risk because "more people seem to be affected," even if the mathematical ratio is identical.
*   **The Principle:** The Ratio-Bias Effect (adapted for visuals).
*   **The Evidence:** Participants perceived baseline risks as more serious, and screenings as more helpful, when looking at arrays of 1,000 icons compared to arrays of 100 icons [@galesic_using_2009].

## Where to Apply <!-- role: context -->
*   **User Goal:** Persuasion or highlighting the efficacy of a medical intervention.
*   **Data Type:** Ratios and probabilities.
*   **Audience:** General audience, specifically when trying to encourage healthy behaviors (e.g., screenings).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Space constraints on mobile devices.
*   **Reason:** 1,000 distinct icons are difficult to render legibly on small screens.
*   **Scenario:** When the goal is strictly neutral calculation without persuasive intent.
*   **Reason:** The larger denominator introduces a psychological bias that increases perceived severity.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity and space.
*   **The Risk:** Clutter. Arrays of 1,000 icons can look dense and intimidating if not designed cleanly (e.g., using simple shapes like circles rather than detailed icons) [@galesic_using_2009].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a denominator of 100 to save space when the goal is to emphasize risk.
*   **Why it fails:** The study shows that 100-icon arrays result in lower ratings of risk seriousness and treatment helpfulness compared to 1,000-icon arrays.

## How to Check <!-- role: check -->
*   **Visual Sign:** Count the total grid size. Is it 10x10 (100) or roughly 32x32 (approx 1,000)?
*   **The Test:** If the "affected" group looks tiny and insignificant (e.g., 1 dot in a 100-dot grid), the risk may be perceived as negligible.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the representation from "1 in 100" to "10 in 1,000" and display the full 1,000 unit grid.
*   **Best Fix:** Use simple geometric shapes (circles) to manage the density of 1,000 icons without creating visual noise.
