---
id: prefer-positional-encoding-for-primary-quantitative-in-trivariate-point-plots
title: Encode the primary quantitative field on a position axis in trivariate point
  plots
bibliography: references.bib
description: For trivariate point-based views with one categorical and two quantitative
  fields, place the primary quantitative variable on x or y to improve accuracy and
  speed across common value and summary tasks.
labels:
- chart:scatter
- task:retrieve-value
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use position for the primary quantitative field in trivariate point charts <!-- role: advice -->

Encode the primary quantitative field using a position axis (x or y) rather than encoding it with size or color in trivariate point-based charts.

## Why position helps primary quantitative decoding <!-- role: reason -->

Placing the primary quantitative field on a spatial axis supports more precise decoding and comparison than encoding that same field with retinal channels when users must read or compare values.

**Mechanism:** Position supports fine-grained value discrimination and reduces decoding ambiguity compared to size or color for the same quantitative judgments.

**Evidence:** Across multiple tasks (retrieve-value, sort, find-extremum, aggregate), encodings that map the primary quantitative field to x or y appear in the top-ranked groups for accuracy and are also among the fastest overall compared to designs where the primary quantitative field is encoded via color-saturation or area/size [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about *which channel carries the primary quantitative field*, not about how to encode the secondary quantitative field or the categorical field.

## When you should apply this <!-- role: context -->

- **User Goal:** Read, compare, or locate values of a primary quantitative variable while still showing category membership and a secondary quantitative variable.
- **Task:** retrieve-value, sort, find-extremum, aggregate.
- **Data:** Trivariate data with 1 categorical field and 2 quantitative fields.
- **Chart Setting:** Static point-based visualization (scatterplot-like), with no interaction assumed.
- **Audience:** General audiences doing exploratory or confirmatory reading.
- **Success Criterion:** Higher accuracy with competitive completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary quantitative field is not actually the value users must decode (for example, the “primary” field is misidentified). **Why:** The advantage depends on which field users are tasked to read or compare.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Using x/y for the primary quantitative field reduces flexibility for assigning x/y to other fields. **Risk:** If you mistakenly treat a secondary field as primary, you may optimize the wrong decoding. **Mitigation:** Confirm which field the user’s questions depend on before assigning channels.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding the primary quantitative field with color-saturation or area/size while reserving x/y for other fields by default. **Why it fails:** It tends to reduce accuracy and can increase time relative to position encodings for the primary quantitative field in the tested tasks.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers repeatedly misread values or need long time to answer simple “what is the value?” questions. **Quick Check:** Ask a teammate to answer a retrieve-value question from the chart; if they hesitate or guess, the primary field may be in a weaker channel. **Stronger Test:** Run a small timed two-choice pilot (retrieve-value or find-extremum) comparing a positional vs non-positional encoding for the primary field.

## What to do instead <!-- role: fix -->

- Swap encodings so the primary quantitative field is on x or y and move the less critical field off position.
- If you must keep another field on position, reduce the design to fewer encoded fields so the remaining positional axis carries the primary quantitative field.
- If the chart must keep all three fields, prioritize position for the primary quantitative field and use a non-positional channel for the secondary quantitative field.
