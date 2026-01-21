---
id: treat-some-correlation-visualizations-as-equivalent-groups-not-total-order
title: Treat Correlation Visualization Choices as Tiers, Not a Total Ranking
bibliography: references.bib
description: For correlation estimation performance (JND), treat similarly-ranked
  designs as equivalent tiers and prefer tier-level choices over fine-grained ordering.
labels:
- task:correlate
- impact:robustness
- data:quantitative
- audience:general
- metric:jnd
- method:bayesian
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When choosing among correlation visualizations, select from the best-performing tier and treat designs within the same tier as effectively similar unless you have additional constraints.

## The Logic <!-- role: reason -->

- **The Principle:** A tiered (partial) ordering avoids over-committing to tiny differences that are not supported as meaningfully distinct by the evidence.
- **The Evidence:** The extracted results for the correlate task are represented as grouped ranks (tiers) under JND, with Bayesian significance reporting; this supports making decisions at the group level rather than forcing a strict total order [@kayWebersLawSecond2016]. The collation paper emphasizes structuring results as ranked groups with significance to support recommendation logic [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Picking an effective visualization for judging correlation when multiple candidate designs are available.
- **Data Type:** Two quantitative variables (correlation-focused).
- **Audience:** Visualization recommendation systems or designers who need stable rules.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must choose between two designs within the same tier due to non-perceptual constraints (e.g., available marks/encodings in your system).
- **Reason:** The tiering only addresses correlation JND performance; external constraints can dominate final choice [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the ability to claim a single “best” chart when multiple are effectively similar by this evidence.
- **The Risk:** If you ignore other requirements (like required encodings or layout constraints), tier-only selection might produce a chart that is hard to integrate.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Hard-coding a strict 1..N ordering among designs that are grouped together in the extracted ranking.
- **Why it fails:** The extracted knowledge explicitly encodes grouped ranks; treating them as strictly ordered contradicts the structure of the evidence [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Your recommendation logic flips between two “top” charts with minimal score differences, producing unstable outputs.
- **The Test:** Inspect whether your chosen chart is distinguished from alternatives by tier membership (grouped rank) rather than by arbitrary tie-breaking [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change your scoring to pick any design from the top tier, using secondary constraints (space, required encodings) only for tie-breaking.
- **Best Fix:** Encode the tier structure directly in your recommendation system (e.g., “choose from tier 1 for correlate tasks”), mirroring the grouped-rank evidence structure [@zengReviewCollationGraphical2023; @kayWebersLawSecond2016].
