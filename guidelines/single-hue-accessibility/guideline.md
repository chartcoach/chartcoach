---
id: single-hue-accessibility
title: Use Single-Hue Shades for Accessibility
bibliography: references.bib
description: Use shades of one hue to ensure charts work for colorblind users and
  grayscale printing.
labels:
- visual:color
- impact:accessibility
- impact:colorblindness
- design:grayscale
- audience:general
---

## The Rule <!-- role: advice -->
Consider using shades of a single hue (sequential scale) instead of different hues, even for categorical data, to ensure accessibility and clean design.

## The Logic <!-- role: reason -->
A mantra for accessible visualization is "Get it right in black and white." It is difficult for humans (and software) to distinguish the lightness difference between two distinct hues (e.g., red vs. blue). However, distinguishing shades of a single hue (light blue vs. dark blue) is intuitive for everyone, including colorblind readers and those printing in grayscale. It also looks more professional and less "colorful" for serious topics [@muth_quantitative_vs_qualitative_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating professional, accessible charts for broad distribution.
*   **Data Type:** Categorical data with few categories (binary or ternary).
*   **Medium:** Print media (newspapers) or reports often printed in black and white.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You have more than 3-4 categories.
*   **Reason:** It is doable to distinguish 2-3 shades, but readers "will give up with four, five, six different shades," especially if they are not ordered or directly labeled [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->
*   **The Risk:** Readers will try to "rationalize" the colors. They may assume the darker category is more important, has higher values, or is the "bad" one.
*   **The Sacrifice:** You lose the ability to treat categories as strictly neutral/equal.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using multiple hues that have the exact same brightness.
*   **Why it fails:** In grayscale or for certain colorblindness types, the colors will look identical.

## How to Check <!-- role: check -->
*   **The Test:** Convert your chart to grayscale.
*   **Visual Sign:** Can you still distinguish the categories? If yes, the design is robust.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change your palette to a single-hue gradient (e.g., light gray, medium gray, dark blue).
*   **Best Fix:** If using shades, ensure the most important data point gets the darkest/strongest color to align with user rationalization.
