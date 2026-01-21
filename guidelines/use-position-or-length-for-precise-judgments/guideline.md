---
id: use-position-or-length-for-precise-judgments
title: Encode Precise Values with Position or Length
bibliography: references.bib
description: Use position or length encodings when users must make accurate quantitative
  judgments.
labels:
- chart:scatter
- task:estimate
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

When users need precise quantitative judgments, encode values with **position** (best) or **length**; avoid encoding important values with **area** or **intensity**.

## The Logic <!-- role: reason -->

- **The Principle:** Visual encodings differ in perceptual precision.
- **The Evidence:** Position supports much smaller estimation error than length, which in turn is more precise than area or intensity in ratio judgments and value extraction [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Reading exact-ish values, estimating ratios, making close comparisons.
- **Data Type:** Quantitative measures (especially when differences are small).
- **Audience:** Decision-makers and general audiences who must be correct, not just “get the gist.”

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is only “big picture” pattern spotting (e.g., quickly detecting clusters or spatial patterns).
- **Reason:** Lower-precision channels like intensity can be acceptable for rapid overview patterns rather than exact value reading [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer variables can be packed into a small space compared with dense intensity-based displays.
- **The Risk:** Overuse of position/length may require more chart real estate or more panels.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding key comparisons via bubble area or heatmap intensity and expecting accurate judgments.
- **Why it fails:** The eye’s estimates from area/intensity are systematically less precise [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must “guess” values because adjacent values look too similar or ambiguous.
- **The Test:** Ask a colleague to estimate a ratio between two marks; if answers vary widely, the encoding is too imprecise.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a position/length encoding for the key measure (e.g., switch a heatmap cell to a small bar-in-cell for critical comparisons).
- **Best Fix:** Change to a position-based chart (dot plot/scatter/line) or a length-based chart (bar) for the primary quantitative task [@zacksDesigningGraphsDecisionMakers2020].
