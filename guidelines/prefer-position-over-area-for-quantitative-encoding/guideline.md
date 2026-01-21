---
id: prefer-position-over-area-for-quantitative-encoding
title: Prefer Position Over Area for Quantitative Values
bibliography: references.bib
description: When encoding quantitative values, use positional encodings instead of
  area encodings for higher perceptual accuracy.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:any
- principle:effectiveness
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

When you need accurate quantitative reading, encode the quantity with position (on an axis) rather than with mark area.

## The Logic <!-- role: reason -->

Different graphical encodings impose different perceptual tasks, and some tasks are performed more accurately than others; position is ranked above area for quantitative judgments, so position-based encodings are more effective for accurate interpretation.

- **The Principle:** Effectiveness via perceptual-task accuracy ranking
- **The Evidence:** The paper uses Cleveland & McGill’s observation and an extended ranking to justify preferring position over area for quantitative data [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Read and compare quantitative values accurately (e.g., identify differences, estimate values)
- **Data Type:** Quantitative measures (numeric ranges)
- **Audience:** Any, especially analytic use

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have no positional channel available because position is already committed to more important quantitative variables.
- **Reason:** The paper’s importance ordering principle can justify using a less effective channel for less important measures [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer dimensions remain for other variables; position consumes axis real estate.
- **The Risk:** Overusing position can force cluttered multi-axis layouts or require composition choices that reduce readability [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding a key quantitative variable with area while claiming it is “just as readable.”
- **Why it fails:** Area judgments are less accurate, especially in scattered layouts where comparisons are harder [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to compare magnitudes unless values are labeled.
- **The Test:** Ask users (or yourself) to estimate ratios or differences between two marks quickly; if area encoding makes this unreliable, switch to position [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the quantitative encoding from size/area to an axis position.
- **Best Fix:** Redesign as a position-based chart (e.g., scatter plot with axes for the two most important quantitative relations) [@mackinlayAutomatingDesignGraphical1986b].
