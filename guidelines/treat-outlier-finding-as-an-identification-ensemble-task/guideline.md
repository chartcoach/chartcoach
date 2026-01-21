---
id: treat-outlier-finding-as-an-identification-ensemble-task
title: Treat Outlier Finding As An Identification Ensemble Task
bibliography: references.bib
description: Frame outlier detection as identifying a subset that deviates from the
  distribution, not as precise value reading.
labels:
- task:find-anomalies
- task:identify
- impact:clarity
- data:quantitative
- audience:designer
- complexity:foundational
---

## The Rule <!-- role: advice -->

When users need to find anomalies/outliers, treat the task as **identification over a distribution** (ensemble-based), not as precise value retrieval.

## The Logic <!-- role: reason -->

Outlier detection depends on perceiving which items are notably different *relative to the rest of the set*, which requires distributional context rather than isolated value reading.

- **The Principle:** Relative-to-Distribution Identification
- **The Evidence:** [@szafirFourTypesEnsemble2016] and its task framing as collated in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** “Find anomalies” / “spot outliers” in a plotted set (e.g., scatterplots, bar collections, or other mark sets).
- **Data Type:** Quantitative values presented as many marks (a collection).
- **Audience:** Analysts doing exploratory inspection; designers or recommenders choosing encodings for anomaly-finding workflows.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user already knows the exact target value or exact target record identity.
- **Reason:** That becomes an absolute-value identification or direct lookup problem rather than distribution-relative outlier discovery [@szafirFourTypesEnsemble2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may not optimize for precise numeric reading of the outlier value.
- **The Risk:** A design that supports “pop-out” may still leave users unsure of the exact magnitude without additional aids.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Designing anomaly views as if they are primarily “retrieve value” tasks (e.g., focusing only on precision of a single mark).
- **Why it fails:** It neglects that the user must first perceive the broader distribution to define what counts as an outlier [@szafirFourTypesEnsemble2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can read values but miss anomalies, or disagree on what is anomalous.
- **The Test:** Ask users to circle the anomalies quickly; if performance is poor, the display likely isn’t supporting distribution-relative identification.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Make the distribution context more visually apparent (e.g., reduce clutter or emphasize the overall set so deviations stand out).
- **Best Fix:** In recommendation logic, route “find anomalies” requests to designs selected for identification tasks rather than value-retrieval tasks, using task metadata as in [@zengReviewCollationGraphical2023].
