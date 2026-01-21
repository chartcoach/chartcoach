---
id: enable-compute-derived-values-over-subsets
title: Enable Computing Derived Values Over Subsets
bibliography: references.bib
description: Support aggregation functions over selected sets of cases.
labels:
- task:aggregate
- impact:analysis
- data:tabular
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Provide direct support for computing aggregate numeric representations (e.g., average, sum, count) over a specified set of cases.

## The Logic <!-- role: reason -->

Computing derived values is a common analytic task and is often implied by users as if the value already exists in the dataset. Aggregation is also frequently embedded inside compound tasks (e.g., aggregate then sort). [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Aggregation as a primitive supporting analytic composition
- **The Evidence:** The paper defines “Compute Derived Value,” describes common aggregators (average/median/count), and discusses compound tasks like “Sort … by average …” [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Summarizing a subset (e.g., “average calorie content of Post cereals”)
- **Data Type:** Any dataset where cases can be grouped into a set S
- **Audience:** Analysts comparing categories or summarizing groups

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is per-case lookup without summarization
- **Reason:** That is “Retrieve Value,” not derived computation [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Added complexity in defining the set S and function F
- **The Risk:** Users may confuse derived values with raw attributes if not clearly distinguished [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Forcing users to manually infer aggregates by scanning values
- **Why it fails:** The paper treats aggregation as a first-class analytic task and notes users often expect it as part of analysis [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users resort to ad-hoc manual counting/averaging outside the system
- **The Test:** Can a user answer “What is F over S?” without exporting data? [@amarLowlevelComponentsAnalytic2005]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a visible way to compute standard aggregations for a selected subset
- **Best Fix:** Make derived values composable with other tasks (e.g., sort by derived values) as described in compound-task examples [@amarLowlevelComponentsAnalytic2005].
