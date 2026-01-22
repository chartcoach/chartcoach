---
id: use-100-percent-stacked-columns-when-shares-matter-more-than-totals
title: Use 100% stacked column charts only when relative shares matter more than totals
bibliography: references.bib
description: Normalize stacks to 100% when you want to compare composition across
  categories and totals are not meaningful to the reader.
labels:
- chart:100%-stacked-column
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:intermediate
---

## Use 100% stacked columns when composition is the point and totals are not <!-- role: advice -->

Use a 100% stacked column chart when the relative shares are more important than absolute values and the totals are not relevant.

## Why normalization changes what comparisons are reliable <!-- role: reason -->

Normalizing forces every column to the same height, shifting attention from totals to composition and creating a consistent top and bottom baseline that can support comparison for two highlighted segments.

**Mechanism:** Equalized heights remove magnitude cues and strengthen share comparisons; the top edge becomes an additional baseline for a segment placed at the top.

**Evidence:** Stacking percentages can be useful when relative part sizes matter more than absolute sizes and totals are not of interest, and it creates a second baseline at the top that can support comparison for another important segment [@muth_stacked_columns_2018].

**Notes:** A 100% stack answers “how is each total composed?” not “how big is each total?”

## When this applies <!-- role: context -->

- **User Goal:** Compare the composition (shares) across categories.
- **Task:** Judge which categories have higher/lower proportion of a part.
- **Data:** Parts that sum to a meaningful whole per category; totals vary but are not important for interpretation.
- **Chart Setting:** Situations where a consistent height improves comparability of shares.
- **Audience:** Readers focused on proportional differences.
- **Success Criterion:** The viewer is not misled into thinking equal column heights imply equal totals.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Totals are important or should be compared. **Why:** Normalizing removes absolute magnitude differences and can hide meaningful changes in totals [@muth_stacked_columns_2018].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** You lose information about absolute totals. **Risk:** Readers may assume categories are equal in size because every column reaches 100%. **Mitigation:** State clearly that the chart shows shares and, if needed, show totals elsewhere.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using 100% stacked columns when readers need to know which totals are larger. **Why it fails:** The normalization suppresses the very differences the reader needs [@muth_stacked_columns_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The audience asks “but how many is that?” or the narrative depends on absolute size. **Quick Check:** Remove totals from your draft text—if the message collapses, don’t normalize. **Stronger Test:** Pair the chart with a one-sentence takeaway; if it must mention totals, a 100% stack is mismatched [@muth_stacked_columns_2018].

## What to do instead <!-- role: fix -->

- Use a regular stacked column chart if both totals and composition matter.
- Use a line or bar-based display of totals if magnitude is central.
- Show composition with another method while keeping totals visible elsewhere (e.g., separate total chart plus composition chart).
- Highlight one or two key shares rather than expecting readers to compare many floating segments.
