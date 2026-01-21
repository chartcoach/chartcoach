---
id: design-for-retrieve-value-lookup
title: Design for Retrieve-Value Lookups
bibliography: references.bib
description: Support users in reading exact attribute values for specified cases.
labels:
- task:retrieve
- impact:clarity
- data:tabular
- audience:novice
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Make it easy to read exact attribute values for user-specified data cases.

## The Logic <!-- role: reason -->

Users frequently need to “read off” attributes once a case is already known, and this value retrieval acts as a subtask that enables other analytic tasks. If the system makes exact lookup hard, downstream analytic activity suffers.

- **The Principle:** Exact-value lookup as a foundational analytic primitive
- **The Evidence:** The paper defines “Retrieve Value” and notes it commonly serves as a subtask after other operations identify cases of interest [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Getting exact values for known cases (e.g., “What is the MPG of the Audi TT?”)
- **Data Type:** Any dataset with identifiable cases and attributes
- **Audience:** Anyone performing analysis, especially when chaining tasks

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s goal is only aggregate understanding (e.g., overall distribution)
- **Reason:** Exact per-case values are not necessary for the intended analytic task [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional UI/ink/space devoted to precise values
- **The Risk:** Overemphasis on single cases can distract from patterns [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming overview-level depiction is sufficient for all tasks
- **Why it fails:** “Retrieve Value” is explicitly distinct and repeatedly needed after other tasks identify relevant cases [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must guess or approximate values for a known case
- **The Test:** Ask: “Can a user answer ‘What is X for case A?’ without additional steps or ambiguity?” [@amarLowlevelComponentsAnalytic2005]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a clear mechanism to access exact values for a selected case
- **Best Fix:** Ensure every case can yield its relevant attribute values on demand to support task chaining [@amarLowlevelComponentsAnalytic2005].
