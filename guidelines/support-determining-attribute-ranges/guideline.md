---
id: support-determining-attribute-ranges
title: Support Determining Attribute Ranges
bibliography: references.bib
description: Let users find the span (or unique set) of values an attribute takes
  within a chosen set of cases.
labels:
- task:determine-range
- impact:analysis
- data:quantitative
- data:categorical
- audience:novice
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Provide a way to determine an attribute’s value span over a selected set, including enumerating unique categorical values.

## The Logic <!-- role: reason -->

Range-finding helps users understand dataset dynamics, suitability for analysis, and the general types of values present. The paper explicitly frames range as a primitive task and notes categorical range can be treated as the set of unique values. [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Coverage and span as a prerequisite for informed analysis
- **The Evidence:** The “Determine Range” task and its rationale are described directly, including categorical attributes as unique-value enumerations [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding span/coverage (e.g., “range of film lengths,” “what actresses are in the data set”)
- **Data Type:** Quantitative (min–max) and categorical (unique values)
- **Audience:** Analysts assessing what the data contains before deeper tasks

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user needs a fuller description of how values are distributed (not just span)
- **Reason:** That goal is “Characterize Distribution,” not range [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Showing full unique-value lists can be space-intensive
- **The Risk:** Range alone can hide important structure inside the span [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only a single example value or a few samples
- **Why it fails:** The user goal is explicitly to know the span or full set of unique values, not anecdotes [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users cannot tell what values are even present for an attribute in the selected set
- **The Test:** Ask: “Can the user list the unique categories or identify min/max for the chosen subset?” [@amarLowlevelComponentsAnalytic2005]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide min/max for quantitative attributes and unique-value enumeration for categorical attributes
- **Best Fix:** Make range queries applicable to arbitrary subsets S (often created via filtering) to support iterative analysis [@amarLowlevelComponentsAnalytic2005].
