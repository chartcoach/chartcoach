---
id: visualize-incremental-risk-change
title: Visually Highlight Incremental Risk Differences
bibliography: references.bib
description: When comparing treatments, visually distinguish the specific units that
  change rather than just showing total values.
labels:
- chart:pictograph
- task:compare
- visual:color
- impact:clarity
- data:change
- audience:novice
---

## The Rule <!-- role: advice -->
When comparing two treatments, visually isolate and highlight only the incremental change (the difference) between the groups, rather than simply displaying two separate total values.

## The Logic <!-- role: reason -->
Focusing on the specific subset of the population that experiences a different outcome helps users contextualize the magnitude of the change.
*   **The Principle:** Incremental Risk Framing. This helps focus attention on the actual change in risk by providing information regarding both the baseline risk and the change simultaneously.
*   **The Evidence:** [@tait_effect_2010] utilized a format where the baseline risk was shown (e.g., solid blue blocks) and the *reduction* in risk for the second drug was shown as a distinct visual category (e.g., grey blocks with blue borders). This highlighted exactly "how many fewer" children would experience a side effect.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the efficacy or safety of a new option (Drug B) against a standard option (Drug A).
*   **Data Type:** Comparative probabilities where one value is a subset of the other.
*   **Audience:** Laypeople trying to determine if a switch in treatment is worth the trade-off.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the two datasets are independent and do not share a baseline population or context.
*   **Reason:** Incremental framing implies a direct "switch" or trade-off logic that may not exist between unrelated groups.

## The Price <!-- role: costs -->
*   **The Risk:** Complexity in the legend. You must explain what three states mean: "Always has condition," "Never has condition," and "Condition changes based on treatment."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing two side-by-side charts (one for Drug A, one for Drug B) without explicit visual links.
*   **Why it fails:** It forces the user to perform mental subtraction to understand the benefit.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to look at Chart A, memorize a number, look at Chart B, and do math?
*   **The Test:** Can the user instantly point to the specific individuals who benefit from the switch?

## How to Fix <!-- role: fix -->
*   **Best Fix:** Use a single pictograph matrix where the baseline risk is one color, and the "saved" or "prevented" cases are a distinct outline or texture, representing the delta directly.
