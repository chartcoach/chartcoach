---
id: use-color-in-small-multiples-to-group-or-highlight-not-to-distinguish-lines
title: Use Color to Group or Highlight Panels, Not to Differentiate Lines
bibliography: references.bib
description: In small multiple line charts, reserve color for emphasis or grouping
  because panel titles already identify series.
labels:
- chart:line
- task:highlight
- visual:color
- impact:clarity
- data:temporal
- audience:general
- chart:small-multiples
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

In small multiple line charts, don’t use different colors just to tell lines apart; use color to highlight specific panels or group categories by meaning.

## The Logic <!-- role: reason -->

Because each series has its own panel and title, color is no longer required for identification; freeing color for grouping/highlighting creates clearer emphasis and reduces unnecessary visual complexity [@muth_small_multiple_line_charts_2024].

- **The Principle:** Reserve color for meaning, not redundancy
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly see categories that belong together (e.g., upward vs downward trends) or notice highlighted cases
- **Data Type:** Faceted time series where each panel represents one category
- **Audience:** General readers scanning for patterns and exceptions

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single panel contains multiple lines (not one series per panel).
- **Reason:** Then color may be necessary to distinguish lines within the same panel; the “panel title identifies the line” assumption no longer holds [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer distinct colors available for other encodings in the same figure/story.
- **The Risk:** Over-highlighting can dilute emphasis if too many panels are colored [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning a unique color to every panel/line by default.
- **Why it fails:** Adds noise without adding information, undermining the opportunity to use color strategically [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Many different colors appear, but they don’t correspond to a clear grouping or message.
- **The Test:** Ask “What does each color mean?” If you can’t answer in one phrase, the color isn’t doing useful work [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Make most lines neutral and apply a highlight color to only the key panel(s).
- **Best Fix:** Define a small set of meaningful groups (e.g., up vs down) and color panels/lines consistently by that grouping [@muth_small_multiple_line_charts_2024].
