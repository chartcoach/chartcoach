---
id: encode-nominal-categories-with-position-then-color-hue
title: Encode Nominal Categories with Position, Then Color Hue
bibliography: references.bib
description: For unordered categories, prefer position encodings; if using color,
  prefer hue over saturation.
labels:
- task:group
- visual:position
- visual:color
- impact:discriminability
- data:nominal
- audience:general
- complexity:foundational
---

## The Rule <!-- role: advice -->

For nominal (unordered) categories, encode category identity with position (x/y) where possible; if using color, use color hue rather than color saturation.

## The Logic <!-- role: reason -->

The theoretical effectiveness ordering for nominal data places position (x/y) highest, with color hue above texture, and with color saturation ranked below hue. This rule comes from [@mackinlayAutomatingDesignGraphical1986a] and is collated for visualization recommendation in [@zengReviewCollationGraphical2023].

- **The Principle:** Effectiveness ordering for nominal perceptual tasks
- **The Evidence:** [@mackinlayAutomatingDesignGraphical1986a], as collated in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguishing groups/categories reliably
- **Data Type:** Nominal categories (no intrinsic order)
- **Audience:** General audiences

## When to Break It <!-- role: exceptions -->

- **Scenario:** Color hue is unavailable (e.g., restricted medium) and you must still differentiate categories.
- **Reason:** The rule assumes hue is feasible; when it is not, lower-ranked alternatives may be required.

## The Price <!-- role: costs -->

- **The Sacrifice:** Using position for nominal grouping can force faceting or re-layout that consumes space.
- **The Risk:** Overusing color hue for too many categories can make groups hard to distinguish (even if hue is preferred over saturation).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding nominal categories with a light-to-dark saturation ramp.
- **Why it fails:** A saturation ramp can imply unintended ordering; the nominal effectiveness ordering prefers hue over saturation.

## How to Check <!-- role: check -->

- **Visual Sign:** Categories look like they progress from light to dark, suggesting an order that does not exist in the data.
- **The Test:** Ask whether a viewer could reasonably infer “greater/less” from the encoding; if yes, you are likely implying an order.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the palette from saturation steps to distinct hues.
- **Best Fix:** Use position-based separation (e.g., separate regions/axes) for the primary category split and reserve hue for secondary grouping.
