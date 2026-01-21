---
id: avoid-large-categorical-palette-sizes-when-possible
title: Minimize the Number of Categorical Colors When Possible
bibliography: references.bib
description: Use fewer categories/colors because discriminability declines as palette
  size increases.
labels:
- chart:categorical
- task:distinguish
- visual:color
- impact:accuracy
- data:categorical
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Use as few categorical colors as your task allows; avoid expanding palettes unnecessarily.

## The Logic <!-- role: reason -->

In Colorgorical’s human-subject discrimination task, error rates rose markedly as palette size increased (3-color < 5-color < 8-color), consistent with the idea that more category colors reduce discriminability and increase processing difficulty [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Discriminability decreases as the number of categories increases
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate and fast category identification
- **Data Type:** Many categories where color is the primary identifier
- **Audience:** General audiences; time-pressured tasks

## When to Break It <!-- role: exceptions -->

- **Scenario:** The dataset truly requires many categories and color is not the only encoding (e.g., categories also separated by labels or structure).
- **Reason:** The palette-size constraint is about color-only discriminability; adding other cues changes the problem [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less granularity—some categories may need grouping/aggregation.
- **The Risk:** Over-aggregation can hide meaningful distinctions users need [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more colors to “fit all categories” without considering discrimination limits.
- **Why it fails:** More colors increases the chance that at least one pair becomes the weak link (the palette is only as good as its least discriminable pair) [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confuse categories, especially those with the smallest pairwise separations.
- **The Test:** Identify the lowest-distance (or lowest Name Difference) pair in the palette; if that pair is hard to tell apart, the whole palette will suffer [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories shown at once (filter, group, or collapse).
- **Best Fix:** Redesign so fewer categories rely on color (or generate a new palette tuned for the exact palette size you must use) [@gramazioColorgoricalCreatingDiscriminable2017a].
