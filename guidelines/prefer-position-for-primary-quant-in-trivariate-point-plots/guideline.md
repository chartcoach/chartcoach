---
id: prefer-position-for-primary-quant-in-trivariate-point-plots
title: Encode the Primary Quantitative Field on X or Y
bibliography: references.bib
description: For trivariate point plots, map the main quantitative variable to position
  (x/y) to maximize accuracy and speed across tasks.
labels:
- chart:scatter
- task:retrieve-value
- task:sort
- task:find-extremum
- task:aggregate
- visual:position
- impact:accuracy
- impact:speed
- data:quantitative
- data:categorical
- complexity:multivariate
---

## The Rule <!-- role: advice -->

Encode the primary quantitative field (Q1) using position on either the x-axis or y-axis, not color-saturation or size/area.

## The Logic <!-- role: reason -->

Position encodings provide more precise and efficient decoding for the primary quantitative field across tasks, reflected by top-ranked accuracy and time results when Q1 is on position (e.g., designs E-1/E-2/E-5/E-6) versus when Q1 is on color-saturation or size/area (e.g., E-9/E-10/E-7/E-8) [@kimAssessingEffectsTask2018]. This guideline is extracted and contextualized for recommendation use cases in the collation [@zengReviewCollationGraphical2023].

- **The Principle:** Positional precision for quantitative decoding
- **The Evidence:** [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate and fast reading/comparing of a primary measure (Q1) in trivariate point-based displays.
- **Data Type:** 2 quantitative fields (Q1, Q2) + 1 nominal field (N), shown with point marks (scatterplot-like designs).
- **Audience:** Broad/general audiences performing quick analytic judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary user goal is specifically to judge aggregate properties where a non-positional encoding for Q1 is explicitly required by the task framing in your system.
- **Reason:** In the study, some non-positional Q1 encodings can be competitive for specific aggregate tasks (e.g., Q1:color-saturation designs E-9/E-10 are not always worst for aggregate accuracy) [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may have fewer high-quality channels left for secondary variables (Q2) once x/y are committed to Q1.
- **The Risk:** Forcing Q1 onto position can increase reliance on less effective channels for other fields, potentially creating trade-offs in multi-field readability [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Put Q1 on color-saturation (E-9/E-10) or on size/area (E-7/E-8) while keeping positions for other fields.
- **Why it fails:** These mappings tend to rank lower for accuracy and/or time compared to position-encoded Q1 across the included tasks [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must “decode” Q1 from color intensity or dot size instead of reading it off an axis.
- **The Test:** Swap Q1 onto x or y (keeping other mappings the same) and check whether the design matches the higher-ranked families (E-1/E-2/E-5/E-6) in the study’s task rankings [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remap Q1 to x or y and move the displaced field to the former Q1 channel.
- **Best Fix:** Use a design where Q1 and Q2 are both on x/y (scatterplot-like) and encode N via color-hue (E-5/E-6) or reserve non-positional channels for secondary information, consistent with the higher-ranked options in the study [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].
