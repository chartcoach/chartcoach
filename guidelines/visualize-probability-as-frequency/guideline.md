---
id: visualize-probability-as-frequency
title: Visualize Probabilities as Natural Frequencies
bibliography: references.bib
description: Use icon arrays or discrete elements to represent risk, helping users
  with low numeracy perform perceptual comparisons.
labels:
- data:probability
- data:risk
- visual:icon-array
- audience:low-numeracy
- impact:accessibility
- industry:healthcare
---

## The Rule <!-- role: advice -->
When communicating risk or probability (e.g., "10% risk"), represent the data visually using natural frequencies (e.g., 10 icons out of 100) rather than abstract percentages or text alone.

## The Logic <!-- role: reason -->
Many people have low "graph literacy" or numeracy. Visualizations that capitalize on Type 1 processing allow these users to make "perceptual comparisons" (seeing that one group of dots is denser than another) rather than performing mathematical calculations. [@padilla_decision_2018] notes that this approach provides a "dual benefit": it is intuitive for novices while remaining accurate for experts.

*   **The Principle:** Perceptual Facilitation / Type 1 Processing
*   **The Evidence:** Galesic et al. (2009), cited in [@padilla_decision_2018], demonstrated that icon arrays helped individuals with lower numeracy accurately understand medical risks, overcoming the difficulties associated with abstract probabilities.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding personal risk, side effects, or treatment efficacy.
*   **Data Type:** Probabilities, percentages, and ratios.
*   **Audience:** General public, patients, or audiences with varied educational backgrounds.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Very small probabilities (e.g., 1 in 1,000,000).
*   **Reason:** Icon arrays become unreadable at very large denominators. The "foreground effect" (focusing only on the active icons and ignoring the massive base rate) can skew perception, as noted by Stone et al. (1997) in [@padilla_decision_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space. Icon arrays take up significantly more room than a bar chart or text.
*   **The Risk:** If the array is not laid out clearly (e.g., random scattering vs. a grid), users may struggle to count or compare areas.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing two different risks with different denominators (e.g., 1 in 10 vs 5 in 100) without normalizing the visual layout.
*   **Why it fails:** It forces a mathematical conversion (Type 2 processing), negating the benefit of the visual aid.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the data represented as a solid bar or a number?
*   **The Test:** Ask a user "How many people out of 100 would be affected?" If they have to do mental math to convert a percentage to a count, the visualization is not maximizing perceptual facilitation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a concrete text label: "10 out of 100 people."
*   **Best Fix:** Replace the bar or pie chart with a 10x10 grid of icons, coloring the active number to represent the probability.
