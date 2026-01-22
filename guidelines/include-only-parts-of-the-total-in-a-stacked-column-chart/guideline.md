---
id: include-only-parts-of-the-total-in-a-stacked-column-chart
title: Include only the parts of the total in a stacked column chart (not the total)
bibliography: references.bib
description: A stacked column chart should be composed only of segments that sum to
  the total; do not add the total as another segment.
labels:
- chart:stacked-column
- task:part-to-whole
- visual:structure
- impact:trust
- data:categorical
- audience:novice
- complexity:basic
---

## Stack only components that sum to the total, and never add the total as a segment <!-- role: advice -->

In a stacked column chart, include all components of the total and include only those components, not the total itself.

## Why mixing totals with parts breaks the meaning of a stack <!-- role: reason -->

A stack encodes an additive relationship, so every segment must be a mutually exclusive component of the whole; adding the total as another segment double-counts and destroys interpretability.

**Mechanism:** The viewer interprets stack height as the sum of segments; violating that assumption makes the graphic internally inconsistent.

**Evidence:** Stacked column charts should contain all parts of the total and only parts of the total; the total should not be included as another stacked element [@muth_stacked_columns_2018].

**Notes:** Completeness matters: missing components can also mislead by implying an incomplete whole.

## When this applies <!-- role: context -->

- **User Goal:** Understand how parts add up to a whole for each category.
- **Task:** Reason about composition and totals simultaneously.
- **Data:** A total decomposed into non-overlapping parts.
- **Chart Setting:** Any stacked column chart where arithmetic additivity is assumed.
- **Audience:** Any audience; this is a correctness constraint.
- **Success Criterion:** The sum of visible segments equals the implied total height.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are not actually showing parts of a whole (segments are not additive). **Why:** A stacked chart is the wrong structure if values overlap or don’t sum cleanly [@muth_stacked_columns_2018].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** You may need extra annotation or a separate mark if you want to show totals explicitly. **Risk:** Omitting a component (even unintentionally) can make the stack appear complete when it is not. **Mitigation:** Validate that parts sum correctly for each category before charting.

## Common mistakes <!-- role: mistakes -->

- **Mistake:** Adding a “Total” series into the stack. **Why it fails:** It double-counts and makes the stack height meaningless [@muth_stacked_columns_2018].
- **Mistake:** Leaving out small components without indicating they were excluded. **Why it fails:** The stack no longer represents the full total even though it appears to [@muth_stacked_columns_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The legend includes an item labeled “Total,” or the stack sum exceeds the known total. **Quick Check:** For a few categories, sum the segment values; they should match the total exactly. **Stronger Test:** If you have totals in your data table, compute (parts sum − total); it should be zero for every category [@muth_stacked_columns_2018].

## What to do instead <!-- role: fix -->

- Remove any “Total” series from the stack and show totals as labels or a separate annotation if needed.
- Ensure all components are represented, or explicitly group small ones into “Other.”
- If the components don’t sum cleanly, switch to a different structure that doesn’t imply additivity.
- Add a clear note when values are rounded and small mismatches are possible.
