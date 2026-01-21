---
id: accept-lower-data-ink-ratio-when-designing-for-memorability
title: Accept a Lower Data-Ink Ratio When Designing for Memorability
bibliography: references.bib
description: Lower data-ink ratios (more non-data ink) are associated with higher
  memorability scores in a large-scale study.
labels:
- chart:any
- task:recall
- visual:annotation
- impact:memorability
- data:any
- audience:general
- evidence:empirical
---

## The Rule <!-- role: advice -->

When memorability matters, do not optimize solely for a “good” data-ink ratio—allow additional non-data ink.

## The Logic <!-- role: reason -->

Extra non-data elements can increase distinctiveness and provide additional cues that make a visualization easier to recognize later.

- **The Principle:** Distinctive non-data cues aid recognition memory
- **The Evidence:** Visualizations rated as having a “bad” data-ink ratio (more non-data ink) had higher memorability scores than those rated “good,” with pairwise significant differences across the three levels [@borkinWhatMakesVisualization2013a].

## Where to Apply <!-- role: context -->

- **User Goal:** Remember the visualization later (as an image)
- **Data Type:** Any; especially in collections where many visuals are similar
- **Audience:** General audiences and rapid-exposure settings

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are evaluating or optimizing for comprehension rather than memorability.
- **Reason:** The paper explicitly cautions that memorability measured here does not imply comprehension of the visualization [@borkinWhatMakesVisualization2013a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Minimalist clarity and possibly speed of reading.
- **The Risk:** Viewers may remember decorative/annotative elements more than the intended data message [@borkinWhatMakesVisualization2013a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “chart junk” as uniformly bad and stripping all non-data elements.
- **Why it fails:** The study’s results show that, in aggregate, lower data-ink ratio correlates with higher memorability [@borkinWhatMakesVisualization2013a].

## How to Check <!-- role: check -->

- **Visual Sign:** The design is extremely minimal with few cues beyond core marks.
- **The Test:** If you remove legends/labels/annotations and the visualization barely changes, you likely have a very high data-ink ratio and may be sacrificing memorability [@borkinWhatMakesVisualization2013a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a small set of non-data cues (annotations, stylized elements) that differentiate the chart visually.
- **Best Fix:** Add non-data ink that creates a distinctive overall image while remaining relevant to the intended message [@borkinWhatMakesVisualization2013a].
