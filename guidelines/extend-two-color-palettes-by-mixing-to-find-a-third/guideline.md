---
id: extend-two-color-palettes-by-mixing-to-find-a-third
title: Mix Two Colors to Find a Compatible Third
bibliography: references.bib
description: To extend a palette, generate a single intermediate mixed color between
  two existing colors as a candidate that matches both.
labels:
- chart:all
- task:categorize
- visual:color
- impact:cohesion
- data:categorical
- audience:general
- complexity:beginner
- source:datawrapper
---

## The Rule <!-- role: advice -->

When you have two existing palette colors and need a third that fits, create a 3–4 step mix/gradient and take the middle color as your candidate.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Intermediate blending inherits hue/lightness/saturation relationships from both anchors
- **The Evidence:** Muth explains that generating a one-step gradient (or using a mixing tool) produces a middle color whose saturation, lightness, and hue sit between the two originals, making it a practical way to add a compatible third color [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Expand a small palette without introducing a clashing new color
- **Data Type:** Existing categorical palette with 2–3 anchor colors
- **Audience:** Any; especially useful when you must preserve an established look

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You need maximum category separation (very distinct colors)
- **Reason:** A mixed color can be “too in-between,” reducing categorical distinctness [@muth_good_color_palettes_2024].
- **Scenario:** Your two anchor colors are already similar
- **Reason:** The mixed color will be even less distinct and won’t add differentiation [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** The new color may be less vivid or less distinctive than a purpose-selected hue
- **The Risk:** You might create a palette with insufficient contrast between categories if you rely on multiple mixed “in-between” colors [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Picking a random “third” color from an unrelated palette collection
- **Why it fails:** It may not harmonize with the two anchors and can shift perceived importance [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Adding multiple intermediate colors between the same two anchors for categorical data
- **Why it fails:** The palette becomes a near-gradient and categories become hard to distinguish [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The new category color looks like a blend/duplicate and is hard to tell apart from one of the originals
- **The Test:** Place the three colors side-by-side at legend-key size and verify each is clearly distinct; if not, the middle color is too close [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a 4-step mix and choose the second or third color (not necessarily the exact middle) to increase separation [@muth_good_color_palettes_2024].
- **Best Fix:** Keep the mixed color as a starting point, then adjust lightness/saturation to restore distinctness while staying stylistically compatible [@muth_good_color_palettes_2024].
