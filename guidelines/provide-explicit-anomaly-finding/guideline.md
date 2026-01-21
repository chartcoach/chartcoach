---
id: provide-explicit-anomaly-finding
title: Provide Explicit Anomaly Finding
bibliography: references.bib
description: Help users identify cases with unexpected or exceptional values relative
  to a relationship or expectation.
labels:
- task:find-anomalies
- impact:analysis
- data:quantitative
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Support identifying anomalies in a selected set relative to a relationship or expectation, not just extreme values.

## The Logic <!-- role: reason -->

The paper treats anomalies as cases with unexpected/exceptional values and notes they are not always the same as extreme values. Anomalies often serve as a basis for further exploration. [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Exception detection relative to expectations
- **The Evidence:** “Find Anomalies” is defined, contrasted with “Find Extremum,” and motivated as a driver of further exploration [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Finding exceptions (e.g., “Are there exceptions to the relationship between horsepower and acceleration?”)
- **Data Type:** Data where relationships/expectations can be articulated
- **Audience:** Analysts investigating irregularities and potential explanations

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user only needs the max/min by a single attribute
- **Reason:** That is an extremum query, and anomalies need not be extreme [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires specifying or implying an expectation/relationship
- **The Risk:** If the assumed expectation is wrong, “anomalies” may be artifacts of a poor model or assumption [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “outliers” as synonymous with “largest/smallest values”
- **Why it fails:** The paper explicitly states anomalies are not always extreme values [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** The system can list top/bottom values but cannot surface “exceptions to a relationship”
- **The Test:** Try an anomaly query framed as “exceptions to relationship R” and see whether the system can identify specific cases [@amarLowlevelComponentsAnalytic2005].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a way to flag exceptional cases within a selected set
- **Best Fix:** Tie anomaly-finding to relationship-focused analysis so users can identify exceptions “with respect to a given relationship or expectation” [@amarLowlevelComponentsAnalytic2005].
