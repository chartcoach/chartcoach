---
id: design-categorical-palettes-by-setting-lightness-first-then-choosing-hues
title: Set Lightness (and Saturation) First, Then Choose Hues
bibliography: references.bib
description: Build categorical palettes by defining lightness steps up front to ensure
  grayscale separability, then select hues that fit within those constraints.
labels:
- chart:all
- task:categorize
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- complexity:advanced
- custom:oklch
- source:datawrapper
---

## The Rule <!-- role: advice -->

Create categorical palettes by first choosing distinct lightness levels for each category (and adjusting saturation so darker colors don’t overpower), then picking hues that fit those lightness/saturation constraints.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Lightness separation preserves distinguishability even without hue
- **The Evidence:** Muth recommends “get it right in black and white” as an indicator of separability and describes a structured method: define different lightness levels (e.g., evenly spaced), reduce saturation for darker colors because they attract more attention, and then select hues using an OKLCH picker to stay within feasible ranges [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Ensure categories remain distinct across contexts (small marks, printing, imperfect screens)
- **Data Type:** Categorical palettes with multiple series (especially 5–10+ categories)
- **Audience:** Mixed audiences; especially useful when charts may be printed or viewed under constraints

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** Your palette must keep a fixed lightness (e.g., strict brand constraints requiring uniform lightness)
- **Reason:** You can’t guarantee grayscale separability if lightness cannot vary [@muth_good_color_palettes_2024].
- **Scenario:** You intentionally want equal lightness for a specific aesthetic (and accept reduced separability)
- **Reason:** The method’s main benefit is grayscale separability, which you’re choosing not to prioritize [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** More time and a more technical workflow (lightness/saturation constraints limit “fun” color choices)
- **The Risk:** If hue contrast becomes too small after constraining lightness/saturation, colors may still feel too similar unless carefully chosen [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Picking hues first and only later discovering some colors collapse in grayscale
- **Why it fails:** Late-stage fixes often require large changes and can break the palette’s cohesion [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Keeping darker colors equally saturated as lighter ones
- **Why it fails:** Dark, saturated colors can pull disproportionate attention, breaking equal importance [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** In grayscale, multiple categories become indistinguishable; in color, darker categories feel “heavier” than others
- **The Test:** Convert the palette to grayscale and confirm every swatch is still separable; compare perceived salience across swatches at small size [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust lightness so each category occupies a distinct step; reduce saturation of the darkest colors [@muth_good_color_palettes_2024].
- **Best Fix:** Rebuild in an OKLCH-based workflow: lock lightness/chroma targets first, then select hues that remain available and distinct within those constraints [@muth_good_color_palettes_2024].
