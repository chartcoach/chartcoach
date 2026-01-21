---
id: measure-term-colorability-before-using-semantic-color-encoding
title: Measure Term Colorability Before Applying Semantic Colors
bibliography: references.bib
description: Only apply semantic color encodings when a term shows strong, measurable
  association with basic color names.
labels:
- chart:categorical
- task:encode
- visual:color
- impact:trust
- data:categorical
- audience:designer
- method:nlp
---

## The Rule <!-- role: advice -->

Before assigning semantic colors, determine whether each category label is actually “colorable”; if it isn’t, do not force a semantic color mapping.

## The Logic <!-- role: reason -->

Semantic color only helps when a label has a strong association with one or more basic colors; otherwise color semantics are weak and may be arbitrary or misleading. The paper operationalizes this using co-occurrence with Berlin & Kay basic color names and a colorability score derived from normalized PMI (NPMI), treating high associations (e.g., NPMI ≥ 0.5) as evidence of colorability [@setlurLinguisticApproachCategorical2016].

- **The Principle:** Only encode semantics that viewers are likely to share.
- **The Evidence:** [@setlurLinguisticApproachCategorical2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Avoid misleading “meaningful-looking” colors and reserve semantic color for categories where it will be recognized.
- **Data Type:** Arbitrary categorical labels, especially mixed sets where some items are strongly color-associated (fruits) and others are not (school subjects).
- **Audience:** Visualization authors building automatic or semi-automatic color assignment.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have a verified domain color standard (e.g., an official brand style guide) even if general language corpora don’t reflect it.
- **Reason:** Corpus-based colorability can miss niche or newly coined associations; domain standards override corpus coverage limitations [@setlurLinguisticApproachCategorical2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some categories will remain uncolored semantically and may fall back to a default palette.
- **The Risk:** Over-filtering can reduce semantic coverage if thresholds are too strict or the corpus lacks the term (e.g., certain brand names) [@setlurLinguisticApproachCategorical2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming every noun has a canonical color and assigning one anyway.
- **Why it fails:** It creates false semantics and inconsistent mappings across datasets [@setlurLinguisticApproachCategorical2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Colors feel arbitrary (“why is this category blue?”) and don’t match common expectations.
- **The Test:** For each label, check whether it has strong association to any basic color term (as defined by the paper’s NPMI-based approach). If no basic color exceeds the association threshold, treat it as non-colorable [@setlurLinguisticApproachCategorical2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Mark low-colorability categories as “no semantic color” and assign them from a neutral categorical palette.
- **Best Fix:** Use an explicit colorability computation (NPMI with basic color terms) to decide which labels get semantic colors and which do not [@setlurLinguisticApproachCategorical2016].
