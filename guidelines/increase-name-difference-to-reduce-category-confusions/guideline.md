---
id: increase-name-difference-to-reduce-category-confusions
title: Increase Name Difference to Reduce Category Confusions
bibliography: references.bib
description: Use name-based separation so categories are less likely to be confused
  when referenced by name.
labels:
- chart:categorical
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Choose categorical colors that differ in their color-name associations (high Name Difference), not just in perceptual distance.

## The Logic <!-- role: reason -->

Two colors can be perceptually distinct yet share common names (e.g., both often called “green”), making them easier to confuse in practice. Colorgorical’s Name Difference compares the full distribution of color-name associations between colors, and the paper shows Name Difference correlates strongly with discrimination performance (errors decrease as Name Difference increases) [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Linguistic-category confusability affects visual identification
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly identify categories that will be referenced in legends, labels, or discussion (“the green one”)
- **Data Type:** Nominal categories with legends
- **Audience:** General users, dashboards, maps, and multi-category charts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Categories are never referenced by color name and users rely solely on spatial grouping or direct labels.
- **Reason:** Name-based confusions become less relevant if name lookup and verbal reference are removed [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher Name Difference can push hues farther apart, which can reduce aesthetic preference (a tradeoff observed in the paper).
- **The Risk:** Over-emphasizing Name Difference may lower palette preference more steeply than emphasizing perceptual distance in some sizes/conditions [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking multiple variants people call by the same basic name (e.g., several “greens”) because they are numerically separated.
- **Why it fails:** Shared naming distributions imply higher risk of confusion in categorical identification [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers describe multiple categories using the same name, or hesitate when mapping legend labels to marks.
- **The Test:** For each pair of colors, assess whether their name-association distributions overlap heavily; if so, expect more errors [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace one of the confusable colors with a hue that has a clearly different common-name distribution.
- **Best Fix:** Use a palette generator/selection process that explicitly optimizes Name Difference alongside perceptual distance (as in Colorgorical) [@gramazioColorgoricalCreatingDiscriminable2017a].
