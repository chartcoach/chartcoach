---
id: mirror-axes-for-horizontal-comparison
title: Mirror Axes When Comparing Distributions Side-by-Side
bibliography: references.bib
description: If bar charts must be placed horizontally adjacent, mirror the axes to
  improve comparison of averages and ranges.
labels:
- chart:bar
- task:aggregate
- task:determine-range
- visual:orientation
- impact:readability
- data:quantitative
---

## The Rule <!-- role: advice -->
If you must arrange two bar charts horizontally (side-by-side) for comparison, mirror their layouts (back-to-back) rather than using a standard left-to-right repetition.

## The Logic <!-- role: reason -->
While vertical stacking is superior, symmetry plays a significant role when horizontal layouts are necessary. According to the collation by Zeng et al. [@zeng_review_2023], the experiments in Jardine et al. [@jardine_perceptual_2020] show that a "Mirrored" arrangement (Design E-3) significantly outperforms a standard "Adjacent" arrangement (Design E-2) for comparing means and ranges. The visual system can leverage symmetry as a proxy for assessing balance and spread between two distributions.

*   **The Principle:** Symmetry Perception / Bilateral Symmetry
*   **The Evidence:** [@jardine_perceptual_2020] via [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the mean or range of two datasets.
*   **Data Type:** Quantitative values categorized by nominal data (bar charts).
*   **Constraint:** Vertical screen space is limited, forcing a horizontal layout.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When reading the specific labels or values is more important than comparing the distributions.
*   **Reason:** Mirroring often requires reversing the axis or labels for one chart, which can make reading specific text values harder for the user.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Standard reading flow (left-to-right) is disrupted for the mirrored chart.
*   **The Risk:** Users unfamiliar with "population pyramid" style charts might initially find the reversed axis confusing.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing two identical bar charts next to each other (standard small multiples) when the goal is comparing the aggregate weight or spread of the groups.
*   **Why it fails:** The experimental results in Jardine et al. [@jardine_perceptual_2020] rank standard adjacent plots lower than mirrored plots for these specific summary tasks.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do both charts start from the left and grow right?
*   **The Test:** If you flip the left chart horizontally, does it look like a reflection of the right chart? If no, apply the rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reverse the scale of the left-hand chart so bars grow from right-to-left, meeting the right-hand chart in the middle.
*   **Best Fix:** Create a "diverging" or back-to-back bar chart layout (Design E-3 in [@jardine_perceptual_2020]).
