---
id: use-triplet-matching-evaluation
title: Use Triplet Matching to Measure Perceptual Similarity
bibliography: references.bib
description: When evaluating visualization designs or icons, use ordinal triplet matching
  rather than Likert scales or spatial arrangement.
labels:
- task:evaluate
- task:test
- visual:perception
- impact:accuracy
- audience:researcher
- source:methodology
---

## The Rule <!-- role: advice -->
When collecting human feedback to determine how similar two visual elements look, use a **Triplet Matching** task ("Is A more similar to Ref than B?"). Avoid using pairwise Likert ratings or manual spatial arrangement tasks.

## The Logic <!-- role: reason -->
Different evaluation methods yield different levels of quality. Triplet matching is the most robust method against variations in subject pool size and provides the most accurate prediction of how visual variables interact (e.g., shape and color together).
*   **The Principle:** Robustness and Consistency
*   **The Evidence:** [@demiralp_learning_2014] compared five methods. Triplet matching (Tm) had the lowest inter-subject variance and the lowest unit task time (confusion time). Spatial Arrangement (SA), while fast, performed poorly for high-dimensional data and showed high variance.

## Where to Apply <!-- role: context -->
*   **User Goal:** Defining a new set of icons, shapes, or custom glyphs and needing to know which ones users will confuse.
*   **Data Type:** Any visual encoding variable (Shape, Size, Color).
*   **Audience:** Visualization designers conducting user studies or A/B testing.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Extremely limited budget or time.
*   **Reason:** **Spatial Arrangement (SA)** is significantly faster and cheaper than triplet matching. If a rough approximation is acceptable and the visual dimensionality is low (2D), SA may suffice [@demiralp_learning_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cost and Time.
*   **The Risk:** Triplet matching scales cubically with the number of stimuli, making it expensive for large palettes compared to the linear cost of spatial arrangement.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using Likert scales (1-5 similarity ratings).
*   **Why it fails:** Subjects have different internal scales (one person's "4" is another's "2"). [@demiralp_learning_2014] found that while Likert scales perform okay, they are less robust and exhibit higher variance than the binary choice of triplet matching.

## How to Check <!-- role: check -->
*   **Visual Sign:** N/A (Methodological check).
*   **The Test:** Are you asking users to assign a number to similarity? If yes, stop. Ask them to make a choice between options relative to a reference instead.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change survey questions from "Rate similarity 1-5" to "Which is more similar to X: A or B?"
*   **Best Fix:** Implement a triplet matching protocol where a reference stimulus is shown, and the user selects the most similar match from two options, then aggregate these ordinal judgments using non-metric multidimensional scaling [@demiralp_learning_2014].
