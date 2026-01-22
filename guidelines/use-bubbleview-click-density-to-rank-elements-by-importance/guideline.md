---
id: use-bubbleview-click-density-to-rank-elements-by-importance
title: Use BubbleView click density to rank elements by importance
bibliography: references.bib
description: Aggregate BubbleView clicks into an importance map and use per-element
  map maxima to rank design or visualization elements.
labels:
- chart:other
- task:rank
- visual:layout
- impact:decision-support
- data:annotated-elements
- audience:designer
- method:bubbleview
---

## Rank elements using BubbleView-derived importance scores <!-- role: advice -->

Convert BubbleView clicks into a smoothed importance map and compute an importance score per element (e.g., maximum map value within the element region) to rank elements by importance.

## Why map overlap yields comparable element-level importance <!-- role: reason -->

A smoothed click map estimates where users concentrate inspection; intersecting that map with element regions converts a spatial attention estimate into per-element scores that can be compared across elements and designs.

**Mechanism:** Aggregated click density operationalizes “importance” as how frequently regions are inspected; reducing the map over each element yields a scalar that supports ranking.

**Evidence:** On information visualizations with labeled elements, element-importance rankings from BubbleView clicks were highly correlated with rankings derived from eye fixations [@kimBubbleViewInterfaceCrowdsourcing2017]. On graphic designs with explicit importance annotations, BubbleView-derived element importance correlated with annotation-derived element importance across designs, supporting its use for ranking [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** This approach depends on having element regions (segmentations or bounding boxes) to score.

## When this guideline applies <!-- role: context -->

- **User Goal:** Determine which elements (titles, legends, images, text blocks, etc.) are most important to viewers.
- **Task:** Element ranking, prioritization, or comparing design alternatives.
- **Data:** Static images plus element regions (manual boxes or dataset segmentations).
- **Chart Setting:** Design evaluation, visualization evaluation, or dataset creation for importance modeling.
- **Audience:** Designers, visualization researchers, or ML practitioners needing per-element labels.
- **Success Criterion:** Element importance rankings are stable and align with other importance signals (fixations or explicit annotations).

## When not to use element ranking from clicks <!-- role: exceptions -->

**Break it when:** Blur causes key elements to become indistinguishable in the peripheral image. **Why:** Elements may be systematically under-clicked because participants cannot detect them well enough to target them [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Element scoring requires element regions and an additional processing step. **Risk:** Rankings can be sensitive to blur settings and to how elements are bounded (tight vs loose boxes). **Mitigation:** Pilot blur/bubble settings and validate rankings on a subset with an independent signal if available [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Comparing raw click maps to uniform element-level importance annotations without reducing both to element scores. **Why it fails:** Click maps vary within elements by construction, while explicit importance masks can be uniform over elements, making map-to-map comparison misleading [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Element rankings flip substantially across random participant subsets or across minor parameter changes. **Quick Check:** Compute rankings from two random halves of participants and compare rank agreement. **Stronger Test:** If you have ground-truth fixations or explicit annotations, compute correlation of element rankings across methods [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Collect or derive element regions before computing per-element importance scores.
- Tune blur so key elements remain discoverable in the blurred view.
- Use more viewing time or participants on dense designs to stabilize rankings.
- Use explicit importance annotation tasks when you need uniform importance within elements rather than within-element variation [@kimBubbleViewInterfaceCrowdsourcing2017].
