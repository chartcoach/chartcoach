---
id: unify-a-palette-by-shifting-hues-with-blend-modes-then-recheck-distinctness
title: Unify Palette Hues With a Blend Mode, Then Re-Validate Distinctness
bibliography: references.bib
description: "Make a disparate palette feel cohesive by applying a hue-shifting blend\
  \ overlay, then confirm you didn\u2019t reduce category separability."
labels:
- chart:all
- task:style
- visual:color
- impact:cohesion
- data:categorical
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

If your palette feels like it doesn’t “belong together,” apply a subtle hue-shifting blend overlay (e.g., Hue blend mode) across all swatches to harmonize them, then re-check that categories are still distinguishable.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Controlled hue alignment increases cohesion but can reduce contrast
- **The Evidence:** Muth describes a workflow in tools like Figma/Photoshop: place a colored rectangle over swatches, set it to “Hue” (or sometimes “Overlay”), and adjust opacity to shift hues toward a common direction; she warns that hue contrast can weaken and should be checked afterward [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Make a multi-color categorical palette feel cohesive/intentional
- **Data Type:** Any categorical palette that looks mismatched or “from different sets”
- **Audience:** Any; especially where visual polish matters (publishing, presentations)

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** Your palette is already barely distinguishable
- **Reason:** Further reducing hue contrast can make categories indistinct [@muth_good_color_palettes_2024].
- **Scenario:** You rely on strong hue differences as the primary separator (same lightness)
- **Reason:** Hue alignment undermines the main discrimination channel [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You may lose some vivid variety between colors
- **The Risk:** Overdoing the overlay can collapse categories into similar hues and harm readability [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Applying a strong overlay at high opacity until everything looks “nice”
- **Why it fails:** It can erase meaningful differences and reduce distinguishability [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Unifying colors and assuming accessibility is unchanged
- **Why it fails:** Muth notes hue contrast can become weaker, so you must re-check [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** After harmonizing, two categories look closer than before (especially in legends or thin lines)
- **The Test:** Compare before/after swatches at small size; run a palette check tool (or your chart tool’s colorblind check) to confirm separability [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce overlay opacity or switch blend mode; choose a different overlay color that shifts hues less aggressively [@muth_good_color_palettes_2024].
- **Best Fix:** Harmonize lightly, then re-introduce separation by adjusting lightness/saturation of individual swatches while keeping the unified hue direction [@muth_good_color_palettes_2024].
