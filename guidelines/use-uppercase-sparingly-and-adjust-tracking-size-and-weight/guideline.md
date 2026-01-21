---
id: use-uppercase-sparingly-and-adjust-tracking-size-and-weight
title: Use Uppercase Sparingly and Compensate with Letter-Spacing
bibliography: references.bib
description: Avoid all-caps for long text; if you use uppercase labels, increase letter-spacing
  and rebalance size and weight.
labels:
- chart:general
- task:label
- visual:typography
- impact:clarity
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use uppercase text sparingly; when you do use it, increase letter-spacing and adjust size and weight so the label remains readable and balanced.

## The Logic <!-- role: reason -->

Uppercase is harder to read than sentence case because words lose the distinctive shapes created by ascenders/descenders; uppercase also becomes wider and can look dense, which can be mitigated by adding tracking (letter-spacing), reducing size, and then increasing weight to maintain stroke presence [@muth_fonts_2022].

- **The Principle:** Word-shape recognition + density management in all-caps
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguishing UI-like labels (filters, group labels, short headers) from other text
- **Data Type:** Short labels (tooltip headers, axis labels, table headers, map region labels)
- **Audience:** General readers scanning for structure and groupings

## When to Break It <!-- role: exceptions -->

- **Scenario:** Longer annotations, descriptions, or notes.
- **Reason:** All-caps becomes a dense rectangle and is harder to read for extended text; the post recommends limiting uppercase to just a few words [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uppercase consumes more horizontal space, often forcing truncation or layout changes.
- **The Risk:** If overused, uppercase makes many elements look equally “important,” weakening hierarchy and slowing reading [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Converting labels to uppercase without changing letter-spacing.
- **Why it fails:** The text gets wider and denser, reducing readability and crowding the layout [@muth_fonts_2022].
- **The Wrong Fix:** Using uppercase for many long labels.
- **Why it fails:** It becomes hard to read and visually dominates other elements [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Uppercase labels look cramped, overly wide, or shouty; words feel like uniform blocks.
- **The Test:** Compare the uppercase version to sentence case. If the uppercase feels denser and harder to scan, increase letter-spacing; if it becomes too long, reduce font size; then increase weight to match perceived stroke thickness [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Limit uppercase to the shortest labels (a few words) and add letter-spacing [@muth_fonts_2022].
- **Best Fix:** Apply the post’s adjustment sequence: (1) add letter-spacing, (2) reduce font size to control width, (3) increase weight to restore stroke presence, and use uppercase primarily for structural labels (e.g., headers, group labels, map region labels) [@muth_fonts_2022].
