---
id: prefer-mark-composition-over-layout-separation-when-combining-encodings
title: Prefer Mark Composition Over Separating Charts When Possible
bibliography: references.bib
description: If multiple relations can be merged into the same marks without conflict,
  do so instead of splitting into separate panels.
labels:
- chart:any
- task:combine
- visual:retinal
- impact:integration
- data:multivariate
- audience:expert
- composition:mark
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

When encodings are compatible, merge variables into the same mark set (mark composition) rather than splitting them into separate charts.

## The Logic <!-- role: reason -->

Mark composition can combine encodings without increasing the number of graphical objects, making the result more integrated than layouts that merely place charts adjacent; the paper ranks mark composition as more effective than single-axis composition in this sense.

- **The Principle:** More integration with fewer added objects improves perceptual access to combined information
- **The Evidence:** Mark composition is described as most effective because it does not increase object count; single-axis composition is least effective because it doesn’t truly merge designs [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Read multiple attributes per item in a single integrated view
- **Data Type:** Shared item domain where additional variables can be encoded via compatible channels (e.g., position + color + size)
- **Audience:** Users comfortable with multichannel encodings

## When to Break It <!-- role: exceptions -->

- **Scenario:** Encodings interact and reduce legibility (e.g., size makes shape discrimination fail when marks get small).
- **Reason:** The paper notes channel interactions can reduce effectiveness and must be checked [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher cognitive load; users must interpret multiple channels simultaneously.
- **The Risk:** Channel interference or insufficient discriminability can make the view misleading or unreadable [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Merging encodings even when they conflict (e.g., trying to use size for two different variables on the same marks).
- **Why it fails:** Mark composition requires that shared retinal constraints encode the same information; otherwise the merge is invalid [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** The same visual property (e.g., size) appears to represent two different variables in the combined view.
- **The Test:** For each visual channel (position, color, size, etc.), confirm it maps to only one variable per mark set and remains consistent across the composed design [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move one variable to a different channel (e.g., shift from size to color if available).
- **Best Fix:** If compatibility can’t be achieved, fall back to axis-based composition (double-axes or single-axis) instead of forcing an invalid mark merge [@mackinlayAutomatingDesignGraphical1986b].
