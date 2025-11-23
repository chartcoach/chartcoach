---
id: principle-importance-ordering
title: Encode Important Data More Effectively
bibliography: references.bib
description: Allocate the most effective visual channels to the most important data
  attributes.
labels:
- task:rank
- task:prioritize
- impact:hierarchy
- design:composition
- data:multivariate
---

## The Rule <!-- role: advice -->
Map the most important information in your dataset to the most effective visual channel (usually **Position**), and relegate less important information to less effective channels (like Area or Color).

## The Logic <!-- role: reason -->
Perceptual tasks have a strict hierarchy of accuracy. Since a single chart has limited "high-accuracy" slots (usually just the X and Y axes), you must prioritize which data gets those slots based on the user's needs.
*   **The Principle:** Principle of Importance Ordering
*   **The Evidence:** [@mackinlay_automating_1986] states: "Encode more important information more effectively." A scatter plot where `Price` is on the axis and `Weight` is area is fundamentally different from `Weight` on the axis and `Price` as area, even if they contain the same data.

## Where to Apply <!-- role: context -->
*   **User Goal:** Analyzing multivariate data where one variable is the primary decision driver (e.g., buying a car based primarily on Price, secondarily on Mileage).
*   **Data Type:** Tuples of relations with varying importance.
*   **Audience:** Users with specific, prioritized questions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** All variables are equally important.
*   **Reason:** If no hierarchy exists, you may need a design that treats variables symmetrically, such as a Scatterplot Matrix (SPLOM) or parallel coordinates, rather than privileging one over the other.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Secondary variables will be harder to read accurately.
*   **The Risk:** If you misidentify what is "important" to the user, you will design a chart that accurately answers the wrong question.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Arbitrarily assigning variables to axes vs. retinal properties (color/shape) without considering user intent.
*   **Why it fails:** It forces the user to perform difficult perceptual tasks (like judging area) for their primary question [@mackinlay_automating_1986].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the main insight buried in a subtle color shift or a small size difference?
*   **The Test:** Identify the "Key Insight." Check if that insight is encoded via Position or Length. If it's encoded via Area or Color, the design is inefficient.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Swap the axes variables with the retinal (color/size) variables.
*   **Best Fix:** Determine the importance ordering of the input relations and generate the design lexicographically based on that order.
