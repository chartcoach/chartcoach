---
id: avoid-random-scatter-comparison
title: Avoid Random Scatter for Comparisons
bibliography: references.bib
description: Do not use random icon scatters for side-by-side comparisons, as they
  obscure moderate differences.
labels:
- chart:icon-array
- task:compare
- impact:discriminability
- visual:position
- audience:patient
---

## The Rule <!-- role: advice -->
When displaying two icon arrays side-by-side for comparison (e.g., "Risk A" vs. "Risk B"), you must use sequential (blocked) arrangements. Never use random scatter layouts for comparative tasks.

## The Logic <!-- role: reason -->
<!-- Why does this work? Don't just say "it's better." Explain the mechanism. Is it about how the eye moves? How the brain counts? Cite your sources. -->
*   **The Principle:** **Visual Noise Interferes with Discrimination.** The cognitive load required to aggregate scattered icons creates a "fuzziness" in estimation that makes distinguishing similar values impossible.
*   **The Evidence:** In testing, more than 25% of respondents confused random graphics depicting 29% and 40%. The inaccuracy induced by random arrangements was large enough to mask an 11 percentage-point difference [@ancker_effect_2011].

## Where to Apply <!-- role: context -->
<!-- Describe the specific situation where this rule applies. Be specific about the data, the user, or the goal. -->
*   **User Goal:** Comparing the effectiveness of a treatment (e.g., "Risk before" vs. "Risk after") or comparing two different population risks.
*   **Data Type:** Two or more proportions with moderate differences (e.g., <15% difference).
*   **Audience:** Patients making medical decisions based on risk reduction.

## When to Break It <!-- role: exceptions -->
<!-- No rule is absolute. When is this advice actually WRONG? -->
*   **Scenario:** When the difference between values is massive (e.g., 5% vs 90%).
*   **Reason:** The difference is likely visible despite the noise of the random arrangement, though sequential is still safer.

## The Price <!-- role: costs -->
<!-- Every design choice has a cost. If I follow this rule, what do I lose? (e.g. "It takes up more space" or "It takes longer to read"). -->
*   **The Sacrifice:** You give up the ability to visually reinforce that *who* gets the disease is random in both scenarios.

## Common Mistakes <!-- role: mistakes -->
<!-- How do people usually screw this up? What are the bad "fixes" people try? -->
*   **The Wrong Fix:** Placing two random arrays next to each other to show that a risk has decreased slightly.
*   **Why it fails:** Small to moderate reductions in risk (the benefit of a treatment) may become invisible to the user due to estimation error [@ancker_effect_2011].

## How to Check <!-- role: check -->
<!-- How can I tell if I've broken this rule? Give me a test. -->
*   **Visual Sign:** Do you have two grids with "noise" patterns side-by-side?
*   **The Test:** Ask someone to identify the larger value within 2 seconds. If they hesitate on values that differ by 10%, the layout is failing.

## How to Fix <!-- role: fix -->
<!-- I've broken the rule. How do I solve it? Give me options. -->
*   **Quick Fix:** Group the icons in both grids into solid blocks starting from the same corner/edge.
*   **Best Fix:** Align the blocks along a shared baseline to maximize comparativeness.
