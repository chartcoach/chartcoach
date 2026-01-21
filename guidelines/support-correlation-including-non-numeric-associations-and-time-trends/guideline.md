---
id: support-correlation-including-non-numeric-associations-and-time-trends
title: Support Correlation Queries Including Non-Numeric Associations and Time Trends
bibliography: references.bib
description: Enable users to look for relationships between attributes, including
  categorical associations and temporal trends.
labels:
- task:correlate
- impact:analysis
- data:multivariate
- data:temporal
- data:categorical
- data:quantitative
- audience:expert
- source:amar-2005
---

## The Rule <!-- role: advice -->

Support users in exploring relationships between attributes, including temporal trends and associations involving non-numeric attributes.

## The Logic <!-- role: reason -->

Correlation was a frequent analytic intent in the collected questions, and the paper notes users often want to “correlate” non-numeric attributes in the sense of finding interesting coincidences/associations, not necessarily building predictive quantitative models. It also interprets trend questions as correlations with temporal variables. [@amarLowlevelComponentsAnalytic2005]

- **The Principle:** Relationship-seeking as a core analytic primitive
- **The Evidence:** The “Correlate” task definition, discussion of non-numeric correlation semantics, and treatment of trends-over-time as temporal correlation [@amarLowlevelComponentsAnalytic2005].

## Where to Apply <!-- role: context -->

- **User Goal:** Discovering relationships (numeric correlation, categorical association, trends)
- **Data Type:** Pairs of attributes (numeric-numeric, categorical-numeric, categorical-categorical, temporal)
- **Audience:** Analysts testing hypotheses or exploring potential relationships

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user is only trying to identify exceptional cases or outliers
- **Reason:** That is “Find Anomalies,” which is complementary but distinct from correlation [@amarLowlevelComponentsAnalytic2005].

## The Price <!-- role: costs -->

- **The Sacrifice:** Relationship exploration can invite overinterpretation
- **The Risk:** Users may conflate categorical “association/coincidence” with true predictive quantitative correlation unless clarified [@amarLowlevelComponentsAnalytic2005].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating all “correlation” questions as requiring numeric predictive modeling
- **Why it fails:** The paper observes many user correlation questions involve non-numeric attributes and are semantically about coincidences/associations [@amarLowlevelComponentsAnalytic2005].

## How to Check <!-- role: check -->

- **Visual Sign:** The system supports only numeric-numeric correlation and fails on categorical relationships or time trends
- **The Test:** Try queries like “country of origin vs MPG” and “trend over years” and verify the system can support relationship-finding for each [@amarLowlevelComponentsAnalytic2005].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add support for examining relationships across different attribute types, not only numeric pairs
- **Best Fix:** Treat trends explicitly as correlation with temporal variables and support categorical association as a first-class relationship query type [@amarLowlevelComponentsAnalytic2005].
