---
id: support-finding-extreme-cases
title: Support Finding Extreme Cases
bibliography: references.bib
description: Help users identify top or bottom cases by an attribute without requiring
  full sorting.
labels:
- task:rank
- task:find-extremum
- impact:analysis
- data:quantitative
- audience:novice
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Support queries for the top/bottom N cases by an attribute as a distinct operation.

## The Logic <!-- role: reason -->

Finding extrema was very common in the studied analytic questions. The paper distinguishes “Find Extremum” from full “Sort” (not always needed) and from “Find Anomalies” (anomalies are not necessarily extreme). Treating extremum-finding as its own capability aligns the system with common analytic intent. [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Extremum identification is not equivalent to sorting or anomaly detection
- **The Evidence:** The paper explicitly differentiates “Find Extremum” from “Sort” and “Find Anomalies” [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify best/worst items (e.g., “car with the highest MPG”)
- **Data Type:** Attributes with an order (quantitative or otherwise orderable)
- **Audience:** Analysts quickly surfacing candidates for follow-up (often followed by Retrieve Value)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user needs the complete ranked order of all cases
- **Reason:** That is the “Sort” task rather than extremum-finding [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Emphasis on extremes may de-emphasize distributional context
- **The Risk:** Users may overgeneralize from a few extreme cases [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making users do a full sort to find only the maximum/minimum
- **Why it fails:** The paper notes a complete sort is not always necessary to find an extreme value [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must scroll through long ordered lists to find maxima/minima
- **The Test:** Ask: “Can the user directly obtain top/bottom N for attribute A?” [@amarLowlevelComponentsAnalytic2005]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a direct “top/bottom N” query pattern per attribute
- **Best Fix:** Make extrema results easy to feed into follow-up tasks like Retrieve Value (reading other attributes of the identified cases) [@amarLowlevelComponentsAnalytic2005].
