---
id: support-filter-by-explicit-conditions
title: Support Filtering by Explicit Attribute Conditions
bibliography: references.bib
description: Enable users to find all cases that satisfy concrete conditions on attribute
  values.
labels:
- task:filter
- impact:clarity
- data:categorical
- data:quantitative
- audience:novice
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Let users specify concrete conditions on attribute values and return the set of cases that satisfy them.

## The Logic <!-- role: reason -->

Filtering is a core analytic task and also a frequent subtask that produces a working set for other tasks (e.g., deriving values, finding extrema, retrieving attributes). The paper emphasizes that filter conditions must be concrete (operationally defined), especially when users use vague terms like “high.” [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Concrete-condition selection as an analytic primitive
- **The Evidence:** “Filter” is defined as finding cases satisfying concrete conditions; the paper highlights the need to operationally define terms like “high” [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying a subset that matches criteria (e.g., “Which funds underperformed the SP-500?”)
- **Data Type:** Attributes that can be evaluated per case independently of other cases
- **Audience:** Analysts iterating over subsets

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user asks for “the highest” or “top N” cases
- **Reason:** That requires comparison across the dataset and belongs to “Find Extremum,” not “Filter” [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires users (or the system) to make thresholds explicit
- **The Risk:** Poorly chosen thresholds can mislead subsequent analysis [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “high” as inherently meaningful without defining it
- **Why it fails:** The paper notes such questions need an operating definition to become concretely answerable as filter criteria [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** The tool can’t clearly explain which cases qualify and why
- **The Test:** Rewrite a vague filter (“high fiber”) into an explicit condition (“> x grams”) and verify the system can support that concretely [@amarLowlevelComponentsAnalytic2005].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a way to express explicit attribute constraints
- **Best Fix:** Make conditions precise and inspectable so users understand inclusion/exclusion as they build subsets for other tasks [@amarLowlevelComponentsAnalytic2005].
