---
id: support-clustering-by-similarity-of-attributes
title: Support Clustering by Similarity of Attributes
bibliography: references.bib
description: Enable users to find groups of cases with similar values across one or
  more attributes.
labels:
- task:cluster
- impact:analysis
- data:multivariate
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Let users identify clusters of cases that are similar across specified attributes.

## The Logic <!-- role: reason -->

Users naturally group similar items, and the meaning of proximity depends on the chosen attributes (competitors, families, “normal” cases vs outliers). The paper defines clustering as a low-level analytic task focused on similarity in attribute values. [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Similarity grouping as a primitive analytic move
- **The Evidence:** The “Cluster” task is defined and its interpretive roles are discussed [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Finding groups/typical cases (e.g., “groups of cereals with similar fat/calories/sugar”)
- **Data Type:** Multivariate cases where similarity can be judged on chosen attributes
- **Audience:** Analysts exploring structure in the data beyond single-variable summaries

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s intent is to test a relationship between two attributes
- **Reason:** That is “Correlate,” not clustering [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Clusters can be sensitive to which attributes are chosen
- **The Risk:** Users may infer strong categorical boundaries where the data varies continuously [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Presenting only a single “average” case as representative of a group
- **Why it fails:** The task goal is explicitly to find *groups of similar cases*, not a single summary [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can see individual cases but cannot identify coherent groups of similarity
- **The Test:** Ask whether the system can help answer “Which cases are similar in X,Y,Z?” for a user-chosen subset S [@amarLowlevelComponentsAnalytic2005].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a mechanism to reveal groups of similar cases for selected attributes
- **Best Fix:** Make clustering results actionable for follow-up tasks (e.g., retrieving values or checking distributions within a cluster) as part of analytic workflow composition [@amarLowlevelComponentsAnalytic2005].
