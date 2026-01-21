---
id: prefer-square-bar-aspect-ratios-to-reduce-recall-bias
title: Use Square-Like Bars to Minimize Recall Bias in Value Retrieval
bibliography: references.bib
description: Square-like bar marks reduce systematic bias when users retrieve and
  recall quantitative values.
labels:
- chart:bar
- task:retrieve-value
- visual:length
- impact:bias-reduction
- data:quantitative
- audience:general
- evidence:experimental
---

## The Rule <!-- role: advice -->

When using bars for a retrieve-value task that involves recall/reproduction, prefer square-like bar aspect ratios over wide or tall bars.

## The Logic <!-- role: reason -->

Square aspect ratios showed the least bias compared with wide and tall aspect ratios in the extracted record of experimental results.

- **The Principle:** Aspect ratio modulates systematic bias in recalled bar position
- **The Evidence:** This guidance is based on collated graphical perception results [@zengReviewCollationGraphical2023] summarizing experimental evidence that square aspect ratio bars exhibit less systematic bias than wide or tall aspect ratios during retrieve-value recall [@cejaTruthSquareAspect2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve a quantitative value from a bar and recall/reproduce it.
- **Data Type:** Quantitative values encoded by bar length (rectangular marks), linear scale.
- **Audience:** General audiences, especially where readers may compare across moments (e.g., between separated views).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your design requires intentionally non-square bars for another purpose (e.g., fixed-width constraints that necessarily create tall/thin bars).
- **Reason:** This rule targets bias reduction in recall; if bias reduction is not the primary objective, you may accept the tradeoff (the structured evidence does not cover those alternative objectives) [@cejaTruthSquareAspect2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space efficiency (square-like bars can demand more horizontal or vertical space).
- **The Risk:** Reduced ability to fit many bars in a compact panel without scrolling or faceting.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping wide bars but assuming “position encoding is always precise enough.”
- **Why it fails:** The extracted evidence explicitly documents systematic bias in recall even for bar/position-style encodings, depending on aspect ratio [@zengReviewCollationGraphical2023; @cejaTruthSquareAspect2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars look close to squares (width and height visually similar) rather than very elongated.
- **The Test:** Inspect typical data values: if most bars render as near-square rectangles rather than extreme strips, you are aligned with the lower-bias condition reported in the collated evidence [@cejaTruthSquareAspect2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust bar thickness or chart dimensions so typical bars appear more square-like.
- **Best Fix:** Redesign the panel/grid so bar geometry remains square-like across responsive breakpoints and across the views where users must remember values, consistent with the bias patterns recorded in the collation [@zengReviewCollationGraphical2023; @cejaTruthSquareAspect2021].
