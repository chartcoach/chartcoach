---
id: order-panels-by-causality
title: Order Panels by Cause and Effect
bibliography: references.bib
description: Sort small multiple charts logically, placing input metrics before the
  output metrics they influence.
labels:
- chart:small-multiples
- task:storytelling
- visual:ordering
- impact:clarity
- data:causal
---

## The Rule <!-- role: advice -->
"Unscramble" your charts to tell a logical story: place the "input" metrics first and the final "output" metric last, rather than grouping by category or alphabet.

## The Logic <!-- role: reason -->
Demographic and statistical trends are often interrelated. By ordering charts as inputs (e.g., fertility, mortality) that influence a final result (e.g., total population), you create an "unfolding story" [@mintzer_sequential_storytelling_2024]. This structure helps the reader understand *why* the final number changed, not just *that* it changed.

## Where to Apply <!-- role: context -->
*   **User Goal:** Explaining complex changes where multiple factors contribute to a net result.
*   **Data Type:** Multi-variable datasets where variables have causal relationships (e.g., Sales + Costs = Profit).
*   **Audience:** Readers attempting to understand the "how" behind a major shift.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Categorical comparison.
*   **Reason:** If the variables are independent (e.g., "Sales in Region A" vs "Sales in Region B"), causal ordering does not exist.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Flexibility of exploration.
*   **The Risk:** You impose a specific narrative interpretation. If your causal logic is flawed (e.g., assuming correlation is causation), the visualization becomes misleading.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Ordering charts alphabetically or by magnitude.
*   **Why it fails:** It presents the data as a "scramble" without a narrative thread, failing to show how the trends connect [@mintzer_sequential_storytelling_2024].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the last chart in the row represent the cumulative result of the previous charts?
*   **The Test:** Can you use the word "therefore" or "resulting in" between the second-to-last and the last chart?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually reorder the panels in your tool settings.
*   **Best Fix:** Identify the dependent variable (the result) and move it to the far right. Arrange independent variables (the causes) to the left.
