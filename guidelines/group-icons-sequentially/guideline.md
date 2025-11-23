---
id: group-icons-sequentially
title: Group Icons in Sequential Blocks
bibliography: references.bib
description: Use blocked arrangements for icon arrays to ensure accurate estimation
  and prevent risk inflation.
labels:
- chart:icon-array
- chart:pictograph
- task:estimate
- visual:position
- impact:accuracy
- audience:patient
- audience:low-numeracy
---

## The Rule <!-- role: advice -->
Arrange affected stick figures (or icons) in a single, contiguous block or line (sequential arrangement). Do not scatter them randomly throughout the array.

## The Logic <!-- role: reason -->
<!-- Why does this work? Don't just say "it's better." Explain the mechanism. Is it about how the eye moves? How the brain counts? Cite your sources. -->
*   **The Principle:** **Summation vs. Estimation.** Estimating proportions from a random scatter requires the viewer to mentally sum non-contiguous areas, which is cognitively effortful and error-prone. Sequential blocking allows for a simple part-to-whole visual comparison.
*   **The Evidence:** In a study of health risk perception, random arrangements led to higher variability in estimates and significant overestimation of the proportion portrayed. Sequential arrangements yielded estimates much closer to the true value [@ancker_effect_2011].

## Where to Apply <!-- role: context -->
<!-- Describe the specific situation where this rule applies. Be specific about the data, the user, or the goal. -->
*   **User Goal:** When the viewer needs to accurately estimate the magnitude of a risk or proportion at a glance (first impression).
*   **Data Type:** Binary proportions (e.g., "X out of 100 people").
*   **Audience:** General health consumers, particularly those with low numeracy or education levels, who are most negatively affected by the complexity of random arrangements.

## When to Break It <!-- role: exceptions -->
<!-- No rule is absolute. When is this advice actually WRONG? -->
*   **Scenario:** Illustrating the concept of unpredictability.
*   **Reason:** Viewers often perceive random arrangements as more "realistic" or truthful regarding the nature of chance (e.g., "disease creates a random pattern"). However, this comes at the cost of accurate quantity estimation [@ancker_effect_2011].

## The Price <!-- role: costs -->
<!-- Every design choice has a cost. If I follow this rule, what do I lose? (e.g. "It takes up more space" or "It takes longer to read"). -->
*   **The Sacrifice:** You lose the visual metaphor of "randomness" or "chance."
*   **The Risk:** The graphic may look more like a bar chart or a rigid data abstraction rather than a representation of a population.

## Common Mistakes <!-- role: mistakes -->
<!-- How do people usually screw this up? What are the bad "fixes" people try? -->
*   **The Wrong Fix:** Using random scatter to make the visualization look "scientific" or "unbiased."
*   **Why it fails:** It creates an optical illusion where the proportion (especially large ones) appears significantly larger than it actually is [@ancker_effect_2011].

## How to Check <!-- role: check -->
<!-- How can I tell if I've broken this rule? Give me a test. -->
*   **Visual Sign:** Are the colored icons distributed like sprinkles on a cookie (random) or slices of a cake (sequential)?
*   **The Test:** If you have to scan the entire grid to find all the colored icons, the arrangement is random.

## How to Fix <!-- role: fix -->
<!-- I've broken the rule. How do I solve it? Give me options. -->
*   **Quick Fix:** Sort the data so all "affected" icons appear first (e.g., filling the grid from bottom-left to top-right).
*   **Best Fix:** Use a standard 10x10 grid where the affected icons fill complete rows or columns sequentially.
