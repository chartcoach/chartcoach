---
id: use-sci-dimensions-to-diversify-shape-choices-not-just-count-shapes
title: Diversify shape choices across segmentability, compactness, and spikiness (not
  just by adding more shapes)
bibliography: references.bib
description: Increase the number of distinguishable shape categories by spanning SCI
  dimensions rather than adding near-duplicate symbols.
labels:
- chart:scatter
- task:group
- visual:shape
- impact:clarity
- data:categorical
- audience:novice
- domain:dataviz
---

## Spread shape categories across SCI dimensions, not within one cluster <!-- role: advice -->

When you need multiple shape categories, choose shapes that collectively span segmentability, compactness, and spikiness instead of selecting many variants that share the same overall structure. Add a new category only if it is meaningfully separated along at least one SCI dimension from the existing set.

## Why spanning SCI expands usable category count <!-- role: reason -->

Adding symbols that are close in feature space creates categories that compete for the same preattentive representation, leading to confusion; spanning distinct SCI dimensions reduces this competition and supports cleaner segmentation.

**Mechanism:** The SCI space provides the dominant axes along which preattentive shape representations differ; allocating categories across these axes increases between-category distances and thus discriminability.

**Evidence:** A three-dimensional SCI space (segmentability, compactness, spikiness) accounted for most variance in shape-pair discriminability in an attention-demanding texture segregation task (r = 0.974), implying that adding categories by increasing SCI spread should increase distinguishability more than adding near-neighbors [@huangSpacePreattentiveShape2020].

**Notes:** The SCI dimensions also refine earlier isolated notions (intersection→segmentability, closure/concavity→compactness, line termination→spikiness), giving a practical checklist for “how” two shapes differ.

## When SCI-based diversification applies <!-- role: context -->

- **User Goal:** Encode multiple categorical groups using shape.
- **Task:** Preattentive separation of multiple groups in a shared space.
- **Data:** Many categories (more than two or three) shown simultaneously.
- **Chart Setting:** Plots where marks overlap or intermix, making quick selection essential.
- **Audience:** Broad audiences; viewers scanning rather than carefully inspecting each mark.
- **Success Criterion:** Low between-category confusion without relying on legend reading.

## When to break SCI-based diversification <!-- role: exceptions -->

**Break it when:** Categories are always shown in separate panels or clearly separated regions, so shape-based segmentation is not needed. **Why:** The primary benefit of SCI spread is in parallel selection within mixed arrays.

## Tradeoffs and risks of SCI-based diversification <!-- role: costs -->

**Sacrifice:** Some desired symbols may be excluded because they are too close to others in SCI space. **Risk:** Overemphasizing spiky or highly segmentable forms can make the plot visually “busy.” **Mitigation:** Keep mark size modest and avoid adding extra visual complexity beyond what is needed for separation.

## Common failures when “adding more shapes” <!-- role: mistakes -->

- **Mistake:** Expanding a shape palette with several similarly compact polygons or similarly open/closed variants. **Why it fails:** These additions do not create large SCI distances, so the effective discriminable set does not grow much.
- **Mistake:** Assuming perceived distinctness in a legend will translate to distinctness in a dense plot. **Why it fails:** The relevant measure is preattentive discriminability in attention-demanding arrays, which SCI approximates.

## Quick checks for SCI palette growth <!-- role: check -->

**Failure Sign:** Additional categories increase legend size but not the ease of finding groups in the plot. **Quick Check:** Hide the legend and see whether you can still separate all categories by shape at a glance. **Stronger Test:** Create a dense mixed sample plot and ask users to point out all marks of a named category; track error rate as categories are added.

## What to do instead if you cannot spread shapes enough <!-- role: fix -->

- Reduce the number of categories encoded by shape and encode remaining categories via another channel.
- Split categories across panels (faceting) to reduce simultaneous shape discrimination demands.
- Collapse similar categories or provide interactive filtering so only a few categories are shown at once.
- Use a small, high-separation subset of shapes rather than a large, low-separation palette.
