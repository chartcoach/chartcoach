---
id: group-icons-in-arrays
title: Group Affected Icons in Pictographs
bibliography: references.bib
description: When using icon arrays, cluster the 'affected' icons together rather
  than scattering them randomly.
labels:
- chart:icon-array
- chart:matrix
- task:estimation
- visual:position
- impact:speed
- impact:accuracy
- audience:low-numeracy
---

## The Rule <!-- role: advice -->
When using an icon array (e.g., a 10x10 matrix) to show probability, group all the "affected" icons together in a solid block. Do not scatter them randomly throughout the grid.

## The Logic <!-- role: reason -->
While random scattering might technically represent the concept of "chance," grouping icons significantly improves the speed of processing and the accuracy of numeric estimation. It makes the proportion easier to visually sum and compare [@lipkus_numeric_2007].

*   **The Principle:** Perceptual Grouping (Gestalt).
*   **The Evidence:** [@lipkus_numeric_2007] notes that assuming accuracy and speed are key outcomes, grouping individuals achieves these goals better than showing randomness.

## Where to Apply <!-- role: context -->
*   **User Goal:** Quickly understanding the magnitude of a risk (e.g., "How likely am I to get this disease?").
*   **Data Type:** Natural frequencies (e.g., "15 out of 100").
*   **Audience:** General audiences, especially those with lower graph literacy or numeracy.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Demonstrating the unpredictability of an event.
*   **Reason:** If the specific educational goal is to teach that a disease strikes randomly and clustering is not guaranteed, a scattered display might be conceptually appropriate, though harder to count.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the visual metaphor of "randomness" or "unpredictability."
*   **The Risk:** Users might infer a pattern (e.g., "only people in the top left corner get sick") that doesn't exist.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Randomly distributing colored dots to look "scientific" or "organic."
*   **Why it fails:** It forces the user to count individual dots, increasing cognitive load and error rates.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the colored icons contiguous?
*   **The Test:** Can you estimate the quantity without moving your eyes back and forth across the grid?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Sort the data so all "events" appear first (e.g., top-left to bottom-right).
*   **Best Fix:** Arrange the affected icons in a solid rectangular block within the larger matrix.
