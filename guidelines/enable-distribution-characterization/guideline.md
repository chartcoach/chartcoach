---
id: enable-distribution-characterization
title: Enable Distribution Characterization for Quantitative Attributes
bibliography: references.bib
description: "Support understanding the distribution of a quantitative attribute\u2019\
  s values over a chosen set of cases."
labels:
- task:characterize-distribution
- impact:analysis
- data:quantitative
- audience:novice
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Let users characterize the distribution of a quantitative attribute over a selected set of cases.

## The Logic <!-- role: reason -->

Distribution characterization gives users a sense of “normalcy” and context for interpreting individual cases and for detecting anomalies. The paper notes distribution questions can be explicit (“What is the distribution of…”) or implicit (locating a case within the distribution). [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Context via distributional “normalcy”
- **The Evidence:** The “Characterize Distribution” task is defined and motivated, including the observation that some questions are really about location within a distribution [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding typical vs uncommon values (e.g., “age distribution of shoppers”)
- **Data Type:** Quantitative attributes over potentially large sets
- **Audience:** Users trying to interpret what counts as normal before judging exceptions

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s goal is to identify specific exceptional cases directly
- **Reason:** That is “Find Anomalies,” which is complementary but distinct [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional representation devoted to summaries rather than individual cases
- **The Risk:** Users may overlook small but meaningful subgroups if they focus only on the overall distribution [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only min/max or a few representative examples
- **Why it fails:** Range does not reveal how values are distributed within the span, which is the core goal here [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** Users cannot tell what values are common vs rare
- **The Test:** Ask: “Can the user describe the distribution of A over S?” and “Can they tell where a given case sits within it?” [@amarLowlevelComponentsAnalytic2005]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a distribution summary for the selected attribute and subset
- **Best Fix:** Make distribution characterization easy to pair with anomaly-finding so users can move from “normalcy” to “exceptions” [@amarLowlevelComponentsAnalytic2005].
