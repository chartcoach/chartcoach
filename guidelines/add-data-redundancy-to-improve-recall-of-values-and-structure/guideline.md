---
id: add-data-redundancy-to-improve-recall-of-values-and-structure
title: Duplicate Key Data Values with Secondary Encodings (e.g., Value Labels)
bibliography: references.bib
description: Data redundancy is linked to higher-quality recall descriptions, suggesting
  clearer encoding of quantitative details.
labels:
- chart:any
- task:read-value
- visual:text
- visual:redundancy
- impact:recall
- impact:clarity
- audience:general
- source:borkin-2016
---

## The Rule <!-- role: advice -->

Add data redundancy by encoding important values more than once (e.g., show numeric labels in addition to position/length).

## The Logic <!-- role: reason -->

Redundant encodings give viewers additional ways to encode the same quantitative information, improving the chances it is remembered accurately.

- **The Principle:** Multiple encodings for the same quantitative fact
- **The Evidence:** Visualizations with data redundancy had higher average description quality than those without (overall 2.01 vs 1.70), and top-third description-quality visualizations were more likely to include data redundancy than bottom-third ones (34% vs 12%) [@borkinMemorabilityVisualizationRecognition2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Recall specific values or key comparisons later
- **Data Type:** Low-to-moderate cardinality displays where labels fit (e.g., a few bars/slices)
- **Audience:** General audiences; presentation contexts where memory matters

## When to Break It <!-- role: exceptions -->

- **Scenario:** High-density charts where labeling every mark would overwhelm the display.
- **Reason:** Additional labels increase clutter and may reduce readability; the paper frames redundancy as beneficial but also shows attention is drawn to text, which can compete with other elements [@borkinMemorabilityVisualizationRecognition2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and visual cleanliness.
- **The Risk:** If overused, value labels can dominate attention and make scanning harder [@borkinMemorabilityVisualizationRecognition2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Labeling everything indiscriminately.
- **Why it fails:** You increase reading burden without targeting what must be remembered [@borkinMemorabilityVisualizationRecognition2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can describe the trend but cannot recall any concrete numbers or magnitudes.
- **The Test:** Ask viewers to report one or two key values after a brief delay; if they consistently can’t, consider targeted redundancy [@borkinMemorabilityVisualizationRecognition2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add numeric labels only to key points (max/min, highlighted categories).
- **Best Fix:** Use a deliberate redundancy strategy: label the values that support the message while keeping the rest uncluttered [@borkinMemorabilityVisualizationRecognition2016].
