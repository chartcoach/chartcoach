---
id: use-color-not-shape-to-separate-groups-when-comparing-group-means-in-multi-class-scatterplots
title: Use color rather than shape to distinguish groups (when comparing average positions
  in multi-class scatterplots)
bibliography: references.bib
description: Color-separated groups can yield higher accuracy than shape-separated
  groups for mean position comparisons in scatterplots.
labels:
- chart:scatter
- task:compare
- visual:color
- impact:accuracy
- data:multivariate
- audience:general
- complexity:intermediate
---

## Prefer color over shape for mean comparisons between scatterplot groups <!-- role: advice -->

Differentiate groups by color when the task is to compare their average positions in a scatterplot. Avoid relying on shape alone to separate the groups for this specific mean-comparison task.

## Why color improves mean position comparison across groups <!-- role: reason -->

When groups are visually separable, viewers can more effectively restrict their ensemble summary to the relevant subset, improving mean-based comparisons between subsets.

**Mechanism:** Color supports broad feature-based selection across a display, which can make it easier to form and compare ensemble summaries for each group than when separation relies on shape.

**Evidence:** For comparing mean position between two groups in a scatterplot, accuracy was higher when groups were distinguished by color (e.g., orange vs. purple) than when distinguished by shape (e.g., circles vs. triangles) [@szafirFourTypesEnsemble2016a].

**Notes:** This guideline is about comparing group means, not about reading exact individual values.

## When you should apply this mapping choice <!-- role: context -->

- **User Goal:** Decide which group is higher/lower “on average” along an axis.
- **Task:** Compare mean vertical position (or mean position) of two (or a few) groups.
- **Data:** Multi-class point clouds with overlapping spatial distributions.
- **Chart Setting:** Static scatterplots or dashboards where quick comparisons matter.
- **Audience:** General audiences and analysts performing rapid comparisons.
- **Success Criterion:** Higher accuracy and faster consensus on which group has the higher mean.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Color cannot be used reliably (for example, due to constraints that eliminate color as a channel). **Why:** The advantage described depends on color being available as the grouping cue.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may have fewer remaining color degrees of freedom for other encodings. **Risk:** If too many categories use distinct colors, group identification can become harder. **Mitigation:** Limit the number of simultaneously compared groups.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using only shape differences to split groups for an average-position comparison task. **Why it fails:** Mean comparisons were less accurate with shape-based grouping than color-based grouping in the evaluated scatterplot task.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers misidentify which group is higher on average unless they painstakingly count or trace points. **Quick Check:** Ask people to answer the mean-comparison question with a brief viewing time; low agreement indicates the grouping cue is weak. **Stronger Test:** Swap color vs shape encodings while keeping data constant and compare accuracy on mean-comparison questions.

## What to do instead when this fails <!-- role: fix -->

- Switch the group encoding from shape to color for the mean-comparison task.
- Reduce the number of concurrently encoded categorical variables so color can be reserved for grouping.
- Provide interaction to isolate one group at a time if color must encode something else.
