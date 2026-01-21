---
id: avoid-row-faceting-when-speed-matters
title: Avoid Row Faceting When Response Time Matters
bibliography: references.bib
description: Row-faceted point plots tend to be slower than non-faceted alternatives
  for value and sort tasks, so avoid them when speed is important.
labels:
- chart:scatter
- task:retrieve-value
- task:sort
- visual:row
- visual:position
- impact:speed
- data:categorical
- data:quantitative
- complexity:multivariate
---

## The Rule <!-- role: advice -->

Do not use row faceting for the nominal field (N:row) when you need faster performance; prefer non-faceted alternatives.

## The Logic <!-- role: reason -->

Row-faceted encodings (E-11/E-12) rank in slower groups for retrieve-value and sort time compared to top-performing non-faceted encodings (notably E-1/E-2 and often E-5/E-6) [@kimAssessingEffectsTask2018]. The collation includes this as a practical recommendation-system constraint (faceting can be time-costly) [@zengReviewCollationGraphical2023].

- **The Principle:** Additional scanning/comparison cost in faceted layouts
- **The Evidence:** [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Fast answers for retrieve-value and sort-like tasks.
- **Data Type:** Trivariate point-based designs where N can be encoded by row faceting.
- **Audience:** Users under time pressure or doing many quick comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You prioritize accuracy equivalence over speed, and row-faceted designs are acceptably accurate for your task.
- **Reason:** For some accuracy rankings (e.g., sort accuracy), faceted designs (E-11/E-12) can sit in the top accuracy group even if they are slower [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the structural separation of categories that faceting provides.
- **The Risk:** Without faceting, category separation must be carried by other channels (e.g., color-hue), which may introduce different limitations [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choose faceting because it “uses position for everything,” assuming it will automatically be fastest.
- **Why it fails:** The measured time rankings place row-faceted designs behind non-faceted alternatives for retrieve-value and sort [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The plot is split into multiple horizontal panels, one per category (row).
- **The Test:** If your encoding matches E-11/E-12, expect a time penalty relative to E-1/E-2 and often E-5/E-6 for value/sort tasks [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace N:row with N:color-hue or N on an axis (depending on the rest of the mapping).
- **Best Fix:** Use a top-ranked non-faceted mapping for your task (e.g., E-1/E-2 for retrieve-value/sort time, or E-5/E-6 for colored-scatterplot value tasks) [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].
