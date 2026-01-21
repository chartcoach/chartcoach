---
id: show-underlying-distributions-not-just-aggregate-statistics
title: Show Data Distributions, Not Only Aggregate Statistics
bibliography: references.bib
description: Prefer visualizations that reveal distributions alongside summaries to
  preserve context and avoid misleading inferences from aggregates.
labels:
- chart:distribution
- task:compare
- visual:position
- impact:transparency
- data:distribution
- audience:analyst
- source:szafir-2018
---

## The Rule <!-- role: advice -->

When feasible, visualize the underlying data distribution (or a transparent summary of it) instead of showing only aggregate statistics like means.

## The Logic <!-- role: reason -->

Aggregates trade away context and can hide critical structure (e.g., variance, skew, bimodality) that viewers can estimate efficiently from distributions; relying only on statistics can therefore reduce flexibility and lead to incomplete conclusions, as argued in [@szafirGoodBadBiased2018].

- **The Principle:** Context loss from aggregation vs. rapid visual estimation of distribution properties
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how groups differ beyond just their means
- **Data Type:** Grouped samples, experimental conditions, cluster comparisons
- **Audience:** Analysts, researchers, and stakeholders making decisions from results

## When to Break It <!-- role: exceptions -->

- **Scenario:** The aggregate statistic is sufficient for the question and additional distribution detail would distract
- **Reason:** The paper notes aggregation is appropriate when summary statistics are sufficient for analysis in [@szafirGoodBadBiased2018].
- **Scenario:** The dataset is too large and showing all points would create clutter
- **Reason:** Overplotting/hairball effects can make the visualization unusable, as discussed in [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Simplicity and compactness of a single summary mark
- **The Risk:** Distribution displays can appear more complex and may require more explanation

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only means with error bars as a substitute for the distribution
- **Why it fails:** The paper describes that such summaries can mislead perception and hide distributional structure in [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Groups appear similar by means, but decisions would change if variance/skew/outliers were visible
- **The Test:** Ask “Could two very different distributions produce this same summary?”—if yes, the view may be overly aggregated, consistent with [@szafirGoodBadBiased2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a distribution-revealing layer (e.g., show the distribution shape alongside the mean)
- **Best Fix:** Use a distribution-focused chart (the paper highlights violin plots as a way to show distributions alongside means) or use visual summaries via clustering/filtering/subsampling to reduce clutter while preserving key distribution properties, per [@szafirGoodBadBiased2018]
