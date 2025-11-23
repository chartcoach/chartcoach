---
id: break-stacks-to-avoid-bias
title: Introduce Gaps to Prevent Part-of-Whole Bias
bibliography: references.bib
description: Separating adjacent segments in a stacked bar can reduce the erroneous
  tendency to read them as a percentage of the total.
labels:
- chart:stacked-bar
- task:compare
- visual:spacing
- impact:bias-reduction
- complexity:nuanced
---

## The Rule <!-- role: advice -->
If users must compare two segments within the same stack, introduce a visual gap or a neutral "distractor" bar between them rather than placing them immediately adjacent to one another.

## The Logic <!-- role: reason -->
When two bars are immediately adjacent within a stack (a "divided bar"), users suffer from a "part-of-whole bias." They tend to estimate the ratio of the smaller bar to the sum of both bars (part-to-whole), rather than the ratio of one bar to the other. Separating them with a gap or another bar breaks this grouping and actually *decreases* error.
*   **The Principle:** Part-of-Whole Bias / Grouping
*   **The Evidence:** In Experiment 3, Talbot et al. found that "separating the compared bars actually decreases the error" in divided bar tasks, suggesting that adjacency triggers an erroneous part-of-whole mental strategy (e.g., seeing 33% instead of 50%) [@talbot_four_2014]. This is a nuanced finding captured in the collation of perception knowledge for visualization recommendation [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the ratio of two specific components within a single composite entity (e.g., "Ratio of Domestic vs. International sales" within a total bar).
*   **Data Type:** Proportions or compositions.
*   **Audience:** Users analyzing internal ratios within a single group.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user actually *wants* to see the part-to-whole relationship (e.g., "What % is X of the total?").
*   **Reason:** In this case, the bias is actually the desired outcome (seeing the percentage of the total).

## The Price <!-- role: costs -->
*   **The Sacrifice:** The chart looks less cohesive and the "total" height becomes meaningless or harder to perceive.
*   **The Risk:** It effectively destroys the "stacked bar" metaphor and turns it into a floating bar arrangement.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing the two bars touching each other to make them "closer."
*   **Why it fails:** While usually good (see Adjacency rule), within a stack, touching bars triggers the part-to-whole confusion.

## How to Check <!-- role: check -->
*   **Visual Sign:** A simple stack of two colors (e.g., Red on top of Blue).
*   **The Test:** Ask a user to estimate the ratio of Top to Bottom. If the top is 30 and bottom is 60, do they say "It's about half" (correct ratio) or "It's about a third" (part-to-whole bias)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a thick white border between the segments to create visual separation.
*   **Best Fix:** Use an interactive technique that allows users to "explode" or separate the segments temporarily for comparison, or switch to a side-by-side comparison.
