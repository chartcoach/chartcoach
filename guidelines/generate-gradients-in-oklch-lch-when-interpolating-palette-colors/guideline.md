---
id: generate-gradients-in-oklch-lch-when-interpolating-palette-colors
title: Interpolate Colors in OKLCH/LCH When Building Palette Steps
bibliography: references.bib
description: When deriving multiple colors between endpoints, generate them in OKLCH
  or LCH for more pleasing, controllable gradients and then verify contrast.
labels:
- chart:bar
- task:style
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
- custom:oklch
- source:datawrapper
---

## The Rule <!-- role: advice -->

If you create palette colors by interpolating between a start and end color, generate the steps in OKLCH or LCH (not RGB/HSL), and ensure the brightest step still meets your contrast needs against the background.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Perceptually guided interpolation yields smoother, more usable ramps
- **The Evidence:** Muth recommends using gradient tools to generate colors between endpoints and specifically suggests OKLCH or LCH for nicer-looking gradients than RGB/HSL/LAB, while warning to check that the brightest color meets the contrast ratio you want/need [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Quickly derive a small set of harmonious colors (especially for larger areas like bars)
- **Data Type:** Categorical palettes derived from two anchor colors (often 3–6 colors)
- **Audience:** General audiences; especially when readability on light backgrounds matters

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You need non-interpolated, maximally distinct categorical colors (not “between” two endpoints)
- **Reason:** Interpolated steps can become too similar for categorical differentiation [@muth_good_color_palettes_2024].
- **Scenario:** Your endpoints are already too close in lightness/chroma
- **Reason:** Interpolation won’t create sufficient separation; you’ll need different anchors [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Some “in-between” colors may feel less distinctive for categories than a purpose-built categorical palette
- **The Risk:** If you don’t check contrast, lighter steps can disappear on white backgrounds [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Interpolating in RGB/HSL and assuming the results will look smooth and balanced
- **Why it fails:** The intermediate colors can look uneven or unpleasant compared to OKLCH/LCH interpolation [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Choosing two dark endpoints or two light endpoints for a white background chart
- **Why it fails:** You end up with steps that either all feel too heavy or lack contrast at the bright end [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Middle colors look “muddy” or unexpectedly grayish; lightest color is hard to see on the background
- **The Test:** Switch the interpolation mode to OKLCH/LCH and compare; verify the lightest color against the background with a contrast check [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Recompute the gradient steps in OKLCH/LCH and pick fewer, more separated steps [@muth_good_color_palettes_2024].
- **Best Fix:** Choose better anchors (e.g., one bright and one dark, saturated color) and tune hue interpolation (“shorter” vs. “longer”) to control hue variety, then validate contrast [@muth_good_color_palettes_2024].
