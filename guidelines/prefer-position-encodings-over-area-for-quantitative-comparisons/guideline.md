---
id: prefer-position-encodings-over-area-for-quantitative-comparisons
title: Prefer position encodings over area encodings for quantitative comparisons
bibliography: references.bib
description: Use positional encodings for quantitative values when accuracy of comparison
  matters, because position is perceived more accurately than area.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- concept:effectiveness
---

## Use position, not area, for accurate quantitative reading <!-- role: advice -->

Prefer encoding quantitative values with position on an axis rather than with mark area when you want viewers to make accurate comparisons.

## Why position yields more accurate quantitative judgments <!-- role: reason -->

Different encodings demand different perceptual tasks, and those tasks vary in accuracy. Position judgments rank above area judgments for quantitative data, so designs that encode key quantities with position support more accurate reading than designs that encode them with area.

**Mechanism:** Position comparisons rely on more precise perceptual discrimination than area comparisons, reducing error when estimating or comparing values.

**Evidence:** Quantitative perceptual tasks are ranked by accuracy with position above area, and this ranking is used to compare alternative graphical languages [@mackinlayAutomatingDesignGraphical1986b]. An explicit comparison of a scatter plot (position-position) versus an area/position design (area-position) treats the position-based encoding as more effective for the quantitative attribute [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** This applies to the most important quantitative fields; less important fields can be encoded with less accurate channels if needed.

## When this applies <!-- role: context -->

- **User Goal:** Compare quantitative values or assess relationships among quantitative variables.
- **Task:** Estimate, compare, or detect patterns in numeric data.
- **Data:** Quantitative ranges where relative differences matter.
- **Chart Setting:** Static 2D charts with axes available.
- **Audience:** Any audience where accurate reading is valued.
- **Success Criterion:** Reduced perceptual error in value comparison.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Position channels are already needed for more important quantitative variables and you must encode an additional variable in the same view. **Why:** Multi-relation designs may require using a less accurate channel for less important information to maintain a single integrated view [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Using position can require additional axes or space, which can limit how many variables fit in one view. **Risk:** Overloading position channels can force awkward layouts or prevent composition with other designs. **Mitigation:** Apply an importance ordering so position is reserved for the most important quantitative relations.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Encoding a primary quantitative variable in area while using position for a less important variable. **Why it fails:** It assigns the more accurate channel to less important information, contradicting the effectiveness ordering [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** Users struggle to judge which of two marks represents a larger value when only size differs. **Quick Check:** If the task includes fine-grained numeric comparison, verify the value is mapped to an axis position rather than to mark area. **Stronger Test:** Ask a few readers to estimate values or rank items; large disagreement indicates the encoding is too low-accuracy.

## What to do instead <!-- role: fix -->

- Move the key quantitative variable to an axis position encoding.
- Relegate secondary quantitative variables to area only after the primary comparisons are supported by position.
- Split into aligned views if adding axes improves positional encoding without clutter.
- Use composition so multiple relations share axes when possible, preserving position accuracy while reducing redundancy.
