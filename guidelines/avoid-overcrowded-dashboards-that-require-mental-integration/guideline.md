---
id: avoid-overcrowded-dashboards-that-require-mental-integration
title: Avoid Dashboards That Force Users to Mentally Combine Many Separate Views
bibliography: references.bib
description: Use integrated structures rather than many disconnected charts; reduce
  mental integration and arbitrary tabular layouts.
labels:
- chart:dashboard
- task:integrate
- visual:layout
- impact:cognitive-load
- data:multifaceted
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not split tightly related facets across many separate charts; integrate them so relationships are perceived directly, not mentally reconstructed.

## The Logic <!-- role: reason -->

When dashboards crowd many visualizations, users must mentally combine representations to complete tasks. If the external organization does not reflect how the data are related (e.g., generic tabular arrangement), users’ internal cognitive processes can be negatively impacted. [@olaSimpleChartsDesign2016]

- **The Principle:** External structure should reduce internal integration work
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Cross-facet reasoning (e.g., connect causes, risks, locations, ages, time)
- **Data Type:** Public health data with multiple related dimensions and levels of granularity
- **Audience:** Professionals doing exploratory analysis and decision support

## When to Break It <!-- role: exceptions -->

- **Scenario:** Independent KPIs that users genuinely monitor separately with little need for cross-linking.
- **Reason:** If tasks do not require integration, separate views can remain efficient. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Integrated views can be harder to design and may reduce the simplicity of any single metric display.
- **The Risk:** Poor integration can create visually dense “hairballs” if relationships are not filtered/structured. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more charts and relying on consistent colors/legends to “connect” them.
- **Why it fails:** Users still must perform the join mentally; layout may not communicate true relationships. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently cross-reference charts (“Look here, then there”) to answer one question.
- **The Test:** Observe whether answering a relationship question requires back-and-forth scanning between multiple panels rather than reading one integrated structure. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit relationship encodings (e.g., linking structures) between facets instead of leaving them disconnected.
- **Best Fix:** Replace the dashboard grid with a principled integrated structure (e.g., stacked tracks around a common coordinate scaffold) that makes co-occurrence perceptually obvious. [@olaSimpleChartsDesign2016]
