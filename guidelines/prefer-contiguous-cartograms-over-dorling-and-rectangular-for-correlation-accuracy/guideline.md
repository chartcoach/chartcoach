---
id: prefer-contiguous-cartograms-over-dorling-and-rectangular-for-correlation-accuracy
title: Prefer contiguous cartograms over Dorling and rectangular cartograms for correlation
  accuracy
bibliography: references.bib
description: Contiguous cartograms achieved higher accuracy than Dorling and rectangular
  cartograms for a correlation task among cartogram types.
labels:
- chart:cartogram
- task:correlate
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:contiguous
---

## Prefer contiguous cartograms for correlation accuracy among these types <!-- role: advice -->

Prefer a contiguous cartogram over Dorling and rectangular cartograms when you need higher accuracy on correlation judgments in cartogram comparisons. If you cannot use contiguous, prefer Dorling over rectangular for this correlation-accuracy scenario.

## Why contiguous cartograms can support correlation judgments here <!-- role: reason -->

Correlation judgments depend on perceiving spatial patterns and co-variation reliably; distortions that interfere with pattern reading can reduce correctness.

**Mechanism:** Preserving a more coherent geographic layout can help viewers detect co-variation patterns more accurately.

**Evidence:** In a correlation task, contiguous cartograms ranked higher than Dorling and rectangular cartograms in accuracy, with significant pairwise differences reported (contiguous over Dorling and rectangular, and Dorling over rectangular) [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** The provided results did not include non-contiguous for this correlation ranking.

## When correlation is the primary reading goal <!-- role: context -->

- **User Goal:** Judge co-variation or relationship patterns accurately using a cartogram view.
- **Task:** Correlate.
- **Data:** Geo-referenced regions with quantitative values encoded by area.
- **Chart Setting:** Static cartogram selection among contiguous, Dorling, and rectangular variants.
- **Audience:** Users needing correct relationship judgments.
- **Success Criterion:** Higher accuracy on correlation questions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your primary objective is not correlation accuracy (e.g., a different task dominates). **Why:** The evidence is specific to correlation accuracy rather than other outcomes.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may trade off other properties that another cartogram type supports better for your overall workflow. **Risk:** If your correlation prompt differs from the tested one, the ranking may not hold. **Mitigation:** Confirm with a small pilot using your actual correlation questions.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using a rectangular cartogram for correlation judgments because it preserves adjacency. **Why it fails:** The tested correlation accuracy ranking places rectangular lowest among the compared types.

## Quick tests <!-- role: check -->

**Failure Sign:** Users make inconsistent or incorrect correlation judgments across repeated questions. **Quick Check:** Compare correlation-answer accuracy for contiguous vs Dorling (and vs rectangular) on representative items. **Stronger Test:** Run a controlled evaluation on your prompt set and measure accuracy differences.

## What to do instead <!-- role: fix -->

- Use a Dorling cartogram if you cannot deploy a contiguous cartogram and still need better accuracy than rectangular.
- Provide a second cartogram view for correlation tasks while using your preferred map type for other tasks.
- Reduce correlation inference demands by presenting correlation results separately and using the cartogram only as contextual display.
- Reframe the analysis question to a different task supported by your chosen cartogram type, then evaluate accuracy.
