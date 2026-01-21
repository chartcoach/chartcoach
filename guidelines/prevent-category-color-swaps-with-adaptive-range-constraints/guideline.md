---
id: prevent-category-color-swaps-with-adaptive-range-constraints
title: Prevent Category Color Swaps with Adaptive Range Constraints
bibliography: references.bib
description: Use adaptive per-iteration change limits during optimization to avoid
  swapping colors between categories and breaking category-color mapping.
labels:
- chart:generic
- task:distinguish
- visual:color-hue
- impact:consistency
- data:categorical
- audience:expert
- constraint:stability
---

## The Rule <!-- role: advice -->

When optimizing an existing categorical palette where category-to-color mapping must remain stable, apply an **adaptive range** (per-iteration change limit) to each color component to avoid category colors swapping identities.

## The Logic <!-- role: reason -->

Some optimizers (notably population-based methods) can jump to a different region of color space, producing “swaps” where two categories trade colors. Adaptive range constraints enforce gradual evolution, preserving identity and preventing abrupt reassignment.

- **The Principle:** Smooth evolution to preserve mapping identity
- **The Evidence:** The paper defines “Adaptive Range” constraints and demonstrates that genetic algorithm optimization without adaptive range can create a color swap effect, while adaptive range (e.g., Δ=10% per iteration on H/S/V components) alleviates swapping and produces smoother evolution [@fangCategoricalColormapOptimization2017]. Capturing such actionable constraint knowledge is aligned with the collation effort’s aim to support recommendation-system rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Improve distinctness without breaking established category-color associations.
- **Data Type:** Nominal categories where the palette is already in use (users have learned it).
- **Audience:** Expert/domain users who depend on consistent mappings across time.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are designing a new palette from scratch and do not care about preserving initial category-color assignments.
- **Reason:** Swaps are only a problem when initial semantic association or learned mapping must be preserved [@fangCategoricalColormapOptimization2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slower exploration of color space; may take longer or get stuck closer to the initial palette.
- **The Risk:** Overly tight adaptive constraints can prevent escaping local maxima and may reduce achievable (D\_{min}) [@fangCategoricalColormapOptimization2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Running an unconstrained genetic algorithm and accepting whatever palette scores highest.
- **Why it fails:** You can end up with swapped or heavily reassigned category colors, losing semantic association and user trust [@fangCategoricalColormapOptimization2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories that used to be, say, “green” and “blue” appear to have traded colors after optimization.
- **The Test:** Compare category→color assignments before/after; if the identity of colors is discontinuous (swap/jump), adaptive range control is missing or too loose [@fangCategoricalColormapOptimization2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add adaptive range constraints (Δ as a per-iteration percentage limit) to enforce gradual changes.
- **Best Fix:** Combine adaptive range constraints with fixed-range (semantic) constraints and fixed background/foreground colors so optimization improves distinctness while keeping mappings stable, reflecting the kind of constraint-based operationalization encouraged by the collation paper [@zengReviewCollationGraphical2023; @fangCategoricalColormapOptimization2017].
