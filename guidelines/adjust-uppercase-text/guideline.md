---
id: adjust-uppercase-text
title: Use uppercase sparingly and adjust spacing
bibliography: references.bib
description: Improve uppercase legibility by increasing tracking and reducing size.
labels:
- visual:typography
- impact:legibility
- task:label
- visual:hierarchy
---

## The Rule <!-- role: advice -->

Avoid using all-caps (uppercase) for long text. If you must use uppercase (e.g., for labels or headers), add letter-spacing (tracking), reduce the font size, and slightly bold the text.

## The Logic <!-- role: reason -->

Uppercase text is harder to read because words lose their distinctive shapes (ascenders and descenders), forming a uniform rectangle. However, uppercase can look "tidier" for short labels. Because standard uppercase letters are visually larger and denser than lowercase, they need adjustment to fit harmoniously.

*   **The Principle:** Word Shape Recognition and Optical Density
*   **The Evidence:** [@muth_fonts_2022] explains that uppercase text looks "dense" and advises increasing tracking to improve legibility.

## Where to Apply <!-- role: context -->

*   **User Goal:** Identifying categories, regions, or headers.
*   **Data Type:** Short labels (e.g., "VOTES," "UKRAINE"), map markers, filter buttons.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Long sentences or paragraphs.
*   **Reason:** Never use uppercase for long text; it is too difficult to read.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Uppercase takes up more horizontal space, especially with added tracking.
*   **The Risk:** If not adjusted, uppercase text looks like it is "shouting."

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Retyping text with Caps Lock on.
*   **Why it fails:** Efficient design software allows you to toggle text case without retyping.
*   **The Wrong Fix:** Using default spacing for uppercase.
*   **Why it fails:** It looks too tight/dense compared to sentence case.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the uppercase text look like a solid block? Is it significantly wider and heavier than surrounding text?
*   **The Test:** Check the letter-spacing value. If it is 0, it likely needs increasing.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add "tracking" (letter-spacing).
*   **Best Fix:** Follow the formula from [@muth_fonts_2022]:
    1. Transform to Uppercase.
    2. Increase letter-spacing (tracking).
    3. Decrease font size slightly.
    4. Make the text slightly bolder (to match original stroke width).
