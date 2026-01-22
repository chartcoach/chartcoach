---
id: compute-term-colorability-from-basic-color-cooccurrence
title: Compute a term colorability score from co-occurrence with basic color names
bibliography: references.bib
description: Estimate whether a category label is semantically color-associated by
  measuring its co-occurrence with basic color terms.
labels:
- chart:categorical
- task:encode
- visual:color
- impact:automation
- data:categorical
- audience:expert
- complexity:advanced
---

## Use co-occurrence with basic color terms to decide if a label is colorable <!-- role: advice -->

Compute a colorability score for each category label by measuring its normalized pointwise mutual information with basic color names, and treat only high-scoring labels as candidates for semantic color assignment.

## Why co-occurrence predicts semantic color association <!-- role: reason -->

If people commonly talk about a concept alongside a color term (e.g., “charcoal gray”), that linguistic pattern is evidence that color is a salient property of the concept; normalized association measures turn this into a comparable score across labels and colors.

**Mechanism:** Normalized Pointwise Mutual Information (NPMI) increases when a term and a color word appear together more than expected by chance, and aggregating NPMI across colors yields a measure of how strongly any basic color is associated with the term.

**Evidence:** A colorability score built from Google n-gram co-occurrence with the 11 basic color terms produces plausible term–color associations and aligns with high-colorability color names in a large crowd-sourced color naming dataset used for validation [@setlurLinguisticApproachCategorical2016].

**Notes:** This step provides both a scalar “colorability” and a ranked set of associated basic colors per term.

## When to use linguistic colorability scoring <!-- role: context -->

- **User Goal:** Automatically decide whether and how to assign semantic categorical colors from text labels.
- **Task:** Pre-processing of category labels before palette construction.
- **Data:** Category names that may be objects, concepts, or multi-word phrases; potentially long-tailed vocabularies.
- **Chart Setting:** Systems that need automatic defaults (e.g., visualization tools, templated reporting).
- **Audience:** Designers and developers building automated encoding.
- **Success Criterion:** Avoid assigning “semantic” colors when semantics are weak; surface likely basic-color options when semantics are strong.

## When this scoring approach is not sufficient <!-- role: exceptions -->

- **Break it when:** The term is absent or poorly represented in the corpus (e.g., some brand names). **Why:** Co-occurrence cannot be estimated reliably, so the method may fail to return any colorability signal [@setlurLinguisticApproachCategorical2016].
- **Break it when:** The same surface form has multiple senses with different colors (e.g., “apple” as fruit vs. company). **Why:** A single score without context can mix meanings and return the wrong association [@setlurLinguisticApproachCategorical2016].

## Tradeoffs of corpus-based colorability <!-- role: costs -->

**Sacrifice:** Requires access to large-scale co-occurrence data and text processing. **Risk:** Corpus artifacts and historical shifts in usage can produce unexpected associations. **Mitigation:** Preserve strong peaks of association and suppress low co-occurrence noise using thresholds [@setlurLinguisticApproachCategorical2016].

## Common implementation pitfalls <!-- role: mistakes -->

- **Mistake:** Treating any nonzero co-occurrence as evidence of colorability. **Why it fails:** Weak co-occurrences are noisy and can generate false semantic color assignments [@setlurLinguisticApproachCategorical2016].
- **Mistake:** Ignoring multi-word phrase structure (e.g., duplicating a terminal color word). **Why it fails:** It can distort counts and inflate or suppress associations incorrectly [@setlurLinguisticApproachCategorical2016].

## Quick checks for colorability scoring quality <!-- role: check -->

**Failure Sign:** Many non-color concepts receive “semantic” colors, or obviously color-linked objects get low scores. **Quick Check:** Inspect top-scoring terms and verify they look inherently color-related. **Stronger Test:** Validate against an external color-name dataset by checking whether known color names and common color-associated objects score highly [@setlurLinguisticApproachCategorical2016].

## What to do instead when the corpus signal is weak <!-- role: fix -->

- Use additional semantic context (such as the field name “Brands” or “Countries”) to switch to symbol-based retrieval (logos/flags).
- Fall back to perceptually designed categorical palettes when colorability is low or missing.
- Add sense-disambiguating context to the label (e.g., “Apple (company)”) before scoring.
- Maintain an override mechanism for domain-specific dictionaries (e.g., named brand palettes) when corpus coverage is inadequate [@setlurLinguisticApproachCategorical2016].
