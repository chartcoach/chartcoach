---
id: treat-sorting-as-a-separate-analytic-capability
title: Treat Sorting as a Separate Analytic Capability
bibliography: references.bib
description: Allow users to rank a set of cases by an ordinal metric when full ordering
  is needed.
labels:
- task:sort
- impact:analysis
- data:ordinal
- data:quantitative
- audience:novice
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

When users need full ordering, let them sort a specified set of cases by an attribute.

## The Logic <!-- role: reason -->

The paper defines “Sort” as ranking cases by an ordinal metric and notes it is often a substrate for other tasks (especially extremum-finding when multiple extreme values are needed). Supporting sort enables a common analytic building block and task composition. [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Ranking as a composable analytic primitive
- **The Evidence:** “Sort” is defined and discussed as a substrate for other operations [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Establishing an ordering over a set (e.g., “Rank cereals by calories”)
- **Data Type:** Any attribute with an inherent order
- **Audience:** Analysts comparing many cases, not just the extremes

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user only needs the top/bottom few items
- **Reason:** “Find Extremum” can satisfy the goal without a full sort [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Full ordering can create long sequences that require navigation
- **The Risk:** Users may interpret rank differences as meaningful even when values are close [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing only extrema and not full ordering
- **Why it fails:** Some tasks require the entire sorted order rather than just extremes [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can’t establish a consistent rank order across the full set
- **The Test:** Can the user answer “What is the sorted order of S by A?” [@amarLowlevelComponentsAnalytic2005]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add ordering controls for a chosen attribute
- **Best Fix:** Ensure sorting can be applied to a user-defined subset S (often produced by filtering) to support compound analytic tasks [@amarLowlevelComponentsAnalytic2005].
