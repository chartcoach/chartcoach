---
id: do-not-use-single-axis-position-encoding-for-one-to-many-relations
title: Do not use single-axis position encoding for one-to-many relations
bibliography: references.bib
description: Avoid encodings where one mark is uniquely tied to a domain value but
  would need multiple positions to represent multiple related values.
labels:
- chart:dot
- task:encode
- visual:position
- impact:accuracy
- data:relational
- audience:expert
- concept:functional-dependency
---

## Single-axis position requires a functional dependency <!-- role: advice -->

Do not use a single-axis position encoding (one mark per item placed along one axis) when a domain value maps to multiple values in the other domain.

## Why single-axis position cannot represent one-to-many <!-- role: reason -->

In the horizontal-position style, each mark is conventionally paired with a unique value in the first domain, and the mark’s position on the axis encodes the associated value in the second domain. A one-to-many relation would require the same mark to take two different positions on the same axis, which is impossible under these semantics.

**Mechanism:** The “one mark ↔ one domain value” convention makes mark position a single-valued function; one-to-many data violates that constraint.

**Evidence:** It is shown that one-to-many relations cannot be expressed in the horizontal-position language because a mark cannot simultaneously occupy two distinct axis positions for two distinct dependent values [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** This limitation depends on the convention that marks represent domain values (not tuples), which is the standard assumption for these encodings [@mackinlayAutomatingDesignGraphical1986b].

## When this restriction applies <!-- role: context -->

- **User Goal:** Encode a binary relation accurately with position on one axis.
- **Task:** Represent multiplicity without losing tuples.
- **Data:** Binary relation where some key value in the first domain relates to multiple values in the second domain.
- **Chart Setting:** Designs that pair one mark with one domain value and use its position on a single axis to encode the dependent value.
- **Audience:** Readers interpreting each mark as “the item.”
- **Success Criterion:** Every tuple in the one-to-many relation is representable without contradiction.

## When you might break this rule <!-- role: exceptions -->

**Break it when:** Your semantics explicitly pair marks with tuples (so multiple marks can share the same first-domain value). **Why:** The impossibility result relies on pairing marks with domain values; changing that convention changes what the design can express [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** You lose the compactness of “one item, one mark” displays when multiplicity is present. **Risk:** Switching encodings can increase mark count and visual clutter. **Mitigation:** Use encodings that allow repeated marks per key value or restructure the view.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Keeping one mark per key value and trying to “average” or “pick one” of multiple dependent values. **Why it fails:** It drops valid tuples, so the chart no longer encodes all facts in the relation [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** A single item must appear at two different positions to show the data. **Quick Check:** For each first-domain value, count how many distinct second-domain values exist; if any count exceeds one, single-axis position per item will fail. **Stronger Test:** Write the implied encoding equation (“value = scale × position + offset”) and verify it is single-valued for each item.

## What to do instead <!-- role: fix -->

- Represent tuples with multiple marks rather than forcing one mark per first-domain value.
- Use an encoding family that can naturally represent one-to-many structure (for example, connection-based designs when appropriate).
- Partition the relation into subsets that are functional and present them separately.
- Add an additional encoding channel that distinguishes multiple tuples for the same key (so each tuple can be represented distinctly).
